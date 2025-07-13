from dataclasses import dataclass
from abc import ABC

from typing import Callable, TYPE_CHECKING, Sequence, Optional, Dict, Set

if TYPE_CHECKING:
    from ..Budokai3Interface import Budokai3Interface


@dataclass
class ItemData(ABC):
    item_id: int
    name: str

    def __init__(self, id: int, name: str):
        self.item_id = id
        self.name = name


def get_capsule_color(item: ItemData) -> int:
    if item.item_id < 400:
        return 1
    elif item.item_id < 500:
        return 2
    elif item.item_id < 600:
        return 3
    else: return 4


@dataclass
class Capsule(ItemData):
    offset: int
    capsule_color: int
    stacks: bool

    def __init__(self, id: int, name: str, offset=0x0, stacks = False):
        super().__init__(id, name)
        self.offset = offset
        self.stacks = stacks

class RedCapsule(Capsule):
    capsule_color = 1

class GreenCapsule(Capsule):
    capsule_color = 2

class YellowCapsule(Capsule):
    capsule_color = 3

class GrayCapsule(Capsule):
    capsule_color = 4


# Ability Capsules (Red)
## Goku
KAIOKEN = RedCapsule(1, "Kaioken")
SSJ_GOKU = RedCapsule(2, "Super Saiyan (Goku)")
SSJ2_GOKU = RedCapsule(3, "Super Saiyan 2 (Goku)")
SSJ3_GOKU = RedCapsule(4, "Super Saiyan 3 (Goku)")
SSJ4_GOKU = RedCapsule(5, "Super Saiyan 4 (Goku)")
KAME_GOKU = RedCapsule(6, "Kamehameha (Goku)", stacks=True)
DRAG_FIST_GOKU = RedCapsule(7, "Dragon Fist", stacks=True)
WARP_KAME_GOKU = RedCapsule(8, "Warp Kamehameha (Goku)", stacks=True)
SPIRIT_BOMB_GOKU = RedCapsule(9, "Spirit Bomb (Goku)", stacks=True)
GOGETA_GOKU = RedCapsule(10, "Fusion - Gogeta (Goku)")
SSJ4_GOGETA_GOKU = RedCapsule(11, "Fusion - Super Saiyan 4 Gogeta (Goku)")
VEGITO_GOKU = RedCapsule(12, "Potara - Vegito (Goku)")
BREAK_GOKU = RedCapsule(13, "Breakthrough (Goku)")

## Kid Goku
KAME_KGOKU = RedCapsule(14, "Kamehameha (Kid Goku)", stacks=True)
RSP_KGOKU = RedCapsule(15, "Rock-Scissors-Paper", stacks=True)
DRAG_FIST_KGOKU = RedCapsule(16, "Super Dragon Fist", stacks=True)
BREAK_KGOKU = RedCapsule(17, "Breakthrough (Kid Goku)")

## Kid Gohan
POTENTIAL_KGOHAN = RedCapsule(18, "Hidden Potential (Kid Gohan)")
MASENKO = RedCapsule(19, "Masenko")
BREAK_KGOHAN = RedCapsule(20, "Breakthrough (Kid Gohan)")

## Teen Gohan
SSJ_TGOHAN = RedCapsule(21, "Super Saiyan (Teen Gohan)")
SSJ2_TGOHAN = RedCapsule(22, "Super Saiyan 2 (Teen Gohan)")
KAME_TGOHAN = RedCapsule(23, "Kamehameha (Teen Gohan)", stacks=True)
SOAR_TGOHAN = RedCapsule(24, "Soaring Dragon Strike (Teen Gohan)", stacks=True)
FS_KAME = RedCapsule(25, "Father-Son Kamehameha", stacks=True)
BREAK_TGOHAN = RedCapsule(26, "Breakthrough (Teen Gohan)")

## Gohan
SSJ_GOHAN = RedCapsule(27, "Super Saiyan (Gohan)")
SSJ2_GOHAN = RedCapsule(28, "Super Saiyan 2 (Gohan)")
ELDER_UNLOCK = RedCapsule(29, "Elder Kai Unlock Ability")
KAME_GOHAN = RedCapsule(30, "Kamehameha (Gohan)", stacks=True)
SOAR_GOHAN = RedCapsule(31, "Soaring Dragon Strike (Gohan)", stacks=True)
SUPER_KAME_GOHAN = RedCapsule(32, "Super Kamehameha", stacks=True)
BREAK_GOHAN = RedCapsule(33, "Breakthrough (Gohan)")

## Gt. Saiyaman
JPUNCH = RedCapsule(34, "Justice Punch", stacks=True)
JKICK = RedCapsule(35, "Justice Kick", stacks=True)
JPOSE = RedCapsule(36, "Justice Pose") # this is not a mistake, though the move certainly is
BREAK_GTS = RedCapsule(37, "Breakthrough (Gt Saiyaman)")

## Goten
SSJ_GOTEN = RedCapsule(38, "Super Saiyan (Goten)")
KAME_GOTEN = RedCapsule(39, "Kamehameha (Goten)", stacks=True)
CHARGE = RedCapsule(40, "Charge", stacks=True)
GOTENKS_GOTEN = RedCapsule(41, "Fusion - Gotenks (Goten)")
BREAK_GOTEN = RedCapsule(42, "Breakthrough (Goten)")

## Vegeta
SSJ_VEGETA = RedCapsule(43, "Super Saiyan (Vegeta)")
SSJ2_VEGETA = RedCapsule(44, "Super Saiyan 2 (Vegeta)")
SSJ4_VEGETA = RedCapsule(45, "Super Saiyan 4 (Vegeta)")
GALICK = RedCapsule(46, "Galick Gun", stacks=True)
FINAL_IMPACT = RedCapsule(47, "Final Impact", stacks=True)
FINAL_FLASH = RedCapsule(48, "Final Flash", stacks=True)
BIG_BANG = RedCapsule(49, "Big Bang Attack", stacks=True)
GOGETA_VEGETA = RedCapsule(50, "Fusion - Gogeta (Vegeta)")
SSJ4_GOGETA_VEGETA = RedCapsule(51, "Fusion - Super Saiyan 4 Gogeta (Vegeta)")
VEGITO_VEGETA = RedCapsule(52, "Potara - Vegito (Vegeta)")
BREAK_VEGETA = RedCapsule(53, "Breakthrough (Vegeta)")

## Trunks
SSJ_TRUNKS = RedCapsule(54, "Super Saiyan (Trunks)")
SSJ2_TRUNKS = RedCapsule(55, "Super Saiyan 2 (Trunks)")
BUSTER_CANNON = RedCapsule(56, "Buster Cannon", stacks=True)
FINISH_BUSTER = RedCapsule(57, "Finish Buster", stacks=True)
BURNING_SLASH = RedCapsule(58, "Burning Slash", stacks=True)
BREAK_TRUNKS = RedCapsule(59, "Breakthrough (Trunks)")

## Kid Trunks
SSJ_KTRUNKS = RedCapsule(60, "Super Saiyan (Kid Trunks)")
DOUBLE_BUSTER = RedCapsule(61, "Double Buster", stacks=True)
FINAL_CANNON = RedCapsule(62, "Final Cannon", stacks=True)
GOTENKS_KTRUNKS = RedCapsule(63, "Fusion - Gotenks (Kid Trunks)")
BREAK_KTRUNKS = RedCapsule(64, "Breakthrough (Kid Trunks)")

## Krillin
POTENTIAL_KRILLIN = RedCapsule(65, "Hidden Potential (Krillin)")
KAME_KRILLIN = RedCapsule(66, "Kamehameha (Krillin)", stacks=True)
DD_KRILLIN = RedCapsule(67, "Destructo Disc (Krillin)", stacks=True)
FIERCE_DD = RedCapsule(68, "Fierce Destructo Disc", stacks=True)
BREAK_KRILLIN = RedCapsule(69, "Breakthrough (Krillin)")

## Piccolo
SYNC_NAIL = RedCapsule(70, "Sync With Nail")
FUSE_KAMI = RedCapsule(71, "Fuse With Kami")
DWAVE = RedCapsule(72, "Destructive Wave", stacks=True)
LGRENADE = RedCapsule(73, "Light Grenade", stacks=True)
SBEAM_CANNON = RedCapsule(74, "Special Beam Cannon", stacks=True)
HZGRENADE = RedCapsule(75, "Hellzone Grenade", stacks=True)
BREAK_PICCOLO = RedCapsule(76, "Breakthrough (Piccolo)")

## Tien
DODON = RedCapsule(77, "Dodompa", stacks=True)
BLAST_CANNON = RedCapsule(78, "Ki Blast Cannon", stacks=True)
NEO_BLAST_CANNON = RedCapsule(79, "Neo Ki Blast Cannon", stacks=True)
BREAK_TIEN = RedCapsule(80, "Breakthrough (Tien)")

## Yamcha
KAME_YAMCHA = RedCapsule(81, "Kamehameha (Yamcha)", stacks=True)
WOLF_FANG = RedCapsule(82, "Wolf Fang Fist", stacks=True)
SPIRIT_BALL = RedCapsule(83, "Spirit Ball Attack", stacks=True)
BREAK_YAMCHA = RedCapsule(84, "Breakthrough (Yamcha)")

## Hercule
TENSION = RedCapsule(85, "High Tension")
DYNAMITE_KICK = RedCapsule(86, "Dynamite Kick", stacks=True)
ROLLING_PUNCH = RedCapsule(87, "Rolling Hercule Punch", stacks=True)
HERC_SPECIAL = RedCapsule(88, "Hercule Special") # same deal as Justice Pose
PRESENT = RedCapsule(89, "Present For You", stacks=True)
BREAK_HERCULE = RedCapsule(90, "Breakthrough (Hercule)")

## Videl
EAGLE_KICK = RedCapsule(91, "Eagle Kick", stacks=True)
HAWK_ARROW = RedCapsule(92, "Hawk Arrow", stacks=True)
CLOSE_CALL = RedCapsule(93, "Videl's Close Call", stacks=True)
BREAK_VIDEL = RedCapsule(94, "Breakthrough (Videl)")

## Supreme Kai
SHOCKWAVE = RedCapsule(95, "Shockwave",stacks=True)
ABILITIES = RedCapsule(96, "Supernatural Abilities", stacks=True)
KIBITOKAI = RedCapsule(97, "Potara - Kibitoshin")
BREAK_SK = RedCapsule(98, "Breakthrough (Supreme Kai)")

## Uub
KI_CANNON = RedCapsule(99, "Ki Cannon", stacks=True)
FIERCE_FLURRY = RedCapsule(100, "Fierce Flurry", stacks=True)
BREAK_UUB = RedCapsule(101, "Breakthrough (Uub)")

## Raditz
SUNDAY = RedCapsule(102, "Double Sunday", stacks=True)
SATURDAY = RedCapsule(103, "Saturday Crush", stacks=True)
BREAK_RADITZ = RedCapsule(104, "Breakthrough (Raditz)")

## Nappa
BOMBER_DX = RedCapsule(105, "Bomber DX", stacks=True)
BREAK_CANNON = RedCapsule(106, "Break Cannon", stacks=True)
GIANT_STORM = RedCapsule(107, "Giant Storm", stacks=True)
BREAK_NAPPA = RedCapsule(108, "Breakthrough (Nappa)")

## Ginyu
SFP1 = RedCapsule(109, "Super Fighting Pose 1")
SFP2 = RedCapsule(110, "Super Fighting Pose 2")
MILKY_CANNON = RedCapsule(111, "Milky Cannon", stacks=True)
STRONG_JERSEY = RedCapsule(112, "Strong Jersey", stacks=True)
BODY_CHANGE = RedCapsule(113, "Body Change", stacks=True)
BREAK_GINYU = RedCapsule(114, "Breakthrough (Capt Ginyu)")

## Recoome
SFP3 = RedCapsule(115, "Super Fighting Pose 3")
SFP4 = RedCapsule(116, "Super Fighting Pose 4")
ERASER_GUN = RedCapsule(117, "Recoome Eraser Gun", stacks=True)
REC_KICK = RedCapsule(118, "Recoome Kick", stacks=True)
REC_BOMBER = RedCapsule(119, "Recoome Bomber", stacks=True)
BREAK_REC = RedCapsule(120, "Breakthrough (Recoome)")

## Frieza
SECOND_FORM = RedCapsule(121, "Second Form")
THIRD_FORM = RedCapsule(122, "Third Form")
FINAL_FORM_FRIEZA = RedCapsule(123, "Final Form (Frieza)")
HUNDRED_PERCENT = RedCapsule(124, "100% Final Form")
DEATH_BEAM = RedCapsule(125, "Death Beam", stacks=True)
DEATH_WAVE = RedCapsule(126, "Death Wave", stacks=True)
DEATH_BALL = RedCapsule(127, "Death Ball", stacks=True)
BREAK_FRIEZA = RedCapsule(128, "Breakthrough (Frieza)")

## Android 16
ROCKET_PUNCH = RedCapsule(129, "Rocket Punch", stacks=True)
HELL_FLASH = RedCapsule(130, "Hell Flash", stacks=True)
BREAK_16 = RedCapsule(131, "Breakthrough (16)")

## Android 17
POWER_BLITZ_17 = RedCapsule(132, "Power Blitz (17)", stacks=True)
ENERGY_FIELD_17 = RedCapsule(133, "Energy Field (17)", stacks=True)
ACCEL_DANCE_17 = RedCapsule(134, "Accel Dance (17)", stacks=True)
BREAK_17 = RedCapsule(135, "Breakthrough (17)")

## Android 18
POWER_BLITZ_18 = RedCapsule(136, "Power Blitz (18)", stacks=True)
DD_18 = RedCapsule(137, "Destructo Disc (18)", stacks=True)
ACCEL_DANCE_18 = RedCapsule(138, "Accel Dance (18)", stacks=True)
BREAK_18 = RedCapsule(139, "Breakthrough (18)")

## Dr. Gero (Android 20)
PHOTON_WAVE = RedCapsule(140, "Photon Wave", stacks=True)
KI_ABSORB = RedCapsule(141, "Ki Blast Absorption", stacks=True)
LIFE_DRAIN = RedCapsule(142, "Life Drain", stacks=True)
BREAK_GERO = RedCapsule(143, "Breakthrough (Dr Gero)")

## Cell
ABSORB_17 = RedCapsule(144, "17 Absorption")
PERFECT_FORM = RedCapsule(145, "Perfect Form")
SUPER_PERFECT = RedCapsule(146, "Super Perfect Form")
KAME_CELL = RedCapsule(147, "Kamehameha (Cell)", stacks=True)
ENERGY_FIELD_CELL = RedCapsule(148, "Energy Field (Cell)", stacks=True)
SPIRIT_BOMB_CELL = RedCapsule(149, "Spirit Bomb (Cell)", stacks=True)
BREAK_CELL = RedCapsule(150, "Breakthrough (Cell)")

## Majin Buu
INN_CANNON = RedCapsule(151, "Innocence Cannon", stacks=True)
INN_EXPRESS = RedCapsule(152, "Innocence Express", stacks=True)
ANGRY_EXPLODE = RedCapsule(153, "Angry Explosion", stacks=True)
BREAK_MBUU = RedCapsule(154, "Breakthrough (Majin Buu)")

## Super Buu
ABSORB = RedCapsule(155, "Absorption")
ILL_FLASH = RedCapsule(156, "Ill Flash", stacks=True)
ILL_BALL = RedCapsule(157, "Ill Ball Attack", stacks=True)
BREAK_SBUU = RedCapsule(158, "Breakthrough (Super Buu)")

## Kid Buu
VANISH_BALL = RedCapsule(159, "Vanish Ball", stacks=True)
KAME_KBUU = RedCapsule(160, "Kamehameha (Kid Buu)", stacks=True)
WARP_KAME_KBUU = RedCapsule(161, "Warp Kamehameha (Kid Buu)", stacks=True)
BREAK_KBUU = RedCapsule(162, "Breakthrough (Kid Buu)")

## Dabura
DEMON_WILL = RedCapsule(163, "Demonic Will")
HELL_BLITZ = RedCapsule(164, "Hell Blitz", stacks=True)
EVIL_BLAST = RedCapsule(165, "Evil Blast", stacks=True)
HELL_RUSH = RedCapsule(166, "Hell Blade Rush", stacks=True)
BREAK_DABURA = RedCapsule(167, "Breakthrough (Dabura)")

## Cooler
FINAL_FORM_COOLER = RedCapsule(168, "Final Form (Cooler)")
DESTRUCT_RAY = RedCapsule(169, "Destructive Ray", stacks=True)
SAUZER_BLADE = RedCapsule(170, "Sauzer Blade", stacks=True)
SUPERNOVA = RedCapsule(171, "Supernova", stacks=True)
BREAK_COOLER = RedCapsule(172, "Breakthrough (Cooler)")

## Bardock
RIOT_JAVELIN = RedCapsule(173, "Riot Javelin", stacks=True)
HEAT_PHALANX = RedCapsule(174, "Heat Phalanx", stacks=True)
SPIRIT_SAIYANS = RedCapsule(175, "Spirit of Saiyans", stacks=True)
BREAK_BARDOCK = RedCapsule(176, "Breakthrough (Bardock)")

## Broly
LSSJ_BROLY = RedCapsule(177, "Legendary Super Saiyan")
BLASTER_SHELL = RedCapsule(178, "Blaster Shell", stacks=True)
GIGANT_PRESS = RedCapsule(179, "Gigantic Press", stacks=True)
GIGANT_METEOR = RedCapsule(180, "Gigantic Meteor", stacks=True)
BREAK_BROLY = RedCapsule(181, "Breakthrough (Broly)")

## Omega Shenron
WHIRLWIND = RedCapsule(182, "Whirlwind Spin", stacks=True)
DTHUNDER = RedCapsule(183, "Dragon Thunder", stacks=True)
MINUS_BALL = RedCapsule(184, "Minus Power Energy Ball", stacks=True)
BREAK_OMEGA = RedCapsule(185, "Breakthrough (Omega Shenron)")

## Saibaman
ACID = RedCapsule(186, "Acid", stacks=True)
SELFDESTRUCT = RedCapsule(187, "Self-Destruct") # also does not stack
BREAK_SAIBA = RedCapsule(188, "Breakthrough (Saibaman)")

## Cell Jr
KAME_CELLJR = RedCapsule(189, "Kamehameha (Cell Jr)", stacks=True)
BREAK_CELLJR = RedCapsule(190, "Breakthrough (Cell Jr)")

# Equipment Capsules (Green)
## Attack up
Z_SWORD = GreenCapsule(191, "Z Sword")
JUICE = GreenCapsule(192, "Juice!")
DAIMAOS_POWER = GreenCapsule(193, "Daimao's Power")
FRUITS_TRAINING = GreenCapsule(194, "Fruits of Training")
VIDELS_KISS = GreenCapsule(195, "Videl's Kiss")
KIBITOS_BACKING = GreenCapsule(196, "Kibito's Backing")
BATTLE_TESTAMENT = GreenCapsule(197, "Battle Testament")
POWER_AMP = GreenCapsule(198, "Power Amplification System")
WARRIOR_GENETICS = GreenCapsule(199, "Warrior Genetics")
DEMON_REALM_FLAMES = GreenCapsule(200, "Demon Realm's Flames")
KAKAROTS_CRYING = GreenCapsule(201, "Kakarot's Crying")
GINYU_SPECIAL_FORCES = GreenCapsule(202, "Ginyu Special Forcees")
COOLER_ARMORED_SQUAD = GreenCapsule(203, "Cooler's Armored Squad")
POWER_FRIENDS = GreenCapsule(204, "Power of Friends")
APPETITES_MEN = GreenCapsule(205, "Appetites of Men")
STRENGTH_SERUM = GreenCapsule(206, "Strength Serum")
KINGS_LINEAGE = GreenCapsule(207, "King's Lineage")
CHEERING = GreenCapsule(208, "Cheering")

## Defense up
GENERAL_VEST = GreenCapsule(209, "General Vest")
TRAINING_VEST = GreenCapsule(210, "Training Vest")
STURDY_VEST = GreenCapsule(211, "Sturdy Vest")
MYSTERIOUS_VEST = GreenCapsule(212, "Mysterious Vest")
VEST_GPA_GOHAN = GreenCapsule(213, "Vest from Grandpa Gohan")
VEST_HOLE_TAIL = GreenCapsule(214, "Vest with Hole for Tail")
TURTLE_VEST = GreenCapsule(215, "Turtle School Vest")
KAMI_VEST = GreenCapsule(216, "Kami's Vest")
TRIBE_UNIFORM = GreenCapsule(217, "Normal Tribe Uniform")
E_TRAINING_UNIFORM = GreenCapsule(218, "Evil Training Uniform")
E_STURDY_UNIFORM = GreenCapsule(219, "Evil Sturdy Uniform")
E_MYSTERY_UNIFORM = GreenCapsule(220, "Evil Mystery Uniform")
NORMAL_JACKET = GreenCapsule(221, "Normal Fiber Jacket")
QUALITY_JACKET = GreenCapsule(222, "Quality Fiber Jacket")
STURDY_JACKET = GreenCapsule(223, "Sturdy Fiber Jacket")
MYSTERY_JACKET = GreenCapsule(224, "Mystery Fiber Jacket")
KAMI_OUTFIT = GreenCapsule(225, "Kami's Outfit")
KINGKAI_OUTFIT = GreenCapsule(226, "King-Kai's Outfit")
GRANDKAI_OUTFIT = GreenCapsule(227, "Grand Kai's Outfit")
SUPREMEKAI_OUTFIT = GreenCapsule(228, "Supreme Kai's Outfit")
OLD_TRAINING_VEST = GreenCapsule(229, "Old Training Vest")
WEDDING_VEST = GreenCapsule(230, "Wedding Vest")
CHAMP_VEST = GreenCapsule(231, "World Champion Vest")
HIGHTECH_VEST = GreenCapsule(232, "High-Tech Vest")
CHAMPION_BELT = GreenCapsule(232, "Champion Belt")
TSHIRT = GreenCapsule(233, "T-shirt")
BLACK_BELT_VEST = GreenCapsule(234, "Black Belt Vest")
SPARRING_OUTFIT = GreenCapsule(235, "Sparring Outfit")
GTS_WARDROBE = GreenCapsule(236, "Great Saiyaman's Wardrobe")
OLD_STYLE_ARMOR = GreenCapsule(237, "Old Style Armor")
RIT_ARMOR = GreenCapsule(238, "RIT Armor")
NEW_STYLE_ARMOR = GreenCapsule(239, "New Style Armor")
BULMAS_ARMOR = GreenCapsule(240, "Bulma's Armor")
SPECIAL_COATING = GreenCapsule(241, "Special Coating")
IMP_SPECIAL_COATING = GreenCapsule(242, "Improved Special Coating")
NANOMACHINE = GreenCapsule(243, "Nanomachine")
IMPROVE_NANO = GreenCapsule(244, "Improved Nanomachine")
LIFE_EXTRACT_10 = GreenCapsule(245, "Life Extract for 10")
LIFE_EXTRACT_100 = GreenCapsule(246, "Life Extract for 100")
LIFE_EXTRACT_1000 = GreenCapsule(247, "Life Extract for 1000")
LIFE_EXTRACT_10000 = GreenCapsule(248, "Life Extract for 10000")
DEMON_REALM_GUARD = GreenCapsule(249, "Demon Realm Guard")
MAGE_GUARD = GreenCapsule(250, "Mage Guard")
BABIDIS_GUARD = GreenCapsule(251, "Babidi's Guard")
BIBIDIS_GUARD = GreenCapsule(252, "Bibidi's Guard")
NORMAL_BELT = GreenCapsule(253, "Normal Belt")
TRAINING_BELT = GreenCapsule(254, "Training Belt")
WARRIOR_BELT = GreenCapsule(255, "Warrior Belt")
MAJIN_BELT = GreenCapsule(256, "Majin Belt")
LOW_CLASS_GUARD = GreenCapsule(257, "Lower-class Saiyan Guard")
KANASSAN_GUARD = GreenCapsule(258, "Kanassan-made Guard")
BATTLE_JACKET_PROTO = GreenCapsule(259, "Battle Jacket (Prototype)")
PATCHED_BATTLE_JACKET = GreenCapsule(260, "Patched-up Battle Jacket")
STRONG_BODY_WRAP = GreenCapsule(261, "Strongman's Body Wrap")
KING_BODY_WRAP = GreenCapsule(262, "King's Body Wrap")
GOD_BODY_WRAP = GreenCapsule(263, "God of Destruction Body Wrap")
LEGEND_BODY_WRAP = GreenCapsule(264, "Legendary Body Wrap")
SHENRONS_HIDE = GreenCapsule(265, "Shenron's Hide")
PORUNGAS_HIDE = GreenCapsule(266, "Porunga's Hide")
SHADOW_DRAGONS_HIDE = GreenCapsule(267, "Shadow Dragon's Hide")
# According to the guide I'm working from, there is no fourth Omega armor
SERUM_2X = GreenCapsule(268, "2X Enriched Serum")
SERUM_16X = GreenCapsule(269, "16X Enriched Serum")
SERUM_64X = GreenCapsule(270, "64X Enriched Serum")
SERUM_128X = GreenCapsule(271, "128X Enriched System")

## Time-based stat boosters
MIXED_BLOOD_POWER = GreenCapsule(272, "Mixed Blood Power")
MOON_LIGHT = GreenCapsule(273, "Moon Light")
FULL_MOON_GLOW = GreenCapsule(274, "Full Moon's Glow")
POTENTIAL_BOOST = GreenCapsule(275, "Potential")
UNIVERSAL_POWER = GreenCapsule(276, "Universal Power")
MIRACLE_POWER = GreenCapsule(277, "Miracle Power")
ULTIMATE_POWER = GreenCapsule(278, "Ultimate Power")
KINGS_CONFIDENCE = GreenCapsule(279, "King's Confidence")
MODE_SWITCH_SYS = GreenCapsule(280, "Mode-switching Systems")
SAIYANS_AWAKEN = GreenCapsule(281, "Saiyan's Awakening")
WAR_RACE_AWAKEN = GreenCapsule(282, "Warrior Race's Awakening")
NATURE_EVIL = GreenCapsule(283, "Nature of Evil")
HATRED_KAKAROT = GreenCapsule(284, "Hatred of Kakarot")
BLACK_DRAGONBALL = GreenCapsule(285, "Black Dragonball")
TOXIC_CHOCOLATE = GreenCapsule(286, "Toxic Chocolate")
RAGE_E = GreenCapsule(287, "Rage!")
RAGE_EE = GreenCapsule(288, "Rage!!")
RAGE_EEE = GreenCapsule(289, "Rage!!!")
SPIRIT_E = GreenCapsule(290, "Spirit!")
SPIRIT_EE = GreenCapsule(291, "Spirit!!")
SPIRIT_EEE = GreenCapsule(292, "Spirit!!!")
SERIOUS_E = GreenCapsule(293, "Serious!")
SERIOUS_EE = GreenCapsule(294, "Serious!!")
SERIOUS_EEE = GreenCapsule(295, "Serious!!!")
POWER_NEAR_LIMIT = GreenCapsule(296, "Power Near the Limit")
DESPERATE_RES = GreenCapsule(297, "Desperate Resolution")
DESPERATE_POWER = GreenCapsule(298, "Desperate Power")
PRIDE_STRONGEST = GreenCapsule(299, "Pride of the Strongest")
OUNCE_STRENGTH = GreenCapsule(300, "Last Ounce of Strength")
PRESSURE_CHAMP = GreenCapsule(301, "Pressure on the Champ")
DABURA_COOKIE = GreenCapsule(302, "Dabura Cookie")
PICCOLOS_REGEN = GreenCapsule(303, "Piccolo's Regeneration")
BUUS_REGEN = GreenCapsule(304, "Majin Buu's Regeneration")
DENDES_RECOVERY = GreenCapsule(305, "Dende's Recovery")
KIBITOS_REVIVAL = GreenCapsule(306, "Kibito's Revival")
MEDICAL_MACHINE = GreenCapsule(307, "Medical Machine")
AUTO_RESTORE = GreenCapsule(308, "Automatic Restoration")
SAIYAN_SPIRIT = GreenCapsule(309, "Saiyan Spirit")
GOING_ALL_OUT = GreenCapsule(310, "Going All-out!!")
GINYU_FORCE_BADGE = GreenCapsule(311, "Ginyu Force Badge")
HERC_FALSE_COURAGE = GreenCapsule(312, "Hercule's False Courage")
RUSH_EEE = GreenCapsule(313, "Rush!!!")
OVERTENSION = GreenCapsule(314, "Overtension")
GERO_DEFLECT = GreenCapsule(315, "Gero's Deflection R&D")
GERO_DEFLECT_BACK = GreenCapsule(316, "Gero's Deflect-Back R&D")
GERO_ENERGY = GreenCapsule(317, "Gero's Energy R&D")
VIRAL_HEART_DISEASE = GreenCapsule(318, "Viral Heart Disease")

## Transformations
FRIEZA_SPACESHIP = GreenCapsule(319, "Frieza's Spaceship")
COOLER_SPACESHIP = GreenCapsule(320, "Cooler's Spaceship")
BABIDI_MIND_CONTROL = GreenCapsule(321, "Babidi's Mind Control")

## Ki-reduction abilities
BABIDI_SCOPE = GreenCapsule(322, "Babidi's Scope")
KI_CONTROL = GreenCapsule(323, "Ki Control")
WARRIOR_CAREER = GreenCapsule(324, "Warrior's Career")
POWER_SAVE_SYS = GreenCapsule(325, "Power Save System")
BREATH_ROOM_STRONG = GreenCapsule(326, "Breathing Room of the Strongest")
PARAGUS_ADMON = GreenCapsule(327, "Paragas' Admonsihment") # this is misspelled in the game don't @ me
EVIL_GRIN = GreenCapsule(328, "Evil Grin")

## Ki suppression abilities
MEDITATION = GreenCapsule(329, "Meditation")
YAKON = GreenCapsule(330, "Yakon")
ANGEL_HALO = GreenCapsule(331, "Angel's Halo")
HUMAN_CANDY = GreenCapsule(332, "Human Candy")
MARRONS_WISH = GreenCapsule(333, "Marron's Wish")
CHIAOTZUS_WISH = GreenCapsule(334, "Chiaotzu's Wish")
PUARS_WISH = GreenCapsule(335, "Puar's Wish")
CHICHIS_WISH = GreenCapsule(336, "Chi-Chi's Wish")
DENDES_WISH = GreenCapsule(337, "Dende's Wish")
BULMAS_WISH = GreenCapsule(338, "Bulma's Wish")
WORLDS_EXPECT = GreenCapsule(339, "World's Expectations")
LOYAL_FRIEZA = GreenCapsule(340, "Loyalty to Frieza")
UNIVERSAL_AMB = GreenCapsule(341, "Universal Ambition")
PRIDE_CLAN = GreenCapsule(342, "Pride of the Clan")
ANDROID_GOALS = GreenCapsule(343, "Androids' Goals")
ESSENCE_MIGHTY = GreenCapsule(344, "Essence of the Mighty")
LOYAL_BABIDI = GreenCapsule(345, "Loyalty to Babidi")
KIBITOS_WISH = GreenCapsule(346, "Kibito's Wish")
KINGKAIS_WISH = GreenCapsule(347, "King-Kai's Wish")
THIRST_EARTH_DESTRUCT = GreenCapsule(348, "Thirst for Earth's Destruction")
THOUGHTS_FRIENDS = GreenCapsule(349, "Thoughts of Friends")
GOD_DEST_ARROGANCE =  GreenCapsule(350, "God of Destruction's Arrogance")
GPA_GOHANS_TEACHINGS = GreenCapsule(351, "Grandpa Gohan's Teachings")
GOKUS_TEACHINGS = GreenCapsule(352, "Goku's Teachings")

## Dodging and teleporting
TURTLE_SHELL = GreenCapsule(353, "Turtle Shell")
CONCENTRATION = GreenCapsule(354, "Concentration")

## Bonus money
SPARKING_E = GreenCapsule(355, "Sparking!")
SPARKING_EE = GreenCapsule(356, "Sparking!!")
SPARKING_EEE = GreenCapsule(357, "Sparking!!!")
SPARKING_EEEE = GreenCapsule(358, "Sparking!!!!")
SPARKING_EEEEE = GreenCapsule(359, "Sparking!!!!!")
SPARKING_EEEEEE = GreenCapsule(360, "Sparking!!!!!!")
SPARKING_EEEEEEE = GreenCapsule(361, "Sparking!!!!!!!")

## Bonus Exp
WE_GOTTA_POWER_E = GreenCapsule(362, "WE GOTTA POWER!")
WE_GOTTA_POWER_EE = GreenCapsule(363, "WE GOTTA POWER!!")
WE_GOTTA_POWER_EEE = GreenCapsule(364, "WE GOTTA POWER!!!")
WE_GOTTA_POWER_EEEE = GreenCapsule(365, "WE GOTTA POWER!!!!")

# Item Capsules (Yellow)
