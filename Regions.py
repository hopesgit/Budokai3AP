import typing
from BaseClasses import Region
from .data.Locations import GOKU_LOCS, GOKU_WISH_LOCS, DRAGON_ARENA_LOCS, WT_LOCS, SHOP_LOCS, TRAINING_LOCS, MENU_CAPSULE_1


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
    connections: typing.List[str]
    locations: typing.List[str]

    def __init__(self, name, connections, locations):
        self.name = name
        self.connections = connections
        self.locations = locations


regions = [
    RegionInfo(RegionName.Menu, 
               [RegionName.DU_Goku, RegionName.Dragon_Arena, RegionName.Tournament, RegionName.Shop, RegionName.Training], []),
    RegionInfo(RegionName.Training, [RegionName.Menu], [location.name for location in TRAINING_LOCS]),
    RegionInfo(RegionName.Tournament, [RegionName.Menu], [location.name for location in WT_LOCS]),
    RegionInfo(RegionName.Shop, [RegionName.Menu], [location.name for location in SHOP_LOCS]),
    RegionInfo(RegionName.Dragon_Arena, [RegionName.Menu], [location.name for location in DRAGON_ARENA_LOCS]),
    RegionInfo(RegionName.DU_Goku, [RegionName.Menu, RegionName.Shenron_Goku, RegionName.Credits], 
               [location.name for location in GOKU_LOCS]),
    RegionInfo(RegionName.Shenron_Goku, [RegionName.Credits], [location.name for location in GOKU_WISH_LOCS]),
    RegionInfo(RegionName.Credits, [RegionName.Menu, RegionName.Congrats], []),
    RegionInfo(RegionName.Congrats, [RegionName.Menu], [MENU_CAPSULE_1.name])
]