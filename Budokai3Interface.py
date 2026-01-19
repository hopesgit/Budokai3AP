# from dataclasses import dataclass, field
from enum import Enum, IntEnum
from logging import Logger
from typing import Optional, Dict

from .data import Items

from .pcsx2_interface.pine import Pine
from .data.Addresses import Addresses
from .data.addresses.US import VERSION as USVER
from .data.addresses.US_GH import VERSION as USGHVER
from .data.addresses.PAL import VERSION as PALVER
from .data.addresses.PAL_CE import VERSION as PALCEVER
from .data.addresses.JP import VERSION as JPVER
from .data.addresses.JP_BS import VERSION as JPBSVER

_SUPPORTED_VERSIONS = [USVER, USGHVER]

HUD_MESSAGE_DURATION = 2.0
HUD_MAX_MESSAGE_WIDTH = 35

MEMORY_SEGMENTS = 35


class MissingAddressError(Exception):
    pass


class ConnectionState(Enum):
    DISCONNECTED = 0
    IN_GAME = 1
    IN_MENU = 2


class Budokai3Screen(IntEnum):
    TITLE = 0x0004
    MAIN = 0x0005
    PRACTICE = 0x0013
    SHOP = 0x0016
    OPTIONS = 0x001C
    DU_TITLE = 0x0106
    DU_CHAR_SEL = 0x0107
    DU_WORLD_MAP = 0x0108
    DU_BATTLE = 0x0109
    DU_BATTLE_RESULT = 0x010A
    SHENRON = 0x010B
    CREDITS = 0x010C
    DUEL_MENU = 0x020E
    DUEL_BATTLE = 0x020F
    WT_MENU = 0x0310
    WT_BRACKET = 0x0311
    WT_BATTLE = 0x0312
    PRAC_CHAR_SEL = 0x0413
    PRAC_BATTLE = 0x0414
    TRN_CHAP_SEL = 0x0513
    TRN_BATTLE = 0x0515
    DA_ENTRANCE = 0x0617
    DA_CHAR_SEL = 0x0618
    DA_BATTLE = 0x0619
    DA_RESULTS = 0x061A
    DA_SAVE = 0x061B

BATTLE_SCREENS = [
    Budokai3Screen.DU_BATTLE.value, Budokai3Screen.DUEL_BATTLE.value, Budokai3Screen.WT_BATTLE.value, Budokai3Screen.PRAC_BATTLE.value, 
    Budokai3Screen.TRN_BATTLE.value, Budokai3Screen.DA_BATTLE.value
]

SAVE_FILE_LOADED = [x.value for x in Budokai3Screen if x.value != Budokai3Screen.TITLE.value]

# class Shop:
#     # CURSOR_OFFSET: int = -0xC0
#     # SUBMENU_OFFSET: int = -0xBC
#     # MODEL_UPDATE_OFFSET: int = -0xB0
#     # SLOT_COUNT_OFFSET: int = 0x600
#     # VENDOR_TYPE_OFFSET: int = -0xF0
#     # VENDOR_WEAPON_TYPE_OFFSET: int = 0x604
#     # SLOT_SIZE: int = 0x18

#     class ShopSlot(NamedTuple):
#         item_id: int

#     def __init__(self, interface: "Budokai3Interface"):
#         self.interface: Budokai3Interface = interface
#         self.slots: list[Shop.ShopSlot] = []
#         self.recently_bought_locations: list[int] = []

#     def notify_item_bought(self, location_id: int):
#         self.recently_bought_locations.append(location_id)

#     def set_slot(self, slot_num: int, slot_data: ShopSlot) -> None:
#         shop_slot_table = self._get_shop_slot_table()

#         address = shop_slot_table + slot_num * self.SLOT_SIZE
#         self.interface.pcsx2_interface.write_int32(address, slot_data.item_id)
#         self.interface.pcsx2_interface.write_int32(address + 0x10, 0)

#     def populate_slots(self, slots: list[ShopSlot]) -> None:
#         self.slots = slots
#         for i, slot in enumerate(slots):
#             self.set_slot(i, slot)

#         shop_slot_table = self._get_shop_slot_table()
#         self.interface.pcsx2_interface.write_int8(shop_slot_table + self.SLOT_COUNT_OFFSET, len(slots))
#         self.set_cursor_position(self.get_cursor_position())

#     def get_slot_count(self) -> Optional[int]:
#         shop_slot_table = self._get_shop_slot_table()
#         return self.interface.pcsx2_interface.read_int8(shop_slot_table + self.SLOT_COUNT_OFFSET)

#     def set_cursor_position(self, slot: int):
#         shop_slot_table = self._get_shop_slot_table()

#         # Make sure cursor stays in bounds
#         slot = min(self.get_slot_count() - 1, slot)
#         slot = max(0, slot)

        # self.interface.pcsx2_interface.write_int8(shop_slot_table + self.CURSOR_OFFSET, slot)
        # # Changing the cursor directly doesn't update the model view. Changing this value will force an update.
        # self.interface.pcsx2_interface.write_int8(shop_slot_table + self.MODEL_UPDATE_OFFSET, 3)

    # def get_cursor_position(self) -> Optional[int]:
    #     shop_slot_table = self._get_shop_slot_table()
    #     return self.interface.pcsx2_interface.read_int8(shop_slot_table + self.CURSOR_OFFSET)

    # def get_unlock_list(self) -> list[int]:
    #     items = []
    #     for i in range(32):
    #         item = self.interface.pcsx2_interface.read_int8(self.interface.addresses.shop_list + i)
    #         if item == 0xFF:
    #             break
    #         items.append(item & 0x3F)
    #     return items

    # def _get_shop_slot_table(self) -> int:
    #     current_planet = self.interface.get_current_planet()
    #     if not current_planet:
    #         raise MissingAddressError("Could not get current planet")

    #     shop_slot_table = self.interface.addresses.planet[current_planet].shop_slot_table
    #     if not shop_slot_table:
    #         raise MissingAddressError

    #     return shop_slot_table


class Budokai3Interface:
    """Interface sitting in front of the pcsx2_interface to provide higher level functions for interacting with Budokai3"""
    pcsx2_interface: Pine = Pine()
    addresses: Addresses = None
    # shop: Shop = None
    connection_status: str
    logger: Logger
    _previous_message_size: int = 0
    game_id_error: Optional[str] = None
    game_rev_error: Optional[int] = None
    current_game: Optional[str] = None
    text_ids_cache: Dict[int, int] = {}

    def __init__(self, logger) -> None:
        self.logger = logger
        # self.shop = Shop(self)


    def give_system_capsule_to_player(self, item):
        self.logger.info(f'Applying item {item.name} to offset {item.offset}...')
        self.pcsx2_interface.write_int8(item.offset, 1)


    def give_capsule_to_player(self, item):
        item_data = Items.from_id(item.item)
        offset = item_data.offset
        current_count = self.pcsx2_interface.read_int8(offset)
        if current_count < 9:
            new_count = current_count + 1
            self.logger.info(f'Incrementing item {item.name} to offset {offset} with count {new_count}...')
            self.pcsx2_interface.write_int8(offset, current_count + 1)

 
    def increment_money(self, item):
        name: str = item.name.rsplit(' Zenie', 1)[0]
        amount: int = int(name)
        current_zenie = self.pcsx2_interface.read_int32(0x58F718)
        max = 0xFFFF
        if current_zenie + amount > max:
            new_amount = max
        else:
            new_amount = current_zenie + amount
        self.logger.info(f"Adding {new_amount} Zenie.")
        self.pcsx2_interface.write_int32(0x58F718, new_amount)

    def get_screen(self) -> int:
        return self.pcsx2_interface.read_int16(self.addresses.current_screen().start_offset)

    def in_battle(self) -> bool:
        return self.get_screen() in BATTLE_SCREENS
    
    def save_file_loaded(self) -> bool:
        return self.get_screen() in SAVE_FILE_LOADED

    def read_p1_hp(self) -> int:
        return self.pcsx2_interface.read_int32(self.addresses.p1_hp().start_offset)
    
    def deathlink_set_p1_hp(self):
        self.pcsx2_interface.write_int32(self.addresses.p1_hp().start_offset, 0x00000000)

    def return_to_main_menu(self, save: bool = False):
        pass

    def connect_to_game(self):
        """Initializes the connection to PCSX2 and verifies it is connected to Budokai 3"""
        if not self.pcsx2_interface.is_connected():
            self.pcsx2_interface.connect()
            if not self.pcsx2_interface.is_connected():
                return
            self.logger.info("Connected to PCSX2.")
        try:
            game_id = self.pcsx2_interface.get_game_id()
            self.current_game = None
            if game_id in _SUPPORTED_VERSIONS:
                self.current_game = game_id
                self.addresses = Addresses(game_id)
            if self.current_game is None and self.game_id_error != game_id and game_id != b'\x00\x00\x00\x00\x00\x00':
                self.logger.warning(
                    f"Connected to the wrong game, {game_id}.\n"
                    f"Please open Dragon Ball Z: Budokai 3 for the PlayStation 2 system.\n"
                    f"Game ID is {USVER}/{USGHVER} for NTSC-U versions; {PALVER}/{PALCEVER} for PAL; {JPVER}/{JPBSVER} for NTSC-J.\n"
                    f"For now, only {USVER} is supported.")
                self.game_id_error = game_id
        except RuntimeError:
            pass
        except ConnectionError:
            pass

    def disconnect_from_game(self):
        self.pcsx2_interface.disconnect()
        self.current_game = None
        self.logger.info("Disconnected from PCSX2.")

    def get_connection_state(self) -> bool:
        try:
            connected = self.pcsx2_interface.is_connected()
            if not connected or self.current_game is None:
                return False
            else:
                return True
        except RuntimeError:
            return False

    def read_instruction(self, address: int) -> int:
        return self.pcsx2_interface.read_int32(address)

    def write_instruction(self, address: int, instruction: int):
        self.pcsx2_interface.write_int32(address, instruction)

    def nop_instruction(self, address: int):
        self.write_instruction(address, 0x0)

    def call_credits(self):
        self.pcsx2_interface.read_bytes(0x104970, 4)

    # def get_text_address(self, text_id: int) -> Optional[int]:
    #     offset_addr = self.get_text_offset_addr(text_id)
    #     if offset_addr:
    #         return self.pcsx2_interface.read_int32(offset_addr)
    #     return None

    # def set_text_address(self, text_id: int, addr: int) -> bool:
    #     offset_addr = self.get_text_offset_addr(text_id)
    #     if offset_addr:
    #         self.pcsx2_interface.write_int32(offset_addr, addr)
    #         return True
    #     return False

    # def trigger_hud_notification_display(self):
    #     try:
    #         # Overwrite from start of "You got a skill point!" text with payload message.
    #         self.pcsx2_interface.write_int8(self.addresses.custom_text_notification_trigger, 0x01)
    #         return True
    #     except RuntimeError:
    #         return False

    # def is_hud_notification_pending(self):
    #     return self.pcsx2_interface.read_int8(self.addresses.custom_text_notification_trigger) == 0x01
