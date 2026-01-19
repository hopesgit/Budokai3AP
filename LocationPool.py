from typing import Any, Callable, NamedTuple, Sequence

from .data import Locations
from .data.Locations import LocationData


def return_true(slot_data: dict[str, int]) -> bool:
    return True

def dragon_radar_randomized(slot_data: dict[str, int]) -> bool:
    val = int(slot_data["randomize_dragon_radar"])
    match val:
        case 0:
            return False
        case 1 | 2:
            return True
        case _:
            return False
        
def dragon_balls_randomized(slot_data: dict[str, int]) -> bool:
    val = bool(slot_data["randomize_dragon_balls"])
    return val

def money_spots_randomized(slot_data: dict[str, int]) -> bool:
    val = bool(slot_data["randomize_money_spots"])
    return val

def shop_randomized(slot_data: dict[str, int]) -> bool:
    val = bool(slot_data["shop_rando"])
    return val

def goku_enabled(slot_data: dict[str, list[str]]) -> bool:
    return "Goku" in slot_data["choose_du_characters"]

def kid_gohan_enabled(slot_data: dict[str, list[str]]) -> bool:
    return "Kid Gohan" in slot_data["choose_du_characters"]

def teen_gohan_enabled(slot_data: dict[str, list[str]]) -> bool:
    return "Teen Gohan" in slot_data["choose_du_characters"]

def gohan_enabled(slot_data: dict[str, list[str]]) -> bool:
    return "Gohan" in slot_data["choose_du_characters"]

def krillin_enabled(slot_data: dict[str, list[str]]) -> bool:
    return "Krillin" in slot_data["choose_du_characters"]

def piccolo_enabled(slot_data: dict[str, list[str]]) -> bool:
    return "Piccolo" in slot_data["choose_du_characters"]

def vegeta_enabled(slot_data: dict[str, list[str]]) -> bool:
    return "Vegeta" in slot_data["choose_du_characters"]

def tien_enabled(slot_data: dict[str, list[str]]) -> bool:
    return "Tien" in slot_data["choose_du_characters"]

def yamcha_enabled(slot_data: dict[str, list[str]]) -> bool:
    return "Yamcha" in slot_data["choose_du_characters"]

def uub_enabled(slot_data: dict[str, list[str]]) -> bool:
    return "Uub" in slot_data["choose_du_characters"]

def broly_enabled(slot_data: dict[str, list[str]]) -> bool:
    return "Broly" in slot_data["choose_du_characters"]


class LocationGroup(NamedTuple):
    name: str
    number: int
    locations: Sequence[LocationData] = []
    enable_if: Callable = return_true
    

LOCATION_GROUPS: Sequence[LocationGroup] = [
    LocationGroup("DU: Goku: Bosses", 0, Locations.GOKU_BOSSES, goku_enabled),
    LocationGroup("DU: Goku: Capsules", 1, Locations.GOKU_CAPSULES, goku_enabled),
    LocationGroup("DU: Goku: Money", 2, [], lambda slot_data: goku_enabled(slot_data) and money_spots_randomized(slot_data)),
    LocationGroup("DU: Goku: Dragon Balls", 3, [], lambda slot_data: goku_enabled(slot_data) and dragon_balls_randomized(slot_data)),
    LocationGroup("DU: Goku: Dragon Radars", 4, [], lambda slot_data: goku_enabled(slot_data) and dragon_radar_randomized(slot_data)),
    LocationGroup("DU: Goku: Reenactments", 5, Locations.GOKU_REENACTMENTS, goku_enabled),
    LocationGroup("DU: Kid Gohan: Bosses", 5, Locations.KID_GOHAN_BOSSES, kid_gohan_enabled),
    LocationGroup("DU: Kid Gohan: Capsules", 6, Locations.KGOHAN_CAPSULES, kid_gohan_enabled),
    LocationGroup("DU: Kid Gohan: Money", 7, [], lambda slot_data: kid_gohan_enabled(slot_data) and money_spots_randomized(slot_data)),
    LocationGroup("DU: Kid Gohan: Dragon Balls", 8, [], lambda slot_data: kid_gohan_enabled(slot_data) and dragon_balls_randomized(slot_data)),
    LocationGroup("DU: Kid Gohan: Reenactments", 9, Locations.KID_GOHAN_REENACTMENTS, kid_gohan_enabled),
    LocationGroup("DU: Kid Gohan: Dragon Radars", 9, [], lambda slot_data: kid_gohan_enabled(slot_data) and dragon_radar_randomized(slot_data)),
    LocationGroup("DU: Teen Gohan: Bosses", 10, Locations.TEEN_GOHAN_BOSSES),
    LocationGroup("DU: Teen Gohan: Capsules", 11, Locations.TGOHAN_CAPSULES),
    LocationGroup("DU: Teen Gohan: Money", 12, []),
    LocationGroup("DU: Teen Gohan: Dragon Balls", 13, [], dragon_balls_randomized),
    LocationGroup("DU: Teen Gohan: Dragon Radars", 14, [], dragon_radar_randomized),
    LocationGroup("DU: Gohan: Bosses", 15, Locations.GOHAN_BOSSES),
    LocationGroup("DU: Gohan: Capsules", 16, Locations.GOHAN_CAPSULES),
    LocationGroup("DU: Gohan: Money", 17, []),
    LocationGroup("DU: Gohan: Dragon Balls", 18, [], dragon_balls_randomized),
    LocationGroup("DU: Gohan: Dragon Radars", 19, [], dragon_radar_randomized),
    LocationGroup("DU: Krillin: Bosses", 20, Locations.KRILLIN_BOSSES),
    LocationGroup("DU: Krillin: Capsules", 21, Locations.KRILLIN_CAPSULES),
    LocationGroup("DU: Krillin: Money", 22, []),
    LocationGroup("DU: Krillin: Dragon Balls", 23, [], dragon_balls_randomized),
    LocationGroup("DU: Krillin: Dragon Radars", 24, [], dragon_radar_randomized),
    LocationGroup("DU: Vegeta: Bosses", 25, Locations.VEGETA_BOSSES),
    LocationGroup("DU: Vegeta: Capsules", 26, Locations.VEGETA_CAPSULES),
    LocationGroup("DU: Vegeta: Money", 27, []),
    LocationGroup("DU: Vegeta: Dragon Balls", 28, [], dragon_balls_randomized),
    LocationGroup("DU: Vegeta: Dragon Radars", 29, [], dragon_radar_randomized),
    LocationGroup("DU: Piccolo: Bosses", 30, Locations.PICCOLO_BOSSES),
    LocationGroup("DU: Piccolo: Capsules", 31, Locations.PICCOLO_CAPSULES),
    LocationGroup("DU: Piccolo: Money", 32, []),
    LocationGroup("DU: Piccolo: Dragon Balls", 33, [], dragon_balls_randomized),
    LocationGroup("DU: Piccolo: Dragon Radars", 34, [], dragon_radar_randomized),
    LocationGroup("DU: Tien: Bosses", 35, Locations.TIEN_BOSSES),
    LocationGroup("DU: Tien: Capsules", 36, Locations.TIEN_CAPSULES),
    LocationGroup("DU: Tien: Money", 37, []),
    LocationGroup("DU: Tien: Dragon Balls", 38, [], dragon_balls_randomized),
    LocationGroup("DU: Tien: Dragon Radars", 39, [], dragon_radar_randomized),
    LocationGroup("DU: Yamcha: Bosses", 40, Locations.YAMCHA_BOSSES),
    LocationGroup("DU: Yamcha: Capsules", 41, Locations.YAMCHA_CAPSULES),
    LocationGroup("DU: Yamcha: Money", 42, []),
    LocationGroup("DU: Yamcha: Dragon Balls", 43, [], dragon_balls_randomized),
    LocationGroup("DU: Yamcha: Dragon Radars", 44, [], dragon_radar_randomized),
    LocationGroup("DU: Uub: Bosses", 45, Locations.UUB_BOSSES),
    LocationGroup("DU: Uub: Capsules", 46, Locations.UUB_CAPSULES),
    LocationGroup("DU: Uub: Money", 47, []),
    LocationGroup("DU: Uub: Dragon Balls", 48, [], dragon_balls_randomized),
    LocationGroup("DU: Uub: Dragon Radars", 49, [], dragon_radar_randomized),
    LocationGroup("DU: Broly: Bosses", 50, Locations.BROLY_BOSSES),
    LocationGroup("DU: Broly: Capsules", 51, Locations.BROLY_CAPSULES),
    LocationGroup("DU: Broly: Money", 52, []),
    LocationGroup("DU: Broly: Dragon Balls", 53, [], dragon_balls_randomized),
    LocationGroup("DU: Broly: Dragon Radars", 54, [], dragon_radar_randomized),
    LocationGroup("DU: Difficulty", 55, Locations.DU_DIFFICULTIES, return_true),
    LocationGroup("DU: Reenactments", 56, Locations.DU_REENACTMENTS),
    LocationGroup("Dragon Arena: Break-Ins", 57, Locations.DA_BREAK_IN_LOCS, return_true),
    LocationGroup("Dragon Arena: Challenger Milestones", 58, Locations.DA_CHALLENGER_LOCS, return_true),
    LocationGroup("World Tournament", 59, Locations.WT_LOCS, return_true),
    LocationGroup("Training", 60, Locations.TRAINING_LOCS, return_true),
    LocationGroup("Skill Shop", 61, Locations.SHOP_LOCS, shop_randomized)
]

ALL_LOCATIONS: Sequence[LocationData] = [
    location
    for locations in [group.locations for group in LOCATION_GROUPS]
    for location in locations
]


def get_active_locations(options_as_dict: dict[str, Any]):
    active_groups = [group for group in LOCATION_GROUPS if group.enable_if(options_as_dict)]
    group_locations = [group.locations for group in active_groups]
    return [location for location in group_locations]