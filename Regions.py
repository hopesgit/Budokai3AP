import typing

from BaseClasses import Region, MultiWorld
from .Logic import *
from .data.Locations import GOKU_LOCS, GOKU_WISH_LOCS, DRAGON_ARENA_LOCS, WT_LOCS, SHOP_LOCS


class Budokai3Region(Region):
    game = "Dragon Ball Z Budokai 3"


def create_regions(world: MultiWorld, player: int):
    menu = Budokai3Region("Menu", player, world)
    dw_goku = Budokai3Region("Dragon World - Goku", player, world)
    # dw_kgohan = Budokai3Region("Dragon World - Kid Gohan", player, world)
    # dw_tgohan = Budokai3Region("Dragon World - Teen Gohan", player, world)
    # dw_gohan = Budokai3Region("Dragon World - Gohan", player, world)
    # dw_krillin = Budokai3Region("Dragon World - Krillin", player, world)
    # dw_piccolo = Budokai3Region("Dragon World - Piccolo", player, world)
    # dw_tien = Budokai3Region("Dragon World - Tien", player, world)
    # dw_yamcha = Budokai3Region("Dragon World - Yamcha", player, world)
    # dw_vegeta = Budokai3Region("Dragon World - Vegeta", player, world)
    # dw_uub = Budokai3Region("Dragon World - Uub", player, world)
    # dw_broly = Budokai3Region("Dragon World - Broly", player, world)
    wish_goku = Budokai3Region("Shenron - Goku", player, world)
    # wish_kgohan = Budokai3Region("Shenron - Kid Gohan", player, world)
    # wish_tgohan = Budokai3Region("Shenron - Teen Gohan", player, world)
    # wish_gohan = Budokai3Region("Shenron - Gohan", player, world)
    # wish_krillin = Budokai3Region("Shenron - Krillin", player, world)
    # wish_piccolo = Budokai3Region("Shenron - Piccolo", player, world)
    # wish_tien = Budokai3Region("Shenron - Tien", player, world)
    # wish_yamcha = Budokai3Region("Shenron - Yamcha", player, world)
    # wish_vegeta = Budokai3Region("Shenron - Vegeta", player, world)
    # wish_uub = Budokai3Region("Shenron - Uub", player, world)
    # wish_broly = Budokai3Region("Shenron - Broly", player, world)
    credits = Budokai3Region("Credits", player, world)
    dragon_arena = Budokai3Region("Dragon Arena", player, world)
    shop = Budokai3Region("Shop", player, world)
    training = Budokai3Region("Training", player, world)
    tournament = Budokai3Region("Tournament", player, world)

    dw_goku.add_event(
        location_name="Dragon World Goku Cleared", 
        item_name="Event - Dragon World Goku Cleared"
    )
    # dw_kgohan.add_event(
    #     "Dragon World Kid Gohan Cleared", 
    #     "Event - Dragon World Kid Gohan Cleared"
    # )
    # dw_tgohan.add_event(
    #     "Dragon World Teen Gohan Cleared", 
    #     "Event - Dragon World Teen Gohan Cleared"
    # )
    # dw_gohan.add_event(
    #     "Dragon World Gohan Cleared", 
    #     "Event - Dragon World Gohan Cleared"
    # )
    # dw_krillin.add_event(
    #     "Dragon World Krillin Cleared", 
    #     "Event - Dragon World Krillin Cleared"
    # )
    # dw_piccolo.add_event(
    #     "Dragon World Piccolo Cleared", 
    #     "Event - Dragon World Piccolo Cleared"
    # )
    # dw_tien.add_event(
    #     "Dragon World Tien Cleared", 
    #     "Event - Dragon World Tien Cleared"
    # )
    # dw_yamcha.add_event(
    #     "Dragon World Yamcha Cleared", 
    #     "Event - Dragon World Yamcha Cleared"
    # )
    # dw_vegeta.add_event(
    #     "Dragon World Vegeta Cleared", 
    #     "Event - Dragon World Vegeta Cleared"
    # )
    # dw_uub.add_event(
    #     "Dragon World Uub Cleared", 
    #     "Event - Dragon World Uub Cleared"
    # )
    # dw_broly.add_event(
    #     "Dragon World Broly Cleared", 
    #     "Event - Dragon World Broly Cleared"
    # )

    menu.add_exits(
        exits=["Dragon World - Goku", #"Dragon World - Kid Gohan", "Dragon World - Teen Gohan", "Dragon World - Gohan",
               # "Dragon World - Krillin", "Dragon World - Piccolo", "Dragon World - Vegeta", "Dragon World - Tien", 
               # "Dragon World - Yamcha", "Dragon World - Uub", "Dragon World - Broly", 
               "Dragon Arena", "Training", "Tournament"],
        rules={
            "Dragon World - Goku": lambda multiworld: has_goku(multiworld, player),
            # "Dragon World - Kid Gohan": lambda multiworld: has_kid_gohan(multiworld, player),
            # "Dragon World - Teen Gohan": lambda multiworld: has_teen_gohan(multiworld, player),
            # "Dragon World - Gohan": lambda multiworld: has_gohan(multiworld, player),
            # "Dragon World - Krillin": lambda multiworld: has_krillin(multiworld, player),
            # "Dragon World - Piccolo": lambda multiworld: has_piccolo(multiworld, player),
            # "Dragon World - Tien": lambda multiworld: has_tien(multiworld, player),
            # "Dragon World - Yamcha": lambda multiworld: has_yamcha(multiworld, player),
            # "Dragon World - Vegeta": lambda multiworld: has_vegeta(multiworld, player),
            # "Dragon World - Uub": lambda multiworld: has_uub(multiworld, player),
            # "Dragon World - Broly": lambda multiworld: has_broly(multiworld, player),
            "Tournament": lambda multiworld: (has_tournament_novice() or has_tournament_adept(multiworld, player) or
                                              has_tournament_advanced(multiworld, player) or has_cell_games(multiworld, player)),
            "Shop": lambda multiworld: True,
            "Dragon Arena": lambda multiworld: has_dragon_arena(multiworld, player)
        }
    )

    dw_goku.add_locations({loc.name: loc.location_id for loc in GOKU_LOCS})
    dw_goku.add_exits(
        exits=["Menu", "Credits", "Shenron - Goku"],
        rules={
            "Menu": lambda multiworld: True,
            "Credits": lambda multiworld: can_goku(multiworld, player),
            "Shenron - Goku": lambda multiworld: can_wish_goku(multiworld, player) 
        })
    
    wish_goku.add_locations({loc.name: loc.location_id for loc in GOKU_WISH_LOCS})
    wish_goku.add_exits(
        exits=["Credits"],
        rules={
            "Credits": lambda multiworld: True
        }
    )
    
    credits.add_exits(
        exits=["Menu"],
        rules={
            "Menu": lambda multiworld: True
        }
    )

    dragon_arena.add_locations({loc.name: loc.location_id for loc in DRAGON_ARENA_LOCS})
    dragon_arena.add_exits(
        exits=["Menu"],
        rules={
            "Menu": lambda multiworld: True
        }
    )

    tournament.add_locations({loc.name: loc.location_id for loc in WT_LOCS})
    tournament.add_exits(
        exits=["Menu"],
        rules={
            "Menu": lambda multiworld: True
        }
    )

    shop.add_locations({loc.name: loc.location_id for loc in SHOP_LOCS})
    shop.add_exits(
        exits=["Menu"],
        rules={
            "Menu": lambda multiworld: True
        }
    )

    world.regions.append(menu)
    world.regions.append(credits)
    world.regions.append(dragon_arena)
    world.regions.append(dw_goku)
    # world.regions.append(dw_kgohan)
    # world.regions.append(dw_tgohan)
    # world.regions.append(dw_gohan)
    # world.regions.append(dw_krillin)
    # world.regions.append(dw_piccolo)
    # world.regions.append(dw_tien)
    # world.regions.append(dw_yamcha)
    # world.regions.append(dw_vegeta)
    # world.regions.append(dw_uub)
    # world.regions.append(dw_broly)
    world.regions.append(wish_goku)
    # world.regions.append(wish_kgohan)
    # world.regions.append(wish_tgohan)
    # world.regions.append(wish_gohan)
    # world.regions.append(wish_krillin)
    # world.regions.append(wish_piccolo)
    # world.regions.append(wish_tien)
    # world.regions.append(wish_yamcha)
    # world.regions.append(wish_vegeta)
    # world.regions.append(wish_uub)
    # world.regions.append(wish_broly)
    world.regions.append(shop)
    world.regions.append(training)    