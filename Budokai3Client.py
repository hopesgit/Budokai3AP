from typing import Optional

import Utils
import asyncio
import os
from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, logger, server_loop, gui_enabled
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

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.game_interface = Budokai3Interface(logger)
        self.notification_manager = NotificationManager(HUD_MESSAGE_DURATION)

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(Budokai3Context, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    # def on_package(self, cmd: str, args: dict):
    #     if cmd == "Connected":
    #         self.slot_data = args["slot_data"]

    #         # Scout all active locations for lookups that may be required later on
    #         all_locations = [loc.location_id for loc in get_all_active_locations(self.slot_data)]
    #         self.locations_scouted = set(all_locations)
    #         Utils.async_start(self.send_msgs([{
    #             "cmd": "LocationScouts",
    #             "locations": list(self.locations_scouted)
    #         }]))

    def run_gui(self):
        from kvui import GameManager

        class Budokai3Manager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago DBZ Budokai 3 Client"

        self.ui = Budokai3Manager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")


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
                await _handle_game_ready(ctx)
            else:
                await _handle_game_not_ready(ctx)
        except ConnectionError:
            ctx.game_interface.disconnect_from_game()
        except Exception as e:
            if isinstance(e, RuntimeError):
                logger.error(str(e))
            else:
                logger.error(traceback.format_exc())
            await asyncio.sleep(3)
            continue



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
            ctx.auth = get_name_from_aprac2(args.apdbz3_file)

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
