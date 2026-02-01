import os
import typing
from typing import Any, Dict, Mapping, Optional, List, TYPE_CHECKING

import settings
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import Component, SuffixIdentifier, Type, components, launch_subprocess, icon_paths

from BaseClasses import MultiWorld, Tutorial, Region, Location, ItemClassification, Item
from .data.Items import item_name_groups
from .Regions import regions, RegionName
# from .Container import Budokai3ProcedurePatch, generate_patch
from .Budokai3Options import Budokai3Options
from . import ItemPool, LocationPool
from .data import Items, Locations
from .data.Items import Capsule
from .import Logic

version = "0.1.0"


def run_client(_url: Optional[str] = None):
    from .Budokai3Client import launch
    launch_subprocess(launch, name="DBZ Budokai 3 Client")


components.append(
    Component(
        "DBZ Budokai 3 Client", 
        func=run_client, 
        component_type=Type.CLIENT,
        file_identifier=SuffixIdentifier(".apdbzb3"),
        icon="Budokai 3"
    )
)
icon_paths["Budokai 3"] = "ap:worlds.dbz_budokai_3.data/img/budokai3logo.png"

class OptionError(ValueError):
    pass

class Budokai3Settings(settings.Group):
    class IsoFile(settings.UserFilePath):
        """File name of the DBZ Budokai 3 ISO"""
        description = "DBZ Budokai 3 PS2 ISO file"
        copy_to = "Budokai3.iso"

    class IsoStart(str):
        """
        Set this false to never autostart an iso (such as after patching),
        Set it to true to have the operating system default program open the iso
        Alternatively, set it to a path to a program to open the .iso file with (like PCSX2)
        """

    class GameINI(str):
        """ Set to file path to an existing PCSX2 game setting INI file to have the patcher
        create an appropriately named INI with the rest of the patch output. This can be used to
        allow you to use you own custom PCSX2 setting with patched ISO. """

    iso_file: IsoFile = IsoFile(IsoFile.copy_to)
    iso_start: typing.Union[IsoStart, bool] = False
    game_ini: GameINI = ""


class Budokai3Web(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up DBZ Budokai 3 for Archipelago",
        "English",
        "setup.md",
        "setup/en",
        ["kenna_puppers"]
    )]
    theme="ocean"


class Budokai3World(World):
    """
    Only one will prevail! Dragon Ball Z Budokai 3 is a 2D fighting game based on the Dragon Ball anime series, mainly Dragon Ball Z.
    Released in 2004, DBZ Budokai 3 stars Earth's defenders (and Broly) as you play through the story of Dragon Ball Z from their perspectives.
    The iconic attacks and transformations the characters can use are represented by the Exciting Skill System (ESS), skills contained in capsules.
    Power up via capsules and take down your enemies in Dragon Universe, Tournament, and Dragon Arena modes in order to save the Earth!
    """
    game = "Dragon Ball Z Budokai 3"
    web = Budokai3Web()
    options_dataclass = Budokai3Options
    options = Budokai3Options
    topology_present = True
    item_name_to_id = {item.name: item.code for item in Items.ALL_ITEMS}
    location_name_to_id = {location.name: location.location_id for location in Locations.LOCATIONS}
    item_name_groups = item_name_groups()
    settings: Budokai3Settings
    starting_items: List[Capsule] = []
    ut_loaded: bool
    passthrough: dict[str, Any]
    ut_can_gen_without_yaml = True
    disable_ut: bool = False


    def __init__(self, multiworld: 'MultiWorld', player: int):
        super().__init__(multiworld, player)
        sd = self.fill_slot_data()
        self.slot_data = sd
        self.location_name_groups = LocationPool.get_active_locations(sd)


    def create_item(self, name: str) -> Capsule:
        return Items.get_name_pairs()[name]


    def get_filler_item_name(self) -> str:
        return Items.ZENIE_2K.name


    def create_regions(self) -> None:
        player = self.player
        name_to_region = {}
        for region_info in regions:
            region = Region(region_info.name, player, self.multiworld)
            name_to_region[region_info.name] = region
            for location in region_info.locations:
                loc = Location(player, location, self.location_name_to_id.get(location), region)
                region.locations.append(loc)
            self.multiworld.regions.append(region)
    
        for region_info in regions:
            region = name_to_region[region_info.name]
            for connection in region_info.connections:
                entrance = region.connect(name_to_region[connection])
                if connection == RegionName.Shenron_Goku:
                    entrance.access_rule = lambda state: Logic.can_wish_goku(state, self.player)
                if connection == RegionName.DU_Goku:
                    entrance.access_rule = lambda state: Logic.has_goku(state, self.player)
                if connection == RegionName.Dragon_Arena:
                    entrance.access_rule = lambda state: Logic.has_dragon_arena(state, self.player)
                if connection in [RegionName.Menu, RegionName.Shop, RegionName.Credits]:
                    entrance.access_rule = lambda state: True


    def create_event(self, name: str) -> "Item":
        return Item(name, ItemClassification.progression, None, self.player)

    # def pre_fill(self) -> None:
    #     for location_name, item_name in self.prefilled_item_map.items():
    #         location = self.get_location(location_name)
    #         item = self.create_item(item_name, ItemClassification.progression)
    #         location.place_locked_item(item)
    #
    def create_items(self) -> None:
        items_to_add: List[Capsule] = []
        items_to_add += ItemPool.create_grays(False)
        # # items_to_add += ItemPool.create_greens()
        # items_to_add += ItemPool.create_yellows()
        items_to_add += ItemPool.create_reds(False)

        unfilled_locs = [item for item in self.multiworld.get_unfilled_locations(self.player) if not item.is_event]
        remaining = len(unfilled_locs) - len(items_to_add)
        assert remaining >= 0, "There are more items than locations."
        print(f"[Budokai 3]: Trying to fill {remaining} remaining locations...")
        for _ in range(remaining):
            item = Capsule(531, self.get_filler_item_name())
            items_to_add.append(item)

        self.multiworld.itempool = items_to_add


    def set_rules(self) -> None:
        congrats = self.multiworld.get_location(Locations.MENU_CAPSULE_1.name, self.player)
        congrats.place_locked_item(self.create_event("Victory"))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
    

    # def generate_output(self, output_directory: str) -> None:
    #     apdbzb3 = Budokai3ProcedurePatch(player=self.player, player_name=self.multiworld.get_player_name(self.player))
    #     generate_patch(self, apdbzb3)
    #     rom_path = os.path.join(output_directory,
    #                             f"{self.multiworld.get_out_file_name_base(self.player)}{apdbzb3.patch_file_ending}")
    #     apdbzb3.write(rom_path)
    
    def get_options_as_dict(self) -> Dict[str, Any]:
        return self.options.as_dict(self,
            "completionist",
            "choose_du_characters",
            "start_with_story_characters",
            "require_super_attacks",
            "super_attack_starters",
            "progressive_characters",
            "randomize_dragon_radar",
            "randomize_dragon_balls",
            "randomize_money_spots",
            "shop_rando",
            "attack_rando",
            "inspiration",
            "pandemic",
            "colorblind_mode_red",
            "colorblind_mode_blue",
            "colorblind_mode_green",
            "death_link",
        )
    
    def fill_slot_data(self) -> dict[str, Any]:
        return self.get_options_as_dict()


    def fill_hook(self,
                  progitempool: List["Item"],
                  usefulitempool: List["Item"],
                  filleritempool: List["Item"],
                  fill_locations: List["Location"]) -> None:
        pass

    def generate_early(self):
        self.handle_option_issues()
        self.location_name_groups = LocationPool.get_active_locations(self.fill_slot_data())
        self.create_regions()

    def handle_option_issues(self):
        opts = self.options
        if bool(opts.completionist.value) and bool(opts.minimalist.value):
            raise OptionError("Minimalist and Completionist are opposites. You cannot combine these.")
        if not opts.choose_du_characters.value:
            raise OptionError("Choosing 0 DU characters results in too few locations to generate. Please choose at least 1 character.")
        

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        return slot_data