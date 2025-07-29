from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Item, CollectionState

from .data import Items, Locations
from .data.Items import ItemData
from .Budokai3Options import StartWithStoryCharacters, StartWithSuperAttacks

if TYPE_CHECKING:
    from . import Budokai3World


def get_classification(item: ItemData):
    match item.color:
        case _: return  ItemClassification.filler


def create_equipment(world: "Rac2World") -> list["Item"]:
    equipment_to_add: list[EquipmentData] = list(Items.EQUIPMENT)

    # Starting Weapons
    weapons: list[EquipmentData] = []
    if world.options.starting_weapons == StartingWeapons.option_balanced:
        weapons = [weapon for weapon in Items.LV1_WEAPONS if weapon.power <= 5]
    elif world.options.starting_weapons == StartingWeapons.option_non_broken:
        weapons = [weapon for weapon in Items.LV1_WEAPONS if weapon.power < 10]
    elif world.options.starting_weapons == StartingWeapons.option_unrestricted:
        weapons = list(Items.LV1_WEAPONS)

    if len(weapons) > 0:
        world.random.shuffle(weapons)
    else:
        weapons = [Items.LANCER, Items.GRAVITY_BOMB]

    world.multiworld.push_precollected(world.create_item(weapons[0].name))
    world.multiworld.push_precollected(world.create_item(weapons[1].name))
    world.starting_weapons = [weapons[0], weapons[1]]
    if Items.LANCER not in world.starting_weapons:
        equipment_to_add.append(Items.LANCER)
    if Items.GRAVITY_BOMB not in world.starting_weapons:
        equipment_to_add.append(Items.GRAVITY_BOMB)

    # Gadgetron Vendor
    if world.options.randomize_gadgetron_vendor:
        equipment_to_add += [i for i in Items.GADGETRON_VENDOR_WEAPONS if i not in world.starting_weapons]
    else:
        mapping: list[tuple[Locations.LocationData, Items.WeaponData]] = zip(Locations.GADGETRON_VENDOR_LOCATIONS, Items.GADGETRON_VENDOR_WEAPONS)
        for loc, item in mapping:
            location = world.multiworld.get_location(loc.name, world.player)
            location.place_locked_item(world.create_item(item.name))

    # Megacorp Vendor
    if world.options.randomize_megacorp_vendor:
        equipment_to_add += [i for i in Items.MEGACORP_VENDOR_WEAPONS if i not in world.starting_weapons]
    else:
        mapping: list[tuple[Locations.LocationData, Items.WeaponData]] = zip(Locations.MEGACORP_VENDOR_LOCATIONS, Items.MEGACORP_VENDOR_WEAPONS)
        for loc, item in mapping:
            location = world.multiworld.get_location(loc.name, world.player)
            location.place_locked_item(world.create_item(item.name))

    # Misc Weapons
    equipment_to_add += [Items.SHEEPINATOR]

    # Take out expensive items if they are excluded and in the pool.
    if world.options.exclude_very_expensive_items:
        if Items.RYNO_II in equipment_to_add:
            location = world.multiworld.get_location(Locations.BARLOW_GADGETRON_5.name, world.player)
            location.place_locked_item(world.create_item(Items.RYNO_II.name))
            equipment_to_add.remove(Items.RYNO_II)
        if Items.ZODIAC in equipment_to_add:
            location = world.multiworld.get_location(Locations.ARANOS_VENDOR_WEAPON_2.name, world.player)
            location.place_locked_item(world.create_item(Items.ZODIAC.name))
            equipment_to_add.remove(Items.ZODIAC)

    precollected_ids: list[int] = [item.code for item in world.multiworld.precollected_items[world.player]]
    equipment_to_add = [equipment for equipment in equipment_to_add if equipment.item_id not in precollected_ids]

    return [world.create_item(equipment.name) for equipment in equipment_to_add]


def create_collectables(world: "Rac2World") -> list["Item"]:
    collectable_items: list["Item"] = []

    for _ in range(20):
        collectable_items.append(world.create_item(Items.PLATINUM_BOLT.name))

    precollected_nanotech_boosts: int = len([
        item for item in world.multiworld.precollected_items[world.player]
        if item.code == Items.NANOTECH_BOOST.item_id
    ])
    assert precollected_nanotech_boosts <= Items.NANOTECH_BOOST.max_capacity, "Added too many Nanotech Boosts to Start Inventory"
    for _ in range(Items.NANOTECH_BOOST.max_capacity - precollected_nanotech_boosts):
        collectable_items.append(world.create_item(Items.NANOTECH_BOOST.name))

    precollected_hypnomatic_parts: int = len([
        item for item in world.multiworld.precollected_items[world.player]
        if item.code == Items.HYPNOMATIC_PART.item_id
    ])
    assert precollected_hypnomatic_parts <= Items.HYPNOMATIC_PART.max_capacity, "Added too many Hypnomatic Parts to Start Inventory"
    for _ in range(Items.HYPNOMATIC_PART.max_capacity - precollected_hypnomatic_parts):
        collectable_items.append(world.create_item(Items.HYPNOMATIC_PART.name))

    return collectable_items


def create_upgrades(world: "Rac2World") -> list["Item"]:
    upgrades_to_add: list[ProgressiveUpgradeData] = list(Items.UPGRADES)
    # There are two wrench upgrades, add one more
    upgrades_to_add.append(Items.WRENCH_UPGRADE)

    # Remove the armor upgrade from the pool, as it currently is only for debug purpose
    # TODO: Remove this line once armor locations get implemented
    upgrades_to_add.remove(Items.ARMOR_UPGRADE)

    return [world.create_item(upgrade.name) for upgrade in upgrades_to_add]