from typing import Dict, Optional, Mapping, Any
import typing
import os

from worlds.LauncherComponents import Component, SuffixIdentifier, Type, components, launch_subprocess
import settings
from worlds.AutoWorld import World, WebWorld
from BaseClasses import Item, Tutorial, ItemClassification

# from . import ItemPool
# from .data import Items, Locations
# from .data.Items import EquipmentData
# from .Regions import create_regions
# from .Container import Budokai3ProcedurePatch, generate_patch
from .Budokai3Options import Budokai3Options


def run_client(_url: Optional[str] = None):
    from .Budokai3Client import launch
    launch_subprocess(launch, name="DBZ Budokai 3 Client")


components.append(
    Component("Budokai3Client", func=run_client, component_type=Type.CLIENT,
              file_identifier=SuffixIdentifier(".apdbzb3"))
)


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


class Budokai3Item(Item):
    game: str = "Dragon Ball Z Budokai 3"


class Budokai3World(World):
    """
    Only one will prevail! Dragon Ball Z Budokai 3 is a 2D fighting game based on the Dragon Ball anime series, mainly Dragon Ball Z.
    Released in 2004, DBZ Budokai 3 stars Earth's defenders (and Broly) as you play through the story of Dragon Ball Z from their perspectives.
    The iconic skills and transformations the characters can use are represented by the Exciting Skill System (ESS), skills contained in capsules.
    Power up via capsules and take down your enemies in Dragon World, Tournament, and Dragon Arena modes in order to save the Earth!
    """
    game = "Dragon Ball Z Budokai 3"
    web = Budokai3Web()
    options_dataclass = "Budokai3Options"
    options: Budokai3Options
    topology_present = True
    # item_name_to_id = {item.name: item.item_id for item in Items.ALL}
    # location_name_to_id = {location.name: location.location_id for location in Planets.ALL_LOCATIONS if location.location_id}
    # item_name_groups = Items.get_item_groups()
    # location_name_groups = Planets.get_location_groups()
    settings: Budokai3Settings
    # starting_planet: Optional[PlanetData] = None
    # starting_weapons: list[EquipmentData] = []
    prefilled_item_map: Dict[str, str] = {}  # Dict of location name to item name

    # def get_filler_item_name(self) -> str:
    #     return Items.BOLT_PACK.name

    # def create_regions(self) -> None:
    #     create_regions(self)

    # def create_item(self, name: str, override: Optional[ItemClassification] = None) -> "Item":
    #     if override:
    #         return Budokai3Item(name, override, self.item_name_to_id[name], self.player)
    #     item_data = Items.from_name(name)
    #     return Budokai3Item(name, ItemPool.get_classification(item_data), self.item_name_to_id[name], self.player)

    # def create_event(self, name: str) -> "Item":
    #     return Budokai3Item(name, ItemClassification.progression, None, self.player)

    # def pre_fill(self) -> None:
    #     for location_name, item_name in self.prefilled_item_map.items():
    #         location = self.get_location(location_name)
    #         item = self.create_item(item_name, ItemClassification.progression)
    #         location.place_locked_item(item)
    #
    # def create_items(self) -> None:
    #     items_to_add: list["Item"] = []
    #     items_to_add += ItemPool.create_planets(self)
    #     items_to_add += ItemPool.create_equipment(self)
    #     items_to_add += ItemPool.create_collectables(self)
    #     items_to_add += ItemPool.create_upgrades(self)

        # # add platinum bolts in whatever slots we have left
        # unfilled = [i for i in self.multiworld.get_unfilled_locations(self.player) if not i.is_event]
        # remain = len(unfilled) - len(items_to_add)
        # assert remain >= 0, "There are more items than locations. This is not supported."
        # print(f"Not enough items to fill all locations. Adding {remain} filler items to the item pool")
        # for _ in range(remain):
        #     items_to_add.append(self.create_item(Items.BOLT_PACK.name, ItemClassification.filler))
        #
        # self.multiworld.itempool += items_to_add

    # def set_rules(self) -> None:
    #     boss_location = self.multiworld.get_location(Locations.YEEDIL_DEFEAT_MUTATED_PROTOPET.name, self.player)
    #     boss_location.place_locked_item(self.create_event("Victory"))
    #     self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
    #
    # def generate_output(self, output_directory: str) -> None:
    #     apdbzb3 = Budokai3ProcedurePatch(player=self.player, player_name=self.multiworld.get_player_name(self.player))
    #     generate_patch(self, apdbzb3)
    #     rom_path = os.path.join(output_directory,
    #                             f"{self.multiworld.get_out_file_name_base(self.player)}{apdbzb3.patch_file_ending}")
    #     apdbzb3.write(rom_path)
    #
    # def get_options_as_dict(self) -> Dict[str, Any]:
    #     return self.options.as_dict(
    #         "death_link",
    #         "skip_wupash_nebula",
    #         "extra_spaceship_challenge_locations",
    #         "starting_weapons",
    #         "randomize_megacorp_vendor",
    #         "randomize_gadgetron_vendor",
    #         "extend_weapon_progression",
    #     )
    #
    # def fill_slot_data(self) -> Mapping[str, Any]:
        return self.get_options_as_dict()