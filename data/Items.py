from dataclasses import dataclass
from abc import ABC

from typing import Callable, TYPE_CHECKING, Sequence, Optional, Dict, List

if TYPE_CHECKING:
    from ..Budokai3Interface import Budokai3Interface


## vanilla starting items:
## Goku, Kid Gohan, Krillin, Piccolo, Tien, Yamcha, Raditz, Nappa, Training 1, Green Membership Card,
## World Tournament (Novice), World Tournament Stage, Hyperbolic Time Chamber, Archipelago, Mountains, Plains
## I'd like to find out what happens if those are removed
@dataclass
class ItemData(ABC):
    item_id: int
    name: str

    def __init__(self, id: int, name: str):
        self.item_id = id
        # if id is 999, it's not a capsule that should not be in the pool
        self.name = name

class Item(ItemData):
    pass


@dataclass
class Capsule(Item):
    offset: int
    capsule_color: int
    stacks: bool
    max_copies: int

    def __init__(self, id: int, name: str, offset=0x0, stacks = False, max_copies = 1):
        super().__init__(id, name)
        self.offset = offset
        self.stacks = stacks # if the item stacks, go up to that max and don't worry about the rest
        # this is logically relevant because there's no need for more than 3 of any item, and only Red Capsules at that
        if max_copies != 1: copies = max_copies
        elif stacks: copies = 3
        else: copies = 1
        self.max_copies =  copies

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
KAIOKEN = RedCapsule(1, "Kaioken", 0x4DFB1A)
SSJ_GOKU = RedCapsule(2, "Super Saiyan (Goku)", 0x4DFB1B)
SSJ2_GOKU = RedCapsule(3, "Super Saiyan 2 (Goku)", 0x4DFB1C)
SSJ3_GOKU = RedCapsule(4, "Super Saiyan 3 (Goku)", 0x4DFB1D)
SSJ4_GOKU = RedCapsule(5, "Super Saiyan 4 (Goku)", 0x4DFB1E)
SSJ4_GOKU_GOGETA = RedCapsule(999, "Super Saiyan 4 (SSJ4 Gogeta) (Goku)", 0x4DFBC9)
KAME_10X_GOKU = RedCapsule(999, "10X Kamehameha (Goku)", 0x4DFB21)
KAME_10X_GOGETA = RedCapsule(999, "10X Kamehameha (SSJ4 Gogeta) (Goku)", 0x4DFBCB)
BIG_KAME_100X_GOKU = RedCapsule(999, "100X Big Bang Kamehameha (SSJ4 Gogeta) (Goku)", 0x4DFBCE)
BIG_KAME_GOKU = RedCapsule(999, "Big Bang Kamehameha (Gogeta) (Goku)", 0x4DFBCC)
KAME_GOGETA_GOKU = RedCapsule(999, "Kamehameha (Gogeta) (Goku)", 0x4DFBC1)
KAME_GOGETA_SSJ4_GOKU = RedCapsule(999, "Kamehameha (SSJ4 Gogeta) (Goku)", 0x4DFBCB)
KAME_GOKU = RedCapsule(6, "Kamehameha (Goku)", 0x4DFB1F, stacks=True)
DRAG_FIST_GOKU = RedCapsule(7, "Dragon Fist", 0x4DFB21, stacks=True)
WARP_KAME_GOKU = RedCapsule(8, "Warp Kamehameha (Goku)", 0x4DFB22, stacks=True)
SPIRIT_BOMB_GOKU = RedCapsule(9, "Spirit Bomb (Goku)", 0x4DFB24, stacks=True)
SUPER_SPIRIT_BOMB = RedCapsule(999, "Super Spirit Bomb", 0x4DFB24)
SUPER_DRAG_FIST = RedCapsule(999, "Super Dragon Fist")
GOGETA_GOKU = RedCapsule(10, "Fusion - Gogeta (Goku)", 0x4DFBC1) # both are listed as "Fusion" so this
# and SSJ4 are a guess as to which address belongs to which
SOUL_PUNISHER_GOKU = RedCapsule(999, "Soul Punisher (Goku)", 0x4DFBC3)
SOUL_STRIKE_GOKU = RedCapsule(999, "Soul Strike (Goku)", 0x4DFBC2)
SSJ4_GOGETA_GOKU = RedCapsule(11, "Fusion - Super Saiyan 4 Gogeta (Goku)", 0x4DFBC8)
VEGITO_GOKU = RedCapsule(12, "Potara - Vegito (Goku)", 0x4DFBD4)
BREAK_GOKU = RedCapsule(13, "Breakthrough (Goku)", 0x4DFBE8)

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
SSJ_GOHAN = RedCapsule(27, "Super Saiyan (Gohan)", 0x4DFB30)
SSJ2_GOHAN = RedCapsule(28, "Super Saiyan 2 (Gohan)", 0x4DFB31)
ELDER_UNLOCK = RedCapsule(29, "Elder Kai Unlock Ability", 0x4DFB32)
KAME_GOHAN = RedCapsule(30, "Kamehameha (Gohan)", 0x4DFB33, stacks=True)
SOAR_GOHAN = RedCapsule(31, "Soaring Dragon Strike (Gohan)", 0x4DFB34, stacks=True)
SUPER_KAME_GOHAN = RedCapsule(32, "Super Kamehameha", 0x4DFB35, stacks=True)
BREAK_GOHAN = RedCapsule(33, "Breakthrough (Gohan)", 0x4DFBEC)

## Gt. Saiyaman
JPUNCH = RedCapsule(34, "Justice Punch", 0x4DFB37, stacks=True)
JKICK = RedCapsule(35, "Justice Kick", stacks=True) # no address given
JPOSE = RedCapsule(36, "Justice Pose", 0x4DFB38)
BREAK_GTS = RedCapsule(37, "Breakthrough (Gt Saiyaman)", 0x4DFBEE)

## Goten
SSJ_GOTEN = RedCapsule(38, "Super Saiyan (Goten)", 0x4DFB39)
KAME_GOTEN = RedCapsule(39, "Kamehameha (Goten)", 0x4DFB3A, stacks=True)
CHARGE = RedCapsule(40, "Charge", 0x4DFB3B, stacks=True)
CHARGE_GOTENKS = RedCapsule(999, "Charge (Gotenks)", 0x4DFBB3)
GOTENKS_GOTEN = RedCapsule(41, "Fusion - Gotenks (Goten)", 0x4DFBAF)
SSJ_GOTENKS_GOTEN = RedCapsule(999, "Super Saiyan Gotenks (Goten)", 0x4DFBB1)
SSJ3_GOTENKS_GOTEN = RedCapsule(999, "Super Saiyan 3 Gotenks (Goten)", 0x4DFBB1)
KAME_GOTENKS_GOTEN = RedCapsule(999, "Kamehameha (Gotenks) (Goten)", 0x4DFBB2)
KAME_SSJ3_GOTENKS = RedCapsule (999, "Kamehameha (SSJ3 Gotenks) (Goten)", 0x4DFBBB)
DONUTS_GOTEN = RedCapsule(999, "Galactica Donuts (Goten)", 0x4DFBB5)
GHOST_GOTEN = RedCapsule(999, "Super Ghost Kamikaze Attk (Goten)", 0x4DFBB6)
VICTORY_GOTEN = RedCapsule(999, "Victory Cannon (Gotenks) (Goten)", 0x4DFBB4)
BREAK_GOTEN = RedCapsule(42, "Breakthrough (Goten)", 0x4DFBEE)

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
DEST_WAVE = RedCapsule(72, "Destructive Wave", stacks=True)
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
SFP1 = RedCapsule(109, "Super Fighting Pose 1", 0x4DFB6F)
SFP2 = RedCapsule(110, "Super Fighting Pose 2", 0x4DFB71)
MILKY_CANNON = RedCapsule(111, "Milky Cannon", 0x4DFB71, stacks=True)
STRONG_JERSEY = RedCapsule(112, "Strong Jersey", 0x4DFB72, stacks=True)
BODY_CHANGE = RedCapsule(113, "Body Change", 0x4DFB74, stacks=True)
BREAK_GINYU = RedCapsule(114, "Breakthrough (Capt Ginyu)", 0x4DFBFC)

## Recoome
SFP3 = RedCapsule(115, "Super Fighting Pose 3")
SFP4 = RedCapsule(116, "Super Fighting Pose 4")
ERASER_GUN = RedCapsule(117, "Recoome Eraser Gun", stacks=True)
REC_KICK = RedCapsule(118, "Recoome Kick", stacks=True)
REC_BOMBER = RedCapsule(119, "Recoome Bomber", stacks=True)
BREAK_REC = RedCapsule(120, "Breakthrough (Recoome)")

## Frieza
SECOND_FORM = RedCapsule(121, "Second Form", 0x4DFB79)
THIRD_FORM = RedCapsule(122, "Third Form", 0x4DFB7A)
FINAL_FORM_FRIEZA = RedCapsule(123, "Final Form (Frieza)", 0x4DFB7B)
HUNDRED_PERCENT = RedCapsule(124, "100% Final Form", 0x4DFB7C)
DEATH_BEAM = RedCapsule(125, "Death Beam", 0x462DF0, stacks=True)
DEATH_WAVE = RedCapsule(126, "Death Wave", 0x4DFB7E, stacks=True)
DEATH_BALL = RedCapsule(127, "Death Ball", 0x4DFB7F, stacks=True)
BREAK_FRIEZA = RedCapsule(128, "Breakthrough (Frieza)", 0x4DFBFE)

## Android 16
ROCKET_PUNCH = RedCapsule(129, "Rocket Punch", 0x4DFB81, stacks=True)
HELL_FLASH = RedCapsule(130, "Hell Flash", 0x4DFB82, stacks=True)
BREAK_16 = RedCapsule(131, "Breakthrough (16)", 0x4DFBFF)

## Android 17
POWER_BLITZ_17 = RedCapsule(132, "Power Blitz (17)", 0x4DFB82, stacks=True)
ENERGY_FIELD_17 = RedCapsule(133, "Energy Field (17)", 0x4DFB83, stacks=True)
ACCEL_DANCE_17 = RedCapsule(134, "Accel Dance (17)", 0x4DFB84, stacks=True)
BREAK_17 = RedCapsule(135, "Breakthrough (17)", 0x4DFC00)

## Android 18
POWER_BLITZ_18 = RedCapsule(136, "Power Blitz (18)", 0x4DFB85, stacks=True)
DD_18 = RedCapsule(137, "Destructo Disc (18)", 0x4DFB86, stacks=True)
ACCEL_DANCE_18 = RedCapsule(138, "Accel Dance (18)", 0x4DFB87, stacks=True)
BREAK_18 = RedCapsule(139, "Breakthrough (18)", 0x4DFC01)

## Dr. Gero (Android 20)
PHOTON_WAVE = RedCapsule(140, "Photon Wave", 0x4DFB88, stacks=True)
KI_ABSORB = RedCapsule(141, "Ki Blast Absorption", 0x4DFB89, stacks=True)
LIFE_DRAIN = RedCapsule(142, "Life Drain", 0x4DFB8A, stacks=True)
BREAK_GERO = RedCapsule(143, "Breakthrough (Dr Gero)", 0x4DFC02)

## Cell
ABSORB_17 = RedCapsule(144, "17 Absorption", 0x4DFB8B)
PERFECT_FORM = RedCapsule(145, "Perfect Form", 0x4DFB8C)
SUPER_PERFECT = RedCapsule(146, "Super Perfect Form", 0x4DFB8E)
KAME_CELL = RedCapsule(147, "Kamehameha (Cell)", 0x4DFB8E, stacks=True)
ENERGY_FIELD_CELL = RedCapsule(148, "Energy Field (Cell)", 0x4DFB8F, stacks=True)
SPIRIT_BOMB_CELL = RedCapsule(149, "Spirit Bomb (Cell)", 0x4DFB91, stacks=True)
BREAK_CELL = RedCapsule(150, "Breakthrough (Cell)", 0x4DFC03)

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
DEMON_WILL = RedCapsule(163, "Demonic Will", 0x4DFB9A)
HELL_BLITZ = RedCapsule(164, "Hell Blitz", 0x4DFB9B, stacks=True)
EVIL_BLAST = RedCapsule(165, "Evil Blast", 0x4DFB9C, stacks=True)
HELL_RUSH = RedCapsule(166, "Hell Blade Rush", 0x4DFB9E, stacks=True)
BREAK_DABURA = RedCapsule(167, "Breakthrough (Dabura)", 0x4DFC07)

## Cooler
FINAL_FORM_COOLER = RedCapsule(168, "Final Form (Cooler)", 0x4DFB9E)
DESTRUCT_RAY = RedCapsule(169, "Destructive Ray", 0x4DFB9F, stacks=True)
SAUZER_BLADE = RedCapsule(170, "Sauzer Blade", 0x4DFBA1, stacks=True)
SUPERNOVA = RedCapsule(171, "Supernova", 0x4DFBA1, stacks=True)
BREAK_COOLER = RedCapsule(172, "Breakthrough (Cooler)", 0x4DFC08)

## Bardock
RIOT_JAVELIN = RedCapsule(173, "Riot Javelin", 0x4DFBA2, stacks=True)
HEAT_PHALANX = RedCapsule(174, "Heat Phalanx", 0x4DFBA3, stacks=True)
SPIRIT_SAIYANS = RedCapsule(175, "Spirit of Saiyans", 0x4DFBA4, stacks=True)
BREAK_BARDOCK = RedCapsule(176, "Breakthrough (Bardock)", 0x4DFC09)

## Broly
LSSJ_BROLY = RedCapsule(177, "Legendary Super Saiyan", 0x4DFBA5)
BLASTER_SHELL = RedCapsule(178, "Blaster Shell", 0x4DFBA6, stacks=True)
GIGANT_PRESS = RedCapsule(179, "Gigantic Press", 0x4DFBA7, stacks=True)
GIGANT_METEOR = RedCapsule(180, "Gigantic Meteor", 0x4DFBA8, stacks=True)
BREAK_BROLY = RedCapsule(181, "Breakthrough (Broly)", 0x4DFC0B)

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
KAME_CELLJR = RedCapsule(189, "Kamehameha (Cell Jr)", 0x4DFBAE, stacks=True)
BREAK_CELLJR = RedCapsule(190, "Breakthrough (Cell Jr)")

RED_CAPSULES = [
    # Goku
    KAIOKEN, SSJ_GOKU, SSJ2_GOKU, SSJ3_GOKU, SSJ4_GOKU, KAME_GOKU, DRAG_FIST_GOKU, WARP_KAME_GOKU, SPIRIT_BOMB_GOKU,
    GOGETA_GOKU, SSJ4_GOGETA_GOKU, VEGITO_GOKU, BREAK_GOKU,
    # Kid Gohan
    POTENTIAL_KGOHAN, MASENKO, BREAK_KGOHAN,
    # Teen Gohan
    SSJ_TGOHAN, SSJ2_TGOHAN, KAME_TGOHAN, SOAR_TGOHAN, FS_KAME, BREAK_TGOHAN,
    # Gohan
    SSJ_GOHAN, SSJ2_GOHAN, ELDER_UNLOCK, KAME_GOHAN, SOAR_GOHAN, SUPER_KAME_GOHAN, BREAK_GOHAN,
    # Gt Saiyaman
    JPUNCH, JKICK, JPOSE, BREAK_GTS,
    # Goten
    SSJ_GOTEN, KAME_GOTEN, CHARGE, GOTENKS_GOTEN, BREAK_GOTEN,
    # Vegeta
    SSJ_VEGETA, SSJ2_VEGETA, SSJ4_VEGETA, GALICK, FINAL_IMPACT, FINAL_FLASH, BIG_BANG, GOGETA_VEGETA,
    SSJ4_GOGETA_VEGETA, VEGITO_VEGETA, BREAK_VEGETA,
    # Trunks
    SSJ_TRUNKS, SSJ2_TRUNKS, FINISH_BUSTER, BUSTER_CANNON, BURNING_SLASH, BREAK_TRUNKS,
    # Kid Trunks
    SSJ_KTRUNKS, DOUBLE_BUSTER, FINAL_CANNON, GOTENKS_KTRUNKS, BREAK_KTRUNKS,
    # Krillin
    POTENTIAL_KRILLIN, KAME_KRILLIN, DD_KRILLIN, FIERCE_DD, BREAK_KRILLIN,
    # Piccolo
    SYNC_NAIL, FUSE_KAMI, DEST_WAVE, LGRENADE, SBEAM_CANNON, HZGRENADE, BREAK_PICCOLO,
    # Tien
    DODON, BLAST_CANNON, NEO_BLAST_CANNON, BREAK_TIEN,
    # Yamcha
    KAME_YAMCHA, WOLF_FANG, SPIRIT_BALL, BREAK_YAMCHA,
    # Hercule
    TENSION, DYNAMITE_KICK, ROLLING_PUNCH, HERC_SPECIAL, PRESENT, BREAK_HERCULE,
    # Videl
    EAGLE_KICK, HAWK_ARROW, CLOSE_CALL, BREAK_VIDEL,
    # Supreme Kai
    SHOCKWAVE, ABILITIES, KIBITOKAI, BREAK_SK,
    # Uub
    KI_CANNON, FIERCE_FLURRY, BREAK_UUB,
    # Raditz
    SUNDAY, SATURDAY, BREAK_RADITZ,
    # Nappa
    BOMBER_DX, BREAK_CANNON, GIANT_STORM, BREAK_NAPPA,
    # Ginyu
    MILKY_CANNON, STRONG_JERSEY, SFP1, SFP2, BODY_CHANGE, BREAK_GINYU,
    # Recoome
    ERASER_GUN, REC_KICK, SFP3, SFP4, REC_BOMBER, BREAK_REC,
    # Frieza
    SECOND_FORM, THIRD_FORM, FINAL_FORM_FRIEZA, HUNDRED_PERCENT, DEATH_BEAM, DEATH_WAVE, DEATH_BALL, BREAK_FRIEZA,
    # 16
    ROCKET_PUNCH, HELL_FLASH, BREAK_16,
    # 17
    POWER_BLITZ_17, ENERGY_FIELD_17, ACCEL_DANCE_17, BREAK_17,
    # 18
    POWER_BLITZ_18, DD_18, ACCEL_DANCE_18, BREAK_18,
    # Dr Gero
    PHOTON_WAVE, KI_ABSORB, LIFE_DRAIN, BREAK_GERO,
    # Cell
    ABSORB_17, PERFECT_FORM, SUPER_PERFECT, KAME_CELL, ENERGY_FIELD_CELL, SPIRIT_BOMB_CELL, BREAK_CELL,
    # Majin Buu
    INN_CANNON, INN_EXPRESS, ANGRY_EXPLODE, BREAK_MBUU,
    # Super Buu
    ABSORB, ILL_FLASH, ILL_BALL, BREAK_SBUU,
    # Kid Buu
    KAME_KBUU, VANISH_BALL, WARP_KAME_KBUU, BREAK_KBUU,
    # Dabura
    DEMON_WILL, HELL_BLITZ, EVIL_BLAST, HELL_RUSH, BREAK_DABURA,
    # Cooler
    FINAL_FORM_COOLER, DESTRUCT_RAY, SAUZER_BLADE, SUPERNOVA, BREAK_COOLER,
    # Bardock
    RIOT_JAVELIN, HEAT_PHALANX, SPIRIT_SAIYANS, BREAK_BARDOCK,
    # Broly
    LSSJ_BROLY, BLASTER_SHELL, GIGANT_PRESS, GIGANT_METEOR, BREAK_BROLY,
    # Omega
    DTHUNDER, WHIRLWIND, MINUS_BALL, BREAK_OMEGA,
    # Saiba
    ACID, SELFDESTRUCT, BREAK_SAIBA,
    # Cell Jr
    KAME_CELLJR, BREAK_CELLJR
]

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

GREEN_CAPSULES = [
    Z_SWORD, JUICE, DAIMAOS_POWER, FRUITS_TRAINING, VIDELS_KISS, KIBITOS_BACKING, BATTLE_TESTAMENT, POWER_AMP,
    WARRIOR_GENETICS, DEMON_REALM_FLAMES, KAKAROTS_CRYING, GINYU_SPECIAL_FORCES, COOLER_ARMORED_SQUAD, POWER_FRIENDS,
    APPETITES_MEN, STRENGTH_SERUM, KINGS_LINEAGE, CHEERING,
    GENERAL_VEST, TRAINING_VEST, STURDY_VEST, MYSTERIOUS_VEST, VEST_GPA_GOHAN, VEST_HOLE_TAIL, TURTLE_VEST, KAMI_VEST,
    TRIBE_UNIFORM, E_TRAINING_UNIFORM, E_STURDY_UNIFORM, E_MYSTERY_UNIFORM, NORMAL_JACKET, QUALITY_JACKET,
    STURDY_JACKET, MYSTERY_JACKET, KAMI_OUTFIT, KINGKAI_OUTFIT, GRANDKAI_OUTFIT, SUPREMEKAI_OUTFIT, OLD_TRAINING_VEST,
    WEDDING_VEST, CHAMP_VEST, HIGHTECH_VEST, CHAMPION_BELT, TSHIRT, BLACK_BELT_VEST, SPARRING_OUTFIT, GTS_WARDROBE,
    OLD_STYLE_ARMOR, RIT_ARMOR, NEW_STYLE_ARMOR, BULMAS_ARMOR, SPECIAL_COATING, IMP_SPECIAL_COATING, NANOMACHINE,
    IMPROVE_NANO, LIFE_EXTRACT_10, LIFE_EXTRACT_100, LIFE_EXTRACT_1000, LIFE_EXTRACT_10000, DEMON_REALM_GUARD,
    MAGE_GUARD, BABIDIS_GUARD, BIBIDIS_GUARD, NORMAL_BELT, TRAINING_BELT, WARRIOR_BELT, MAJIN_BELT, LOW_CLASS_GUARD,
    KANASSAN_GUARD, BATTLE_JACKET_PROTO, PATCHED_BATTLE_JACKET, STRONG_BODY_WRAP, KING_BODY_WRAP, GOD_BODY_WRAP,
    LEGEND_BODY_WRAP, SHENRONS_HIDE, PORUNGAS_HIDE, SHADOW_DRAGONS_HIDE, SERUM_2X, SERUM_16X, SERUM_64X, SERUM_128X,
    MIXED_BLOOD_POWER, MOON_LIGHT, FULL_MOON_GLOW, POTENTIAL_BOOST, UNIVERSAL_POWER, MIRACLE_POWER, ULTIMATE_POWER,
    KINGS_CONFIDENCE, MODE_SWITCH_SYS, SAIYANS_AWAKEN, WAR_RACE_AWAKEN, NATURE_EVIL, HATRED_KAKAROT, BLACK_DRAGONBALL,
    TOXIC_CHOCOLATE, RAGE_E, RAGE_EE, RAGE_EEE, SPIRIT_E, SPIRIT_EE, SPIRIT_EEE, SERIOUS_E, SERIOUS_EE, SERIOUS_EEE,
    POWER_NEAR_LIMIT, DESPERATE_RES, DESPERATE_POWER, PRIDE_STRONGEST, OUNCE_STRENGTH, PRESSURE_CHAMP, DABURA_COOKIE,
    PICCOLOS_REGEN, BUUS_REGEN, DENDES_RECOVERY, KIBITOS_REVIVAL, MEDICAL_MACHINE, AUTO_RESTORE, SAIYAN_SPIRIT,
    GOING_ALL_OUT, GINYU_FORCE_BADGE, HERC_FALSE_COURAGE, RUSH_EEE, OVERTENSION, GERO_DEFLECT, GERO_DEFLECT_BACK,
    GERO_ENERGY, VIRAL_HEART_DISEASE, FRIEZA_SPACESHIP, COOLER_SPACESHIP, BABIDI_MIND_CONTROL, BABIDI_SCOPE,
    WARRIOR_CAREER, POWER_SAVE_SYS, BREATH_ROOM_STRONG, PARAGUS_ADMON, EVIL_GRIN, MEDITATION, YAKON, ANGEL_HALO,
    HUMAN_CANDY, MARRONS_WISH, CHIAOTZUS_WISH, PUARS_WISH, CHICHIS_WISH, DENDES_WISH, BULMAS_WISH, WORLDS_EXPECT,
    LOYAL_FRIEZA, UNIVERSAL_AMB, PRIDE_CLAN, ANDROID_GOALS, ESSENCE_MIGHTY, LOYAL_BABIDI, KIBITOS_WISH, KINGKAIS_WISH,
    THIRST_EARTH_DESTRUCT, THOUGHTS_FRIENDS, GOD_DEST_ARROGANCE, GPA_GOHANS_TEACHINGS, GOKUS_TEACHINGS, TURTLE_SHELL,
    CONCENTRATION, SPARKING_E, SPARKING_EE, SPARKING_EEE, SPARKING_EEEE, SPARKING_EEEEE, SPARKING_EEEEEE,
    SPARKING_EEEEEEE, WE_GOTTA_POWER_E, WE_GOTTA_POWER_EE, WE_GOTTA_POWER_EEE, WE_GOTTA_POWER_EEEE
]

# Item Capsules (Yellow)
TEMPURA = YellowCapsule(366, "Tempura Bowl", 0x4DFC0F)
TONKATSU = YellowCapsule(367, "Tonkatsu (Fried Pork) Bowl", 0x4DFC11)
CHICKEN_EGG = YellowCapsule(368, "Chicken & Egg Bowl", offset=0x4DFC11)
CHILLED = YellowCapsule(369, "Chilled Juice", offset=0x4DFC12)
WELL_CHILLED = YellowCapsule(370, "Well Chilled Juice", 0x4DFC13)
EXTREME_CHILLED = YellowCapsule(371, "Extremely Chilled Juice", offset=0x4DFC14)
THIRD_SENZU = YellowCapsule(372, "1/3 Senzu Bean", offset=0x4DFC15)
HALF_SENZU = YellowCapsule(373, "1/2 Senzu Bean", offset=0x4DFC16)
SENZU_BEAN = YellowCapsule(374, "Senzu Bean", offset=0x4DFC17)
KINGKAIS_WATER = YellowCapsule(375, "King Kai's Water", offset=0x4DFC18)
SUPREMEKAIS_WATER = YellowCapsule(376, "Supreme Kai's Water", 0x4DFC19)
GRANDKAIS_WATER = YellowCapsule(377, "Grand Supreme Kai's Water", offset=0x4DFC1B)
HOLY_WATER_DROP = YellowCapsule(378, "Super Holy Water Drop", 0x4DFC1B)
HOLY_WATER_BOTTLE = YellowCapsule(379, "Super Holy Water Bottle", offset=0x4DFC1C)
HOLY_WATER = YellowCapsule(380, "Super Holy Water", offset=0x4DFC1E)
HERC_DRINK = YellowCapsule(381, "Hercule Drink", offset=0x4DFC1E)
HERC_DRINK_DX = YellowCapsule(382, "Hercule Drink DX", offset=0x4DFC1F)
HERC_DRINK_SP = YellowCapsule(383, "Hercule Drink SP", offset=0x4DFC20)
KAMI_WATER_DROP = YellowCapsule(384, "Super Kami Water Drop", 0x4DFC21)
KAMI_WATER_BOTTLE = YellowCapsule(385, "Super Kami Water Bottle", 0x4DFC22)
KAMI_WATER = YellowCapsule(386, "Super Kami Water", offset=0x4DFC23)
PSHIELD_PROTO = YellowCapsule(387, "Portable Shield (Prototype)", offset=0x4DFC24)
PSHIELD_IMPROVED = YellowCapsule(388, "Portable Shield (Improved)", offset=0x4DFC25)
PSHIELD_PROD = YellowCapsule(389, "Portable Shield (Production)", offset=0x4DFC26)
PORT_BARRIER = YellowCapsule(390, "Portable Barrier System", offset=0x4DFC27)
GERO_DEF_SYS = YellowCapsule(391, "Gero Style Defense System", offset=0x4DFC28)
GERO_BARRIER_SYS = YellowCapsule(392, "Gero Style Barrier System", offset=0x4DFC29)
BIBIDIS_POT = YellowCapsule(393, "Bibidi's Pot", offset=0x4DFC2A)
VACCINE = YellowCapsule(394, "Vaccine", 0x4DFC2B)
SENZU_ROOT = YellowCapsule(395, "Senzu Root", offset=0x4DFC2C)
SENZU_LEAF = YellowCapsule(396, "Senzu Leaf", offset=0x4DFC2E)
SENZU_SEEDLING = YellowCapsule(397, "Senzu Seedling", offset=0x4DFC2E)
EEL_SOUP = YellowCapsule(398, "Centipede Eel Soup", offset=0x4DFC2F)
CF_TOAD = YellowCapsule(399, "Chicken-fried 7-Seasoned Toad", offset=0x4DFC30)
PAOZU_TAIL = YellowCapsule(400, "Paozusaurus Tail", offset=0x4DFC31)
GAMBLE = YellowCapsule(401, "Gamble", offset=0x4DFD5B)

YELLOW_CAPSULES = [
    TEMPURA, TONKATSU, CHICKEN_EGG, CHILLED, WELL_CHILLED, EXTREME_CHILLED, THIRD_SENZU, HALF_SENZU, SENZU_BEAN,
    KINGKAIS_WATER, SUPREMEKAIS_WATER, GRANDKAIS_WATER, HOLY_WATER_DROP, HOLY_WATER_DROP, HOLY_WATER_BOTTLE, HOLY_WATER,
    HERC_DRINK, HERC_DRINK_DX, HERC_DRINK_SP, KAMI_WATER_DROP, KAMI_WATER_BOTTLE, KAMI_WATER, PSHIELD_PROTO,
    PSHIELD_IMPROVED, PSHIELD_PROD, PORT_BARRIER, GERO_DEF_SYS, GERO_BARRIER_SYS, BIBIDIS_POT, VACCINE, SENZU_ROOT,
    SENZU_LEAF, SENZU_SEEDLING, EEL_SOUP, CF_TOAD, PAOZU_TAIL, GAMBLE
]

# System Capsules (Gray)
GOKU = GrayCapsule(401, "Goku", offset=0x4DFCE2)
KID_GOKU = GrayCapsule(402, "Kid Goku", offset=0x4DFCE3)
KID_GOHAN = GrayCapsule(403, "Kid Gohan", offset=0x4DFCE5)
TEEN_GOHAN = GrayCapsule(404, "Teen Gohan", offset=0x4DFCE5)
GOHAN = GrayCapsule(405, "Gohan", offset=0x4DFCE6)
GT_SAIYAMAN = GrayCapsule(406, "Great Saiyaman") # my guess is 0x4DFCE7
GOTEN = GrayCapsule(407, "Goten", offset=0x4DFCE8)
VEGETA = GrayCapsule(408, "Vegeta", offset=0x4DFCE9)
TRUNKS = GrayCapsule(409, "Trunks", offset=0x4DFCEA)
KID_TRUNKS = GrayCapsule(410, "Kid Trunks", offset=0x4DFCEB)
KRILLIN = GrayCapsule(411, "Krillin", offset=0x4DFCEC)
PICCOLO = GrayCapsule(412, "Piccolo", offset=0x4DFCED)
TIEN = GrayCapsule(413,"Tien", offset=0x4DFCEE)
YAMCHA = GrayCapsule(414, "Yamcha", offset=0x4DFCEF)
HERCULE = GrayCapsule(415, "Hercule", offset=0x4DFCF0)
VIDEL = GrayCapsule(416, "Videl", offset=0x4DFCF1)
SUPREME_KAI = GrayCapsule(417, "Supreme Kai", offset=0x4DFCF2)
UUB = GrayCapsule(418, "Uub", offset=0x4DFCF3)
RADITZ = GrayCapsule(419, "Raditz", offset=0x4DFCF5)
NAPPA = GrayCapsule(420, "Nappa", offset=0x4DFCF5)
GINYU = GrayCapsule(421, "Captain Ginyu", offset=0x4DFCF6)
RECOOME = GrayCapsule(422, "Recoome", offset=0x4DFCF8)
FRIEZA = GrayCapsule(423, "Frieza") # you'll have to find the location yourself, Hope
ANDROID_16 = GrayCapsule(424, "Android 16", offset=0x4DFCF9)
ANDROID_17 = GrayCapsule(425, "Android 17", offset=0x4DFCFA)
ANDROID_18 = GrayCapsule(426, "Android 18", offset=0x4DFCFB)
DR_GERO = GrayCapsule(427, "Dr Gero", offset=0x4DFCFC)
CELL = GrayCapsule(428, "Cell", offset=0x4DFCFD)
MAJIN_BUU = GrayCapsule(429, "Majin Buu", offset=0x4DFCFE)
SUPER_BUU = GrayCapsule(430, "Super Buu", offset=0x4DFCFF)
KID_BUU = GrayCapsule(431, "Kid Buu", offset=0x4DFD00)
DABURA = GrayCapsule(432, "Dabura", offset=0x4DFD01)
COOLER = GrayCapsule(433, "Cooler", offset=0x4DFD02)
BARDOCK = GrayCapsule(434, "Bardock", offset=0x4DFD03)
BROLY = GrayCapsule(435, "Broly", offset=0x4DFD04)
OMEGA_SHENRON = GrayCapsule(436, "Omega Shenron", offset=0x4DFD05)
SAIBAMAN = GrayCapsule(437, "Saibaman", offset=0x4DFD06) # value not provided
CELL_JR = GrayCapsule(438, "Cell Jr", offset=0x4DFD07)
# Bulma is also listed as a character that can be enabled by writing 1 to 0x4DFD08. Since this is the character used in
# the last training, I doubt she works at all. Still, enabling her is an interesting prospect...
# Further note: she is not selectable normally, even when enabled. Must be hacked...
TRAINING_1 = GrayCapsule(439, "Training 1 Scouter", offset=0x4DFD09)
TRAINING_2 = GrayCapsule(440, "Training 2 Fighting Basics", offset=0x4DFD0A)
TRAINING_3 = GrayCapsule(441, "Training 3 Ki Control", offset=0x4DFD0B)
TRAINING_4 = GrayCapsule(442, "Training 4 Death-moves", offset=0x4DFD0C)
TRAINING_5 = GrayCapsule(443, "Training 5 Ki Control 2", offset=0x4DFD0D)
TRAINING_6 = GrayCapsule(444, "Training 6 Dodging", offset=0x4DFD0E)
TRAINING_7 = GrayCapsule(445, "Training 7 Teleporting", offset=0x4DFD0F)
TRAINING_8 = GrayCapsule(446, "Training 8 Hi-level Fighting", offset=0x4DFD10)
TRAINING_9 = GrayCapsule(447, "Training 9 Ultimate Moves", offset=0x4DFD11)
TRAINING_10 = GrayCapsule(448, "Training 10 Dragon Rush", offset=0x4DFD12)
TRAINING_11 = GrayCapsule(449, "Training 11 Item Skills", offset=0x4DFD13)
TRAINING_12 = GrayCapsule(450, "Training 12 Final Secrets", offset=0x4DFD14)
GREEN_CARD = GrayCapsule(451, "Green Membership Card", offset=0x4DFD15)
SILVER_CARD = GrayCapsule(452, "Silver Membership Card", offset=0x4DFD16)
GOLD_CARD = GrayCapsule(453, "Gold Membership Card", offset=0x4DFD17)
BLACK_CARD = GrayCapsule(454, "Black Membership Card", offset=0x4DFD18)
TOURNEY_NOVICE = GrayCapsule(455, "World Tournament - Novice", offset=0x4DFD19)
TOURNEY_ADEPT = GrayCapsule(456, "World Tournament - Adept", offset=0x4DFD1A)
TOURNEY_ADV = GrayCapsule(457, "World Tournament - Advanced", offset=0x4DFD1B)
TOURNEY_CELL = GrayCapsule(458, "World Tournament - Cell Games", offset=0x4DFD1C)
DRAGON_ARENA = GrayCapsule(459, "Dragon Arena Ticket", offset=0x4DFD1D)
TOURNEY_STAGE = GrayCapsule(460, "World Tournament Stage") # no location listed
TIME_CHAMBER = GrayCapsule(461, "Hyperbolic Time Chamber", offset=0x4DFD1F)
ARCHIPELAGO = GrayCapsule(462, "Archipelago", offset=0x4DFD20)
MOUNTAINS = GrayCapsule(463, "Mountains", offset=0x4DFD22)
URBAN_AREA = GrayCapsule(464, "Urban Area", offset=0x4DFD22)
# todo: renumber after this
PLAINS = GrayCapsule(464, "Plains", offset=0x4DFD23)
GPA_GOHANS_HOUSE = GrayCapsule(465, "Grandpa Gohan's House", offset=0x4DFD25)
NAMEK = GrayCapsule(466, "Planet Namek", offset=0x4DFD25)
CELL_RING = GrayCapsule(467, "Cell Ring", offset=0x4DFD26)
SUPREME_KAIS_WORLD = GrayCapsule(468, "Supreme Kai's World", offset=0x4DFD28)
INSIDE_BUU = GrayCapsule(469, "Inside Buu", offset=0x4DFD28)
RED_RIBBON_BASE = GrayCapsule(470, "Red Ribbon Base", offset=0x4DFD29)
GOKUS_WISH = GrayCapsule(471, "Goku's Wish", offset=0x4DFD2A)
PATH_POWER = GrayCapsule(472, "The Path to Power", offset=0x4DFD2B)
ENDLESS_PATH = GrayCapsule(473, "The Endless Path to Power", offset=0x4DFD2C)
STRONGEST_TROPHY = GrayCapsule(474, "Strongest of Universe Trophy", offset=0x4DFD2D)
MEMORIES_GOKU = GrayCapsule(475, "Memories of Goku", offset=0x4DFD2E)
MEMORIES_PICCOLO = GrayCapsule(476, "Memories of Piccolo", offset=0x4DFD2F)
MEMORIES_KID_GOHAN = GrayCapsule(477, "Memories of Kid Gohan", offset=0x4DFD30)
MEMORIES_TEEN_GOHAN = GrayCapsule(478, "Memories of Teen Gohan", offset=0x4DFD32)
MEMORIES_GOHAN = GrayCapsule(479, "Memories of Gohan", offset=0x4DFD32)
MEMORIES_VEGETA = GrayCapsule(480, "Memories of Vegeta", offset=0x4DFD33)
MEMORIES_GOTEN = GrayCapsule(481, "Memories of Goten", offset=0x4DFD35)
MEMORIES_TRUNKS = GrayCapsule(482, "Memories of Trunks", offset=0x4DFD35)
MEMORIES_KID_TRUNKS = GrayCapsule(483, "Memories of Kid Trunks", offset=0x4DFD36)
MEMORIES_KRILLIN = GrayCapsule(484, "Memories of Krillin", offset=0x4DFD38)
MEMORIES_TIEN = GrayCapsule(485, "Memories of Tien", offset=0x4DFD38)
MEMORIES_YAMCHA = GrayCapsule(486, "Memories of Yamcha", offset=0x4DFD39)
MEMORIES_HERCULE = GrayCapsule(487, "Memories of Hercule", offset=0x4DFD3A)
MEMORIES_VIDEL = GrayCapsule(488, "Memories of Videl", offset=0x4DFD3B)
MEMORIES_GT_SAIYAMAN = GrayCapsule(489, "Memories of Gt Saiyaman", offset=0x4DFD3C)
MEMORIES_ANDROID_16 = GrayCapsule(490, "Memories of Android 16", offset=0x4DFD3D)
MEMORIES_ANDROID_17 = GrayCapsule(491, "Memories of Android 17", offset=0x4DFD3E)
MEMORIES_ANDROID_18 = GrayCapsule(492, "Memories of Android 18", offset=0x4DFD3F)
MEMORIES_SUPREME_KAI = GrayCapsule(493, "Memories of Supreme Kai", offset=0x4DFD40)
MEMORIES_KID_GOKU = GrayCapsule(494, "Memories of Kid Goku", offset=0x4DFD42)
MEMORIES_BARDOCK = GrayCapsule(495, "Memories of Bardock", offset=0x4DFD42)
MEMORIES_UUB = GrayCapsule(496, "Memories of Uub", offset=0x4DFD43)
MEMORIES_RADITZ = GrayCapsule(497, "Memories of Raditz", offset=0x4DFD45)
MEMORIES_NAPPA = GrayCapsule(498, "Memories of Nappa", offset=0x4DFD45)
MEMORIES_RECOOME = GrayCapsule(499, "Memories of Recoome", offset=0x4DFD46)
MEMORIES_GINYU = GrayCapsule(500, "Memories of Captain Ginyu", offset=0x4DFD48)
MEMORIES_FRIEZA = GrayCapsule(501, "Memories of Frieza", offset=0x4DFD48)
MEMORIES_DR_GERO = GrayCapsule(502, "Memories of Dr Gero", offset=0x4DFD49)
MEMORIES_CELL = GrayCapsule(503, "Memories of Cell" ) # offset not provided
MEMORIES_DABURA = GrayCapsule(504, "Memories of Dabura", offset=0x4DFD4B)
MEMORIES_MAJIN_BUU = GrayCapsule(505, "Memories of Majin Buu", offset=0x4DFD4C)
MEMORIES_SUPER_BUU = GrayCapsule(506, "Memories of Super Buu", offset=0x4DFD4D)
MEMORIES_KID_BUU = GrayCapsule(507, "Memories of Kid Buu", offset=0x4DFD4E)
MEMORIES_COOLER = GrayCapsule(508, "Memories of Cooler", offset=0x4DFD4F)
MEMORIES_BROLY = GrayCapsule(509, "Memories of Broly", offset=0x4DFD50)
MEMORIES_OMEGA = GrayCapsule(510, "Memories of Omega Shenron", offset=0x4DFD52)
MEMORIES_SAIBAMEN = GrayCapsule(511, "Memories of Saibamen", offset=0x4DFD52)
MEMORIES_CELL_JR = GrayCapsule(512, "Memories of Cell Jr", offset=0x4DFD53)
MEMORIES_HEROES = GrayCapsule(513, "Memories of Heroes", offset=0x4DFD55)
MEMORIES_SUPPORTERS = GrayCapsule(514, "Memories of Supporters", offset=0x4DFD55)
CRYSTAL_BALL_0 = GrayCapsule(515, "Baba's Crystal Ball 000", offset=0x4DFD56)
CRYSTAL_BALL_1 = GrayCapsule(516, "Baba's Crystal Ball 001", offset=0x4DFD57)
CRYSTAL_BALL_2 = GrayCapsule(517, "Baba's Crystal Ball 002", offset=0x4DFD58)
CRYSTAL_BALL_3 = GrayCapsule(518, "Baba's Crystal Ball 003", offset=0x4DFD59)
CRYSTAL_BALL_4 = GrayCapsule(519, "Baba's Crystal Ball 004", offset=0x4DFD5A)

GRAY_CAPSULES = [
    # Fighters
    GOKU, KID_GOKU, KID_GOHAN, TEEN_GOHAN, GOHAN, GT_SAIYAMAN, GOTEN, VEGETA, TRUNKS, KID_TRUNKS, KRILLIN, PICCOLO,
    TIEN, YAMCHA, HERCULE, VIDEL, SUPREME_KAI, UUB, RADITZ, NAPPA, RECOOME, GINYU, FRIEZA, ANDROID_16, ANDROID_17,
    ANDROID_18, DR_GERO, CELL, MAJIN_BUU, SUPER_BUU, KID_BUU, DABURA, COOLER, BARDOCK, BROLY, OMEGA_SHENRON, SAIBAMEN,
    CELL_JR,
    # Training
    TRAINING_1, TRAINING_2, TRAINING_3, TRAINING_4, TRAINING_5, TRAINING_6, TRAINING_7, TRAINING_8, TRAINING_9,
    TRAINING_10, TRAINING_11, TRAINING_12,
    # Cards
    GREEN_CARD, SILVER_CARD, GOLD_CARD, BLACK_CARD,
    # Modes
    TOURNEY_NOVICE, TOURNEY_ADEPT, TOURNEY_ADV, TOURNEY_CELL, DRAGON_ARENA,
    # Stages
    TOURNEY_STAGE, TIME_CHAMBER, ARCHIPELAGO, MOUNTAINS, PLAINS, GPA_GOHANS_HOUSE, NAMEK, CELL_RING, SUPREME_KAIS_WORLD,
    INSIDE_BUU, RED_RIBBON_BASE, URBAN_AREA,
    # Difficulty
    GOKUS_WISH, PATH_POWER, ENDLESS_PATH, STRONGEST_TROPHY,
    # Memories
    MEMORIES_GOKU, MEMORIES_PICCOLO, MEMORIES_KID_GOHAN, MEMORIES_TEEN_GOHAN, MEMORIES_GOHAN, MEMORIES_VEGETA,
    MEMORIES_GOTEN, MEMORIES_TRUNKS, MEMORIES_KID_TRUNKS, MEMORIES_KRILLIN, MEMORIES_TIEN, MEMORIES_YAMCHA,
    MEMORIES_HERCULE, MEMORIES_VIDEL, MEMORIES_GT_SAIYAMAN, MEMORIES_ANDROID_16, MEMORIES_ANDROID_17, MEMORIES_ANDROID_18,
    MEMORIES_SUPREME_KAI, MEMORIES_KID_GOKU, MEMORIES_BARDOCK, MEMORIES_UUB, MEMORIES_RADITZ, MEMORIES_NAPPA,
    MEMORIES_RECOOME, MEMORIES_GINYU, MEMORIES_FRIEZA, MEMORIES_DR_GERO, MEMORIES_CELL, MEMORIES_DABURA,
    MEMORIES_MAJIN_BUU, MEMORIES_SUPER_BUU, MEMORIES_KID_BUU, MEMORIES_COOLER, MEMORIES_BROLY, MEMORIES_OMEGA,
    MEMORIES_SAIBAMEN, MEMORIES_CELL_JR, MEMORIES_HEROES, MEMORIES_SUPPORTERS, CRYSTAL_BALL_0, CRYSTAL_BALL_1,
    CRYSTAL_BALL_2, CRYSTAL_BALL_3, CRYSTAL_BALL_4
]

## I don't know what to do with the Story Reenactment voice clips. They can be unlocked, so they can be "items"
##todo: figure out Story Reenactment later

# Custom items
DRAGON_RADAR_GOKU = ItemData(520, "Dragon Radar (Goku)")
DRAGON_RADAR_KGOHAN = ItemData(521, "Dragon Radar (Kid Gohan)")
DRAGON_RADAR_TGOHAN = ItemData(522, "Dragon Radar (Teen Gohan)")
DRAGON_RADAR_GOHAN = ItemData(523, "Dragon Radar (Gohan)")
DRAGON_RADAR_PICCOLO = ItemData(524, "Dragon Radar (Piccolo)")
DRAGON_RADAR_KRILLIN = ItemData(525, "Dragon Radar (Krillin)")
DRAGON_RADAR_TIEN = ItemData(526, "Dragon Radar (Tien)")
DRAGON_RADAR_VEGETA = ItemData(527, "Dragon Radar (Vegeta)")
DRAGON_RADAR_YAMCHA = ItemData(528, "Dragon Radar (Yamcha)")
DRAGON_RADAR_UUB = ItemData(529, "Dragon Radar (Uub)")
DRAGON_RADAR_BROLY = ItemData(530, "Dragon Radar (Broly)")

CUSTOM_ITEMS = [
    DRAGON_RADAR_GOKU, DRAGON_RADAR_KGOHAN, DRAGON_RADAR_TGOHAN, DRAGON_RADAR_GOHAN, DRAGON_RADAR_PICCOLO,
    DRAGON_RADAR_KRILLIN, DRAGON_RADAR_TIEN, DRAGON_RADAR_VEGETA, DRAGON_RADAR_YAMCHA, DRAGON_RADAR_UUB, DRAGON_RADAR_BROLY,
]

## the basic order roughly mirrors how items are given in game
GOKU_CAPSULES = [GOKU, KAME_GOKU, KAIOKEN, DRAG_FIST_GOKU, SPIRIT_BOMB_GOKU, SSJ_GOKU, WARP_KAME_GOKU, SSJ2_GOKU,
                 SSJ3_GOKU, SSJ4_GOKU, BREAK_GOKU]
KID_GOHAN_CAPSULES = [KID_GOHAN, MASENKO, POTENTIAL_KGOHAN, BREAK_KGOHAN]
TEEN_GOHAN_CAPSULES = [TEEN_GOHAN, KAME_TGOHAN, SSJ_TGOHAN, SSJ2_TGOHAN, SOAR_TGOHAN, FS_KAME, BREAK_TGOHAN]
GOHAN_CAPSULES = [GOHAN, KAME_GOHAN, SSJ_GOHAN, SSJ2_GOHAN, SOAR_GOHAN, SUPER_KAME_GOHAN, ELDER_UNLOCK, BREAK_GOHAN]
KRILLIN_CAPSULES = [KRILLIN, KAME_KRILLIN, DD_KRILLIN, POTENTIAL_KRILLIN, FIERCE_DD, BREAK_KRILLIN]
VEGETA_CAPSULES = [VEGETA, GALICK, FINAL_IMPACT, SSJ_VEGETA, BIG_BANG, FINAL_FLASH, SSJ2_VEGETA, SSJ4_VEGETA, BREAK_VEGETA]
PICCOLO_CAPSULES = [PICCOLO, DEST_WAVE, SBEAM_CANNON, SYNC_NAIL, FUSE_KAMI, LGRENADE, HZGRENADE, BREAK_PICCOLO]
TIEN_CAPSULES = [TIEN, BLAST_CANNON, DODON, NEO_BLAST_CANNON, BREAK_TIEN]
YAMCHA_CAPSULES = [YAMCHA, KAME_YAMCHA, WOLF_FANG, SPIRIT_BALL, BREAK_YAMCHA]
UUB_CAPSULES = [UUB, KI_CANNON, FIERCE_FLURRY, BREAK_UUB]
BROLY_CAPSULES = [BROLY, BLASTER_SHELL, LSSJ_BROLY, GIGANT_PRESS, GIGANT_METEOR, BREAK_BROLY]
DW_RED_CAPSULES = [GOKU_CAPSULES[1:], KID_GOHAN_CAPSULES[1:], TEEN_GOHAN_CAPSULES[1:], GOHAN_CAPSULES[1:],
                   KRILLIN_CAPSULES[1:], VEGETA_CAPSULES[1:], PICCOLO_CAPSULES[1:], TIEN_CAPSULES[1:],
                   YAMCHA_CAPSULES[1:], UUB_CAPSULES[1:], BROLY_CAPSULES[1:]]

PROGRESSIVE_GOKU = Capsule(id=531, name="Progressive Goku", max_copies=len(GOKU_CAPSULES))
PROGRESSIVE_KID_GOHAN = Capsule(id=532, name= "Progressive Kid Gohan", max_copies=len(KID_GOHAN_CAPSULES))
PROGRESSIVE_TEEN_GOHAN = Capsule(id=533, name= "Progressive Teen Gohan", max_copies=len(TEEN_GOHAN_CAPSULES))
PROGRESSIVE_GOHAN = Capsule(id=534, name= "Progressive Gohan", max_copies=len(GOHAN_CAPSULES))
PROGRESSIVE_KRILLIN = Capsule(id=535, name= "Progressive Krillin", max_copies=len(KRILLIN_CAPSULES))
PROGRESSIVE_PICCOLO = Capsule(id=536, name= "Progressive Piccolo", max_copies=len(PICCOLO_CAPSULES))
PROGRESSIVE_VEGETA = Capsule(id=537, name= "Progressive Vegeta", max_copies=len(VEGETA_CAPSULES))
PROGRESSIVE_TIEN = Capsule(id=538, name= "Progressive Tien", max_copies=len(TIEN_CAPSULES))
PROGRESSIVE_YAMCHA = Capsule(id=539, name= "Progressive Yamcha", max_copies=len(YAMCHA_CAPSULES))
PROGRESSIVE_UUB = Capsule(id=540, name= "Progressive Uub", max_copies=len(UUB_CAPSULES))
PROGRESSIVE_BROLY = Capsule(id=541, name= "Progressive Broly", max_copies=len(BROLY_CAPSULES))
PROGRESSIVE_CAPSULES = [PROGRESSIVE_GOKU, PROGRESSIVE_KID_GOHAN, PROGRESSIVE_TEEN_GOHAN, PROGRESSIVE_GOHAN,
                        PROGRESSIVE_KRILLIN, PROGRESSIVE_PICCOLO, PROGRESSIVE_VEGETA, PROGRESSIVE_YAMCHA,
                        PROGRESSIVE_TIEN, PROGRESSIVE_UUB, PROGRESSIVE_BROLY]

ALL_ITEMS = [
    *RED_CAPSULES,
    *GREEN_CAPSULES,
    *YELLOW_CAPSULES,
    *GRAY_CAPSULES,
    *PROGRESSIVE_CAPSULES,
    # *CUSTOM_ITEMS
]

DW_CHARACTERS = [GOKU, KID_GOHAN, TEEN_GOHAN, GOHAN, PICCOLO, KRILLIN, TIEN, VEGETA, BROLY, UUB, YAMCHA]

dw_characters_as_dict = {}
for char in DW_CHARACTERS:
    dw_characters_as_dict[char.name] = char.item_id
DW_CHARACTER_NAMES = dw_characters_as_dict

def get_name_pairs() -> Dict[int, ItemData]:
    collector = {}
    for item in ALL_ITEMS:
        collector[item.name] = item
    return collector

def get_id_pairs() -> Dict[str, ItemData]:
    collector = {}
    for item in ALL_ITEMS:
        collector[item.item_id] = item
    return collector

NAME_PAIRS = get_name_pairs()

ID_PAIRS = get_id_pairs()

def item_name_to_id(name) -> int | None:
    return NAME_PAIRS[name].item_id


def item_id_to_name(id) -> str | None:
    return ID_PAIRS[id].name

var =
print()