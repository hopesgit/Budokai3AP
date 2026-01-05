from BaseClasses import ItemClassification, CollectionState
from .Logic import _get_options
from .data import Items
from .data.Items import *


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
    goku_norm = [GOKU.code, KAME_GOKU.code, KAIOKEN.code, DRAG_FIST_GOKU.code, SPIRIT_BOMB_GOKU.code, SSJ_GOKU.code, 
                 WARP_KAME_GOKU.code, SSJ2_GOKU.code, SSJ3_GOKU.code, SSJ4_GOKU.code, BREAK_GOKU.code, VEGITO_GOKU.code, 
                 GOGETA_GOKU.code, SSJ4_GOGETA_GOKU.code]
    goku_attacks = [GOKU.code, KAME_GOKU.code, DRAG_FIST_GOKU.code, WARP_KAME_GOKU.code, SPIRIT_BOMB_GOKU.code, 
                    KAIOKEN.code, SSJ_GOKU.code, SSJ2_GOKU.code, SSJ3_GOKU.code, SSJ4_GOKU.code, BREAK_GOKU.code, 
                    VEGITO_GOKU.code, GOGETA_GOKU.code, SSJ4_GOGETA_GOKU.code]
    goku_transforms = [GOKU.code, KAIOKEN.code, SSJ_GOKU.code, SSJ2_GOKU.code, SSJ3_GOKU.code, SSJ4_GOKU.code, 
                       KAME_GOKU.code, DRAG_FIST_GOKU.code, WARP_KAME_GOKU.code, SPIRIT_BOMB_GOKU.code, BREAK_GOKU.code, 
                       VEGITO_GOKU.code, GOGETA_GOKU.code, SSJ4_GOGETA_GOKU.code]
    kgohan_norm = [KID_GOHAN.code, MASENKO.code, POTENTIAL_KGOHAN.code, BREAK_KGOHAN.code]
    kgohan_attacks = [KID_GOHAN.code, MASENKO.code, POTENTIAL_KGOHAN.code, BREAK_KGOHAN.code]
    kgohan_transforms = [KID_GOHAN.code, POTENTIAL_KGOHAN.code, MASENKO.code, BREAK_KGOHAN.code]
    tgohan_norm = [TEEN_GOHAN.code, KAME_TGOHAN.code, SSJ_TGOHAN.code, SSJ2_TGOHAN.code, SOAR_TGOHAN.code, FS_KAME.code, 
                   BREAK_TGOHAN.code]
    tgohan_attacks = [TEEN_GOHAN.code, KAME_TGOHAN.code, SOAR_TGOHAN.code, FS_KAME.code, SSJ_TGOHAN.code, SSJ2_TGOHAN.code, 
                      BREAK_TGOHAN.code]
    tgohan_transforms = [TEEN_GOHAN.code, SSJ_TGOHAN.code, SSJ2_TGOHAN.code, KAME_TGOHAN.code, SOAR_TGOHAN.code, 
                         FS_KAME.code, BREAK_TGOHAN.code]
    gohan_norm = [GOHAN.code, KAME_GOHAN.code, SSJ_GOHAN.code, SSJ2_GOHAN.code, SOAR_GOHAN.code, SUPER_KAME_GOHAN.code, 
                  ELDER_UNLOCK.code, BREAK_GOHAN.code]
    gohan_attacks = [GOHAN.code, KAME_GOHAN.code, SOAR_GOHAN.code, SUPER_KAME_GOHAN.code, SSJ_GOHAN.code, SSJ2_GOHAN.code, 
                     ELDER_UNLOCK.code, BREAK_GOHAN.code]
    gohan_transforms = [GOHAN.code, SSJ_GOHAN.code, SSJ2_GOHAN.code, ELDER_UNLOCK.code, KAME_GOHAN.code, SOAR_GOHAN.code, 
                        SUPER_KAME_GOHAN.code, BREAK_GOHAN.code]
    vegeta_norm = [VEGETA.code, GALICK.code, FINAL_IMPACT.code, SSJ_VEGETA.code, BIG_BANG.code, FINAL_FLASH.code, 
                   SSJ2_VEGETA.code, SSJ4_VEGETA.code, BREAK_VEGETA.code, VEGITO_VEGETA.code, GOGETA_VEGETA.code, SSJ4_GOGETA_VEGETA.code]
    vegeta_attacks = [VEGETA.code, GALICK.code, FINAL_IMPACT.code, BIG_BANG.code, FINAL_FLASH.code, SSJ_VEGETA.code, 
                      SSJ2_VEGETA.code, SSJ4_VEGETA.code, BREAK_VEGETA.code, VEGITO_VEGETA.code, GOGETA_VEGETA.code, SSJ4_GOGETA_VEGETA.code]
    vegeta_transforms = [VEGETA.code, SSJ_VEGETA.code, SSJ2_VEGETA.code, SSJ4_VEGETA.code, GALICK.code, FINAL_IMPACT.code, 
                         BIG_BANG.code, FINAL_FLASH.code, BREAK_VEGETA.code, VEGITO_VEGETA.code, GOGETA_VEGETA.code, SSJ4_GOGETA_VEGETA.code]
    krillin_norm = [KRILLIN.code, KAME_KRILLIN.code, DD_KRILLIN.code, POTENTIAL_KRILLIN.code, FIERCE_DD.code, BREAK_KRILLIN.code]
    krillin_attacks = [KRILLIN.code, KAME_KRILLIN.code, DD_KRILLIN.code, FIERCE_DD.code, POTENTIAL_KRILLIN.code, BREAK_KRILLIN.code]
    krillin_transforms = [KRILLIN.code, POTENTIAL_KRILLIN.code, KAME_KRILLIN.code, DD_KRILLIN.code, FIERCE_DD.code, BREAK_KRILLIN.code]
    piccolo_norm = [PICCOLO.code, DEST_WAVE.code, SBEAM_CANNON.code, SYNC_NAIL.code, FUSE_KAMI.code, LGRENADE.code, 
                    HZGRENADE.code, BREAK_PICCOLO.code]
    piccolo_attacks = [PICCOLO.code, DEST_WAVE.code, SBEAM_CANNON.code, LGRENADE.code, HZGRENADE.code, SYNC_NAIL.code, 
                       FUSE_KAMI.code, BREAK_PICCOLO.code]
    piccolo_transforms = [PICCOLO.code, SYNC_NAIL.code, FUSE_KAMI.code, DEST_WAVE.code, SBEAM_CANNON.code, LGRENADE.code, 
                          HZGRENADE.code, BREAK_PICCOLO.code]
    tien_norm = [TIEN.code, BLAST_CANNON.code, DODON.code, NEO_BLAST_CANNON.code, BREAK_TIEN.code]
    yamcha_norm = [YAMCHA.code, KAME_YAMCHA.code, WOLF_FANG.code, SPIRIT_BALL.code, BREAK_YAMCHA.code]
    uub_norm = [UUB.code, KI_CANNON.code, FIERCE_FLURRY.code, BREAK_UUB.code]
    broly_norm = [BROLY.code, LSSJ_BROLY.code, BLASTER_SHELL.code, GIGANT_PRESS.code, GIGANT_METEOR.code, BREAK_BROLY.code]
    broly_attacks = [BROLY.code, BLASTER_SHELL.code, GIGANT_PRESS.code, GIGANT_METEOR.code, LSSJ_BROLY.code, BREAK_BROLY.code]
    broly_transforms = [BROLY.code, LSSJ_BROLY.code, BLASTER_SHELL.code, GIGANT_PRESS.code, GIGANT_METEOR.code, BREAK_BROLY.code]

    # 531 - 541: Goku, Kid Gohan, Teen Gohan, Gohan, Krillin, Piccolo, Vegeta, Tien, Yamcha, Uub, Broly
    match id:
        case 531:
            if prog_type == 'prog_normal': return goku_norm[index]
            if prog_type == 'prog_attacks': return goku_attacks[index]
            if prog_type == "prog_transforms": return goku_transforms[index]
        case 532:
            if prog_type == 'prog_normal': return kgohan_norm[index]
            if prog_type == 'prog_attacks': return kgohan_attacks[index]
            if prog_type == "prog_transforms": return kgohan_transforms[index]
        case 533:
            if prog_type == 'prog_normal': return tgohan_norm[index]
            if prog_type == 'prog_attacks': return tgohan_attacks[index]
            if prog_type == "prog_transforms": return tgohan_transforms[index]
        case 534:
            if prog_type == 'prog_normal': return gohan_norm[index]
            if prog_type == 'prog_attacks': return gohan_attacks[index]
            if prog_type == "prog_transforms": return gohan_transforms[index]
        case 535:
            if prog_type == 'prog_normal': return krillin_norm[index]
            if prog_type == 'prog_attacks': return krillin_attacks[index]
            if prog_type == "prog_transforms": return krillin_transforms[index]
        case 536:
            if prog_type == 'prog_normal': return piccolo_norm[index]
            if prog_type == 'prog_attacks': return piccolo_attacks[index]
            if prog_type == "prog_transforms": return piccolo_transforms[index]
        case 537:
            if prog_type == 'prog_normal': return vegeta_norm[index]
            if prog_type == 'prog_attacks': return vegeta_attacks[index]
            if prog_type == "prog_transforms": return vegeta_transforms[index]
        case 538:
            return tien_norm[index]
        case 539:
            return yamcha_norm[index]
        case 540:
            return uub_norm[index]
        case 541:
            if prog_type == 'prog_normal': return broly_norm[index]
            if prog_type == 'prog_attacks': return broly_attacks[index]
            if prog_type == "prog_transforms": return broly_transforms[index]
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
