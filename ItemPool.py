from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Item
from .data import Items, Locations
from .data.Items import CoordData, EquipmentData, ProgressiveUpgradeData, ItemData
from .Budokai3Options import StartWithStoryCharacters, StartWithSuperAttacks

if TYPE_CHECKING:
    from . import Rac2World


def get_classification(item: ItemData)