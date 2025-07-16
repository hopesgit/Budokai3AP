from BaseClasses import CollectionState

from data.Items import YAMCHA
from .data import Items


def can_goku_dw(state: CollectionState, player: int) -> bool:
    return state.has(Items.GOKU.name, player)

def can_kid_gohan_dw(state: CollectionState, player: int) -> bool:
    return state.has(Items.KID_GOHAN.name, player)

def can_teen_gohan_dw(state: CollectionState, player: int) -> bool:
    return state.has(Items.TEEN_GOHAN.name, player)

def can_gohan_dw(state: CollectionState, player: int) -> bool:
    return state.has(Items.GOHAN.name, player)

def can_piccolo_dw(state: CollectionState, player: int) -> bool:
    return state.has(Items.PICCOLO.name, player)

def can_vegeta_dw(state: CollectionState, player: int) -> bool:
    return state.has(Items.VEGETA.name, player)

def can_krillin_dw(state: CollectionState, player: int) -> bool:
    return state.has(Items.KRILLIN.name, player)

def can_tien_dw(state: CollectionState, player: int) -> bool:
    return state.has(Items.TIEN.name, player)

def can_yamcha_dw(state: CollectionState, player: int) -> bool:
    return state.has(Items.YAMCHA.name, player)

def can_broly_dw(state: CollectionState, player: int) -> bool:
    return state.has(Items.BROLY.name, player)

def can_uub_dw(state: CollectionState, player: int) -> bool:
    return state.has(Items.UUB.name, player)

def can_wish_goku(state: CollectionState, player: int) -> bool:
    return state.has(Items.GOKU.name, player) and state.has(Items.EVENT_GOKU_CLEAR.name, player)

def can_wish_kid_gohan(state: CollectionState, player: int) -> bool:
    return state.has(Items.KID_GOHAN.name, player) and state.has(Items.EVENT_KID_GOHAN_CLEAR.name, player)

def can_wish_teen_gohan(state: CollectionState, player: int) -> bool:
    return state.has(Items.TEEN_GOHAN.name, player) and state.has(Items.EVENT_TEEN_GOHAN_CLEAR.name, player)

def can_wish_gohan(state: CollectionState, player: int) -> bool:
    return state.has(Items.KID_GOHAN.name, player) and state.has(Items.EVENT_GOHAN_CLEAR.name, player)

def can_wish_piccolo(state: CollectionState, player: int) -> bool:
    return state.has(Items.PICCOLO.name, player) and state.has(Items.EVENT_PICCOLO_CLEAR.name, player)

def can_wish_vegeta(state: CollectionState, player: int) -> bool:
    return state.has(Items.VEGETA.name, player) and state.has(Items.EVENT_VEGETA_CLEAR.name, player)

def can_wish_krillin(state: CollectionState, player: int) -> bool:
    return state.has(Items.KRILLIN.name, player) and state.has(Items.EVENT_KRILLIN.name, player)

def can_wish_tien(state: CollectionState, player: int) -> bool:
    return state.has(Items.TIEN.name, player) and state.has(Items.EVENT_TIEN_CLEAR.name, player)

def can_wish_yamcha(state: CollectionState, player: int) -> bool:
    return state.has(Items.YAMCHA.name, player) and state.has(Items.EVENT_YAMCHA_CLEAR.name, player)

def can_wish_uub(state: CollectionState, player: int) -> bool:
    return state.has(Items.UUB.name, player) and state.has(Items.EVENT_UUB_CLEAR.name, player)

def can_wish_broly(state: CollectionState, player: int) -> bool:
    return state.has(Items.BROLY.name, player) and state.has(Items.EVENT_BROLY_CLEAR.name, player)

def can_complete_reenactment_0(state: CollectionState, player: int) -> bool:
    return state.has(Items.GOKU.name, player) and state.has_any(Items.KAME_GOKU.name, player)

def can_complete_reenactment_1(state: CollectionState, player: int) -> bool:
    return state.has(Items.PICCOLO.name, player) and state.has_any(Items.SBEAM_CANNON.name, player)

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
    return (state.has(Items.PICCOLO.name, player) and state.has_any(Items.SYNC_NAIL.name, player) and
            state.has_any(Items.FUSE_KAMI.name, player))

def can_complete_reenactment_8(state: CollectionState, player: int) -> bool:
    return state.has(Items.VEGETA.name, player) # you only need Vegeta. Plenty of items make it easier, but it's possible with nothing

def can_complete_reenactment_9(state: CollectionState, player: int) -> bool:
    return (state.has(Items.VEGETA.name, player) and state.has(Items.SSJ_VEGETA.name, player) and
            state.has_any(Items.FINAL_FLASH.name, player))

def can_complete_reenactment_10(state: CollectionState, player: int) -> bool:
    return state.has(Items.TEEN_GOHAN.name, player) and state.has(Items.SSJ_TGOHAN.name, player)

def can_complete_reenactment_11(state: CollectionState, player: int) -> bool:
    return (state.has(Items.TEEN_GOHAN.name, player) and state.has(Items.SSJ_TGOHAN.name, player) and
            state.has(Items.SSJ2_TGOHAN.name, player) and state.has(Items.FS_KAME.name, player))

def can_complete_reenactment_12(state: CollectionState, player: int) -> bool:
    return (state.has(Items.VEGETA.name, player) and state.has(Items.SSJ_VEGETA.name, player) and
            state.has_any(Items.BIG_BANG.name, player))

def can_complete_reenactment_13(state: CollectionState, player: int) -> bool:
    return state.has(Items.GOKU.name, player) # this is another Goku with a predetermined moveset

def can_complete_reenactment_14(state: CollectionState, player: int) -> bool:
    return state.has(Items.PICCOLO.name, player)

def can_complete_reenactment_15(state: CollectionState, player: int) -> bool:
    return (state.has(Items.GOHAN.name, player) and state.has(Items.SSJ_GOHAN.name, player) and
            state.has(Items.SSJ2_GOHAN.name, player) and state.has(Items.ELDER_UNLOCK.name, player))

def can_complete_reenactment_16(state: CollectionState, player: int) -> bool:
    return (state.has(Items.GOKU.name, player) and state.has(Items.KAIOKEN.name, player) and
            state.has(Items.SSJ_GOKU.name, player) and state.has_any(Items.SPIRIT_BOMB_GOKU.name, player))

def can_complete_reenactment_17(state: CollectionState, player: int) -> bool:
    return (state.has(Items.VEGETA.name, player) and state.has(Items.SSJ_VEGETA.name, player) and
            state.has(Items.SSJ2_VEGETA.name, player) and state.has(Items.SSJ4_VEGETA.name, player))

def can_complete_reenactment_18(state: CollectionState, player: int) -> bool:
    return can_complete_reenactment_16(state, player) # may also need SSJ4 and all its prereqs but that hasn't been tested yet

def can_complete_reenactment_19(state: CollectionState, player: int) -> bool:
    return state.has(Items.BROLY.name, player) and state.has(Items.GIGANT_METEOR.name, player)

def can_complete_reenactment_20(state: CollectionState, player: int) -> bool:
    return state.has(Items.UUB.name, player) and state.has(Items.KI_CANNON.name, player)

def can_complete_z_hard(state: CollectionState, player: int) -> bool:
    return state.has(Items.GOKUS_WISH.name, player)

def can_complete_z_hard_2(state: CollectionState, player: int) -> bool:
    return state.has(Items.PATH_POWER.name, player)

def can_complete_z_hard_3(state: CollectionState, player: int) -> bool:
    return state.has(Items.ENDLESS_PATH.name, player)

def can_tournament_novice(state: CollectionState, player: int) -> bool:
    return True

def can_tournament_adept(state: CollectionState, player: int) -> bool:
    return state.has(Items.TOURNEY_ADEPT.name, player)

def can_tournament_advanced(state: CollectionState, player: int) -> bool:
    return state.has(Items.TOURNEY_ADV.name, player)

def can_shop() -> bool:
    return True

def can_dragon_arena(state: CollectionState, player: int) -> bool:
    return state.has(Items.DRAGON_ARENA.name, player)