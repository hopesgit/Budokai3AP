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

def minimalist_enabled(slot_data: dict[str, int]) -> bool:
    return bool(slot_data["minimalist"])

def non_minimalist(slot_data: dict[str, int]) -> bool:
    return not minimalist_enabled(slot_data)

def goku_non_minimal(slot_data) -> bool:
    return goku_enabled(slot_data) and non_minimalist(slot_data)

def kid_gohan_non_minimal(slot_data) -> bool:
    return kid_gohan_enabled(slot_data) and non_minimalist(slot_data)

def teen_gohan_non_minimal(slot_data) -> bool:
    return teen_gohan_enabled(slot_data) and non_minimalist(slot_data)

def gohan_non_minimal(slot_data) -> bool:
    return gohan_enabled(slot_data) and non_minimalist(slot_data)

def krillin_non_minimal(slot_data) -> bool:
    return krillin_enabled(slot_data) and non_minimalist(slot_data)

def piccolo_non_minimal(slot_data) -> bool:
    return piccolo_enabled(slot_data) and non_minimalist(slot_data)

def vegeta_non_minimal(slot_data) -> bool:
    return vegeta_enabled(slot_data) and non_minimalist(slot_data)

def tien_non_minimal(slot_data) -> bool:
    return tien_enabled(slot_data) and non_minimalist(slot_data)

def yamcha_non_minimal(slot_data) -> bool:
    return yamcha_enabled(slot_data) and non_minimalist(slot_data)

def uub_non_minimal(slot_data) -> bool:
    return uub_enabled(slot_data) and non_minimalist(slot_data)

def broly_non_minimal(slot_data) -> bool:
    return broly_enabled(slot_data) and non_minimalist(slot_data)


class LocationGroup(NamedTuple):
    name: str
    locations: Sequence[LocationData] = []
    enable_if: Callable = return_true
    

LOCATION_GROUPS: Sequence[LocationGroup] = [
    # Goku
    LocationGroup("DU: Goku: Story Bosses", Locations.GOKU_STORY_BOSSES, goku_enabled),
    LocationGroup("DU: Goku: Optional Bosses", Locations.GOKU_OPT_BOSSES, goku_non_minimal),
    LocationGroup("DU: Goku: Story Capsules", Locations.GOKU_CAPSULES, goku_enabled),
    LocationGroup("DU: Goku: Optional Capsules", [], goku_non_minimal),
    LocationGroup("DU: Goku: Wishes", Locations.GOKU_WISH_LOCS, goku_non_minimal),
    LocationGroup("DU: Goku: Reenactments", Locations.GOKU_REENACTMENTS, goku_non_minimal),
    LocationGroup("DU: Goku: Money", Locations.GOKU_MONEY_SPOTS, 
                  lambda slot_data: goku_enabled(slot_data) and money_spots_randomized(slot_data)),
    LocationGroup("DU: Goku: Dragon Balls", Locations.GOKU_DRAGON_BALLS, 
                  lambda slot_data: goku_enabled(slot_data) and dragon_balls_randomized(slot_data)),
    LocationGroup("DU: Goku: Dragon Radars", Locations.GOKU_DRAGON_RADARS, 
                  lambda slot_data: goku_enabled(slot_data) and dragon_radar_randomized(slot_data)),

    # Kid Gohan
    LocationGroup("DU: Kid Gohan: Story Bosses", Locations.KID_GOHAN_STORY_BOSSES, kid_gohan_enabled),
    LocationGroup("DU: Kid Gohan: Optional Bosses", Locations.KID_GOHAN_OPT_BOSSES, kid_gohan_non_minimal),
    LocationGroup("DU: Kid Gohan: Story Capsules", Locations.KID_GOHAN_STORY_CAPSULES, kid_gohan_enabled),
    LocationGroup("DU: Kid Gohan: Optional Capsules", Locations.KID_GOHAN_OPT_CAPSULES, kid_gohan_non_minimal),
    LocationGroup("DU: Kid Gohan: Wish", Locations.KID_GOHAN_WISH_LOCS, kid_gohan_non_minimal),
    LocationGroup("DU: Kid Gohan: Reenactments", Locations.KID_GOHAN_REENACTMENTS, kid_gohan_non_minimal),
    LocationGroup("DU: Kid Gohan: Money", Locations.KID_GOHAN_MONEY_SPOTS, 
                  lambda slot_data: kid_gohan_enabled(slot_data) and money_spots_randomized(slot_data)),
    LocationGroup("DU: Kid Gohan: Dragon Balls", Locations.KID_GOHAN_DRAGON_BALLS, 
                  lambda slot_data: kid_gohan_enabled(slot_data) and dragon_balls_randomized(slot_data)),
    LocationGroup("DU: Kid Gohan: Dragon Radars", Locations.KID_GOHAN_DRAGON_RADARS, 
                  lambda slot_data: kid_gohan_enabled(slot_data) and dragon_radar_randomized(slot_data)),

    # # Teen Gohan
    # LocationGroup("DU: Teen Gohan: Story Bosses", Locations.TEEN_GOHAN_STORY_BOSSES, teen_gohan_enabled),
    # LocationGroup("DU: Teen Gohan: Optional Bosses", Locations.TEEN_GOHAN_OPT_BOSSES, teen_gohan_non_minimal),
    # LocationGroup("DU: Teen Gohan: Story Capsules", Locations.TEEN_GOHAN_STORY_CAPSULES, teen_gohan_enabled),
    # LocationGroup("DU: Teen Gohan: Optional Capsules", Locations.TEEN_GOHAN_OPT_CAPSULES, teen_gohan_non_minimal),
    # LocationGroup("DU: Teen Gohan: Reenactments", Locations.TEEN_GOHAN_REENACTMENTS, teen_gohan_enabled),
    # LocationGroup("DU: Teen Gohan: Money", []),
    # LocationGroup("DU: Teen Gohan: Dragon Balls", [], dragon_balls_randomized),
    # LocationGroup("DU: Teen Gohan: Dragon Radars", [], dragon_radar_randomized),

    # # Gohan
    # LocationGroup("DU: Gohan: Bosses", Locations.GOHAN_BOSSES),
    # LocationGroup("DU: Gohan: Capsules", Locations.GOHAN_CAPSULES),
    # LocationGroup("DU: Gohan: Money", []),
    # LocationGroup("DU: Gohan: Dragon Balls", [], dragon_balls_randomized),
    # LocationGroup("DU: Gohan: Dragon Radars", [], dragon_radar_randomized),
    
    # # Krillin
    # LocationGroup("DU: Krillin: Bosses", Locations.KRILLIN_BOSSES),
    # LocationGroup("DU: Krillin: Capsules", Locations.KRILLIN_CAPSULES),
    # LocationGroup("DU: Krillin: Money", []),
    # LocationGroup("DU: Krillin: Dragon Balls", [], dragon_balls_randomized),
    # LocationGroup("DU: Krillin: Dragon Radars", [], dragon_radar_randomized),
    
    # # Vegeta
    # LocationGroup("DU: Vegeta: Bosses", Locations.VEGETA_BOSSES),
    # LocationGroup("DU: Vegeta: Capsules", Locations.VEGETA_CAPSULES),
    # LocationGroup("DU: Vegeta: Money", []),
    # LocationGroup("DU: Vegeta: Dragon Balls", [], dragon_balls_randomized),
    # LocationGroup("DU: Vegeta: Dragon Radars", [], dragon_radar_randomized),
    
    # # Piccolo
    # LocationGroup("DU: Piccolo: Bosses", Locations.PICCOLO_BOSSES),
    # LocationGroup("DU: Piccolo: Capsules", Locations.PICCOLO_CAPSULES),
    # LocationGroup("DU: Piccolo: Money", 32, []),
    # LocationGroup("DU: Piccolo: Dragon Balls", 33, [], dragon_balls_randomized),
    # LocationGroup("DU: Piccolo: Dragon Radars", 34, [], dragon_radar_randomized),
    
    # # Tien
    # LocationGroup("DU: Tien: Bosses", 35, Locations.TIEN_BOSSES),
    # LocationGroup("DU: Tien: Capsules", 36, Locations.TIEN_CAPSULES),
    # LocationGroup("DU: Tien: Money", 37, []),
    # LocationGroup("DU: Tien: Dragon Balls", 38, [], dragon_balls_randomized),
    # LocationGroup("DU: Tien: Dragon Radars", 39, [], dragon_radar_randomized),
    
    # # Yamcha
    # LocationGroup("DU: Yamcha: Bosses", 40, Locations.YAMCHA_BOSSES),
    # LocationGroup("DU: Yamcha: Capsules", 41, Locations.YAMCHA_CAPSULES),
    # LocationGroup("DU: Yamcha: Money", 42, []),
    # LocationGroup("DU: Yamcha: Dragon Balls", 43, [], dragon_balls_randomized),
    # LocationGroup("DU: Yamcha: Dragon Radars", 44, [], dragon_radar_randomized),
    
    # # Uub
    # LocationGroup("DU: Uub: Bosses", 45, Locations.UUB_BOSSES),
    # LocationGroup("DU: Uub: Capsules", 46, Locations.UUB_CAPSULES),
    # LocationGroup("DU: Uub: Money", 47, []),
    # LocationGroup("DU: Uub: Dragon Balls", 48, [], dragon_balls_randomized),
    # LocationGroup("DU: Uub: Dragon Radars", 49, [], dragon_radar_randomized),
    
    # # Broly
    # LocationGroup("DU: Broly: Bosses", 50, Locations.BROLY_BOSSES),
    # LocationGroup("DU: Broly: Capsules", 51, Locations.BROLY_CAPSULES),
    # LocationGroup("DU: Broly: Money", 52, []),
    # LocationGroup("DU: Broly: Dragon Balls", 53, [], dragon_balls_randomized),
    # LocationGroup("DU: Broly: Dragon Radars", 54, [], dragon_radar_randomized),
    
    # Others
    LocationGroup("DU: Difficulty", Locations.DU_DIFFICULTIES, non_minimalist),
    LocationGroup("Dragon Arena: Break-Ins", Locations.DA_BREAK_IN_LOCS, non_minimalist),
    LocationGroup("Dragon Arena: Challenger Milestones", Locations.DA_CHALLENGER_LOCS, non_minimalist),
    LocationGroup("World Tournament", Locations.WT_LOCS, non_minimalist),
    LocationGroup("Training", Locations.TRAINING_LOCS, non_minimalist),
    LocationGroup("Skill Shop", Locations.SHOP_LOCS, shop_randomized)
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