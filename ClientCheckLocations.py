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
        if location.address is not None:
            if location.bit_flag_location is not None:
                check = ctx.check_bitflag_loc(location.address, location.bit_flag_location)
                if check: checked_locations.add(location.location_id)
            addr = location.checked_flag_address(ctx.game_interface.addresses)
            if ctx.game_interface.pcsx2_interface.read_int8(addr) != 0:
                checked_locations.add(location.location_id)
    
    checked_locations = checked_locations.difference(ctx.checked_locations)
    await ctx.send_msgs([{"cmd": "LocationChecks", "locations": checked_locations}])
