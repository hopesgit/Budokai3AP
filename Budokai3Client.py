from typing import Optional

import Utils
import asyncio
import os
import threading
from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, logger, server_loop, gui_enabled
from . import version
from .data import ROMAddresses
from .data.Items import get_offset_from_name
from .data.Locations import get_all_active_locations
from .Budokai3Interface import Budokai3Interface, ConnectionState
from .NotificationManager import NotificationManager

HUD_MESSAGE_DURATION = 50


class Budokai3CommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

    def _cmd_test_hud(self, *args):
        """Send a message to the game interface."""
        if isinstance(self.ctx, Budokai3Context):
            self.ctx.notification_manager.queue_notification(' '.join(map(str, args)))

    def _cmd_status(self):
        """Display the current PCSX2 connection status."""
        if isinstance(self.ctx, Budokai3Context):
            logger.info(f"Connection status: {'Connected' if self.ctx.is_connected else 'Disconnected'}")
    
    def _cmd_unlock_capsule(self, name):
        """Debug option to unlock a capsule. For testing ONLY"""
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
            logger.info("Done! Be sure to save using Save/Quit in Dragon World or Save in the Options menu to enable the capsule.")

    def _cmd_test_deathlink(self):
        """
        Test function. Doesn't accept any arguments.
        """
        # self.ctx.begin_death_link()
        self.ctx.store_deathlink()


class Budokai3Context(CommonContext):
    command_processor = Budokai3CommandProcessor
    game_interface: Budokai3Interface
    notification_manager: NotificationManager
    game = "Dragon Ball Z Budokai 3"
    items_handling = 0b111
    pcsx2_sync_task = None
    is_connected = ConnectionState.DISCONNECTED
    is_loading: bool = False
    slot_data: dict[str, Utils.Any] | None = None
    last_error_message: Optional[str] = None
    death_link_timer = None
    deathlink_queued: bool = False

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


    def begin_death_link(self):

        def update_p1hp():
            Budokai3Interface.pcsx2_interface.write_int32(ROMAddresses.P1HP.start_offset, 0x00000000)
    

        logger.info('Death Link received.')
        timer = threading.Timer(60.0, logger.info, args=["Death link timer expired."])
        if not self.death_link_timer:
            logger.info('Setting Player 1 HP to 0...')
            self.death_link_timer = timer
            self.death_link_timer.start()
        else:
            logger.info('Death link abuse protection triggered; death cancelled.')

        while self.death_link_timer.is_alive():
            update_p1hp()
            
        self.death_link_timer = None


    def store_deathlink(self):
        self.deathlink_queued = True
        logger.info("Deathlink received.")

        # Check for currently in battle; if so, apply deathlink now
        if self.game_interface.read_p1_hp() > 0:
            self.game_interface.deathlink_set_p1_hp()
            logger.info("Battle detected. HP reduced. Enjoy!")
            self.deathlink_queued = False

        # if not, queue a thing to check until P1HP changes
        # asyncio.create_task(self.await_battle(), name = "Await Battle")
        self.await_battle()


    def await_battle(self):
        import time
        logger.info("Awaiting battle...")
        while self.game_interface.read_p1_hp() == 0:
            time.sleep(1)
        self.game_interface.deathlink_set_p1_hp()
        logger.info("Battle detected. HP reduced. Enjoy!")
        self.deathlink_queued = False
    

def update_connection_status(ctx: Budokai3Context, status: bool):
    if ctx.is_connected == status:
        return

    if status:
        logger.info("Connected to DBZ Budokai 3")
    else:
        logger.info("Unable to connect to the PCSX2 instance, attempting to reconnect...")
    ctx.is_connected = status


async def pcsx2_sync_task(ctx: Budokai3Context):
    logger.info("Starting Budokai 3 Connector, attempting to connect to emulator...")
    ctx.game_interface.connect_to_game()
    while not ctx.exit_event.is_set():
        try:
            is_connected = ctx.game_interface.get_connection_state()
            update_connection_status(ctx, is_connected)
            if is_connected:
                await _handle_game_ready(ctx) # note to self: leave this alone
            else:
                await _handle_game_not_ready(ctx) # note to self: leave this alone
        except ConnectionError:
            ctx.game_interface.disconnect_from_game()
        except Exception as e:
            if isinstance(e, RuntimeError):
                logger.error(str(e))
            await asyncio.sleep(3)
            continue


async def handle_deathlink(ctx: Budokai3Context):
    if ctx.game_interface.get_alive():
        if ctx.is_pending_death_link_reset:
            ctx.is_pending_death_link_reset = False
        if ctx.queued_deaths > 0 and ctx.game_interface.get_pause_state() == 0 and ctx.game_interface.get_ratchet_state() != 97:
            ctx.is_pending_death_link_reset = True
            ctx.game_interface.kill_player()


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
