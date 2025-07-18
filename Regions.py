import typing
from BaseClasses import Region, CollectionState, Location

from Logic import *
from .data import Items, Locations

if typing.TYPE_CHECKING:
    from . import Budokai3World

class Budokai3Region(Region):
    game = "Dragon Ball Z Budokai 3"


def create_regions(world:'Budokai3World'):
    menu = Region("Menu", world.player, world.multiworld)
    world.multiworld.regions.append(menu)

    dragon_world = Region("Dragon World", world.player, world.multiworld)
    world.multiworld.regions.append(dragon_world)
    menu.connect(dragon_world, None, None) # no access rule needed for base DW

    congrats = Region("Congratulations", world.player, world.multiworld)
    world.multiworld.regions.append(congrats)
    congrats.exit(menu)

    credits = Region("Credits", world.player, world.multiworld)
    world.multiworld.regions.append(credits)
    credits.exit(congrats)
    credits.exit(menu)

    wish = Region("Shenron", world.player, world.multiworld)
    world.multiworld.regions.append(wish)
    wish.exit(credits)

    dw_goku = Region("Dragon World - Goku", world.player, world.multiworld)
    dw_goku.place_locked_item("Event - Dragon World Goku Cleared")
    world.multiworld.regions.append(dw_goku)
    dragon_world.connect(dw_goku, None, has_goku)
    dw_goku.exit(wish, None, can_wish_goku)
    dw_goku.exit(credits, None, can_wish_goku)

    dw_kid_gohan = Region("Dragon World - Kid Gohan", world.player, world.multiworld)
    dw_kid_gohan.place_locked_item("Event - Dragon World Kid Gohan Cleared")
    world.multiworld.regions.append(dw_kid_gohan)
    dragon_world.connect(dw_kid_gohan, None, has_kid_gohan)

    dw_teen_gohan = Region("Dragon World - Teen Gohan", world.player, world.multiworld)
    dw_teen_gohan.place_locked_item("Event - Dragon World Teen Gohan Cleared")
    world.multiworld.regions.append(dw_teen_gohan)
    dragon_world.connect(dw_teen_gohan, None, has_teen_gohan)

    dw_gohan = Region("Dragon World - Gohan", world.player, world.multiworld)
    dw_gohan.place_locked_item("Event - Dragon World Gohan Cleared")
    world.multiworld.regions.append(dw_gohan)
    dragon_world.connect(dw_gohan, None, has_gohan)







    dragon_arena = Region("Dragon Arena", world.player, world.multiworld)
    world.multiworld.regions.append(dragon_arena)
    menu.connect(dragon_arena, None, has_dragon_arena)

    shop = Region("Shop", world.player, world.multiworld)
    world.multiworld.regions.append(shop)
    menu.connect(shop, None, can_shop)

    training = Region("Training", world.player, world.multiworld)
    world.multiworld.regions.append(training)
    menu.connect(training, None, None)

