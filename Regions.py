import typing

from BaseClasses import Region, MultiWorld
from Logic import *

if typing.TYPE_CHECKING:
    from . import Budokai3World

class Budokai3Region(Region):
    game = "Dragon Ball Z Budokai 3"


def create_regions(world, player):
    menu = Budokai3Region("Menu", world.player, world.multiworld)
    credits = Budokai3Region("Credits", world.player, world.multiworld)
    wish_goku = Budokai3Region("Shenron - Goku", world.player, world.multiworld)
    wish_kgohan = Budokai3Region("Shenron - Kid Gohan", world.player, world.multiworld)
    wish_tgohan = Budokai3Region("Shenron - Teen Gohan", world.player, world.multiworld)
    wish_gohan = Budokai3Region("Shenron - Gohan", world.player, world.multiworld)
    wish_krillin = Budokai3Region("Shenron - Krillin", world.player, world.multiworld)
    wish_piccolo = Budokai3Region("Shenron - Piccolo", world.player, world.multiworld)
    wish_tien = Budokai3Region("Shenron - Tien", world.player, world.multiworld)
    wish_yamcha = Budokai3Region("Shenron - Yamcha", world.player, world.multiworld)
    wish_vegeta = Budokai3Region("Shenron - Vegeta", world.player, world.multiworld)
    wish_uub = Budokai3Region("Shenron - Uub", world.player, world.multiworld)
    wish_broly = Budokai3Region("Shenron - Broly", world.player, world.multiworld)
    dw_goku = Budokai3Region("Dragon World - Goku", world.player, world.multiworld)
    dw_kgohan = Budokai3Region("Dragon World - Kid Gohan", world.player, world.multiworld)
    dw_tgohan = Budokai3Region("Dragon World - Teen Gohan", world.player, world.multiworld)
    dw_gohan = Budokai3Region("Dragon World - Gohan", world.player, world.multiworld)
    dw_krillin = Budokai3Region("Dragon World - Krillin", world.player, world.multiworld)
    dw_piccolo = Budokai3Region("Dragon World - Piccolo", world.player, world.multiworld)
    dw_tien = Budokai3Region("Dragon World - Tien", world.player, world.multiworld)
    dw_yamcha = Budokai3Region("Dragon World - Yamcha", world.player, world.multiworld)
    dw_vegeta = Budokai3Region("Dragon World - Vegeta", world.player, world.multiworld)
    dw_uub = Budokai3Region("Dragon World - Uub", world.player, world.multiworld)
    dw_broly = Budokai3Region("Dragon World - Broly", world.player, world.multiworld)
    dragon_arena = Budokai3Region("Dragon Arena", world.player, world.multiworld)
    shop = Budokai3Region("Shop", world.player, world.multiworld)
    training = Budokai3Region("Training", world.player, world.multiworld)

    dw_goku.add_event(
        location_name="Dragon World Goku Cleared", 
        item_name="Event - Dragon World Goku Cleared"
    )
    dw_kgohan.add_event(
        "Dragon World Kid Gohan Cleared", 
        "Event - Dragon World Kid Gohan Cleared"
    )
    dw_tgohan.add_event(
        "Dragon World Teen Gohan Cleared", 
        "Event - Dragon World Teen Gohan Cleared"
    )
    dw_gohan.add_event(
        "Dragon World Gohan Cleared", 
        "Event - Dragon World Gohan Cleared"
    )
    dw_krillin.add_event(
        "Dragon World Krillin Cleared", 
        "Event - Dragon World Krillin Cleared"
    )
    dw_piccolo.add_event(
        "Dragon World Piccolo Cleared", 
        "Event - Dragon World Piccolo Cleared"
    )
    dw_tien.add_event(
        "Dragon World Tien Cleared", 
        "Event - Dragon World Tien Cleared"
    )
    dw_yamcha.add_event(
        "Dragon World Yamcha Cleared", 
        "Event - Dragon World Yamcha Cleared"
    )
    dw_vegeta.add_event(
        "Dragon World Vegeta Cleared", 
        "Event - Dragon World Vegeta Cleared"
    )
    dw_uub.add_event(
        "Dragon World Uub Cleared", 
        "Event - Dragon World Uub Cleared"
    )
    dw_broly.add_event(
        "Dragon World Broly Cleared", 
        "Event - Dragon World Broly Cleared"
    )

    world.multiworld.regions.append(menu)
    world.multiworld.regions.append(credits)
    world.multiworld.regions.append(dragon_arena)
    world.multiworld.regions.append(dw_goku)
    world.multiworld.regions.append(dw_kgohan)
    world.multiworld.regions.append(dw_tgohan)
    world.multiworld.regions.append(dw_gohan)
    world.multiworld.regions.append(dw_krillin)
    world.multiworld.regions.append(dw_piccolo)
    world.multiworld.regions.append(dw_tien)
    world.multiworld.regions.append(dw_yamcha)
    world.multiworld.regions.append(dw_vegeta)
    world.multiworld.regions.append(dw_uub)
    world.multiworld.regions.append(dw_broly)
    world.multiworld.regions.append(wish_goku)
    world.multiworld.regions.append(wish_kgohan)
    world.multiworld.regions.append(wish_tgohan)
    world.multiworld.regions.append(wish_gohan)
    world.multiworld.regions.append(wish_krillin)
    world.multiworld.regions.append(wish_piccolo)
    world.multiworld.regions.append(wish_tien)
    world.multiworld.regions.append(wish_yamcha)
    world.multiworld.regions.append(wish_vegeta)
    world.multiworld.regions.append(wish_uub)
    world.multiworld.regions.append(wish_broly)
    world.multiworld.regions.append(shop)
    world.multiworld.regions.append(training)    