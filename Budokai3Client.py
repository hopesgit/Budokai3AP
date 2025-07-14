from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, logger, server_loop, gui_enabled



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




class Budokai3Context(CommonContext):
    is_pending_death_link_reset = False
    command_processor = Budokai3CommandProcessor
    game_interface: Budokai3Interface
    notification_manager: NotificationManager
    game = "Dragon Ball Z Budokai 3"
    items_handling = 0b111
    pcsx2_sync_task = None
    is_connected = ConnectionState.DISCONNECTED
    is_loading: bool = False
    slot_data: dict[str, Utils.Any] = None
    last_error_message: Optional[str] = None
    death_link_enabled = False
    queued_deaths: int = 0
    previous_decoy_glove_ammo: int = 0

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.game_interface = Budokai3Interface(logger)
        self.notification_manager = NotificationManager(HUD_MESSAGE_DURATION)

    def on_deathlink(self, data: Utils.Dict[str, Utils.Any]) -> None:
        super().on_deathlink(data)
        if self.death_link_enabled:
            self.queued_deaths += 1
            cause = data.get("cause", "")
            if cause:
                self.notification_manager.queue_notification(f"DeathLink: {cause}")
            else:
                self.notification_manager.queue_notification(f"DeathLink: Received from {data['source']}")

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(Budokai3Context, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            self.slot_data = args["slot_data"]
            # Set death link tag if it was requested in options
            if "death_link" in args["slot_data"]:
                self.death_link_enabled = bool(args["slot_data"]["death_link"])
                Utils.async_start(self.update_death_link(
                    bool(args["slot_data"]["death_link"])))

            # Scout all active locations for lookups that may be required later on
            all_locations = [loc.location_id for loc in get_all_active_locations(self.slot_data)]
            self.locations_scouted = set(all_locations)
            Utils.async_start(self.send_msgs([{
                "cmd": "LocationScouts",
                "locations": list(self.locations_scouted)
            }]))

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
    Utils.init_logging("RAC2 Client")

    async def main():
        multiprocessing.freeze_support()
        logger.info("main")
        parser = get_base_parser()
        parser.add_argument('aprac2_file', default="", type=str, nargs="?",
                            help='Path to an aprac2 file')
        args = parser.parse_args()

        ctx = Rac2Context(args.connect, args.password)

        if os.path.isfile(args.aprac2_file):
            logger.info("aprac2 file supplied, beginning patching process...")
            await patch_and_run_game(args.aprac2_file)
            ctx.auth = get_name_from_aprac2(args.aprac2_file)

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