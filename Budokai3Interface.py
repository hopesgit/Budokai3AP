import array
import dataclasses
import struct
from dataclasses import dataclass, field
from enum import Enum, IntEnum
from logging import Logger
from typing import Optional, List, Dict, NamedTuple, TYPE_CHECKING

from .data import Items

from .pcsx2_interface.pine import Pine

if TYPE_CHECKING:
    pass

_SUPPORTED_VERSIONS = ["SLUS-20998", "SLUS-20998GH"]

HUD_MESSAGE_DURATION = 2.0
HUD_MAX_MESSAGE_WIDTH = 35

MOBY_SIZE = 0x100
MEMORY_SEGMENTS = 35


class MissingAddressError(Exception):
    pass


class ConnectionState(Enum):
    DISCONNECTED = 0
    IN_GAME = 1
    IN_MENU = 2


class Budokai3Planet(IntEnum):
    """Game planets with their corresponding IDs"""
    Title_Screen = -1
    Aranos_Tutorial = 0
    Oozla = 1
    Maktar_Nebula = 2
    Endako = 3
    Barlow = 4
    Feltzin_System = 5
    Notak = 6
    Siberius = 7
    Tabora = 8
    Dobbo = 9
    Hrugis_Cloud = 10
    Joba = 11
    Todano = 12
    Boldan = 13
    Aranos_Prison = 14
    Gorn = 15
    Snivelak = 16
    Smolg = 17
    Damosel = 18
    Grelbin = 19
    Yeedil = 20
    Dobbo_Orbit = 22
    Damosel_Orbit = 23
    Ship_Shack = 24
    Wupash_Nebula = 25
    Jamming_Array = 26
    Insomniac_Museum = 30


class PauseState(Enum):
    INGAME = 0
    CUTSCENE = 2
    MENU = 3
    QUICKSELECT = 4
    VENDOR = 5
    SHIP = 6
    MINIGAME = 7
    UPGRADE = 8


@dataclass
class MobyInstance:
    address: int
    x: float  # 0x10, 32 bits
    y: float  # 0x14, 32 bits
    z: float  # 0x18, 32 bits
    state: int  # 0x20, 8 bits
    group: int  # 0x21, 8 bits
    moby_class: int  # 0x22, 8 bits
    alpha: int  # 0x23, 8 bits
    class_address: int  # 0x24, 32 bits
    chain_address: int  # 0x28, 32 bits
    scale: float  # 0x2C, 32 bits
    is_drawn: bool  # 0x31, 8 bits
    draw_distance: int  # 0x32, 16 bits
    flags1: int  # 0x34, 16 bits
    flags2: int  # 0x36, 16 bits
    lighting: float  # 0x38, 32 bits
    red: int  # 0x3C, 8 bits
    green: int  # 0x3D, 8 bits
    blue: int  # 0x3E, 8 bits
    shine: int  # 0x3F, 8 bits
    update_function_address: int  # 0x64, 32 bits
    pvars_address: int  # 0x68, 32 bits
    colldata_address: int  # 0x98, 32 bits
    oclass: int  # 0xAA, 16 bits
    uid: int  # 0xB2, 16 bits

    def push(self):
        Budokai3Interface.pcsx2_interface.write_float(self.address + 0x10, self.x)
        Budokai3Interface.pcsx2_interface.write_float(self.address + 0x14, self.y)
        Budokai3Interface.pcsx2_interface.write_float(self.address + 0x18, self.z)
        Budokai3Interface.pcsx2_interface.write_int8(self.address + 0x20, self.state)
        Budokai3Interface.pcsx2_interface.write_int8(self.address + 0x21, self.group)
        Budokai3Interface.pcsx2_interface.write_int8(self.address + 0x22, self.moby_class)
        Budokai3Interface.pcsx2_interface.write_int8(self.address + 0x23, self.alpha)
        Budokai3Interface.pcsx2_interface.write_int32(self.address + 0x24, self.class_address)
        Budokai3Interface.pcsx2_interface.write_int32(self.address + 0x28, self.chain_address)
        Budokai3Interface.pcsx2_interface.write_float(self.address + 0x2C, self.scale)
        Budokai3Interface.pcsx2_interface.write_int8(self.address + 0x31, self.is_drawn)
        Budokai3Interface.pcsx2_interface.write_int16(self.address + 0x32, self.draw_distance)
        Budokai3Interface.pcsx2_interface.write_int16(self.address + 0x34, self.flags1)
        Budokai3Interface.pcsx2_interface.write_int16(self.address + 0x36, self.flags2)
        Budokai3Interface.pcsx2_interface.write_float(self.address + 0x38, self.lighting)
        Budokai3Interface.pcsx2_interface.write_int8(self.address + 0x3C, self.red)
        Budokai3Interface.pcsx2_interface.write_int8(self.address + 0x3D, self.green)
        Budokai3Interface.pcsx2_interface.write_int8(self.address + 0x3E, self.blue)
        Budokai3Interface.pcsx2_interface.write_int8(self.address + 0x3F, self.shine)
        Budokai3Interface.pcsx2_interface.write_int32(self.address + 0x64, self.update_function_address)
        Budokai3Interface.pcsx2_interface.write_int32(self.address + 0x68, self.pvars_address)
        Budokai3Interface.pcsx2_interface.write_int32(self.address + 0x98, self.colldata_address)
        Budokai3Interface.pcsx2_interface.write_int16(self.address + 0xAA, self.oclass)
        Budokai3Interface.pcsx2_interface.write_int16(self.address + 0xB2, self.uid)


@dataclass(frozen=True)
class MemorySegmentTable:
    kernel: int = field()
    code: int
    base: int
    tfrag_geometry: int
    occlusion: int
    sky: int
    collision: int
    shared_vram: int
    particle_vram: int
    effects_vram: int
    moby_classes: int
    ties: int
    shrubs: int
    ratchet_seqs: int
    help_messages: int
    tie_instances: int
    shrub_instances: int
    moby_instances: int
    moby_pvars: int
    misc_instances: int
    misc_instances_end: int
    hud: int
    gui: int

    @classmethod
    def from_list(cls, raw_table: List[int]):
        return cls(
            kernel=raw_table[0],
            code=raw_table[1],
            base=raw_table[2],
            tfrag_geometry=raw_table[7],
            occlusion=raw_table[8],
            sky=raw_table[9],
            collision=raw_table[10],
            shared_vram=raw_table[11],
            particle_vram=raw_table[12],
            effects_vram=raw_table[13],
            moby_classes=raw_table[14],
            ties=raw_table[15],
            shrubs=raw_table[16],
            ratchet_seqs=raw_table[17],
            help_messages=raw_table[19],
            tie_instances=raw_table[20],
            shrub_instances=raw_table[21],
            moby_instances=raw_table[22],
            moby_pvars=raw_table[23],
            misc_instances=raw_table[24],
            misc_instances_end=raw_table[25],
            hud=raw_table[31],
            gui=raw_table[32],
        )

    def __repr__(self):
        string: str = ""
        for f in dataclasses.fields(self):
            string += f"{f.name:<18}: 0x{getattr(self, f.name):0>8X}\n"
        return string


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
    # addresses: Addresses = None
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
        self.pcsx2_interface.write_int8(item.offset, 1)


    def give_capsule_to_player(self, item):
        item_data = Items.from_id(item.item)
        offset = item_data.offset
        current_count = self.pcsx2_interface.read_int8(offset)
        if current_count < 9:
            self.pcsx2_interface.write_int8(offset, current_count + 1)

 
    def increment_money(self, item):
        name: str = item.name.strip(' Zenie')
        amount: int = int(name)
        current_zenie = self.pcsx2_interface.read_int32(0x58F718)
        max = 0xFFFF
        if current_zenie + amount > max:
            new_amount = max
        else:
            new_amount = current_zenie + amount
        self.pcsx2_interface.write_int32(0x58F718, new_amount)

    # def get_pause_state(self) -> int:
    #     address = self.addresses.pause_state
    #     if self.get_current_planet() is Budokai3Planet.Oozla:
    #         address = self.addresses.oozla_pause_state
    #     return self.pcsx2_interface.read_int8(address)

    def connect_to_game(self):
        """Initializes the connection to PCSX2 and verifies it is connected to Budokai 3"""
        if not self.pcsx2_interface.is_connected():
            self.pcsx2_interface.connect()
            if not self.pcsx2_interface.is_connected():
                return
            self.logger.info("Connected to PCSX2 Emulator")
        try:
            game_id = self.pcsx2_interface.get_game_id()
            self.current_game = None
            if game_id in _SUPPORTED_VERSIONS:
                self.current_game = game_id
                # self.addresses = Addresses(game_id)
            if self.current_game is None and self.game_id_error != game_id and game_id != b'\x00\x00\x00\x00\x00\x00':
                self.logger.warning(
                    f"Connected to the wrong game ({game_id}, "
                    f"please connect to DBZ Budokai 3 (Game ID starts with a SLUS-)")
                self.game_id_error = game_id
        except RuntimeError:
            pass
        except ConnectionError:
            pass

    def disconnect_from_game(self):
        self.pcsx2_interface.disconnect()
        self.current_game = None
        self.logger.info("Disconnected from PCSX2 Emulator")

    def get_connection_state(self) -> bool:
        try:
            connected = self.pcsx2_interface.is_connected()
            if not connected or self.current_game is None:
                return False
            else:
                return True
        except RuntimeError:
            return False

    # def is_loading(self) -> bool:
    #     return not self.pcsx2_interface.read_int8(self.addresses.loaded_flag)

    # def get_moby(self, uid: int) -> Optional[MobyInstance]:
    #     address = self.get_segment_pointer_table().moby_instances
    #     uid_offset = 0xB2
    #     for _ in range(self.get_segment_pointer_table().moby_instances, self.get_segment_pointer_table().moby_pvars):
    #         if self.pcsx2_interface.read_int16(address + uid_offset) == uid:
    #             moby_data = struct.unpack("<16xfff4xBBBBIIfx?HHHIBBBB36xII44xI14xH6xH76x",
    #                                       self.pcsx2_interface.read_bytes(address, MOBY_SIZE))
    #             return MobyInstance(*((address,) + moby_data))
    #         address += MOBY_SIZE

    #     return None

    def read_instruction(self, address: int) -> int:
        return self.pcsx2_interface.read_int32(address)

    def write_instruction(self, address: int, instruction: int):
        self.pcsx2_interface.write_int32(address, instruction)

    def nop_instruction(self, address: int):
        self.write_instruction(address, 0x0)

    # def get_text_offset_addr(self, text_id: int) -> Optional[int]:
    #     text_address_table = self.get_segment_pointer_table().help_messages

    #     # If text segment starts with "WAD", it means the game is currently performing a light reload
    #     # (e.g. after a death) and writing over this data would most likely crash the game.
    #     header = self.pcsx2_interface.read_int32(text_address_table)
    #     if header & 0x00FFFFFF == 0x444157:  # "WAD"
    #         return None

    #     # Since the order of text IDs is always the same in the table for a given version of the game, we store the
    #     # position of each text ID we encounter to avoid looping over that table ever again.
    #     if text_id in self.text_ids_cache:
    #         offset_addr = text_address_table + self.text_ids_cache[text_id] * 0x10
    #         found_text_id = self.pcsx2_interface.read_int32(offset_addr + 0x4)
    #         if found_text_id == text_id:
    #             return offset_addr
    #         # When changing planets, offsets can slightly shift for some reason: invalidate the cache
    #         self.text_ids_cache.clear()

    #     # Perform a lookup on the text offsets table to know the address of the string referenced by the given text ID
    #     # Cache all offsets in this table inside the dictionary to not have to perform that lookup next time.
    #     i = 0
    #     while True:
    #         current_text_id = self.pcsx2_interface.read_int32(text_address_table + i * 0x10 + 0x4)
    #         self.text_ids_cache[current_text_id] = i
    #         if current_text_id > 0x2000000:
    #             return None
    #         if current_text_id == text_id:
    #             return text_address_table + i * 0x10
    #         i += 1

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

    # def can_display_hud_notification(self):
    #     return self.get_pause_state() == 0 and self.get_ratchet_state() != 97

    # def trigger_hud_notification_display(self):
    #     try:
    #         # Overwrite from start of "You got a skill point!" text with payload message.
    #         self.pcsx2_interface.write_int8(self.addresses.custom_text_notification_trigger, 0x01)
    #         return True
    #     except RuntimeError:
    #         return False

    # def is_hud_notification_pending(self):
    #     return self.pcsx2_interface.read_int8(self.addresses.custom_text_notification_trigger) == 0x01

    # def get_segment_pointer_table(self) -> Optional[MemorySegmentTable]:
    #     # if self.addresses is None:
    #     #     return None

    #     # table_base_address = self.addresses.planet[self.get_current_planet().value].segment_pointers
    #     # if table_base_address is None:
    #     #     return None

    #     try:
    #         table_bytes = self.pcsx2_interface.read_bytes(table_base_address, MEMORY_SEGMENTS * 4)
    #     except ValueError:
    #         return None

    #     return MemorySegmentTable.from_list(array.array('I', table_bytes).tolist())
