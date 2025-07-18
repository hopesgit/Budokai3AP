# noinspection PyUnresolvedReferences
from BaseClasses import CollectionState

from .data import Items

def _get_options(state: CollectionState, player: int):
    return state.multiworld.worlds[player].options

def has_goku(state: CollectionState, player: int) -> bool:
    return state.has(Items.GOKU.name, player)

def can_goku(state: CollectionState, player: int) -> bool:
    check1 = has_goku(state, player)
    check2 = True
    opt = _get_options(state, player).start_with_super_attacks
    if opt in ["random", "plando", "start"]:
        check2 = state.has_any([Items.KAME_GOKU.name, Items.DRAG_FIST_GOKU.name], player)
    elif opt == 'choose':
        opt2 = _get_options(state, player).super_attack_starters
        if Items.GOKU.name in opt2:
            check2 = state.has_any([Items.KAME_GOKU.name, Items.DRAG_FIST_GOKU.name], player)

    return check1 and check2

def can_super_spirit_bomb(state: CollectionState, player: int) -> bool:
    return can_goku and state.has_all([Items.KAIOKEN.name, Items.SSJ_GOKU.name, Items.SPIRIT_BOMB_GOKU.name], player)

def can_wish_and_spirit_bomb(state: CollectionState, player: int) -> bool:
    return can_wish_goku(state, player) and can_super_spirit_bomb(state, player)

def has_kid_gohan(state: CollectionState, player: int) -> bool:
    return state.has(Items.KID_GOHAN.name, player)

def can_kid_gohan(state: CollectionState, player: int) -> bool:
    check1 = has_kid_gohan(state, player)
    check2 = True
    opt = _get_options(state, player).start_with_super_attacks
    if opt in ["random", "plando", "start"]:
        check2 = state.has(Items.MASENKO.name, player)
    elif opt == 'choose':
        opt2 = _get_options(state, player).super_attack_starters
        if Items.KID_GOHAN.name in opt2:
            check2 = state.has(Items.MASENKO.name, player)

    return check1 and check2

def has_teen_gohan(state: CollectionState, player: int) -> bool:
    return state.has(Items.TEEN_GOHAN.name, player)

def can_teen_gohan(state: CollectionState, player: int) -> bool:
    check1 = has_teen_gohan(state, player)
    check2 = True
    can_soar = state.has_all([Items.SOAR_TGOHAN.name, Items.SSJ_TGOHAN.name, Items.SSJ2_TGOHAN.name], player)
    opt = _get_options(state, player).start_with_super_attacks
    if opt in ["random", "plando", "start"]:
        check2 = state.has(Items.KAME_TGOHAN.name, player) or can_soar
    elif opt == 'choose':
        opt2 = _get_options(state, player).super_attack_starters
        if Items.TEEN_GOHAN.name in opt2:
            check2 = state.has(Items.KAME_TGOHAN.name, player) or can_soar

    return check1 and check2

def has_gohan(state: CollectionState, player: int) -> bool:
    return state.has(Items.GOHAN.name, player)

def can_gohan(state: CollectionState, player: int) -> bool:
    check1 = has_gohan(state, player)
    check2 = True
    opt = _get_options(state, player).start_with_super_attacks
    if opt in ["random", "plando", "start"]:
        check2 = state.has_any([Items.KAME_GOHAN.name, Items.SOAR_GOHAN.name], player)
    elif opt == 'choose':
        opt2 = _get_options(state, player).super_attack_starters
        if Items.GOHAN.name in opt2:
            check2 = state.has_any([Items.KAME_GOHAN.name, Items.SOAR_GOHAN], player)

    return check1 and check2

def has_piccolo(state: CollectionState, player: int) -> bool:
    return state.has(Items.PICCOLO.name, player)

def can_piccolo(state: CollectionState, player: int) -> bool:
    check1 = has_piccolo(state, player)
    check2 = True
    can_light_grenade = state.has_all([Items.LGRENADE.name, Items.SYNC_NAIL.name, Items.FUSE_KAMI.name], player)
    opt = _get_options(state, player).start_with_super_attacks
    if opt in ["random", "plando", "start"]:
        check2 = state.has(Items.DEST_WAVE.name, player) or can_light_grenade
    elif opt == 'choose':
        opt2 = _get_options(state, player).super_attack_starters
        if Items.PICCOLO.name in opt2:
            check2 = state.has(Items.DEST_WAVE.name, player) or can_light_grenade

    return check1 and check2

def has_vegeta(state: CollectionState, player: int) -> bool:
    return state.has(Items.VEGETA.name, player)

def can_vegeta(state: CollectionState, player: int) -> bool:
    check1 = has_vegeta(state, player)
    check2 = True
    opt = _get_options(state, player).start_with_super_attacks
    if opt in ["random", "plando", "start"]:
        check2 = state.has_any([Items.GALICK.name, Items.FINAL_IMPACT.name], player)
    elif opt == 'choose':
        opt2 = _get_options(state, player).super_attack_starters
        if Items.VEGETA.name in opt2:
            check2 = state.has_any([Items.GALICK.name, Items.FINAL_IMPACT.name], player)

    return check1 and check2

def can_wish_goku_vegeta(state: CollectionState, player: int) -> bool:
    """Two fights in Goku's second path use this logic"""
    return can_wish_goku(state, player) and can_wish_vegeta(state, player)

def has_krillin(state: CollectionState, player: int) -> bool:
    return state.has(Items.KRILLIN.name, player)

def can_krillin(state: CollectionState, player: int) -> bool:
    check1 = has_krillin(state, player)
    check2 = True
    opt = _get_options(state, player).start_with_super_attacks
    if opt in ["random", "plando", "start"]:
        check2 = state.has_any([Items.KAME_KRILLIN.name, Items.DD_KRILLIN.name], player)
    elif opt == 'choose':
        opt2 = _get_options(state, player).super_attack_starters
        if Items.KRILLIN.name in opt2:
            check2 = state.has_any([Items.KAME_KRILLIN.name, Items.DD_KRILLIN.name], player)

    return check1 and check2

def has_tien(state: CollectionState, player: int) -> bool:
    return state.has(Items.TIEN.name, player)

def can_tien(state: CollectionState, player: int) -> bool:
    check1 = has_tien(state, player)
    check2 = True
    opt = _get_options(state, player).start_with_super_attacks
    if opt in ["random", "plando", "start"]:
        check2 = state.has_any([Items.DODON.name, Items.BLAST_CANNON.name], player)
    elif opt == 'choose':
        opt2 = _get_options(state, player).super_attack_starters
        if Items.TIEN.name in opt2:
            check2 = state.has_any([Items.DODON.name, Items.BLAST_CANNON.name], player)

    return check1 and check2

def has_yamcha(state: CollectionState, player: int) -> bool:
    return state.has(Items.YAMCHA.name, player)

def can_yamcha(state: CollectionState, player: int) -> bool:
    check1 = has_yamcha(state, player)
    check2 = True
    opt = _get_options(state, player).start_with_super_attacks
    if opt in ["random", "plando", "start"]:
        check2 = state.has_any([Items.KAME_YAMCHA.name, Items.WOLF_FANG.name], player)
    elif opt == 'choose':
        opt2 = _get_options(state, player).super_attack_starters
        if Items.YAMCHA.name in opt2:
            check2 = state.has_any([Items.KAME_YAMCHA.name, Items.WOLF_FANG.name], player)

    return check1 and check2

def has_broly(state: CollectionState, player: int) -> bool:
    return state.has(Items.BROLY.name, player)

def can_broly(state: CollectionState, player: int) -> bool:
    check1 = has_broly(state, player)
    check2 = True
    can_press = state.has_all([Items.LSSJ_BROLY.name, Items.GIGANT_PRESS.name], player)
    opt = _get_options(state, player).start_with_super_attacks
    if opt in ["random", "plando", "start"]:
        check2 = state.has(Items.BLASTER_SHELL.name, player) or can_press
    elif opt == 'choose':
        opt2 = _get_options(state, player).super_attack_starters
        if Items.BROLY.name in opt2:
            check2 = state.has(Items.BLASTER_SHELL.name, player) or can_press

    return check1 and check2

def has_uub(state: CollectionState, player: int) -> bool:
    return state.has(Items.UUB.name, player)

def can_uub(state: CollectionState, player: int) -> bool:
    check1 = has_uub(state, player)
    check2 = True
    opt = _get_options(state, player).start_with_super_attacks
    if opt in ["random", "plando", "start"]:
        check2 = state.has_any([Items.KI_CANNON.name, Items.FIERCE_FLURRY.name], player)
    elif opt == 'choose':
        opt2 = _get_options(state, player).super_attack_starters
        if Items.UUB.name in opt2:
            check2 = state.has_any([Items.KI_CANNON.name, Items.FIERCE_FLURRY.name], player)

    return check1 and check2

def can_wish_goku(state: CollectionState, player: int) -> bool:
    return state.has(Items.GOKU.name, player) and state.has("Event - Dragon World Goku Cleared", player)

def can_wish_kid_gohan(state: CollectionState, player: int) -> bool:
    return state.has(Items.KID_GOHAN.name, player) and state.has("Event - Dragon World Kid Gohan Cleared", player)

def can_wish_teen_gohan(state: CollectionState, player: int) -> bool:
    return state.has(Items.TEEN_GOHAN.name, player) and state.has("Event - Dragon World Teen Gohan Cleared", player)

def can_wish_gohan(state: CollectionState, player: int) -> bool:
    return state.has(Items.KID_GOHAN.name, player) and state.has("Event - Dragon World Gohan Cleared", player)

def can_wish_piccolo(state: CollectionState, player: int) -> bool:
    return state.has(Items.PICCOLO.name, player) and state.has("Event - Dragon World Goku Cleared", player)

def can_wish_vegeta(state: CollectionState, player: int) -> bool:
    return state.has(Items.VEGETA.name, player) and state.has("Event - Dragon World Vegeta Cleared", player)

def can_wish_krillin(state: CollectionState, player: int) -> bool:
    return state.has(Items.KRILLIN.name, player) and state.has("Event - Dragon World Krillin Cleared", player)

def can_wish_tien(state: CollectionState, player: int) -> bool:
    return state.has(Items.TIEN.name, player) and state.has("Event - Dragon World Tien Cleared", player)

def can_wish_yamcha(state: CollectionState, player: int) -> bool:
    return state.has(Items.YAMCHA.name, player) and state.has("Event - Dragon World Yamcha Cleared", player)

def can_wish_uub(state: CollectionState, player: int) -> bool:
    return state.has(Items.UUB.name, player) and state.has("Event - Dragon World Uub Cleared", player)

def can_wish_broly(state: CollectionState, player: int) -> bool:
    return state.has(Items.BROLY.name, player) and state.has("Event - Dragon World Broly Cleared", player)

def has_cleared_story(state: CollectionState, player: int) -> bool:
    return state.has_all(["Event - Dragon World Goku Cleared", "Event - Dragon World Kid Gohan Cleared",
                          "Event - Dragon World Teen Gohan Cleared", "Event - Dragon World Gohan Cleared",
                          "Event - Dragon World Krillin Cleared", "Event - Dragon World Piccolo Cleared",
                          "Event - Dragon World Vegeta Cleared", "Event - Dragon World Tien Cleared",
                          "Event - Dragon World Yamcha Cleared", "Event - Dragon World Broly Cleared",
                          "Event - Dragon World Uub Cleared"], player)

def can_complete_reenactment_0(state: CollectionState, player: int) -> bool:
    return state.has(Items.GOKU.name, player) and state.has(Items.KAME_GOKU.name, player)

def can_complete_reenactment_1(state: CollectionState, player: int) -> bool:
    return state.has(Items.PICCOLO.name, player) and state.has(Items.SBEAM_CANNON.name, player)

def can_complete_reenactment_2(state: CollectionState, player: int) -> bool:
    return state.has(Items.TIEN.name, player) and state.has_any(Items.BLAST_CANNON.name, player)

def can_complete_reenactment_3(state: CollectionState, player: int) -> bool:
    return state.has(Items.KID_GOHAN.name, player) and state.has_any(Items.MASENKO.name, player)

def can_complete_reenactment_4(state: CollectionState, player: int) -> bool:
    return state.has(Items.KRILLIN.name, player) and state.has_any(Items.DD_KRILLIN.name, player)

def can_complete_reenactment_5(state: CollectionState, player: int) -> bool:
    return state.has(Items.GOKU.name, player) # you use a Goku with a predetermined moveset

def can_complete_reenactment_6(state: CollectionState, player: int) -> bool:
    return state.has(Items.YAMCHA.name, player) and state.has_any(Items.SENZU_BEAN.name, player)

def can_complete_reenactment_7(state: CollectionState, player: int) -> bool:
    return state.has_all([Items.PICCOLO.name, Items.SYNC_NAIL.name, Items.FUSE_KAMI.name], player)

def can_complete_reenactment_8(state: CollectionState, player: int) -> bool:
    return has_vegeta(state, player) # you only need Vegeta. Plenty of items make it easier, but it's possible with nothing

def can_complete_reenactment_9(state: CollectionState, player: int) -> bool:
    return state.has([Items.VEGETA.name, Items.SSJ_VEGETA.name, Items.FINAL_FLASH.name], player)

def can_complete_reenactment_10(state: CollectionState, player: int) -> bool:
    return state.has(Items.TEEN_GOHAN.name, player) and state.has(Items.SSJ_TGOHAN.name, player)

def can_complete_reenactment_11(state: CollectionState, player: int) -> bool:
    return state.has_all([Items.TEEN_GOHAN.name, Items.SSJ_TGOHAN.name, Items.SSJ2_TGOHAN.name, Items.FS_KAME.name], player)

def can_complete_reenactment_12(state: CollectionState, player: int) -> bool:
    return state.has_all([Items.VEGETA.name, Items.SSJ_VEGETA.name, Items.BIG_BANG.name], player)

def can_complete_reenactment_13(state: CollectionState, player: int) -> bool:
    return state.has(Items.GOKU.name, player) # this is another Goku with a predetermined moveset

def can_complete_reenactment_14(state: CollectionState, player: int) -> bool:
    return has_piccolo(state, player)

def can_complete_reenactment_15(state: CollectionState, player: int) -> bool:
    return state.has_all([Items.GOHAN.name, Items.SSJ_GOHAN.name, Items.SSJ2_GOHAN.name, Items.ELDER_UNLOCK.name], player)

def can_complete_reenactment_16(state: CollectionState, player: int) -> bool:
    return can_super_spirit_bomb(state, player)

def can_complete_reenactment_17(state: CollectionState, player: int) -> bool:
    return state.has_all([Items.VEGETA.name, Items.SSJ_VEGETA.name, Items.SSJ2_VEGETA.name, Items.SSJ4_VEGETA.name], player)

def can_complete_reenactment_18(state: CollectionState, player: int) -> bool:
    return can_complete_reenactment_16(state, player) # may also need SSJ4 and all its prereqs but that hasn't been tested yet

def can_complete_reenactment_19(state: CollectionState, player: int) -> bool:
    return state.has(Items.BROLY.name, player) and state.has(Items.GIGANT_METEOR.name, player)

def can_complete_reenactment_20(state: CollectionState, player: int) -> bool:
    return state.has(Items.UUB.name, player) and state.has(Items.KI_CANNON.name, player)

def has_z_hard(state: CollectionState, player: int) -> bool:
    return state.has(Items.GOKUS_WISH.name, player)

def has_z_hard_2(state: CollectionState, player: int) -> bool:
    return state.has(Items.PATH_POWER.name, player)

def has_z_hard_3(state: CollectionState, player: int) -> bool:
    return state.has(Items.ENDLESS_PATH.name, player)

def has_tournament_novice() -> bool:
    return True

def has_tournament_adept(state: CollectionState, player: int) -> bool:
    return state.has(Items.TOURNEY_ADEPT.name, player)

def has_tournament_advanced(state: CollectionState, player: int) -> bool:
    return state.has(Items.TOURNEY_ADV.name, player)

def can_shop() -> bool:
    return True

def has_dragon_arena(state: CollectionState, player: int) -> bool:
    return state.has(Items.DRAGON_ARENA.name, player)

def has_training_1() -> bool:
    return True

def has_training_2(state: CollectionState, player: int) -> bool:
    return state.has(Items.TRAINING_2.name, player)

def has_training_3(state: CollectionState, player: int) -> bool:
    return state.has(Items.TRAINING_3.name, player)

def has_training_4(state: CollectionState, player: int) -> bool:
    return state.has(Items.TRAINING_4.name, player)

def has_training_5(state: CollectionState, player: int) -> bool:
    return state.has(Items.TRAINING_5.name, player)

def has_training_6(state: CollectionState, player: int) -> bool:
    return state.has(Items.TRAINING_6.name, player)

def has_training_7(state: CollectionState, player: int) -> bool:
    return state.has(Items.TRAINING_7.name, player)

def has_training_8(state: CollectionState, player: int) -> bool:
    return state.has(Items.TRAINING_8.name, player)

def has_training_9(state: CollectionState, player: int) -> bool:
    return state.has(Items.TRAINING_9.name, player)

def has_training_10(state: CollectionState, player: int) -> bool:
    return state.has(Items.TRAINING_10.name, player)

def has_training_11(state: CollectionState, player: int) -> bool:
    return state.has(Items.TRAINING_11.name, player)

def has_training_12(state: CollectionState, player: int) -> bool:
    return state.has(Items.TRAINING_12.name, player)