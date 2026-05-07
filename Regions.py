from typing import List
from BaseClasses import Region
from .LocationPool import LocationGroup, get_active_location_groups
from .data.Locations import GOKU_LOCS, GOKU_WISH_LOCS, MENU_CAPSULE_1

class Budokai3Region(Region):
    game = "Dragon Ball Z Budokai 3"

class RegionName:
    Menu = "Menu"
    DU_Goku = "Dragon Universe - Goku"
    DU_KidGohan = "Dragon Universe - Kid Gohan"
    DU_TeenGohan = "Dragon Universe - Teen Gohan"
    DU_Gohan = "Dragon Universe - Gohan"
    DU_Krillin = "Dragon Universe - Krillin"
    DU_Piccolo = "Dragon Universe - Piccolo"
    DU_Tien = "Dragon Universe - Tien"
    DU_Yamcha = "Dragon Universe - Yamcha"
    DU_Vegeta = "Dragon Universe - Vegeta"
    DU_Uub = "Dragon Universe - Uub"
    DU_Broly = "Dragon Universe - Broly"
    Shenron_Goku = "Shenron - Goku"
    Shenron_KidGohan = "Shenron - Kid Gohan"
    Shenron_TeenGohan = "Shenron - Teen Gohan"
    Shenron_Gohan = "Shenron - Gohan"
    Shenron_Krillin = "Shenron - Krillin"
    Shenron_Piccolo = "Shenron - Piccolo"
    Shenron_Tien = "Shenron - Tien"
    Shenron_Yamcha = "Shenron - Yamcha"
    Shenron_Vegeta = "Shenron - Vegeta"
    Shenron_Uub = "Shenron - Uub"
    Shenron_Broly = "Shenron - Broly"
    Dragon_Arena = "Dragon Arena"
    Training = "Training"
    Shop = "Shop"
    Tournament = "Tournament"
    Credits = "Credits"
    Congrats = "Congratulations"


class RegionInfo:
    name: str
    connections: list[str]
    groups: list[LocationGroup]
    locations: list[str]

    def __init__(self, name, connections, groups):
        self.name = name
        self.connections = connections
        self.groups = groups
        locations = []
        for group in self.groups:
            if not group: continue
            for location in group.locations:
                locations.append(location.name)
        self.locations = locations

def create_regions(slot_data):
    locgroups = get_active_location_groups(slot_data)
    regions = [
        RegionInfo(
            name=RegionName.Menu,
            connections=[RegionName.Dragon_Arena, RegionName.Congrats], # remove congrats from this later
            # add back later: RegionName.DU_Goku, RegionName.Tournament, RegionName.Shop, RegionName.Training
            groups=[]
        ),
        # RegionInfo(RegionName.Training, [RegionName.Menu], [locgroups[-3]]),
        # RegionInfo(RegionName.Tournament, [RegionName.Menu], [locgroups[-4]]),
        # RegionInfo(RegionName.Shop, [RegionName.Menu], [locgroups[-2]]),
        RegionInfo(RegionName.Dragon_Arena, [RegionName.Menu], [*locgroups[-7:-5]]),
        # RegionInfo(
        #     name=RegionName.DU_Goku,
        #     connections=[RegionName.Shenron_Goku, RegionName.Credits],
        #     groups=[*locgroups[0:3], *locgroups[5:8]]
        # ),
        # RegionInfo(RegionName.Shenron_Goku, [RegionName.Credits], [locgroups[4]]),
        # RegionInfo(RegionName.Credits, [RegionName.Congrats], []),
        RegionInfo(RegionName.Congrats, [RegionName.Menu], [locgroups[-1]]),
    ]
    return regions
