from abc import ABC, abstractmethod
from typing import Callable, Sequence, Any, Mapping

from .data import Locations
from .data.Locations import LocationData


def return_true(slot_data: dict[str, int]) -> bool:
    return True

def dragon_radar_randomized(slot_data: dict[str, int]) -> bool:
    val = int(slot_data["randomize_dragon_radar"])
    val = None
    match val:
        case 0:
            return False
        case 1 | 2:
            return True
        case _:
            return False
        
def dragon_balls_randomized(slot_data: dict[str, int]) -> bool:
    val = bool(slot_data["randomize_dragon_balls"])
    return False

def money_spots_randomized(slot_data: dict[str, int]) -> bool:
    val = bool(slot_data["randomize_money_spots"])
    return False

def shop_randomized(slot_data: dict[str, int]) -> bool:
    val = bool(slot_data["shop_rando"])
    return False

def challengersanity(slot_data: dict[str, int]) -> bool:
    val = bool(slot_data["challengersanity"])
    return True

def goku_enabled(slot_data: dict[str, list[str]]) -> bool:
    return False
    # "Goku" in slot_data["choose_du_characters"]

def kid_gohan_enabled(slot_data: dict[str, list[str]]) -> bool:
    return False
    # "Kid Gohan" in slot_data["choose_du_characters"]

def teen_gohan_enabled(slot_data: dict[str, list[str]]) -> bool:
    return False
    # "Teen Gohan" in slot_data["choose_du_characters"]

def gohan_enabled(slot_data: dict[str, list[str]]) -> bool:
    return False
    # "Gohan" in slot_data["choose_du_characters"]

def krillin_enabled(slot_data: dict[str, list[str]]) -> bool:
    return False
    # "Krillin" in slot_data["choose_du_characters"]

def piccolo_enabled(slot_data: dict[str, list[str]]) -> bool:
    return False
    # "Piccolo" in slot_data["choose_du_characters"]

def vegeta_enabled(slot_data: dict[str, list[str]]) -> bool:
    return False
    # "Vegeta" in slot_data["choose_du_characters"]

def tien_enabled(slot_data: dict[str, list[str]]) -> bool:
    return False
    # "Tien" in slot_data["choose_du_characters"]

def yamcha_enabled(slot_data: dict[str, list[str]]) -> bool:
    return False
    # "Yamcha" in slot_data["choose_du_characters"]

def uub_enabled(slot_data: dict[str, list[str]]) -> bool:
    return False
    # "Uub" in slot_data["choose_du_characters"]

def broly_enabled(slot_data: dict[str, list[str]]) -> bool:
    return False
    # "Broly" in slot_data["choose_du_characters"]

def minimalist_enabled(slot_data: dict[str, int]) -> bool:
    return True
    # bool(slot_data["minimalist"])

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


class LocationGroup:
    name: str
    locations: Sequence[LocationData] = []
    include_func: Callable = return_true # Whether to include the group in the world's locations.
    include: bool = True

    def __init__(self, name, locations, include_func):
        self.locations = locations
        self.name = name
        self.include_func = include_func

    def recalculate_include(self, slot_data: dict[str, Any]):
        self.include = self.include_func(slot_data)
    

location_groups: list[LocationGroup] = [
    # Goku
    LocationGroup("DU: Goku: Story Bosses", Locations.GOKU_STORY_BOSSES, goku_enabled),
    LocationGroup("DU: Goku: Optional Bosses", Locations.GOKU_OPT_BOSSES, goku_non_minimal),
    LocationGroup("DU: Goku: Story Capsules", Locations.GOKU_STORY_CAPSULES, goku_enabled),
    LocationGroup("DU: Goku: Optional Capsules", Locations.GOKU_OPT_CAPSULES, goku_non_minimal),
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
    LocationGroup("DU: Kid Gohan: Wishes", Locations.KID_GOHAN_WISH_LOCS, kid_gohan_non_minimal),
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
    # LocationGroup("DU: Teen Gohan: Wishes", Locations.TEEN_GOHAN_WISH_LOCS, teen_gohan_non_minimal)
    # LocationGroup("DU: Teen Gohan: Reenactments", Locations.TEEN_GOHAN_REENACTMENTS, teen_gohan_non_minimal),
    # LocationGroup("DU: Teen Gohan: Money", Locations.TEEN_GOHAN_MONEY_SPOTS,
    #               lambda slot_data: teen_gohan_enabled(slot_data) and money_spots_randomized(slot_data)),
    # LocationGroup("DU: Teen Gohan: Dragon Balls", Locations.TEEN_GOHAN_DRAGON_BALLS,
    #               lambda slot_data: teen_gohan_enabled(slot_data) and dragon_balls_randomized(slot_data)),
    # LocationGroup("DU: Teen Gohan: Dragon Radars", Locations.TEEN_GOHAN_DRAGON_RADARS,
    #               lambda slot_data: teen_gohan_enabled(slot_data) and dragon_radar_randomized(slot_data)),

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
    LocationGroup("Dragon Arena: Break-Ins", Locations.DA_BREAK_IN_LOCS, challengersanity),
    LocationGroup("Dragon Arena: Challenger Milestones", Locations.DA_CHALLENGER_LOCS, challengersanity),
    LocationGroup("Dragon Arena: Challengersanity Locations", Locations.DA_CHALLENGERSANITY_LOCS, challengersanity),
    LocationGroup("World Tournament", Locations.WT_LOCS, non_minimalist),
    LocationGroup("Training", Locations.TRAINING_LOCS, non_minimalist),
    LocationGroup("Skill Shop", Locations.SHOP_LOCS, shop_randomized),
    LocationGroup("Menu", [Locations.MENU_CAPSULE_1], return_true)
]


ALL_LOCATIONS: list[LocationData] = [
    location
    for locations in [group.locations for group in location_groups]
    for location in locations
]


def get_active_location_groups(slot_data) -> list[LocationGroup]:
    """For use in the world. Slot data arg is the world's slot_data property."""
    for index, group in enumerate(location_groups):
        if type(group) == LocationGroup:
            group.recalculate_include(slot_data)
            if group.include:
                location_groups[index] = group
            else:
                location_groups[index] = None
        else: continue
    return location_groups


def get_active_locations(slot_data) -> list[LocationData]:
    """For use in the ClientCheckLocations file. Slot data arg is the client's slot_data property."""
    print(f'in get_active_locations: slot_data is {slot_data}')
    location_groups = get_active_location_groups(slot_data)
    locgroups = get_active_location_groups(slot_data)
    print('in get_active_locations: locgroups exists')
    loclist: list[LocationData] = []
    for group in locgroups:
        if not group:
            continue
        for location in group.locations:
            loclist.append(location)
    print(f'in get_active_locations: loclist is {loclist}')
    return loclist
