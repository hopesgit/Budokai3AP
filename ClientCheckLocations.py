from typing import Set
from .data import Locations
from .Budokai3Client import Budokai3Context

async def handle_checked_locations(ctx: Budokai3Context):
    checked_locations: Set = set()
    active_locations = Locations.LOCATIONS
    for location in active_locations:
        if location.address is not None:
            if location.bit_flag_location is not None:
                check = ctx.check_bitflag_loc(location.address, location.bit_flag_location)
                print('after bitflag loc check')
                if check: checked_locations.add(location.location_id)
                print('after loc add')
                continue
            print('after addr...')
            amount = ctx.game_interface.pcsx2_interface.read_int8(location.address)
            print('after amount...')
            if amount == 1:
                checked_locations.add(location.location_id)

    diff = checked_locations.difference(ctx.checked_locations)
    if diff:
        for location in diff:
            loc = Locations.location_id_pairs()[location]
            in_game = location in checked_locations
            if not in_game:
                print(f"Location {location} is not active in game, but is active on server. Saving...")
                ctx.game_interface.activate_location(loc.address, loc.bit_flag_location)
                diff.remove(location) # since this is an item that's on the server but not in game,
                # we don't want to send it to the server again
    await ctx.send_msgs([{"cmd": "LocationChecks", "locations": diff}])
