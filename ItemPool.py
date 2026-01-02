from BaseClasses import ItemClassification, CollectionState, Item
from .Logic import _get_options
from .data import Items
from .data.Items import *

if TYPE_CHECKING:
    # from . import Budokai3World
    from .Budokai3Client import Budokai3Context


def create_pool(state: CollectionState, player: int):
    prog_chars = _get_options(state, player).progressive_characters != 'off'
    create_greens()
    create_yellows()
    if prog_chars:
        create_reds(prog_chars)
        create_grays(prog_chars)
        create_prog_characters()
    else:
        create_reds()
        create_grays()
    # create_custom(state, player)


def create_greens():
    return GREEN_CAPSULES


def create_yellows():
    return YELLOW_CAPSULES


def create_grays(progressive_characters: bool = False):
    accum = []
    for item in GRAY_CAPSULES:
        if progressive_characters and item in DW_CHARACTERS:
            continue
        else: accum.append(item)

    return accum


def create_reds(progressive_characters: bool = False):
    accum = []
    for item in RED_CAPSULES:
        if progressive_characters and item in DW_RED_CAPSULES:
            continue
        else: accum.append(item)

    return accum


def create_prog_characters():
    return PROGRESSIVE_CAPSULES


def progressive_order(item: ItemData, prog_type: str, count: int):
    id = item.item_id
    index = count - 1
    if not id: raise AttributeError
    if not prog_type: raise AttributeError
    goku_norm = [6, 1, 7, 9, 2, 8, 3, 4, 5, 13, 12, 10, 11]
    goku_attacks = [6, 7, 8, 9, 1, 2, 3, 4, 5, 13, 12, 10, 11]
    goku_transforms = [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 12, 10, 11]
    kgohan_norm = [19, 18, 20]
    kgohan_attacks = [19, 18, 20]
    kgohan_transforms = [18, 19, 20]
    tgohan_norm = [23, 21, 22, 24, 25, 26]
    tgohan_attacks = [23, 24, 25, 21, 22, 26]
    tgohan_transforms = [21, 22, 23, 24, 25, 26]
    gohan_norm = [30, 27, 28, 31, 32, 33]
    gohan_attacks = [30, 31, 32, 27, 28, 29, 33]
    gohan_transforms = [27, 28, 29, 30, 31, 32, 33]
    vegeta_norm = [46, 47, 43, 49, 48, 44, 45, 53, 52, 50, 51]
    vegeta_attacks = [46, 47, 49, 48, 43, 44, 45, 52, 50, 51]
    vegeta_transforms = [43, 44, 45, 46, 47, 49, 48, 53, 52, 50, 51]
    krillin_norm = [66, 67, 65, 68, 69]
    krillin_attacks = [66, 67, 68, 65, 69]
    krillin_transforms = [65, 66, 67, 68, 69]
    piccolo_norm = [72, 74, 70, 71, 73, 75, 76]
    piccolo_attacks = [72, 74, 73, 75, 70, 71, 76]
    piccolo_transforms = [70, 71, 72, 74, 73, 75, 76]
    tien_norm = [77, 78, 79, 80]
    yamcha_norm = [81, 82, 83, 84]
    uub_norm = [99, 100, 101]
    broly_norm = [177, 178, 179, 180, 181]
    broly_attacks = [178, 179, 180, 177, 181]
    broly_transforms = [177, 178, 179, 180, 181]

    # 531 - 541: Goku, Kid Gohan, Teen Gohan, Gohan, Krillin, Piccolo, Vegeta, Tien, Yamcha, Uub, Broly
    match id:
        case 531:
            if prog_type is 'prog_normal': return goku_norm[index]
            if prog_type is 'prog_attacks': return goku_attacks[index]
            if prog_type is "prog_transforms": return goku_transforms[index]
        case 532:
            if prog_type is 'prog_normal': return kgohan_norm[index]
            if prog_type is 'prog_attacks': return kgohan_attacks[index]
            if prog_type is "prog_transforms": return kgohan_transforms[index]
        case 533:
            if prog_type is 'prog_normal': return tgohan_norm[index]
            if prog_type is 'prog_attacks': return tgohan_attacks[index]
            if prog_type is "prog_transforms": return tgohan_transforms[index]
        case 534:
            if prog_type is 'prog_normal': return gohan_norm[index]
            if prog_type is 'prog_attacks': return gohan_attacks[index]
            if prog_type is "prog_transforms": return gohan_transforms[index]
        case 535:
            if prog_type is 'prog_normal': return krillin_norm[index]
            if prog_type is 'prog_attacks': return krillin_attacks[index]
            if prog_type is "prog_transforms": return krillin_transforms[index]
        case 536:
            if prog_type is 'prog_normal': return piccolo_norm[index]
            if prog_type is 'prog_attacks': return piccolo_attacks[index]
            if prog_type is "prog_transforms": return piccolo_transforms[index]
        case 537:
            if prog_type is 'prog_normal': return vegeta_norm[index]
            if prog_type is 'prog_attacks': return vegeta_attacks[index]
            if prog_type is "prog_transforms": return vegeta_transforms[index]
        case 538:
            return tien_norm[index]
        case 539:
            return yamcha_norm[index]
        case 540:
            return uub_norm[index]
        case 541:
            if prog_type is 'prog_normal': return broly_norm[index]
            if prog_type is 'prog_attacks': return broly_attacks[index]
            if prog_type is "prog_transforms": return broly_transforms[index]
    return None


def add_to_starting_pool(ctx: Budokai3Context, item: Item):
    pass


def get_classification(item: ItemData):
    if 'Progressive' in item.name: 
        return ItemClassification.progression
    if (item.name in Items.item_name_groups()["Fighters"] or item.name in Items.item_name_groups()["Tournament"]
    or item.name in Items.item_name_groups()["Training"] or item.name in Items.item_name_groups()["Cards"]
    or item.name in Items.item_name_groups()["Modes"] or item.name in Items.item_name_groups()["Difficulties"]):
        return ItemClassification.progression
    if item.name == "Senzu Bean":
        return ItemClassification.progression
    items_useful_for_story_reenactments = ["Kaioken", "Super Saiyan (Goku)", "Spirit Bomb (Goku)", "Special Beam Cannon",
                                           "Ki Blast Cannon", "Masenko", "Destructo Disc (Krillin)", "Sync With Nail", 
                                           "Fuse With Kami", "Super Saiyan (Vegeta)", "Final Flash", "Super Saiyan (Teen Gohan)",
                                           "Super Saiyan 2 (Teen Gohan)", "Father-Son Kamehameha", "Super Saiyan (Gohan)", 
                                           "Super Saiyan 2 (Gohan)", "Elder Kai Unlock Ability", "Super Saiyan 2 (Vegeta)", 
                                           "Super Saiyan 4 (Goku)", "Super Saiyan 3", "Legendary Super Saiyan", "Gigantic Meteor",
                                           "Ki Cannon"]
    if item in items_useful_for_story_reenactments:
        return ItemClassification.progression
    
    return ItemClassification.filler
