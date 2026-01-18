from typing import NamedTuple, Optional, Callable, Dict
from ..Logic import *
from .Addresses import Address


class LocationData(NamedTuple):
    location_id: int
    name: str
    access_rule: Callable[[CollectionState, int], bool]
    is_shop: bool = False
    address: Optional[Address] = None


# Dragon Universe Checks
## Goku
GOKU_RADITZ_CLEAR = LocationData(1, "Goku: Saiyan Saga - Defeat Raditz", can_goku)
GOKU_NAPPA_CLEAR = LocationData(2, "Goku: Saiyan Saga - Defeat Nappa", can_goku)
GOKU_VEGETA_1_CLEAR = LocationData(3, "Goku: Saiyan Saga - Defeat Vegeta", can_goku)
GOKU_RECOOME_CLEAR = LocationData(4, "Goku: Namek Saga - Defeat Recoome", can_goku)
GOKU_GINYU_CLEAR = LocationData(5, "Goku: Namek Saga - Defeat Ginyu", can_goku)
GOKU_FRIEZA_1_CLEAR = LocationData(6, "Goku: Namek Saga - Defeat Final Form Frieza", can_goku)
GOKU_FRIEZA_2_CLEAR = LocationData(7, "Goku: Namek Saga - Defeat 100% Final Form Frieza", can_goku)
GOKU_COOLER_CLEAR = LocationData(8, "Goku: Android Saga - Defeat Metal Cooler at Time Machine", can_goku)
GOKU_CELL_CLEAR = LocationData(9, "Goku: Android Saga - Defeat Cell at Cell Games Arena", can_goku)
GOKU_MAJIN_VEGETA_CLEAR = LocationData(10, "Goku: Buu Saga - Defeat Majin Vegeta", can_goku)
GOKU_MAJIN_BUU_CLEAR = LocationData(11, "Goku: Buu Saga - Defeat Majin Buu", can_goku)
GOKU_SUPER_BUU_1_CLEAR = LocationData(12, "Goku: Buu Saga - Defeat Super Buu (Gohan)", can_goku)
GOKU_SUPER_BUU_2_CLEAR = LocationData(13, "Goku: Buu Saga - Defeat Super Buu", can_goku)
GOKU_KID_BUU_CLEAR = LocationData(14, "Goku: Buu Saga - Defeat Kid Buu", can_goku)
GOKU_UUB_CLEAR = LocationData(15, "Goku: Extra Saga - Defeat Uub", can_super_spirit_bomb) # Must have defeated Kid Buu 
                                                                                    # with a successful Super Spirit Bomb
GOKU_COOLER_2_CLEAR = LocationData(16, "Goku 2: Namek Saga - Defeat Cooler", can_wish_goku)
GOKU_METAL_COOLER_CLEAR = LocationData(17, "Goku 2: Namek Saga - Defeat Metal Cooler", can_wish_goku)
GOKU_VEGETA_2_CLEAR = LocationData(18, "Goku 2: Namek Saga - Defeat Super Saiyan Vegeta", can_wish_goku_vegeta)
GOKU_COOLER_3_CLEAR = LocationData(19, "Goku 2: Namek Saga - Defeat Cooler after Vegeta", can_wish_goku_vegeta)
GOKU_BROLY_CLEAR = LocationData(20, "Goku 2: Buu Saga - Defeat Broly", can_wish_goku)
GOKU_GOTENKS_CLEAR = LocationData(21, "Goku 2: Extra Saga - Defeat Gotenks", can_wish_and_spirit_bomb)
GOKU_OMEGA_CLEAR = LocationData(22, "Goku 2: Extra Saga - Defeat Omega Shenron", can_wish_and_spirit_bomb)

GOKU_BOSSES = [
    GOKU_RADITZ_CLEAR, GOKU_NAPPA_CLEAR, GOKU_VEGETA_1_CLEAR, GOKU_RECOOME_CLEAR, GOKU_GINYU_CLEAR, GOKU_FRIEZA_1_CLEAR,
    GOKU_FRIEZA_2_CLEAR, GOKU_COOLER_CLEAR, GOKU_CELL_CLEAR, GOKU_MAJIN_VEGETA_CLEAR, GOKU_MAJIN_BUU_CLEAR,
    GOKU_SUPER_BUU_1_CLEAR, GOKU_SUPER_BUU_2_CLEAR, GOKU_KID_BUU_CLEAR, GOKU_UUB_CLEAR, GOKU_COOLER_2_CLEAR,
    GOKU_METAL_COOLER_CLEAR, GOKU_VEGETA_2_CLEAR, GOKU_COOLER_3_CLEAR, GOKU_BROLY_CLEAR, GOKU_GOTENKS_CLEAR,
    GOKU_OMEGA_CLEAR
]

## Kid Gohan
KGOHAN_PICCOLO_CLEAR = LocationData(23, "Kid Gohan: Saiyan Saga - Defeat Piccolo", can_kid_gohan)
KGOHAN_SAIBAMEN_CLEAR = LocationData(24, "Kid Gohan: Saiyan Saga - Defeat Saibamen", can_kid_gohan)
KGOHAN_NAPPA_CLEAR = LocationData(25, "Kid Gohan: Saiyan Saga - Defeat Nappa", can_kid_gohan)
KGOHAN_RECOOME_CLEAR = LocationData(26, "Kid Gohan: Namek Saga - Defeat Recoome", can_kid_gohan)
KGOHAN_FRIEZA_CLEAR = LocationData(27, "Kid Gohan: Namek Saga - Defeat Third Form Frieza", can_kid_gohan)
KGOHAN_GOKU_CLEAR = LocationData(28, "Kid Gohan 2: Saiyan Saga - Defeat Goku at Forest red marker", can_wish_kid_gohan)
KGOHAN_GINYU_GOKU_CLEAR = LocationData(29, "Kid Gohan 2: Namek Saga - Defeat Goku w/ Scouter at western red marker", can_wish_kid_gohan)
KGOHAN_COOLER_CLEAR = LocationData(30, "Kid Gohan 2: Namek Saga - Defeat Cooler", can_wish_kid_gohan)

KID_GOHAN_BOSSES = [
    KGOHAN_PICCOLO_CLEAR, KGOHAN_SAIBAMEN_CLEAR, KGOHAN_NAPPA_CLEAR, KGOHAN_RECOOME_CLEAR,KGOHAN_FRIEZA_CLEAR,
    KGOHAN_GOKU_CLEAR, KGOHAN_GINYU_GOKU_CLEAR, KGOHAN_COOLER_CLEAR
]

## Teen Gohan
TGOHAN_PICCOLO_CLEAR = LocationData(31, "Teen Gohan: Defeat Piccolo", can_teen_gohan)
TGOHAN_KRILLIN_CLEAR = LocationData(32, "Teen Gohan: Defeat Krillin", can_teen_gohan)
TGOHAN_GOKU_CLEAR = LocationData(33, "Teen Gohan: Defeat Super Saiyan Goku", can_teen_gohan)
TGOHAN_CELL_1_CLEAR = LocationData(34, "Teen Gohan: Defeat Perfect Cell", can_teen_gohan)
TGOHAN_CELL_2_CLEAR = LocationData(35, "Teen Gohan: Defeat Super Perfect Cell", can_teen_gohan)
TGOHAN_TIEN_CLEAR = LocationData(36, "Teen Gohan 2: Defeat Tien", can_wish_teen_gohan)
TGOHAN_YAMCHA_CLEAR = LocationData(37, "Teen Gohan 2: Defeat Yamcha", can_wish_teen_gohan)

TEEN_GOHAN_BOSSES = [
    TGOHAN_PICCOLO_CLEAR, TGOHAN_KRILLIN_CLEAR, TGOHAN_GOKU_CLEAR, TGOHAN_CELL_1_CLEAR, TGOHAN_CELL_2_CLEAR,
    TGOHAN_TIEN_CLEAR, TGOHAN_YAMCHA_CLEAR
]

## Gohan
GOHAN_GOTEN_CLEAR = LocationData(38, "Gohan: Defeat Goten", can_gohan)
GOHAN_VIDEL_CLEAR = LocationData(39, "Gohan: Defeat Videl", can_gohan)
GOHAN_PICCOLO_CLEAR = LocationData(40, "Gohan: Defeat Piccolo", can_gohan)
GOHAN_DABURA_CLEAR = LocationData(41, "Gohan: Defeat Dabura", can_gohan)
GOHAN_MAJIN_BUU_CLEAR = LocationData(42, "Gohan: Defeat Majin Buu", can_gohan)
GOHAN_SUPER_BUU_CLEAR = LocationData(999, "Gohan: Defeat Super Buu", can_gohan)
GOHAN_VEGETA_CLEAR = LocationData(43, "Gohan 2: Defeat Vegeta", can_wish_gohan)
GOHAN_MAJIN_VEGETA_CLEAR = LocationData(44, "Gohan 2: Defeat Majin Vegeta", can_wish_gohan)
GOHAN_KID_BUU_CLEAR = LocationData(45, "Gohan 2: Defeat Kid Buu", can_wish_gohan)
GOHAN_BROLY_CLEAR = LocationData(46, "Gohan 2: Defeat Broly", can_wish_gohan)

GOHAN_BOSSES = [
    GOHAN_GOTEN_CLEAR, GOHAN_VIDEL_CLEAR, GOHAN_PICCOLO_CLEAR, GOHAN_DABURA_CLEAR, GOHAN_MAJIN_BUU_CLEAR,
    GOHAN_SUPER_BUU_CLEAR, GOHAN_VEGETA_CLEAR, GOHAN_MAJIN_VEGETA_CLEAR, GOHAN_KID_BUU_CLEAR, GOHAN_BROLY_CLEAR
]

## Vegeta
VEGETA_GOKU_1_CLEAR = LocationData(47, "Vegeta: Saiyan Saga - Defeat Goku", can_vegeta)
VEGETA_KID_GOHAN_CLEAR = LocationData(48, "Vegeta: Saiyan Saga - Defeat Kid Gohan", can_vegeta)
VEGETA_RECOOME_CLEAR = LocationData(49, "Vegeta: Namek Saga - Defeat Recoome", can_vegeta)
VEGETA_FRIEZA_1_CLEAR = LocationData(50, "Vegeta: Namek Saga - Defeat First Form Frieza", can_vegeta)
VEGETA_FRIEZA_2_CLEAR = LocationData(51, "Vegeta: Namek Saga - Defeat Final Form Frieza", can_vegeta)
VEGETA_ANDROID_17_CLEAR = LocationData(52, "Vegeta: Android Saga - Defeat Android 17", can_vegeta)
VEGETA_ANDROID_18_CLEAR = LocationData(53, "Vegeta: Android Saga - Defeat Android 18", can_vegeta)
VEGETA_CELL_1_CLEAR = LocationData(54, "Vegeta: Android Saga - Defeat Cell (17 Absorbed)", can_vegeta)
VEGETA_CELL_2_CLEAR = LocationData(55, "Vegeta: Android Saga - Defeat Perfect Cell", can_vegeta)
VEGETA_GOKU_2_CLEAR = LocationData(56, "Vegeta: Buu Saga - Defeat Super Saiyan 2 Goku", can_vegeta)
VEGETA_MAJIN_BUU_CLEAR = LocationData(57, "Vegeta: Buu Saga - Defeat Majin Buu", can_vegeta)
VEGETA_SUPER_BUU_1_CLEAR = LocationData(58, "Vegeta: Buu Saga - Defeat Super Buu (Gohan)", can_vegeta)
VEGETA_SUPER_BUU_2_CLEAR = LocationData(59, "Vegeta: Buu Saga - Defeat Super Buu", can_vegeta)
VEGETA_KID_BUU_CLEAR = LocationData(60, "Vegeta: Buu Saga - Defeat Kid Buu", can_vegeta)
VEGETA_METAL_COOLER_CLEAR = LocationData(61, "Vegeta 2: Namek Saga - Defeat Metal Cooler", can_wish_vegeta)
VEGETA_BROLY_CLEAR = LocationData(62, "Vegeta 2: Buu Saga - Defeat Broly", can_wish_vegeta)
VEGETA_GOTENKS_CLEAR = LocationData(63, "Vegeta 2: Extra Saga - Defeat Gotenks", can_wish_vegeta)
VEGETA_GOKU_3_CLEAR = LocationData(64, "Vegeta 2: Extra Saga - Defeat Super Saiyan 4 Goku", can_wish_vegeta)

VEGETA_BOSSES = [
    VEGETA_GOKU_1_CLEAR, VEGETA_KID_GOHAN_CLEAR, VEGETA_RECOOME_CLEAR, VEGETA_FRIEZA_1_CLEAR, VEGETA_FRIEZA_2_CLEAR,
    VEGETA_ANDROID_17_CLEAR, VEGETA_ANDROID_18_CLEAR, VEGETA_CELL_1_CLEAR, VEGETA_CELL_2_CLEAR, VEGETA_GOKU_2_CLEAR,
    VEGETA_MAJIN_BUU_CLEAR, VEGETA_SUPER_BUU_1_CLEAR, VEGETA_SUPER_BUU_2_CLEAR, VEGETA_KID_BUU_CLEAR,
    VEGETA_METAL_COOLER_CLEAR, VEGETA_BROLY_CLEAR, VEGETA_GOTENKS_CLEAR, VEGETA_GOKU_3_CLEAR
]

## Krillin
KRILLIN_SAIBAMEN_CLEAR = LocationData(65, "Krillin - Saiyan Saga - Defeat Saibamen", can_krillin)
KRILLIN_NAPPA_CLEAR = LocationData(66, "Krillin - Saiyan Saga - Defeat Nappa", can_krillin)
KRILLIN_RECOOME_CLEAR = LocationData(67, "Krillin - Namek Saga - Defeat Recoome", can_krillin)
KRILLIN_GINYU_GOKU_CLEAR = LocationData(68, "Krillin - Namek Saga - Defeat Goku with Scouter", can_krillin)
KRILLIN_FRIEZA_1_CLEAR = LocationData(69, "Krillin - Namek Saga - Defeat Second Form Frieza", can_krillin)
KRILLIN_FRIEZA_2_CLEAR = LocationData(70, "Krillin - Namek Saga - Defeat Final Form Frieza", can_krillin)
KRILLIN_CELL_CLEAR = LocationData(71, "Krillin 2 - Android Saga - Defeat Perfect Form Cell", can_wish_krillin)

KRILLIN_BOSSES = [
    KRILLIN_SAIBAMEN_CLEAR, KRILLIN_NAPPA_CLEAR, KRILLIN_RECOOME_CLEAR, KRILLIN_GINYU_GOKU_CLEAR, KRILLIN_FRIEZA_1_CLEAR,
    KRILLIN_FRIEZA_2_CLEAR, KRILLIN_CELL_CLEAR
]

## Piccolo
PICCOLO_RADITZ_CLEAR = LocationData(72, "Piccolo: Saiyan Saga - Defeat Raditz", can_piccolo)
PICCOLO_KID_GOHAN_CLEAR = LocationData(73, "Piccolo: Saiyan Saga - Defeat Kid Gohan", can_piccolo)
PICCOLO_SAIBAMEN_CLEAR = LocationData(74, "Piccolo: Saiyan Saga - Defeat Saibamen", can_piccolo)
PICCOLO_NAPPA_CLEAR = LocationData(75, "Piccolo: Saiyan Saga - Defeat Nappa", can_piccolo)
PICCOLO_FRIEZA_1_CLEAR = LocationData(76, "Piccolo: Namek Saga - Defeat Second Form Frieza", can_piccolo)
PICCOLO_FRIEZA_2_CLEAR = LocationData(77, "Piccolo: Namek Saga - Defeat Third Form Frieza", can_piccolo)
PICCOLO_DR_GERO_CLEAR = LocationData(78, "Piccolo: Android Saga - Defeat Dr Gero", can_piccolo)
PICCOLO_CELL_1_CLEAR = LocationData(79, "Piccolo: Android Saga - Defeat Cell", can_piccolo)
PICCOLO_ANDROID_17_CLEAR = LocationData(80, "Piccolo: Android Saga - Defeat Android 17", can_piccolo)
PICCOLO_SUPER_BUU_CLEAR = LocationData(81, "Piccolo: Buu Saga - Defeat Super Buu", can_piccolo)
PICCOLO_GOKU_CLEAR = LocationData(82, "Piccolo 2: Saiyan Saga - Defeat Goku", can_wish_piccolo)
PICCOLO_VEGETA_CLEAR = LocationData(83, "Piccolo 2: Saiyan Saga - Defeat Vegeta", can_wish_piccolo)
PICCOLO_COOLER_CLEAR = LocationData(84, "Piccolo 2: Namek Saga - Defeat Cooler", can_wish_piccolo)
PICCOLO_METAL_COOLER_CLEAR = LocationData(85, "Piccolo 2: Namek Saga - Defeat Metal Cooler", can_wish_piccolo)
PICCOLO_FRIEZA_3_CLEAR = LocationData(86, "Piccolo 2: Namek Saga - Defeat Final Form Frieza", can_wish_piccolo)
PICCOLO_CELL_2_CLEAR = LocationData(87, "Piccolo 2: Android Saga - Defeat Perfect Cell", can_wish_piccolo)
PICCOLO_DABURA_CLEAR = LocationData(88, "Piccolo 2: Buu Saga - Defeat Dabura", can_wish_piccolo)
PICCOLO_BROLY_CLEAR = LocationData(89, "Piccolo 2: Buu Saga - Defeat Broly", can_wish_piccolo)

PICCOLO_BOSSES = [
    PICCOLO_RADITZ_CLEAR, PICCOLO_KID_GOHAN_CLEAR, PICCOLO_SAIBAMEN_CLEAR, PICCOLO_NAPPA_CLEAR, PICCOLO_FRIEZA_1_CLEAR,
    PICCOLO_FRIEZA_2_CLEAR, PICCOLO_DR_GERO_CLEAR, PICCOLO_CELL_1_CLEAR, PICCOLO_ANDROID_17_CLEAR, PICCOLO_SUPER_BUU_CLEAR,
    PICCOLO_GOKU_CLEAR, PICCOLO_VEGETA_CLEAR, PICCOLO_COOLER_CLEAR, PICCOLO_METAL_COOLER_CLEAR, PICCOLO_FRIEZA_3_CLEAR,
    PICCOLO_CELL_2_CLEAR, PICCOLO_DABURA_CLEAR, PICCOLO_BROLY_CLEAR
]

## Tien
TIEN_SAIBAMEN_CLEAR = LocationData(90, "Tien: Saiyan Saga - Defeat Saibaman", can_tien)
TIEN_NAPPA_CLEAR = LocationData(91, "Tien: Saiyan Saga - Defeat Nappa", can_tien)
TIEN_CELL_CLEAR = LocationData(92, "Tien: Android Saga - Defeat Second Form Cell", can_tien)
TIEN_CELL_JR_CLEAR = LocationData(93, "Tien: Android Saga - Defeat Cell Jr", can_tien)
TIEN_SUPER_BUU_CLEAR = LocationData(94, "Tien: Buu Saga - Defeat Super Buu (Gotenks)", can_tien)
TIEN_YAMCHA_CLEAR = LocationData(95, "Tien 2: Extra Saga - Defeat Yamcha", can_wish_tien)

TIEN_BOSSES = [
    TIEN_SAIBAMEN_CLEAR, TIEN_NAPPA_CLEAR, TIEN_CELL_CLEAR, TIEN_CELL_JR_CLEAR, TIEN_SUPER_BUU_CLEAR, TIEN_YAMCHA_CLEAR
]

## Yamcha
YAMCHA_SAIBAMEN_CLEAR = LocationData(96, "Yamcha: Saiyan Saga - Defeat Saibaman at Plains", can_yamcha)
YAMCHA_DR_GERO_CLEAR = LocationData(97, "Yamcha: Android Saga - Defeat Dr Gero at South City", can_yamcha)
YAMCHA_VEGETA_CLEAR = LocationData(98, "Yamcha 2: Buu Saga - Defeat Vegeta at World Tournament", can_yamcha) # find all events relating to Bulma's new partner in Cell Saga
YAMCHA_TIEN_CLEAR = LocationData(99, "Yamcha 2: Buu Saga - Defeat Tien at World Tournament", can_yamcha) # don't find all events relating to Bulma's new partner in Cell Saga

YAMCHA_BOSSES = [
    YAMCHA_SAIBAMEN_CLEAR, YAMCHA_DR_GERO_CLEAR, YAMCHA_TIEN_CLEAR, YAMCHA_VEGETA_CLEAR
]

## Uub
UUB_GOKU_1_CLEAR = LocationData(100, "Uub: Defeat Goku at World Tournament", can_uub)
UUB_VEGETA_CLEAR = LocationData(101, "Uub: Defeat Vegeta at West City", can_uub)
UUB_MAJIN_BUU_CLEAR = LocationData(102, "Uub: Defeat Majin Buu at Hercule City", can_uub)
UUB_GOKU_2_CLEAR = LocationData(103, "Uub: Defeat Goku at Archipelago", can_uub)
UUB_OMEGA_SHENRON_CLEAR = LocationData(104, "Uub 2: Defeat Omega Shenron at Mountains", can_uub) 
# meet Master Roshi at Kame House before Goku 2 and the story's path will diverge

UUB_BOSSES = [
    UUB_GOKU_1_CLEAR, UUB_VEGETA_CLEAR, UUB_MAJIN_BUU_CLEAR, UUB_GOKU_2_CLEAR, UUB_OMEGA_SHENRON_CLEAR
]

## Broly
BROLY_KRILLIN_CLEAR = LocationData(105, "Broly: Defeat Krillin at Kame House", can_broly)
BROLY_PICCOLO_CLEAR = LocationData(106, "Broly: Defeat Piccolo at Kami's Lookout", can_broly)
BROLY_VEGETA_CLEAR = LocationData(107, "Broly: Defeat Vegeta at West City", can_broly)
BROLY_VIDEL_CLEAR = LocationData(108, "Broly: Defeat Videl at Central City marker", can_broly)
BROLY_KID_TRUNKS_CLEAR = LocationData(109, "Broly: Defeat Kid Trunks at Plains marker", can_broly)
BROLY_GOTEN_CLEAR = LocationData(110, "Broly: Defeat Goten at Mountains marker", can_broly)
BROLY_GOHAN_1_CLEAR = LocationData(111, "Broly: Defeat Gohan 1 at Plains marker (Story Route)", can_broly)
BROLY_GOHAN_2_CLEAR = LocationData(112, "Broly: Defeat Gohan 2 at Plains marker", can_broly)
BROLY_GOHAN_3_CLEAR = LocationData(666, "Broly 2: Defeat Gohan at Plains Marker (Goku Route)", can_wish_broly) # Destroy Goku's House before fighting Gohan to unlock this route
BROLY_GOKU_CLEAR = LocationData(113, "Broly 2: Defeat Goku at Plains marker", can_wish_broly) 

BROLY_BOSSES = [
    BROLY_KRILLIN_CLEAR, BROLY_PICCOLO_CLEAR, BROLY_VEGETA_CLEAR, BROLY_VIDEL_CLEAR, BROLY_KID_TRUNKS_CLEAR,
    BROLY_GOTEN_CLEAR, BROLY_GOHAN_1_CLEAR, BROLY_GOHAN_1_CLEAR, BROLY_GOHAN_2_CLEAR, BROLY_GOHAN_2_CLEAR
]

DU_BOSSES = [
    *GOKU_BOSSES,
    *KID_GOHAN_BOSSES,
    *TEEN_GOHAN_BOSSES,
    *GOHAN_BOSSES,
    *VEGETA_BOSSES,
    *KRILLIN_BOSSES,
    *PICCOLO_BOSSES,
    *TIEN_BOSSES,
    *YAMCHA_BOSSES,
    *UUB_BOSSES,
    *BROLY_BOSSES
]

## Story Reenactments
REENACTMENT_0 = LocationData(114, "Goku: Use Kamehameha against Raditz", can_complete_reenactment_0)
REENACTMENT_1 = LocationData(115, "Piccolo: Use Special Beam Cannon against Raditz", can_complete_reenactment_1)
REENACTMENT_2 = LocationData(116, "Tien: Use Ki Blast Cannon against Nappa", can_complete_reenactment_2)
REENACTMENT_3 = LocationData(117, "Kid Gohan: Use Masenko against Nappa", can_complete_reenactment_3)
REENACTMENT_4 = LocationData(118, "Krillin: Use Destructo Disc against Second Form Frieza", can_complete_reenactment_4)
REENACTMENT_5 = LocationData(119, "Goku: Use Super Saiyan against 100% Final Form Frieza", can_complete_reenactment_5)
REENACTMENT_6 = LocationData(120, "Yamcha: Use Senzu Bean during Battle with Dr Gero", can_complete_reenactment_6)
REENACTMENT_7 = LocationData(121, "Piccolo: Use Fuse with Kami against Base Cell", can_complete_reenactment_7)
REENACTMENT_8 = LocationData(122, "Vegeta: Have 2500 HP Remaining at end of Cell (17 Absorbed) Fight", can_complete_reenactment_8)
REENACTMENT_9 = LocationData(123, "Vegeta: Use Final Flash against Perfect Cell", can_complete_reenactment_9)
REENACTMENT_10 = LocationData(124, "Teen Gohan: Use Super Saiyan against Goku", can_complete_reenactment_10)
REENACTMENT_11 = LocationData(125, "Teen Gohan: Defeat Super Perfect Cell with Father-Son Kamehameha", can_complete_reenactment_11)
# You do not have to exceed Cell's meter during the charging segment
REENACTMENT_12 = LocationData(126, "Vegeta: Defeat Majin Buu with Final Explosion", can_complete_reenactment_12)
# You MUST exceed Buu's meter during the charging segment
# Reenactment 12 uses a special Vegeta with access to the necessary move, so you can complete it with just Vegeta
REENACTMENT_13 = LocationData(127, "Goku: Use Super Saiyan 3 against Majin Buu", can_complete_reenactment_13)
REENACTMENT_14 = LocationData(128, "Piccolo: Defeat Super Buu after 60 Seconds have Elapsed", can_complete_reenactment_14)
REENACTMENT_15 = LocationData(129, "Gohan: Use Elder Kai Unlock Ability against Super Buu", can_complete_reenactment_15)
REENACTMENT_16 = LocationData(130, "Goku: Defeat Kid Buu with Super Spirit Bomb", can_complete_reenactment_16)
# To do this, you must already be base Goku or Kaioken and have Super Saiyan in your tray. If you use Spirit Bomb, it will
# become Super Spirit Bomb. Defeat Kid Buu by filling your meter more than he does.
REENACTMENT_17 = LocationData(131, "Vegeta: Use Super Saiyan 4 against Super Saiyan 4 Goku", can_complete_reenactment_17)
REENACTMENT_18 = LocationData(132, "Goku: Defeat Omega Shenron with 100X Big Bang Kamehameha", can_complete_reenactment_18)
REENACTMENT_19 = LocationData(133, "Broly: Use a Fully-Powered Gigantic Meteor against Gohan 1", can_complete_reenactment_19)
REENACTMENT_20 = LocationData(134, "Uub: Use Ki Cannon against Goku 1", can_complete_reenactment_20)

DU_REENACTMENTS = [
    REENACTMENT_0, REENACTMENT_1, REENACTMENT_2, REENACTMENT_3, REENACTMENT_4, REENACTMENT_5, REENACTMENT_6, REENACTMENT_7,
    REENACTMENT_8, REENACTMENT_9, REENACTMENT_10, REENACTMENT_11, REENACTMENT_12, REENACTMENT_13, REENACTMENT_14,
    REENACTMENT_15, REENACTMENT_16, REENACTMENT_17, REENACTMENT_18, REENACTMENT_19, REENACTMENT_20
]

## Difficulty-related
VERY_HARD_CLEAR = LocationData(135, "Dragon Universe: Clear any Route on Very Hard", has_very_hard)
Z1_CLEAR = LocationData(136, "Dragon Universe: Clear any Route on Z1", has_z_hard)
Z2_CLEAR = LocationData(137, "Dragon Universe: Clear any Route on Z2", has_z_hard_2)
Z3_CLEAR = LocationData(138, "Dragon Universe: Clear any Route on Z3", has_z_hard_3)

DU_DIFFICULTIES = [VERY_HARD_CLEAR, Z1_CLEAR, Z2_CLEAR, Z3_CLEAR]

## Wishes
GOKU_WISH_1 = LocationData(139, "Goku Wish 1", can_wish_goku)
GOKU_WISH_2 = LocationData(140, "Goku Wish 2", can_wish_goku)
GOKU_WISH_3 = LocationData(141, "Goku Wish 3", can_wish_goku)
KGOHAN_WISH_1 = LocationData(142, "Kid Gohan Wish 1", can_wish_kid_gohan)
KGOHAN_WISH_2 = LocationData(143, "Kid Gohan Wish 2", can_wish_kid_gohan)
KGOHAN_WISH_3 = LocationData(144, "Kid Gohan Wish 3", can_wish_kid_gohan)
TGOHAN_WISH_1 = LocationData(145, "Teen Gohan Wish 1", can_wish_teen_gohan)
TGOHAN_WISH_2 = LocationData(146, "Teen Gohan Wish 2", can_wish_teen_gohan)
TGOHAN_WISH_3 = LocationData(147, "Teen Gohan Wish 3", can_wish_teen_gohan)
GOHAN_WISH_1 = LocationData(148, "Gohan Wish 1", can_wish_gohan)
GOHAN_WISH_2 = LocationData(149, "Gohan Wish 2", can_wish_gohan)
GOHAN_WISH_3 = LocationData(150, "Gohan Wish 3", can_wish_gohan)
VEGETA_WISH_1 = LocationData(151, "Vegeta Wish 1", can_wish_vegeta)
VEGETA_WISH_2 = LocationData(152, "Vegeta Wish 2", can_wish_vegeta)
VEGETA_WISH_3 = LocationData(153, "Vegeta Wish 3", can_wish_vegeta)
KRILLIN_WISH_1 = LocationData(154, "Krillin Wish 1", can_wish_krillin)
KRILLIN_WISH_2 = LocationData(155, "Krillin Wish 2", can_wish_krillin)
KRILLIN_WISH_3 = LocationData(156, "Krillin Wish 3", can_wish_krillin)
PICCOLO_WISH_1 = LocationData(157, "Piccolo Wish 1", can_wish_piccolo)
PICCOLO_WISH_2 = LocationData(158, "Piccolo Wish 2", can_wish_piccolo)
PICCOLO_WISH_3 = LocationData(159, "Piccolo Wish 3", can_wish_piccolo)
TIEN_WISH_1 = LocationData(160, "Tien Wish 1", can_wish_tien)
TIEN_WISH_2 = LocationData(161, "Tien Wish 2", can_wish_tien)
TIEN_WISH_3 = LocationData(162, "Tien Wish 3", can_wish_tien)
YAMCHA_WISH_1 = LocationData(163, "Yamcha Wish 1", can_wish_yamcha)
YAMCHA_WISH_2 = LocationData(164, "Yamcha Wish 2", can_wish_yamcha)
YAMCHA_WISH_3 = LocationData(165, "Yamcha Wish 3", can_wish_yamcha)
UUB_WISH_1 = LocationData(166, "Uub Wish 1", can_wish_uub)
UUB_WISH_2 = LocationData(167, "Uub Wish 2", can_wish_uub)
UUB_WISH_3 = LocationData(168, "Uub Wish 3", can_wish_uub)
BROLY_WISH_1 = LocationData(169, "Broly Wish 1", can_wish_broly)
BROLY_WISH_2 = LocationData(170, "Broly Wish 2", can_wish_broly)
BROLY_WISH_3 = LocationData(171, "Broly Wish 3", can_wish_broly)

DU_WISHES = [
    GOKU_WISH_1, GOKU_WISH_2, GOKU_WISH_3, KGOHAN_WISH_1, KGOHAN_WISH_2, KGOHAN_WISH_3, TGOHAN_WISH_1, TGOHAN_WISH_2,
    TGOHAN_WISH_3, GOHAN_WISH_1, GOHAN_WISH_2, GOHAN_WISH_3, VEGETA_WISH_1, VEGETA_WISH_2, VEGETA_WISH_3, KRILLIN_WISH_1,
    KRILLIN_WISH_2, KRILLIN_WISH_3, PICCOLO_WISH_1, PICCOLO_WISH_2, PICCOLO_WISH_3, TIEN_WISH_1, TIEN_WISH_2, TIEN_WISH_3,
    YAMCHA_WISH_1, YAMCHA_WISH_2, YAMCHA_WISH_3, UUB_WISH_1, UUB_WISH_2, UUB_WISH_3, BROLY_WISH_1, BROLY_WISH_2,
    BROLY_WISH_3
]

## DU Static Capsules
GOKU_CAPSULE_1 = LocationData(172, "Goku: Starting Capsule", has_goku)
## from beginning
# Goku: Saiyan Saga: Capsule from Bulma at West City after Speaking with Chichi at Goku's House
# Goku: Saiyan Saga: (Gleaming) Capsule north of East City (S4)
# Goku: Saiyan Saga: Capsule after optional battle with Tien at World Tournament (S14)
# Goku: Saiyan Saga: 5-star Dragon Ball at ??? in Glacier (S4) 
# Goku: Saiyan Saga: 3-star Dragon Ball at ??? in ocean North of Kami's Lookout (S1)
# Goku: Saiyan Saga: Capsule at ??? south of Kami's Lookout (S9)
# Goku: Saiyan Saga: Capsule at Gleaming ??? North of Central City (S2)
# Goku: Saiyan Saga: Dragon Radar at Gleaming ??? Between Central and East City (S7)
# Goku: Saiyan Saga: Money at Gleaming ??? in NW Island (S1)
# Goku: Saiyan Saga: (Gleaming) Money in mountains north of West City (S6)
# Goku: Saiyan Saga: (Gleaming) Money in northern mountains (S2)
# Goku: Saiyan Saga: Capsule from Yamcha at North City
# Goku: Saiyan Saga: Capsule at Gleaming ??? on island north of West City 1 (S6) #Membership cards, ugh
# Goku: Saiyan Saga: Capsule at Gleaming ??? on island north of West City 2 (S6) #Membership cards, ugh
## After Raditz
# Goku 2: Saiyan Saga: Capsule from Kami at Kami's Lookout after Raditz (S5)
# Goku 2: Saiyan Saga: Capsule from Chichi at Goku's House after Raditz (S11)
## After Nappa
# Goku: Saiyan Saga: Capsule from Master Roshi at Kame House after Nappa (S12)
## Namek Saga Start
# Goku: Namek Saga: (Gleaming) Dragon Radar on island near Goku's Spaceship (S8)
# Goku: Namek Saga: Dragon Ball on island north of northeast continent (S4)
# Goku: Namek Saga: Dragon Ball in island chain southwest of northwest continent (S5)
# Goku: Namek Saga: (Gleaming) Capsule at spaceship on southeast continent (S11) # green: wishes category
# Goku: Android Saga: (Gleaming) Capsule east of West City (S6) # Dragon Fist; is this consistent?
# Goku: Android Saga: (Gleaming) Capsule near Goku's House (S12) # yellow
# Goku: Android Saga: Capsule at Kami's Lookout (visit twice) # green: armor (Goku) category
# Goku: Android Saga: Dragon Radar at West City (S6)
# Goku: Android Saga: (Gleaming) Money near South City (S14)
# Goku: Android Saga: (Gleaming) Capsule at houses south of Kami's Lookout (S9) # Viral Heart Disease?
# Goku: Android Saga: (Gleaming) Money at forest in northern mountains (S3)
# Goku: Buu Saga: (Gleaming) Money in forest northwest of Kami's Lookout (S5)
# Goku: Buu Saga: Capsule at Goku's House (S7), # random yellow
# Goku: Buu Saga: (Gleaming) Money on river near glacier (S4)
# Goku: Buu Saga: (Gleaming) Capsule in southwest desert (S9) # random red capsule
# Goku: Buu Saga: (Gleaming) Dragon Radar in northern mountains (S3)
# Goku: Buu Saga: Dragon Ball in northern mountains (S3)
# Goku: Buu Saga: Dragon ball on sandy island in southern island chain (S15)
# Goku: Buu Saga: (Gleaming) Capsule in mountains east of Hercule City (S8) 

GOKU_CAPSULE_2 = LocationData(173, "Goku: Saiyan Saga: Capsule at Plains Marker", can_goku) # Raditz
GOKU_CAPSULE_3 = LocationData(174, "Goku: Saiyan Saga: Capsule at Plains", can_goku) # After Nappa
GOKU_CAPSULE_4 = LocationData(175, "Goku: Saiyan Saga: Vegeta Reward", can_goku) # Vegeta
GOKU_CAPSULE_5 = LocationData(176, "Goku: Namek Saga: Capsule at Capsule House on southwest continent (S12)", can_goku) # Turle Shell; must visit twice
GOKU_CAPSULE_6 = LocationData(177, "Goku: Namek Saga: Recoome Reward 1", can_goku)
GOKU_CAPSULE_7 = LocationData(178, "Goku: Namek Saga: Recoome Reward 2", can_goku)
GOKU_CAPSULE_8 = LocationData(179, "Goku: Namek Saga: Ginyu Reward", can_goku) # Captain Ginyu
GOKU_CAPSULE_9 = LocationData(180, "Goku: Namek Saga: Capsule given before 100% Full Power Frieza Battle", can_goku) # Super Saiyan
GOKU_CAPSULE_10 = LocationData(181, "Goku: Namek Saga: 100% Full Power Frieza Reward", can_goku)
GOKU_CAPSULE_11 = LocationData(182, "Goku: Android Saga: Capsule at Plains near Cell Ring", can_goku) # Warp Kamehameha
GOKU_CAPSULE_12 = LocationData(183, "Goku: Android Saga: Capsule near Baba's House", can_goku)
GOKU_CAPSULE_13 = LocationData(184, "Goku: Android Saga: Perfect Form Cell Reward", can_goku) # Cell Ring
GOKU_CAPSULE_14 = LocationData(185, "Goku: Buu Saga: Capsule given in Saga Intro", can_goku) # Super Saiyan 2
GOKU_CAPSULE_15 = LocationData(186, "Goku: Buu Saga: Capsule at Forest near West City", can_goku) # Angel's Halo
GOKU_CAPSULE_16 = LocationData(187, "Goku: Buu Saga: Capsule at North City", can_goku) # Yakon
GOKU_CAPSULE_17 = LocationData(188, "Goku: Buu Saga: Capsule given before Majin Buu Battle in Sky", can_goku) # Super Saiyan 3
GOKU_CAPSULE_18 = LocationData(189, "Goku: Buu Saga: Majin Buu Reward", can_goku) # Majin Buu
GOKU_CAPSULE_19 = LocationData(190, "Goku: Buu Saga: Capsule given before Super Buu (Gohan) Battle at ??? Marker", can_goku)
GOKU_CAPSULE_20 = LocationData(191, "Goku: Buu Saga: Super Buu (Gohan) Reward", can_goku)
GOKU_CAPSULE_21 = LocationData(192, "Goku: Buu Saga: Super Buu Reward", can_goku)
GOKU_CAPSULE_22 = LocationData(193, "Goku: Buu Saga: Kid Buu Reward", can_goku)
GOKU_CAPSULE_23 = LocationData(194, "Goku: Extra Saga: Capsule at ??? in SE Islands", can_super_spirit_bomb)
GOKU_CAPSULE_24 = LocationData(195, "Goku: Extra Saga: Uub Reward", can_super_spirit_bomb)
GOKU_CAPSULE_25 = LocationData(196, "Goku 2: Saiyan Saga: Capsule at Saiyan's Spaceship near East City", can_wish_goku)
GOKU_CAPSULE_26 = LocationData(197, "Goku 2: Saiyan Saga: Capsule at Grandpa Gohan's House", can_wish_goku)
GOKU_CAPSULE_27 = LocationData(198, "Goku 2: Saiyan Saga: Capsule at Korin's Tower", can_wish_goku)
GOKU_CAPSULE_28 = LocationData(199, "Goku 2: Namek Saga: Capsule at ??? on Lone Central Island", can_wish_goku)
GOKU_CAPSULE_29 = LocationData(200, "Goku 2: Namek Saga: Capsule at Namek Village in Southwest Continent", can_wish_goku) # King-Kai's Wish
GOKU_CAPSULE_30 = LocationData(201, "Goku 2: Namek Saga: Capsule given at ??? Marker after Cooler Battle", can_wish_goku)
GOKU_CAPSULE_31 = LocationData(202, "Goku 2: Namek Saga: Cooler Reward (Cooler Battle after Vegeta Battle)", can_wish_goku_vegeta) # Cooler
GOKU_CAPSULE_32 = LocationData(203, "Goku 2: Buu Saga: Broly Reward", can_wish_goku)
GOKU_CAPSULE_33 = LocationData(204, "Goku 2: Extra Saga: Capsule given before Gotenks Battle at World Tournament", can_super_spirit_bomb)
GOKU_CAPSULE_34 = LocationData(205, "Goku 2: Extra Saga: Capsule given before Omega Shenron Battle at Central City", can_super_spirit_bomb)
GOKU_CAPSULE_35 = LocationData(206, "Goku 2: Extra Saga: Omega Shenron Reward", can_super_spirit_bomb)
# 
# Kid Gohan: Saiyan Saga: (Gleaming) Money on plains past bridge near Central City (S7)
# Kid Gohan: Saiyan Saga: (Gleaming) Money on large island near World Tournament Stage (S15)
# Kid Gohan 2: Saiyan Saga: (Gleaming) Money south of longer southwestern peninsula, in middle of ocean (S13)
# Kid Gohan 2: Saiyan Saga: (Gleaming) Money on southeastmost island (S16) 
# Kid Gohan 2: Saiyan Saga: (Gleaming) Money on glacier (S4)

# Kid Gohan: Saiyan Saga: Capsule at Mountains in southwest (S9) # Masenko
# Kid Gohan: Saiyan Saga: Capsule at Mountains spot in mountains near Goku's House 1 (S11)
# Kid Gohan: Saiyan Saga: Capsule at Mountains spot in mountains near Goku's House 2 (S11)
# Kid Gohan: Saiyan Saga: Capsule at West City after Piccolo Battle (S6)
# Kid Gohan: Saiyan Saga: Capsule at East City (S8)
# Kid Gohan: Namek Saga: Capsule at Planet Namek spot on southeastern continent after Recoome Battle (S15)
# Kid Gohan 2: Saiyan Saga: Capsule at Plains near Goku's House (S11) # Chi-Chi's Wish

# Kid Gohan: Saiyan Saga: (Gleaming) Dragon Radar on plains northeast of West City (S6)
# Kid Gohan: Namek Saga: (Gleaming) Dragon radar on southeast continent (S15)

KID_GOHAN_CAPSULE_1 = LocationData(207, "Kid Gohan: Saiyan Saga: Capsule at Mountains near Goku's House", has_kid_gohan)
KID_GOHAN_CAPSULE_2 = LocationData(208, "Kid Gohan: Namek Saga: Capsule at Guru's House", can_kid_gohan)
KID_GOHAN_CAPSULE_3 = LocationData(209, "Kid Gohan: Namek Saga: Recoome Reward", can_kid_gohan)
KID_GOHAN_CAPSULE_4 = LocationData(210, "Kid Gohan: Namek Saga: Capsule given upon Completion", can_kid_gohan)
KID_GOHAN_CAPSULE_5 = LocationData(211, "Kid Gohan 2: Saiyan Saga: Goku Reward", can_wish_kid_gohan)
KID_GOHAN_MONEY_1 = LocationData(607, "Kid Gohan: Saiyan Saga: (Gleaming) Money at glacier (S4)", has_kid_gohan)
TEEN_GOHAN_CAPSULE_1 = LocationData(212, "Teen Gohan: Starting Capsule", has_teen_gohan)
# Teen Gohan: Dragon Ball north of Central City (S3)
# Teen Gohan: Dragon Ball on northeast area of Glacier (S4)
# Teen Gohan: Dragon Ball on forested island east of West City (S6)
# Teen Gohan: (Gleaming) Money on plains northeast of West City (S6)
# Teen Gohan: Dragon Ball south of forested island near West City (S10)
# Teen Gohan: (Gleaming) Membership Cards on island west of North City (S2)
# Teen Gohan: Dragon Ball in southwest mountains
# Teen Gohan: (Gleaming) Dragon Radar in northeast section of main continent (S3)
# Teen Gohan: Dragon Ball south of South City (S14)
# Teen Gohan: Dragon Ball on island south of Goku's House (S11)
# Teen Gohan: Capsule at end of Bulma side-quest
# Teen Gohan: Capsule at event in northwest craggy island (S1)
# Teen Gohan: (Gleaming) Money on large island north of West City (S6)
# Teen Gohan: (Gleaming) Capsule on peninsula near Goku's House (S11)
# Teen Gohan: (Gleaming) Capsule in northeast section of main continent (S3)
## After Goku
# Teen Gohan: Capsule at West City after Battle with Goku (S6)
# Teen Gohan: Capsule at Kami's Lookout after Battle with Goku (S5)
# Teen Gohan: Capsule at Korin's Tower after Battle with Goku (S5)
# Teen Gohan: Capsule in desert near Baba's Palace after Battle with Goku (S13)
# Teen Gohan 2: Capsule in desert north of South City (S14)
# Teen Gohan 2: Capsule at South City (S14)
# Teen Gohan 2: Capsule at Time Machine (S1)
# Teen Gohan 2: (Ki Search) Capsule from Goku at end of Hide & Seek Side-Quest
## this one is complicated to explain, but it goes as follows:
## Meet Goku at Goku's House
## Find him again using Ki Search on an island north of Kami's Lookout
# Teen Gohan 2: Capsule from Chichi at Goku's house after Goku Battle
TEEN_GOHAN_CAPSULE_2 = LocationData(213, "Teen Gohan: Capsule at Central City", can_teen_gohan)
TEEN_GOHAN_CAPSULE_3 = LocationData(214, "Teen Gohan: Capsule at Kami's Lookout", can_teen_gohan)
TEEN_GOHAN_CAPSULE_4 = LocationData(215, "Teen Gohan: Capsule 1 at Cell Ring", can_teen_gohan)
TEEN_GOHAN_CAPSULE_5 = LocationData(216, "Teen Gohan: Capsule 2 at Cell Ring", can_teen_gohan)
TEEN_GOHAN_CAPSULE_6 = LocationData(217, "Teen Gohan: Defeat Super Perfect Cell with Father-Son Kamehameha", can_teen_gohan)
TEEN_GOHAN_CAPSULE_7 = LocationData(218, "Teen Gohan: Capsule given upon Completion", can_teen_gohan)
TEEN_GOHAN_CAPSULE_8 = LocationData(219, "Teen Gohan 2: Capsule at Goku's House", can_wish_teen_gohan)
GOHAN_CAPSULE_1 = LocationData(220, "Gohan: Starting Capsule 1", has_gohan)
GOHAN_CAPSULE_2 = LocationData(221, "Gohan: Starting Capsule 2", has_gohan)
# Gohan: (Gleaming) Money northeast of West City (S6)
# Gohan: Capsule from Bulma at West City (S6)
# Gohan: Dragon Ball at desert near Baba's Palace (S9)
# Gohan: Dragon Ball on island near World Tournament Stage (S15)
# Gohan: Dragon Ball on darker area of plains near Central City (S6)
# Gohan: (Gleaming) Money on forested island east of West City (S6)
# Gohan: Capsule at Hercule City (S8)
# Gohan: Dragon Ball in ocean south of glacier (S8)
# Gohan: Dragon Ball in forests north of Kami's Lookout (S1)
# Gohan: Dragon Ball in northern mountains (S3)
# Gohan: Dragon Radar east of Central City (S7)
# Gohan: Dragon Ball on beach near West City (S6)
# Gohan: Membership Cards in bay in southwest area of main continent (S13)
# Gohan: (Gleaming) Capsule in mountains near Goku's House (S11) # After Videl/Vegeta battle
# Gohan: Capsule on desert/mountains line near Goku's House (S11) # After Videl/Vegeta battle
# Gohan: (Gleaming) Capsule in desert near Goku's House (S11) # After Videl/Vegeta battle
## After meeting Vegeta and Battling Dabura:
# Gohan 2: Capsule in northwest continent (S1) # After Mahjin Vegeta battle
# Gohan 2: Capsule at Plains near Central City (S6) # After Majin Vegeta battle
# Gohan 2: (Gleaming) Capsule in mountains near Goku's House (S11) # After Majin Vegeta battle
GOHAN_CAPSULE_3 = LocationData(222, "Gohan: Capsule at Goku's House 1", can_gohan)
GOHAN_CAPSULE_4 = LocationData(223, "Gohan: Goten Reward", can_gohan)
GOHAN_CAPSULE_5 = LocationData(224, "Gohan: Capsule at End of Videl Side-quest", can_gohan)
GOHAN_CAPSULE_6 = LocationData(225, "Gohan: Capsule at Desert near Babidi's Spaceship", can_gohan)
GOHAN_CAPSULE_7 = LocationData(226, "Gohan: Capsule at Goku's House 2", can_gohan)
GOHAN_CAPSULE_8 = LocationData(227, "Gohan: Dabura Reward", can_gohan)
GOHAN_CAPSULE_9 = LocationData(228, "Gohan: Capsule given before Majin Buu Battle at Forest Marker", can_gohan)
GOHAN_CAPSULE_10 = LocationData(229, "Gohan: Capsule given after Majin Buu Battle", can_gohan)
GOHAN_CAPSULE_11 = LocationData(230, "Gohan: Capsule at ??? in Snowy Continent", can_gohan)
GOHAN_CAPSULE_12 = LocationData(231, "Gohan: Capsule given upon Completion", can_gohan)
GOHAN_CAPSULE_13 = LocationData(232, "Gohan 2: Capsule at Plains near Central City", can_wish_gohan)
GOHAN_CAPSULE_14 = LocationData(233, "Gohan 2: Capsule at Forest North of Kami's Lookout", can_wish_gohan)
VEGETA_CAPSULE_1 = LocationData(234, "Vegeta: Starting Capsule", has_vegeta)
# Vegeta: Saiyan Saga: (Gleaming) Money at East City after destroying it (S3)
# Vegeta: Saiyan Saga: (Gleaming) Money in southeast corner of map (S16)
# Vegeta: Saiyan Saga: Dragon Ball in forests north of Kami's Lookout (S5)
# Vegeta: Saiyan Saga: Dragon Radar at West City (S6)
# Vegeta: Saiyan Saga: (Gleaming) Money at northwest continent (S1)
# Vegeta: Saiyan Saga: Dragon Ball southeast of World Tournament Stage (S15)
# Vegeta: Saiyan Saga: (Gleaming) Capsule in mountains northeast of North City (S3)
# Vegeta: Saiyan Saga: (Gleaming) Membership cards in northeastern mountains (S3)
# Vegeta: Saiyan Saga: (Gleaming) Money on glacier (S4)
# Vegeta: Namek Saga: Dragon Ball at ruined village on southwest continent (S10)
# Vegeta: Namek Saga: Dragon Ball on the tip of the club-shaped chain of islands in southeast (S12)
# Vegeta: Namek Saga: (Gleaming) Capsule on northwest tip of northeast continent (S3)
# Vegeta: Namek Saga: (Gleaming) Dragon Radar on "club-shaped" section of islands in southeast (S12)
# Vegeta: Namek Saga: (Gleaming) Capsule on closest island southeast of southwest continent (S14)
# Vegeta: Android Saga: Capsule at Goku's House (S11)
# Vegeta: Android Saga: Dragon Ball in ocean south of South City (S14)
# Vegeta: Android Saga: (Gleaming) Capsule in lake near Central City (S7)
# Vegeta: Android Saga: (Gleaming) Dragon Radar northeast of West City (S6)
# Vegeta: Android Saga: (Gleaming) Money on island west of North City (S2)
# Vegeta: Android Saga: Capsule at Time Machine (S5) # might only be available after fighting Android 17 & 18
# Vegeta: Android Saga: Capsule at Plains on island near Kame House after Android 17 & 18 battles (S16) # Always Rit Armor?
# Vegeta: Android Saga: Capsule in Forest event near South City (S14) # After Imperfect Cell battle
# Vegeta: Buu Saga: Dragon Ball near Kami's Lookout (S5)
# Vegeta: Buu Saga: Dragon Ball on large island near Kame House (S16)
# Vegeta: Buu Saga: (Gleaming) Capsule in ocean east of Kame House (S12)
# Vegeta: Buu Saga: (Gleaming) Capsule in mountains near Goku's House (S11)
# Vegeta: Buu Saga: Capsule at end of recollections Side-Quest (S6) # before Majin Buu, visit Central City and the mountains near Goku's House. After that battle, visit West City.
VEGETA_CAPSULE_2 = LocationData(235, "Vegeta: Namek Saga: Capsule at Planet Namek in Northwest Continent (S6)", can_vegeta)
VEGETA_CAPSULE_3 = LocationData(236, "Vegeta: Namek Saga: Recoome Reward", can_vegeta)
VEGETA_CAPSULE_4 = LocationData(237, "Vegeta: Android Saga: Capsule given in Saga Intro 1", can_vegeta)
VEGETA_CAPSULE_5 = LocationData(238, "Vegeta: Android Saga: Capsule given in Saga Intro 2", can_vegeta)
VEGETA_CAPSULE_6 = LocationData(239, "Vegeta: Android Saga: Capsule at West City (S6)", can_vegeta)
VEGETA_CAPSULE_7 = LocationData(240, "Vegeta: Buu Saga: Capsule given in Saga Intro", can_vegeta)
VEGETA_CAPSULE_8 = LocationData(241, "Vegeta: Buu Saga: Capsule given before Super Saiyan 2 Goku Battle at Plains Marker", can_vegeta)
VEGETA_CAPSULE_9 = LocationData(242, "Vegeta: Buu Saga: Capsule given after Majin Buu Battle", can_vegeta) # Super Saiyan 2 (Vegeta)
VEGETA_CAPSULE_10 = LocationData(243, "Vegeta: Buu Saga: Capsule given before Super Buu (Gohan) Battle at Plains Marker", can_vegeta) # Potara <Vegito> (Vegeta)
VEGETA_CAPSULE_11 = LocationData(244, "Vegeta: Buu Saga: Super Buu Reward", can_vegeta) # Inside Buu
VEGETA_CAPSULE_12 = LocationData(245, "Vegeta: Buu Saga: Kid Buu Reward", can_vegeta) # Supreme Kai's World
VEGETA_CAPSULE_13 = LocationData(246, "Vegeta: Capsule given upon Completion", can_vegeta) # Trunks
VEGETA_CAPSULE_14 = LocationData(247, "Vegeta 2: Buu Saga: Broly Reward", can_wish_vegeta)
VEGETA_CAPSULE_15 = LocationData(248, "Vegeta 2: Extra Saga: Capsule given before Gotenks Battle at World Tournament Marker", can_wish_vegeta)
VEGETA_CAPSULE_16 = LocationData(249, "Vegeta 2: Extra Saga: Capsule at ??? Marker", can_wish_vegeta)
VEGETA_CAPSULE_17 = LocationData(250, "Vegeta 2: Extra Saga: Goku Reward", can_wish_vegeta)
KRILLIN_CAPSULE_1 = LocationData(251, "Krillin: Starting Capsule", can_krillin)
# Krillin: Saiyan Saga: (Gleaming) Money on glacier (S4)
# Krillin: Saiyan Saga: Dragon Ball at large island north of Kami's Lookout (S5)
# Krillin: Saiyan Saga: Dragon Radar at West City (S6)
# Krillin: Saiyan Saga: Membership cards on large island north of West City (S6)
# Krillin: Saiyan Saga: Dragon Ball northwest of West City (S6)
# Krillin: Saiyan Saga: (Gleaming) Money in ocean south of glacier (S8)
# Krillin: Saiyan Saga: (Gleaming) Money at ??? in central desert (S11)
# Krillin: Saiyan Saga: (Gleaming) Money at southern tip of main continent (S13)
# Krillin: Saiyan Saga: Dragon Ball in ocean east of World Tournament Stage (S15)
# Krillin: Namek Saga: Dragon Radar on northwest continent (S2)
# Krillin: Namek Saga: Dragon Ball on small island northwest of central continent (S3)
# Krillin: Namek Saga: Dragon Ball on large western island (S9)
# Krillin: Namek Saga: Dragon Ball on single large island of southeast continent (S12)
# Krillin: Namek Saga: Dragon Ball on small island southeast of southwest continent (S14)
# Krillin 2: Namek Saga: (Gleaming) Capsule near "neck" of central continent (S7)
# Krillin 2: Namek Saga: (Gleaming) Item at bottom of northeast continent (S8)
# Krillin 2: Android Saga: (Gleaming) Dragon Radar at mountains southwest of Goku's House (S11)
# Krillin 2: Android Saga: (Gleaming) Capsule on northern shore of main continent (S3)
# Krillin 2: Android Saga: (Gleaming) Money at desert near Baba's Palace (S13)
# Krillin 2: Android Saga: (Gleaming) Capsule near South City (S14)
# Krillin 2: Android Saga: Capsule at Muscle Tower (S4)
KRILLIN_CAPSULE_2 = LocationData(252, "Krillin: Saiyan Saga: Capsule at Mountains in Southwest", can_krillin)
KRILLIN_CAPSULE_3 = LocationData(253, "Krillin: Namek Saga: Capsule at Guru's House", can_krillin)
KRILLIN_CAPSULE_4 = LocationData(254, "Krillin: Namek Saga: Recoome Reward", can_krillin)
KRILLIN_CAPSULE_5 = LocationData(255, "Krillin: Namek Saga: Capsule given before Third Form Frieza Battle", can_krillin)
KRILLIN_CAPSULE_6 = LocationData(256, "Krillin: Capsule given upon Completion", can_krillin)
KRILLIN_CAPSULE_7 = LocationData(257, "Krillin 2: Android Saga: Capsule at South City", can_wish_krillin)
KRILLIN_CAPSULE_8 = LocationData(258, "Krillin 2: Android Saga: Capsule at West City at end of Android 16 Quest", can_wish_krillin)
PICCOLO_CAPSULE_1 = LocationData(259, "Piccolo: Starting Capsule", has_piccolo)
# Piccolo: Saiyan Saga: Dragon Ball at NW craggy continent (S1)
# Piccolo: Saiyan Saga: (Gleaming) Money at ??? spot east of craggy continent (S2)
# Piccolo: Saiyan Saga: Membership cards at large island northwest of Kami's Lookout (S5)
# Piccolo: Saiyan Saga: Capsule at Korin's Tower (S5)
# Piccolo: Saiyan Saga: Dragon Ball in desert north of Goku's House (S8)
# Piccolo: Saiyan Saga: Capsule at gleaming ??? spot on peninsula southwest of Kami's Lookout (S9)
# Piccolo: Saiyan Saga: (Gleaming) Money at ??? spot in eastern section of southwest mountains (S10)
# Piccolo: Saiyan Saga: (Gleaming) Money at ??? spot on large island southwest of Kame House (S15)
# Piccolo: Saiyan Saga: Dragon Radar at gleaming ??? spot in southwest desert (S13)
# Piccolo: Namek Saga: (Gleaming) Dragon Radar at eastern end of northwest continent (S2)
# Piccolo: Namek Saga: (Unmarked) Dragon Ball on northmost island of northeast continent (S4)
# Piccolo: Namek Saga: (Unmarked) Dragon Ball on southwest continent (S9)
# Piccolo: Namek Saga: (Gleaming) Item at western end of southeast continent (S11)
# Piccolo: Android Saga: (Gleaming) Capsule on plains northwest of West City (S5)
# Piccolo: Android Saga: Capsule at West City (S6)
# Piccolo: Android Saga: (Gleaming) Dragon Radar in desert east of Baba's Palace (S13)
# Piccolo: Android Saga: (Unmarked) Dragon Ball in sea southeast of West City (S6)
# Piccolo: Android Saga: (Gleaming) Capsule in mushroom patch near mountains west of Goku's House (S11)
# Piccolo: Android Saga: (Unmarked) Dragon Ball in mountains west of Goku's House (S11)
# Piccolo: Android Saga: (Unmarked) Capsule at end of Yajirobe Side-quest (S13)
# Piccolo: Android Saga: (Gleaming) Money on mountain road northeast of Central City (S7)
# Piccolo: Android Saga: (Gleaming) Capsule north of Goku's House (S8)
## After Sky Marker
# piccolo: Buu Saga: (Gleaming) Capsule southwest of Central City (S6)
# Piccolo: Buu Saga: (Unmarked) Capsule at Desert in southwest (S9)
# Piccolo: Buu Saga: (Gleaming) Dragon Radar in desert east of Baba's Palace (S13)
# Piccolo: Buu Saga: (Gleaming) Money at ??? spot near South City (S14)
# Piccolo: Buu Saga: (Unmarked) Dragon Ball on large island southwest of Kame House (S16)
# Piccolo: Buu Saga: (Gleaming) Capsule in mountains near Hercule City (S8)
# Piccolo 2: Buu Saga: (Unmarked) Capsule at Mountains marker at northwest craggy continent 
PICCOLO_CAPSULE_2 = LocationData(260, "Piccolo: Saiyan Saga: Capsule given before Raditz Battle at Plains Marker", can_piccolo)
PICCOLO_CAPSULE_3 = LocationData(261, "Piccolo: Saiyan Saga: (Gleaming) Capsule at Mountains in Northwest Continent", can_piccolo)
PICCOLO_CAPSULE_4 = LocationData(262, "Piccolo: Namek Saga: Capsule given in Saga Intro", can_piccolo)
PICCOLO_CAPSULE_6 = LocationData(264, "Piccolo: Namek Saga: Second Form Frieza Reward", can_piccolo)
PICCOLO_CAPSULE_7 = LocationData(265, "Piccolo: Android Saga: Capsule at Kami's Lookout", can_piccolo)
PICCOLO_CAPSULE_8 = LocationData(266, "Piccolo: Android Saga: Capsule given before Android 17 Battle at Kame House", can_piccolo)
PICCOLO_CAPSULE_9 = LocationData(267, "Piccolo: Android Saga: Android 17 Reward", can_piccolo)
PICCOLO_CAPSULE_10 = LocationData(268, "Piccolo: Buu Saga: Capsule at Central City at end of Hercule Quest", can_piccolo)
PICCOLO_CAPSULE_12 = LocationData(270, "Piccolo 2: Namek Saga: Capsule at Rightmost Red Marker after Second Form Frieza", can_wish_piccolo)
PICCOLO_CAPSULE_11 = LocationData(269, "Piccolo 2: Buu Saga: Capsule at Mountains in Northwest Continent", can_piccolo)
TIEN_CAPSULE_1 = LocationData(271, "Tien: Starting Capsule", has_tien)
TIEN_CAPSULE_2 = LocationData(272, "Tien: Saiyan Saga: Capsule at Plains near West City", can_tien)
# TIen: Saiyan Saga: Money at Gleaming ??? in NW Craggy Continent (S1)
# Tien: Saiyan Saga: Capsule at Gleaming ??? in northern mountains (S3) # membership cards
# Tien: Saiyan Saga: Money at Gleaming ??? NE of Glacier (S4)
# TIen: Saiyan Saga: 7-star Dragon Ball at ??? in ocean south of Glacier (S4)
# Tien: Saiyan Saga: 5-star Dragon Ball at ??? on peninsula near Kami's Lookout (S5)
# Tien: Saiyan Saga: Dragon Radar at West City (S6)
# Tien: Saiyan Saga: Money at Gleaming ??? in bay West of East City (S7)
# Tien: Saiyan Saga: Money at Gleaming ??? in Southern Continent (S14)
# Tien: Android Saga: 2-star Dragon Ball at ??? in ocean north of NW Craggy Continent (S1)
# Tien: Android Saga: Dragon Radar at Gleaming ??? northeast of Central City (S3)
# Tien: Android Saga: 3-star Dragon Ball at ??? on isolated island near Glacier (S4)
# Tien: Android Saga: Capsule at Gleaming ??? near Central City (S6)
# Tien: Android Saga: Capsule at Gleaming ??? near Goku's House (S12)
# Tien: Android Saga: Capsule at Kame House (S12)
# Tien: Android Saga: Money at Gleaming ??? near South City (S14)
# TIen: Android Saga: 6-star Dragon Ball at ??? south of Kame House (S16)
# Tien: Buu Saga: Capsule at Gleaming ??? spot in forest northwest of West City (S1)
# Tien: Buu Saga: 1-star Dragon Ball at ??? south of northern mountains (S2)
# Tien: Buu Saga: Dragon Radar at Gleaming ??? spot south of northern mountains (S3)
# Tien: Buu Saga: 4-star Dragon Ball at ??? spot in southwest mountains (S9)
# Tien: Buu Saga: Capsule at Kame House (S12)
TIEN_CAPSULE_3 = LocationData(273, "Tien: Saiyan Saga: Capsule after Saibaman Battle", can_tien)
TIEN_CAPSULE_4 = LocationData(274, "Tien: Android Saga: Capsule at Kami's Lookout", can_tien)
# Yamcha: Saiyan Saga: Money at Gleaming ??? spot in northwest craggy continent (S1)
# Yamcha: Saiyan Saga: Membership card capsules at gleaming ??? spot in borthen mountains (S3)
# Yamcha: Saiyan Saga: Dragon Ball at ??? on glacier (S4)
# Yamcha: Saiyan Saga: Money at Gleaming ??? spot in sea east of Kami's Lookout (S5)
# Yamcha: Saiyan Saga: Capsule at West City (S6)
# Yamcha: Saiyan Saga: Capsule at Gleaming Plains spot near West City (S6)
# Yamcha: Saiyan Saga: Dragon Ball at ??? in southwest mointains (S9)
# Yamcha: Saiyan Saga: Dragon Radar at Gleaming ??? near Goku's House (S12)
# Yamcha: Saiyan Saga: Money near southernmost tip of largest continent (S13)
# Yamcha: Android Saga: Dragon Ball south of northern mountains (S3)
# Yamcha: Android Saga: Capsule at gleaming ??? spot in northern mountains (S3)
# Yamcha: Android Saga: Capsule at gleaming ??? spot in forest north of Kami's Lookout (S5)
# Yamcha: Android Saga: Capsule at Gleaming ??? on Large Single Island North of West City (S6)
# Yamcha: Android Saga: Dragon Radar at gleaming ??? spot east of West City (S6)
# Yamcha: Android Saga: Money in Ocean East of Goku's House (S12)
# Yamcha: Buu Saga: Money at ??? spot on glacier (S4)
# Yamcha: Buu Saga: Dragon Radar at gleaming ??? spot east of West City (S6)
# Yamcha: Buu Saga: Dragon Ball at ??? spot northeast of West City (S6)
# Yamcha: Buu Saga: Dragon Ball at ??? spot in mountains near Hercule City (S8)
# Yamcha: Buu Saga: Capsule at gleaming ??? spot east of Goku's House (S12)
# Yamcha: Buu Saga: Money at gleaming ??? spot northeast of South City (S14)
# Yamcha: Buu Saga: Capsule at gleaming ??? spot on southern continent (S14)
# Yamcha: Buu Saga: Dragon Ball at ??? spot east of World Tournament Stage (S15)
YAMCHA_CAPSULE_1 = LocationData(275, "Yamcha: Starting Capsule", has_yamcha)
YAMCHA_CAPSULE_2 = LocationData(276, "Yamcha: Saiyan Saga: Capsule at End of Break-up Quest", can_yamcha)
YAMCHA_CAPSULE_3 = LocationData(277, "Yamcha: Saiyan Saga: Capsule at Plains Red Marker", can_yamcha)
YAMCHA_CAPSULE_4 = LocationData(278, "Yamcha: Android Saga: Dr Gero Reward", can_yamcha)
YAMCHA_CAPSULE_5 = LocationData(279, "Yamcha 2: Saiyan Saga: Capsule after Saibamen Battle", can_wish_yamcha)
UUB_CAPSULE_1 = LocationData(280, "Uub: Starting Capsule", has_uub)
BROLY_CAPSULE_1 = LocationData(281, "Broly: Starting Capsule", has_broly)

## Capsules
# Broly: (Gleaming) Capsule near northern mountains (S2) # broly armor?
# Broly: (Gleaming) Membership Cards on small island west of northern mountains (S2)
# Broly: (Gleaming) Capsule in northern mountains near glacier (S3) # desperation-type green capsule
# Broly: Capsule northwest of West City (S5) # random yellow capsule
# Broly: (Gleaming) Capsule on southern continent (S14) # random red capsule
# Broly 2: Capsule at Plains event along road northeast of Central City (S3) # God of Destruction's Arrogance
# Broly 2: Capsule at Plains on island near World Tournament Stage (S15)


## Money
# Broly: (Gleaming) Money on small peninsula southwest of Kami's Lookout (S9)

## Dragon Radar
# Broly: Dragon Radar southeast of Baba's Palace (S13)

## Dragon Balls
# Broly: Dragon Ball along river in northern mountains (S2)
# Broly: Dragon Ball along northern shore (S3)
# Broly: Dragon Ball along river in glacier (S4)
# Broly: Dragon Ball in bay north of Kami's Lookout (S5)
# Broly: Dragon Ball on forested island east of West City (S6)
# Broly: Dragon Ball in ocean northeast of Hercule City (S8)
# Broly: Dragon Ball in southwestern mountains (S10)
BROLY_CAPSULE_2 = LocationData(282, "Broly: Capsule at Grandpa Gohan's House (S12)", can_broly) # Always Gigantic Press?
BROLY_CAPSULE_3 = LocationData(283, "Broly: (Gleaming) Capsule in forests northeast of Kami's Lookout (S5)", can_broly) # Gigantic Press
BROLY_CAPSULE_4 = LocationData(284, "Broly: Capsule Given Before Gohan 1", can_broly) # Gigantic Meteor
BROLY_CAPSULE_5 = LocationData(285, "Broly: Capsule Given upon Completion", can_broly) # Kid Goku
BROLY_CAPSULE_6 = LocationData(286, "Broly 2: Capsule at Plains near Northern Mountains", can_wish_broly)
MENU_CAPSULE_1 = LocationData(287, "Clear all Dragon Universe Stories", has_cleared_story)

GOKU_CAPSULES = [
    GOKU_CAPSULE_1, GOKU_CAPSULE_2, GOKU_CAPSULE_3, GOKU_CAPSULE_4, GOKU_CAPSULE_5, GOKU_CAPSULE_6, GOKU_CAPSULE_7,
    GOKU_CAPSULE_8, GOKU_CAPSULE_9, GOKU_CAPSULE_10, GOKU_CAPSULE_11, GOKU_CAPSULE_12, GOKU_CAPSULE_13, GOKU_CAPSULE_14,
    GOKU_CAPSULE_15, GOKU_CAPSULE_16, GOKU_CAPSULE_17, GOKU_CAPSULE_18, GOKU_CAPSULE_19, GOKU_CAPSULE_20, GOKU_CAPSULE_21,
    GOKU_CAPSULE_22, GOKU_CAPSULE_23, GOKU_CAPSULE_24, GOKU_CAPSULE_25, GOKU_CAPSULE_26, GOKU_CAPSULE_27, GOKU_CAPSULE_28,
    GOKU_CAPSULE_29, GOKU_CAPSULE_30, GOKU_CAPSULE_31, GOKU_CAPSULE_32, GOKU_CAPSULE_33, GOKU_CAPSULE_34, GOKU_CAPSULE_35,
]

KGOHAN_CAPSULES = [
    KID_GOHAN_CAPSULE_1, KID_GOHAN_CAPSULE_2, KID_GOHAN_CAPSULE_3, KID_GOHAN_CAPSULE_4, KID_GOHAN_CAPSULE_5
]

TGOHAN_CAPSULES = [
    TEEN_GOHAN_CAPSULE_1, TEEN_GOHAN_CAPSULE_2, TEEN_GOHAN_CAPSULE_3, TEEN_GOHAN_CAPSULE_4, TEEN_GOHAN_CAPSULE_5,
    TEEN_GOHAN_CAPSULE_6, TEEN_GOHAN_CAPSULE_7, TEEN_GOHAN_CAPSULE_8
]

GOHAN_CAPSULES = [
    GOHAN_CAPSULE_1, GOHAN_CAPSULE_2, GOHAN_CAPSULE_3, GOHAN_CAPSULE_4, 
    GOHAN_CAPSULE_5, GOHAN_CAPSULE_6, GOHAN_CAPSULE_7, GOHAN_CAPSULE_8, 
    GOHAN_CAPSULE_9, GOHAN_CAPSULE_10, GOHAN_CAPSULE_11, GOHAN_CAPSULE_12, 
    GOHAN_CAPSULE_13, GOHAN_CAPSULE_14
]

VEGETA_CAPSULES = [
    VEGETA_CAPSULE_1, VEGETA_CAPSULE_2, VEGETA_CAPSULE_3, VEGETA_CAPSULE_4, 
    VEGETA_CAPSULE_5, VEGETA_CAPSULE_6, VEGETA_CAPSULE_7, VEGETA_CAPSULE_8,
    VEGETA_CAPSULE_9, VEGETA_CAPSULE_10, VEGETA_CAPSULE_11, VEGETA_CAPSULE_12, 
    VEGETA_CAPSULE_13, VEGETA_CAPSULE_14, VEGETA_CAPSULE_15, VEGETA_CAPSULE_16, 
    VEGETA_CAPSULE_17
]

KRILLIN_CAPSULES = [
    KRILLIN_CAPSULE_1, KRILLIN_CAPSULE_2, KRILLIN_CAPSULE_3, KRILLIN_CAPSULE_4, 
    KRILLIN_CAPSULE_5, KRILLIN_CAPSULE_6, KRILLIN_CAPSULE_7, KRILLIN_CAPSULE_8
]

PICCOLO_CAPSULES = [
    PICCOLO_CAPSULE_1, PICCOLO_CAPSULE_2, PICCOLO_CAPSULE_3, PICCOLO_CAPSULE_4, 
    PICCOLO_CAPSULE_6, PICCOLO_CAPSULE_7, PICCOLO_CAPSULE_8, 
    PICCOLO_CAPSULE_9, PICCOLO_CAPSULE_10, PICCOLO_CAPSULE_11, PICCOLO_CAPSULE_12
]

TIEN_CAPSULES = [
    TIEN_CAPSULE_1, TIEN_CAPSULE_2, TIEN_CAPSULE_3, TIEN_CAPSULE_4
]

YAMCHA_CAPSULES = [
    YAMCHA_CAPSULE_1, YAMCHA_CAPSULE_2, YAMCHA_CAPSULE_3, YAMCHA_CAPSULE_4, YAMCHA_CAPSULE_5
]

UUB_CAPSULES = [
    UUB_CAPSULE_1
]

BROLY_CAPSULES = [
    BROLY_CAPSULE_1, BROLY_CAPSULE_2, BROLY_CAPSULE_3, BROLY_CAPSULE_4, 
    BROLY_CAPSULE_5, BROLY_CAPSULE_6
]

DU_STATIC_CAPSULES = [
    *GOKU_CAPSULES, *KGOHAN_CAPSULES, *TGOHAN_CAPSULES, *GOHAN_CAPSULES, 
    *VEGETA_CAPSULES, *KRILLIN_CAPSULES, *PICCOLO_CAPSULES, *TIEN_CAPSULES, 
    *YAMCHA_CAPSULES, UUB_CAPSULE_1, *BROLY_CAPSULES
]

DRAGON_UNIVERSE_LOCS = [
    *DU_BOSSES, *DU_REENACTMENTS, *DU_DIFFICULTIES, *DU_WISHES, *DU_STATIC_CAPSULES
]

GOKU_LOCS = [
    *GOKU_BOSSES, *GOKU_CAPSULES, REENACTMENT_0, REENACTMENT_5, 
    REENACTMENT_13, REENACTMENT_16, REENACTMENT_18
]

GOKU_WISH_LOCS = [
    GOKU_WISH_1, GOKU_WISH_2, GOKU_WISH_3
]

KGOHAN_LOCS = [
    *KID_GOHAN_BOSSES, *KGOHAN_CAPSULES, REENACTMENT_3, KGOHAN_WISH_1,
    KGOHAN_WISH_2, KGOHAN_WISH_3
]

TGOHAN_LOCS = [

]

# Dragon Ball Locs
KID_GOHAN_DB1 = LocationData(600, "Kid Gohan: Saiyan Saga: Dragon Ball in northern mountains near North City (S3)", has_kid_gohan)
KID_GOHAN_DB2 = LocationData(601, "Kid Gohan: Saiyan Saga: Dragon Ball in forest north of Kami's Lookout (S5)", has_kid_gohan)
KID_GOHAN_DB3 = LocationData(602, "Kid Gohan: Saiyan Saga: Dragon Ball in desert south of Central City (S7)", has_kid_gohan)
KID_GOHAN_DB4 = LocationData(603, "Kid Gohan: Saiyan Saga: Dragon Ball in ocean southeast of World Tournament Stage (S15)", has_kid_gohan)
KID_GOHAN_DB5 = LocationData(604, "Kid Gohan: Namek Saga: Dragon Ball on island north of northeast continent (S4)", can_kid_gohan)
KID_GOHAN_DB6 = LocationData(605, "Kid Gohan: Namek Saga: Dragon Ball on large island east of northeast continent (S8)", can_kid_gohan)
KID_GOHAN_DB7 = LocationData(606, "Kid Gohan: Namek Saga: Dragon Ball on large western island (S9)", can_kid_gohan)

# Dragon Arena Checks
GOKU_BREAK_IN = LocationData(600, "Dragon Arena: Defeat Break-In Challenger: Goku", has_dragon_arena)
KRILLIN_BREAK_IN = LocationData(610, "Dragon Arena: Defeat Break-In Challenger: Krillin", has_dragon_arena)
PICCOLO_BREAK_IN = LocationData(611, "Dragon Arena: Defeat Break-In Challenger: Piccolo", has_dragon_arena)
YAMCHA_BREAK_IN = LocationData(613, "Dragon Arena: Defeat Break-In Challenger: Yamcha", has_dragon_arena)
NAPPA_BREAK_IN = LocationData(619, "Dragon Arena: Defeat Break-In Challenger: Nappa", has_dragon_arena)
FRIEZA_BREAK_IN = LocationData(622, "Dragon Arena: Defeat Break-In Challenger: Frieza", has_dragon_arena)
DR_GERO_BREAK_IN = LocationData(626, "Dragon Arena: Defeat Break-In Challenger: Dr Gero", has_dragon_arena)
CELL_BREAK_IN = LocationData(627, "Dragon Arena: Defeat Break-In Challenger: Cell", has_dragon_arena)
MAJIN_BUU_BREAK_IN = LocationData(628, "Dragon Arena: Defeat Break-In Challenger: Majin Buu", has_dragon_arena)
KID_BUU_BREAK_IN = LocationData(630, "Dragon Arena: Defeat Break-In Challenger: Kid Buu", has_dragon_arena)
DABURA_BREAK_IN = LocationData(631, "Dragon Arena: Defeat Break-In Challenger: Dabura", has_dragon_arena)
COOLER_BREAK_IN = LocationData(632, "Dragon Arena: Defeat Break-In Challenger: Cooler", has_dragon_arena)
BROLY_BREAK_IN = LocationData(634, "Dragon Arena: Defeat Break-In Challenger: Broly", has_dragon_arena)
OMEGA_BREAK_IN = LocationData(635, "Dragon Arena: Defeat Break-In Challenger: Omega", has_dragon_arena)
SAIBAMEN_BREAK_IN = LocationData(636, "Dragon Arena: Defeat Break-In Challenger: Saibamen", has_dragon_arena)

DA_BREAK_IN_LOCS = [
    GOKU_BREAK_IN, KRILLIN_BREAK_IN, PICCOLO_BREAK_IN, YAMCHA_BREAK_IN, NAPPA_BREAK_IN,
    FRIEZA_BREAK_IN, DR_GERO_BREAK_IN, CELL_BREAK_IN, MAJIN_BUU_BREAK_IN, KID_BUU_BREAK_IN, 
    DABURA_BREAK_IN, COOLER_BREAK_IN, BROLY_BREAK_IN, OMEGA_BREAK_IN, SAIBAMEN_BREAK_IN
]

DA_TEN_CHALLENGERS = LocationData(999, "Dragon Arena: Defeat 10 Challengers", has_dragon_arena)
DA_TWENTY_CHALLENGERS = LocationData(999, "Dragon Arena: Defeat 20 Challengers", has_dragon_arena)
DA_THIRTY_CHALLENGERS = LocationData(999, "Dragon Arena: Defeat 30 Challengers", has_dragon_arena)
DA_FOURTY_CHALLENGERS = LocationData(999, "Dragon Arena: Defeat 40 Challengers", has_dragon_arena)
DA_FIFTY_CHALLENGERS = LocationData(999, "Dragon Arena: Defeat 50 Challengers", has_dragon_arena)
DA_SIXTY_CHALLENGERS = LocationData(999, "Dragon Arena: Defeat 60 Challengers", has_dragon_arena)
DA_SEVENTY_CHALLENGERS = LocationData(999, "Dragon Arena: Defeat 70 Challengers", has_dragon_arena)
DA_EIGHTY_CHALLENGERS = LocationData(999, "Dragon Arena: Defeat 80 Challengers", has_dragon_arena)
DA_NINETY_CHALLENGERS = LocationData(999, "Dragon Arena: Defeat 90 Challengers", has_dragon_arena)
DA_HUNDRED_CHALLENGERS = LocationData(999, "Dragon Arena: Defeat 100 Challengers", has_dragon_arena)

DA_CHALLENGER_LOCS = [
    DA_TEN_CHALLENGERS, DA_TWENTY_CHALLENGERS, DA_THIRTY_CHALLENGERS, DA_FOURTY_CHALLENGERS,
    DA_FIFTY_CHALLENGERS, DA_SIXTY_CHALLENGERS, DA_SEVENTY_CHALLENGERS, 
    DA_EIGHTY_CHALLENGERS, DA_NINETY_CHALLENGERS, DA_HUNDRED_CHALLENGERS
]

DRAGON_ARENA_LOCS = [
    *DA_BREAK_IN_LOCS,
    *DA_CHALLENGER_LOCS
]

# Training Mode Checks
TRAINING_1_COMPLETED = LocationData(638, "Training: Complete Training 1", has_training_1)
TRAINING_2_COMPLETED = LocationData(639, "Training: Complete Training 2", has_training_2)
TRAINING_3_COMPLETED = LocationData(640, "Training: Complete Training 3", has_training_3)
TRAINING_4_COMPLETED = LocationData(641, "Training: Complete Training 4", has_training_4)
TRAINING_5_COMPLETED = LocationData(642, "Training: Complete Training 5", has_training_5)
TRAINING_6_COMPLETED = LocationData(643, "Training: Complete Training 6", has_training_6)
TRAINING_7_COMPLETED = LocationData(644, "Training: Complete Training 7", has_training_7)
TRAINING_8_COMPLETED = LocationData(645, "Training: Complete Training 8", has_training_8)
TRAINING_9_COMPLETED = LocationData(646, "Training: Complete Training 9", has_training_9)
TRAINING_10_COMPLETED = LocationData(647, "Training: Complete Training 10", has_training_10)
TRAINING_11_COMPLETED = LocationData(648, "Training: Complete Training 11", has_training_11)
TRAINING_12_COMPLETED = LocationData(649, "Training: Complete Training 12", has_training_12)

TRAINING_LOCS = [
    TRAINING_1_COMPLETED,TRAINING_2_COMPLETED,TRAINING_3_COMPLETED,TRAINING_4_COMPLETED, TRAINING_5_COMPLETED,
    TRAINING_6_COMPLETED,TRAINING_7_COMPLETED,TRAINING_8_COMPLETED,TRAINING_9_COMPLETED,TRAINING_10_COMPLETED,
    TRAINING_11_COMPLETED,TRAINING_12_COMPLETED
]

# World Tournament Checks
NOVICE_CLEARED = LocationData(650, "World Tournament: Novice Tournament Champion", has_tournament_novice)
ADEPT_CLEARED = LocationData(651, "World Tournament: Adept Tournament Champion", has_tournament_adept)
ADVANCED_CLEARED = LocationData(652, "World Tournament: Advanced Tournament Champion", has_tournament_advanced)
CELL_GAMES_CLEARED = LocationData(653, "World Tournament: Cell Games Champion", has_cell_games)

WT_LOCS = [
    NOVICE_CLEARED, ADEPT_CLEARED, ADVANCED_CLEARED, CELL_GAMES_CLEARED
]

SHOP_ITEM_ID_BASE = 700
shop_locs = []
x = 0
while x <= 99:
    shop_locs.append(LocationData(SHOP_ITEM_ID_BASE + x, f"Shop Item {x}", lambda state, player: True))
    x += 1
SHOP_LOCS = shop_locs

LOCATIONS = [
    *DRAGON_UNIVERSE_LOCS,
    *DRAGON_ARENA_LOCS,
    *TRAINING_LOCS,
    *WT_LOCS,
    *SHOP_LOCS,
    MENU_CAPSULE_1
]


def location_name_pairs() -> Dict[str, LocationData]:
    locations = {}
    for location in LOCATIONS:
        locations[location.name] = location
    return locations


def location_id_pairs() -> Dict[int, LocationData]:
    locations = {}
    for location in LOCATIONS:
        locations[location.location_id] = location
    return locations


LOC_NAME_PAIRS = location_name_pairs()
LOC_ID_PAIRS = location_id_pairs()


def location_name_to_id(name: str) -> int:
    return LOC_NAME_PAIRS[name].location_id


def location_id_to_name(id: int) -> str:
    return LOC_ID_PAIRS[id].name

def get_all_active_locations():
    return LOC_ID_PAIRS.keys()