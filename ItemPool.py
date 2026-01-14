from BaseClasses import ItemClassification, CollectionState
from .Logic import _get_options
from .data import Items
from .data.Items import *


GOKU_NORM = [GOKU.code, KAME_GOKU.code, KAIOKEN.code, DRAG_FIST_GOKU.code, SPIRIT_BOMB_GOKU.code, SSJ_GOKU.code, 
                WARP_KAME_GOKU.code, SSJ2_GOKU.code, SSJ3_GOKU.code, SSJ4_GOKU.code, BREAK_GOKU.code, VEGITO_GOKU.code, 
                GOGETA_GOKU.code, SSJ4_GOGETA_GOKU.code]
GOKU_ATTACKS = [GOKU.code, KAME_GOKU.code, DRAG_FIST_GOKU.code, WARP_KAME_GOKU.code, SPIRIT_BOMB_GOKU.code, 
                KAIOKEN.code, SSJ_GOKU.code, SSJ2_GOKU.code, SSJ3_GOKU.code, SSJ4_GOKU.code, BREAK_GOKU.code, 
                VEGITO_GOKU.code, GOGETA_GOKU.code, SSJ4_GOGETA_GOKU.code]
GOKU_TRANSFORMS = [GOKU.code, KAIOKEN.code, SSJ_GOKU.code, SSJ2_GOKU.code, SSJ3_GOKU.code, SSJ4_GOKU.code, 
                    KAME_GOKU.code, DRAG_FIST_GOKU.code, WARP_KAME_GOKU.code, SPIRIT_BOMB_GOKU.code, BREAK_GOKU.code, 
                    VEGITO_GOKU.code, GOGETA_GOKU.code, SSJ4_GOGETA_GOKU.code]
KGOHAN_NORM = [KID_GOHAN.code, MASENKO.code, POTENTIAL_KGOHAN.code, BREAK_KGOHAN.code]
KGOHAN_ATTACKS = [KID_GOHAN.code, MASENKO.code, POTENTIAL_KGOHAN.code, BREAK_KGOHAN.code]
KGOHAN_TRANSFORMS = [KID_GOHAN.code, POTENTIAL_KGOHAN.code, MASENKO.code, BREAK_KGOHAN.code]
TGOHAN_NORM = [TEEN_GOHAN.code, KAME_TGOHAN.code, SSJ_TGOHAN.code, SOAR_TGOHAN.code, SSJ2_TGOHAN.code, FS_KAME.code, 
                BREAK_TGOHAN.code]
TGOHAN_ATTACKS = [TEEN_GOHAN.code, KAME_TGOHAN.code, SOAR_TGOHAN.code, FS_KAME.code, SSJ_TGOHAN.code, SSJ2_TGOHAN.code, 
                    BREAK_TGOHAN.code]
TGOHAN_TRANSFORMS = [TEEN_GOHAN.code, SSJ_TGOHAN.code, SSJ2_TGOHAN.code, KAME_TGOHAN.code, SOAR_TGOHAN.code, 
                        FS_KAME.code, BREAK_TGOHAN.code]
GOHAN_NORM = [GOHAN.code, SSJ_GOHAN.code, KAME_GOHAN.code, SSJ2_GOHAN.code, SOAR_GOHAN.code, SUPER_KAME_GOHAN.code, 
                ELDER_UNLOCK.code, BREAK_GOHAN.code]
GOHAN_ATTACKS = [GOHAN.code, KAME_GOHAN.code, SOAR_GOHAN.code, SUPER_KAME_GOHAN.code, SSJ_GOHAN.code, SSJ2_GOHAN.code, 
                    ELDER_UNLOCK.code, BREAK_GOHAN.code]
GOHAN_TRANSFORMS = [GOHAN.code, SSJ_GOHAN.code, SSJ2_GOHAN.code, ELDER_UNLOCK.code, KAME_GOHAN.code, SOAR_GOHAN.code, 
                    SUPER_KAME_GOHAN.code, BREAK_GOHAN.code]
VEGETA_NORM = [VEGETA.code, GALICK.code, FINAL_IMPACT.code, SSJ_VEGETA.code, BIG_BANG.code, FINAL_FLASH.code, 
                SSJ2_VEGETA.code, SSJ4_VEGETA.code, BREAK_VEGETA.code, VEGITO_VEGETA.code, GOGETA_VEGETA.code, SSJ4_GOGETA_VEGETA.code]
VEGETA_ATTACKS = [VEGETA.code, GALICK.code, FINAL_IMPACT.code, BIG_BANG.code, FINAL_FLASH.code, SSJ_VEGETA.code, 
                    SSJ2_VEGETA.code, SSJ4_VEGETA.code, BREAK_VEGETA.code, VEGITO_VEGETA.code, GOGETA_VEGETA.code, SSJ4_GOGETA_VEGETA.code]
VEGETA_TRANSFORMS = [VEGETA.code, SSJ_VEGETA.code, SSJ2_VEGETA.code, SSJ4_VEGETA.code, GALICK.code, FINAL_IMPACT.code, 
                        BIG_BANG.code, FINAL_FLASH.code, BREAK_VEGETA.code, VEGITO_VEGETA.code, GOGETA_VEGETA.code, SSJ4_GOGETA_VEGETA.code]
KRILLIN_NORM = [KRILLIN.code, KAME_KRILLIN.code, DD_KRILLIN.code, POTENTIAL_KRILLIN.code, FIERCE_DD.code, BREAK_KRILLIN.code]
KRILLIN_ATTACKS = [KRILLIN.code, KAME_KRILLIN.code, DD_KRILLIN.code, FIERCE_DD.code, POTENTIAL_KRILLIN.code, BREAK_KRILLIN.code]
KRILLIN_TRANSFORMS = [KRILLIN.code, POTENTIAL_KRILLIN.code, KAME_KRILLIN.code, DD_KRILLIN.code, FIERCE_DD.code, BREAK_KRILLIN.code]
PICCOLO_NORM = [PICCOLO.code, DEST_WAVE.code, SBEAM_CANNON.code, SYNC_NAIL.code, FUSE_KAMI.code, LGRENADE.code, 
                HZGRENADE.code, BREAK_PICCOLO.code]
PICCOLO_ATTACKS = [PICCOLO.code, DEST_WAVE.code, SBEAM_CANNON.code, LGRENADE.code, HZGRENADE.code, SYNC_NAIL.code, 
                    FUSE_KAMI.code, BREAK_PICCOLO.code]
PICCOLO_TRANSFORMS = [PICCOLO.code, SYNC_NAIL.code, FUSE_KAMI.code, DEST_WAVE.code, SBEAM_CANNON.code, LGRENADE.code, 
                        HZGRENADE.code, BREAK_PICCOLO.code]
TIEN_NORM = [TIEN.code, BLAST_CANNON.code, DODON.code, NEO_BLAST_CANNON.code, BREAK_TIEN.code]
YAMCHA_NORM = [YAMCHA.code, KAME_YAMCHA.code, WOLF_FANG.code, SPIRIT_BALL.code, BREAK_YAMCHA.code]
UUB_NORM = [UUB.code, KI_CANNON.code, FIERCE_FLURRY.code, BREAK_UUB.code]
BROLY_NORM = [BROLY.code, LSSJ_BROLY.code, BLASTER_SHELL.code, GIGANT_PRESS.code, GIGANT_METEOR.code, BREAK_BROLY.code]
BROLY_ATTACKS = [BROLY.code, BLASTER_SHELL.code, GIGANT_PRESS.code, GIGANT_METEOR.code, LSSJ_BROLY.code, BREAK_BROLY.code]
BROLY_TRANSFORMS = [BROLY.code, LSSJ_BROLY.code, BLASTER_SHELL.code, GIGANT_PRESS.code, GIGANT_METEOR.code, BREAK_BROLY.code]




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
        if progressive_characters and item in DU_CHARACTERS:
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


def progressive_order(item: Capsule, prog_type: str, count: int):
    id = item.code
    index = count - 1
    if not id: raise AttributeError
    if not prog_type: raise AttributeError
    # 531 - 541: Goku, Kid Gohan, Teen Gohan, Gohan, Krillin, Piccolo, Vegeta, Tien, Yamcha, Uub, Broly
    match id:
        case PROGRESSIVE_GOKU.code:
            if prog_type == 'prog_normal': return GOKU_NORM[index]
            if prog_type == 'prog_attacks': return GOKU_ATTACKS[index]
            if prog_type == "prog_transforms": return GOKU_TRANSFORMS[index]
        case PROGRESSIVE_KID_GOHAN.code:
            if prog_type == 'prog_normal': return KGOHAN_NORM[index]
            if prog_type == 'prog_attacks': return KGOHAN_ATTACKS[index]
            if prog_type == "prog_transforms": return KGOHAN_TRANSFORMS[index]
        case PROGRESSIVE_TEEN_GOHAN.code:
            if prog_type == 'prog_normal': return TGOHAN_NORM[index]
            if prog_type == 'prog_attacks': return TGOHAN_ATTACKS[index]
            if prog_type == "prog_transforms": return TGOHAN_TRANSFORMS[index]
        case PROGRESSIVE_GOHAN.code:
            if prog_type == 'prog_normal': return GOHAN_NORM[index]
            if prog_type == 'prog_attacks': return GOHAN_ATTACKS[index]
            if prog_type == "prog_transforms": return GOHAN_TRANSFORMS[index]
        case PROGRESSIVE_KRILLIN.code:
            if prog_type == 'prog_normal': return KRILLIN_NORM[index]
            if prog_type == 'prog_attacks': return KRILLIN_ATTACKS[index]
            if prog_type == "prog_transforms": return KRILLIN_TRANSFORMS[index]
        case PROGRESSIVE_PICCOLO.code:
            if prog_type == 'prog_normal': return PICCOLO_NORM[index]
            if prog_type == 'prog_attacks': return PICCOLO_ATTACKS[index]
            if prog_type == "prog_transforms": return PICCOLO_TRANSFORMS[index]
        case PROGRESSIVE_VEGETA.code:
            if prog_type == 'prog_normal': return VEGETA_NORM[index]
            if prog_type == 'prog_attacks': return VEGETA_ATTACKS[index]
            if prog_type == "prog_transforms": return VEGETA_TRANSFORMS[index]
        case PROGRESSIVE_TIEN.code:
            return TIEN_NORM[index]
        case PROGRESSIVE_YAMCHA.code:
            return YAMCHA_NORM[index]
        case PROGRESSIVE_UUB.code:
            return UUB_NORM[index]
        case PROGRESSIVE_BROLY.code:
            if prog_type == 'prog_normal': return BROLY_NORM[index]
            if prog_type == 'prog_attacks': return BROLY_ATTACKS[index]
            if prog_type == "prog_transforms": return BROLY_TRANSFORMS[index]
    return None


def get_classification(item: Capsule):
    if 'Progressive' in item.name: 
        return ItemClassification.progression
    if (item.name in Items.item_name_groups()["Fighters"] or item.name in Items.item_name_groups()["Tournament"]
    or item.name in Items.item_name_groups()["Training"] or item.name in Items.item_name_groups()["Cards"]
    or item.name in Items.item_name_groups()["Modes"] or item.name in Items.item_name_groups()["Difficulties"]):
        return ItemClassification.progression
    items_useful_for_story_reenactments = [
        "Goku: Kaioken", "Goku: Super Saiyan", "Goku: Spirit Bomb", 
        "Piccolo: Special Beam Cannon", "Tien: Ki Blast Cannon", 
        "Kid Gohan: Masenko", "Krillin: Destructo Disc", "Piccolo: Sync With Nail", 
        "Piccolo: Fuse With Kami", "Vegeta: Super Saiyan", "Vegeta: Final Flash", 
        "Teen Gohan: Super Saiyan", "Teen Gohan: Super Saiyan 2", 
        "Teen Gohan: Father-Son Kamehameha", "Gohan: Super Saiyan", 
        "Gohan: Super Saiyan 2", "Gohan: Elder Kai Unlock Ability", 
        "Vegeta: Super Saiyan 2", "Vegeta: Super Saiyan 4", 
        "Goku: Super Saiyan 3", "Broly: Legendary Super Saiyan", 
        "Broly: Gigantic Meteor", "Uub: Ki Cannon", "Senzu Bean"]
    if item.name in items_useful_for_story_reenactments:
        return ItemClassification.progression
    
    return ItemClassification.filler
