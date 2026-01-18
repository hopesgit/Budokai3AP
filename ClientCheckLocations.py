from typing import Set

from .TextManager import get_rich_item_name
from . import LocationPool
from .Budokai3Client import Budokai3Context

async def handle_checked_locations(ctx: Budokai3Context):
    checked_locations: Set = set()
    if not ctx.game_interface.save_file_loaded():
        return
    
    active_locations = LocationPool.get_active_locations(ctx.slot_data)
    for location in active_locations:
        if location.checked_flag_address is not None:
            addr = location.checked_flag_address(ctx.game_interface.addresses)
            if ctx.game_interface.pcsx2_interface.read_int8(addr) != 0:
                checked_locations.add(location.location_id)
    
    checked_locations = checked_locations.difference(ctx.checked_locations)
    await ctx.send_msgs([{"cmd": "LocationChecks", "locations": checked_locations}])
    for location_id in checked_locations:
        location = next(loc for loc in active_locations if loc.location_id == location_id)
        ctx.game_interface.logger.info(f"Location checked: {location.name}")
        # if location.is_vendor:
        #     ctx.game_interface.vendor.notify_item_bought(location_id)
        #     item_was_bought = True

        net_item = ctx.locations_info.get(location_id, None)
        if net_item is not None and net_item.player != ctx.slot:
            item_to_player_names = get_rich_item_name(ctx, net_item, True)
            ctx.notification_manager.queue_notification(f"Sent {item_to_player_names}")

    # if item_was_bought:
        # ctx.game_interface.vendor.refresh(ctx)