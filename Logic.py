from BaseClasses import CollectionState
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

def can_tournament_novice(state: CollectionState, player: int) -> bool:
    return True

def can_tournament_adept(state: CollectionState, player: int) -> bool:
    return state.has(Items.TOURNEY_NOVICE.name)

def can_tournament_advanced(state: CollectionState, player: int) -> bool:
