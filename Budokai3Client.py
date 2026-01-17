from typing import Optional

from ClientReceiveItems import handle_received_items
import Utils
import asyncio
import os
import threading
from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, logger, server_loop, gui_enabled
from . import version
from .data.Addresses import Addresses
from .data.Items import get_offset_from_name
from .data.Locations import get_all_active_locations
from .Budokai3Interface import Budokai3Interface, ConnectionState
from .NotificationManager import NotificationManager

HUD_MESSAGE_DURATION = 50


class Budokai3CommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: 'Budokai3Context'):
        super().__init__(ctx)

    def _cmd_test_hud(self, *args):
        """Send a message to the game interface."""
        if isinstance(self.ctx, Budokai3Context):
            self.ctx.notification_manager.queue_notification(' '.join(map(str, args)))

    def _cmd_status(self):
        """Display the current PCSX2 connection status."""
        if isinstance(self.ctx, Budokai3Context):
            logger.info(f"Connection status: {'Connected' if self.ctx.is_connected else 'Disconnected'}")
    
    def _cmd_unlock_capsule(self, *args):
        """Debug option to unlock a capsule. For testing ONLY
        
        @param args: Arbitrary-length collection of strings. I join these together to make one long string, 
        so you should be able to supply a name with multiple words without the use of strings.
        """
        if not args: 
            logger.info('No item name provided.')
            return
        name = ' '.join(map(str, args))
        logger.info(f"Attempting to unlock {name}...")
        offset = get_offset_from_name(name)
        logger.debug(f"Offset is {offset}")
        if not offset:
            logger.info("Item couldn't be found. You may have provided a bad name.")
            return
        if offset == 0x0:
            logger.info("The item was found, but it doesn't have a listed memory location.")
            return
        if isinstance(self.ctx, Budokai3Context):
            logger.debug(f"Writing to {hex(offset)}...")
            Budokai3Interface.pcsx2_interface.write_int8(offset, 1)
            logger.info("Done! Be sure to save using Save/Quit in Dragon Universe or Save in the Options menu to enable the capsule.")

    def _cmd_test_deathlink(self):
        """
        Test function. Doesn't accept any arguments.
        """
        if not self.ctx.deathlink_enabled:
            logger.warning('Death link is not enabled. Use the /deathlink command to toggle it on, then retry this command.')
            return
        self.ctx.store_deathlink()

    def _cmd_deathlink(self):
        """Toggle the deathlink setting. """
        self.ctx.deathlink_enabled = not self.ctx.deathlink_enabled
        ending = "enabled" if self.ctx.deathlink_enabled else "disabled"
        dl_text = f"Death link {ending}."
        logger.info(dl_text)

    def _cmd_trap_party(self):
        """Rave?"""
        party(self.ctx)


class Budokai3Context(CommonContext):
    command_processor = Budokai3CommandProcessor
    game_interface: Budokai3Interface
    notification_manager: NotificationManager
    game = "Dragon Ball Z Budokai 3"
    items_handling = 0b111
    game_version: str = None
    pcsx2_sync_task = None
    is_connected: bool = False
    current_screen: int = None
    is_loading: bool = False
    is_in_menu: bool = False
    is_in_du: bool = False
    is_in_battle: bool = False
    slot_data: dict[str, Utils.Any] | None = None
    last_error_message: Optional[str] = None
    deathlink_queued: bool = False
    deathlink_enabled: bool = False

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.game_interface = Budokai3Interface(logger)
        self.notification_manager = NotificationManager(HUD_MESSAGE_DURATION)

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(Budokai3Context, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def run_gui(self):
        from kvui import GameManager

        class Budokai3Manager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago DBZ Budokai 3 Client"
            base_title += f' v{version} |'

        self.ui = Budokai3Manager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

    def store_deathlink(self):
        self.deathlink_queued = True
        logger.info("Deathlink received. Awaiting battle...")


def on_package(self, cmd: str, args: dict):
    if cmd == 'Connected':
        self.slot_data = args["slot_data"]
        if "death_link" in args["slot_data"]:
            deathlink = args["slot_data"]["death_link"]
            self.deathlink_enabled = deathlink
            Utils.async_start(self.update_death_link(deathlink))
    
def update_connection_status(ctx: Budokai3Context, status: bool):
    if ctx.is_connected == status:
        return

    ctx.is_connected = status
    if status:
        logger.info("Connected to DBZ Budokai 3")
    else:
        logger.info("Unable to connect to the PCSX2 instance. Attempting to reconnect...")

async def pcsx2_sync_task(ctx: Budokai3Context):
    logger.info("Starting Budokai 3 Connector. Attempting to connect to emulator...")
    ctx.game_interface.connect_to_game()
    while not ctx.exit_event.is_set():
        try:
            # await prevent_idents(ctx)
            is_connected = ctx.game_interface.get_connection_state()
            update_connection_status(ctx, is_connected)
            if is_connected:
                await _handle_game_ready(ctx)
            else:
                await _handle_game_not_ready(ctx)
        except ConnectionError:
            ctx.game_interface.disconnect_from_game()
        except Exception as e:
            if isinstance(e, RuntimeError):
                logger.error(str(e))
            await asyncio.sleep(3)
            continue

def party(ctx: Budokai3Context):
    ctx.game_interface.pcsx2_interface.write_int32(Addresses.p1_hp().start_offset, 0x45ff0000)
    ctx.game_interface.pcsx2_interface.write_int32(Addresses.p2_hp().start_offset, 0x45ff0000)

async def prevent_idents(ctx: Budokai3Context):
    start = 0x01050b0
    count = 0
    while count < 168:
        ctx.game_interface.nop_instruction((start + count))
        count += 4

    start = 0x0105168
    count = 0
    while count < 248:
        ctx.game_interface.nop_instruction((start + count))
        count += 4

    start = 0x0105260
    count = 0
    while count < 256:
        ctx.game_interface.nop_instruction((start + count))
        count += 4

    start = 0x0105360
    count = 0
    while count < 160:
        ctx.game_interface.nop_instruction((start + count))
        count += 4

    start = 0x0105400
    count = 0
    while count < 176:
        ctx.game_interface.nop_instruction((start + count))
        count += 4

    start = 0x01054b0
    count = 0
    while count < 224:
        ctx.game_interface.nop_instruction((start + count))
        count += 4

    start = 0x0105b90
    count = 0
    while count < 232:
        ctx.game_interface.nop_instruction((start + count))
        count += 4

    start = 0x0105678
    count = 0
    while count < 216:
        ctx.game_interface.nop_instruction((start + count))
        count += 4

    start = 0x01750
    count = 0
    while count < 208:
        ctx.game_interface.nop_instruction((start + count))
        count += 4

    start = 0x0105820
    count = 0
    while count < 288:
        ctx.game_interface.nop_instruction((start + count))
        count += 4

    start = 0x0105940
    count = 0
    while count < 280:
        ctx.game_interface.nop_instruction((start + count))
        count += 4

async def _handle_game_ready(ctx: Budokai3Context):
    connected_to_server = (ctx.server is not None) and (ctx.slot is not None)
    if connected_to_server:
        init(ctx)
    update(ctx, connected_to_server)

    if ctx.server:
        ctx.last_error_message = None
        if not ctx.slot:
            await asyncio.sleep(1)
            return
        
        if not ctx.game_interface.in_battle() and ctx.game_interface.save_file_loaded(): 
            await handle_received_items(ctx)
        await handle_checked_locations(ctx)
        await handle_check_goal_complete(ctx)

        if ctx.deathlink_enabled:
            await handle_deathlink(ctx)
        await asyncio.sleep(0.1)

    else:
        message = "Waiting for player to connect to server"
        if ctx.last_error_message is not message:
            logger.info(message)
            ctx.last_error_message = message
        await asyncio.sleep(1)

async def handle_check_goal_complete(ctx: Budokai3Context):
    if ctx.

async def _handle_game_not_ready(ctx: Budokai3Context):
    """If the game is not connected, try to reconnect."""
    ctx.game_interface.connect_to_game()
    if ctx.game_interface.current_game: ctx.game_version = ctx.game_interface.current_game
    await asyncio.sleep(3)

def init(ctx: 'Budokai3Context'):
    """
    Gets called every time the game is connected.
    
    Game fixes go here.
    """
    pass

def update(ctx: 'Budokai3Context', ap_connected: bool):
    button_input = ctx.game_interface.pcsx2_interface.read_int8(Addresses.Controller_Shoulder_Buttons.start_offset)
    if button_input == 0xFFFFFFFF: # L1 + L2 + R1 + R2
        ctx.game_interface.return_to_main_menu(True)

async def handle_deathlink(ctx: Budokai3Context):
    if ctx.deathlink_enabled:
        if ctx.deathlink_queued:
            if ctx.game_interface.pcsx2_interface.read_int32(Addresses.P1HP.start_offset) != 0:
                logger.info("Battle detected.")
                ctx.deathlink_queued = False
                ctx.game_interface.pcsx2_interface.write_int32(Addresses.P1HP.start_offset, 0x00000000)
                logger.info("P1 HP reduced. Enjoy!")

def launch():
    import multiprocessing

    Utils.init_logging("Budokai 3 Client")

    async def main():
        multiprocessing.freeze_support()
        logger.info("main")
        parser = get_base_parser()
        parser.add_argument('apdbzb3_file', default="", type=str, nargs="?",
                            help='Path to an apdbzb3 file')
        args = parser.parse_args()

        ctx = Budokai3Context(args.connect, args.password)

        if os.path.isfile(args.apdbzb3_file):
            logger.info("apdbzb3 file supplied, beginning patching process...")
            await patch_and_run_game(args.apdbz3_file)
            ctx.auth = get_name_from_apdbzb3(args.apdbz3_file)

        logger.info("Connecting to server...")
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="Server Loop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        logger.info("Running game...")
        ctx.pcsx2_sync_task = asyncio.create_task(pcsx2_sync_task(ctx), name="PCSX2 Sync")

        await ctx.exit_event.wait()
        ctx.server_address = None

        await ctx.shutdown()

        if ctx.pcsx2_sync_task:
            await asyncio.sleep(3)
            await ctx.pcsx2_sync_task

    import colorama

    colorama.init()

    asyncio.run(main())
    colorama.deinit()


if __name__ == '__main__':
    launch()
