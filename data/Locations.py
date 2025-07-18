from typing import NamedTuple, Optional, Callable, Dict
from BaseClasses import CollectionState
from ..Logic import *

class LocationData(NamedTuple):
    location_id: Optional[int]
    name: str
    access_rule: Optional[Callable[[CollectionState, int], bool]] = None
    is_shop: bool = False


# Dragon World Checks
## Goku
GOKU_RADITZ_CLEAR = LocationData(1, "Goku - Saiyan Saga - Defeat Raditz", can_goku)
GOKU_NAPPA_CLEAR = LocationData(2, "Goku - Saiyan Saga - Defeat Nappa", can_goku)
GOKU_VEGETA_1_CLEAR = LocationData(3, "Goku - Saiyan Saga - Defeat Vegeta", can_goku)
GOKU_RECOOME_CLEAR = LocationData(4, "Goku - Namek Saga - Defeat Recoome", can_goku)
GOKU_GINYU_CLEAR = LocationData(5, "Goku - Namek Saga - Defeat Ginyu", can_goku)
GOKU_FRIEZA_1_CLEAR = LocationData(6, "Goku - Namek Saga - Defeat Final Form Frieza", can_goku)
GOKU_FRIEZA_2_CLEAR = LocationData(7, "Goku - Namek Saga - Defeat 100% Final Form Frieza", can_goku)
GOKU_COOLER_CLEAR = LocationData(8, "Goku - Android Saga - Defeat Cooler", can_goku)
GOKU_CELL_CLEAR = LocationData(9, "Goku - Android Saga - Defeat Cell", can_goku)
GOKU_MAJIN_VEGETA_CLEAR = LocationData(10, "Goku - Buu Saga - Defeat Majin Vegeta", can_goku)
GOKU_MAJIN_BUU_CLEAR = LocationData(11, "Goku - Buu Saga - Defeat Majin Buu", can_goku)
GOKU_SUPER_BUU_1_CLEAR = LocationData(12, "Goku - Buu Saga - Defeat Super Buu (Gohan)", can_goku)
GOKU_SUPER_BUU_2_CLEAR = LocationData(13, "Goku - Buu Saga - Defeat Super Buu", can_goku)
GOKU_KID_BUU_CLEAR = LocationData(14, "Goku - Buu Saga - Defeat Kid Buu", can_goku)
GOKU_UUB_CLEAR = LocationData(15, "Goku - Extra Saga - Defeat Uub", can_super_spirit_bomb) # Must have defeated Kid Buu with a
                                                                                     # successful Super Spirit Bomb
GOKU_COOLER_2_CLEAR = LocationData(16, "Goku 2 - Namek Saga - Defeat Cooler", can_wish_goku)
GOKU_METAL_COOLER_CLEAR = LocationData(17, "Goku 2 - Namek Saga - Defeat Metal Cooler", can_wish_goku)
GOKU_VEGETA_2_CLEAR = LocationData(18, "Goku 2 - Namek Saga - Defeat Super Saiyan Vegeta", can_wish_goku_vegeta)
GOKU_COOLER_3_CLEAR = LocationData(19, "Goku 2 - Namek Saga - Defeat Cooler after Vegeta", can_wish_goku_vegeta)
GOKU_BROLY_CLEAR = LocationData(20, "Goku 2 - Buu Saga - Defeat Broly", can_wish_goku)
GOKU_GOTENKS_CLEAR = LocationData(21, "Goku 2 - Extra Saga - Defeat Gotenks", can_wish_and_spirit_bomb)
GOKU_OMEGA_CLEAR = LocationData(22, "Goku 2 - Extra Saga - Defeat Omega Shenron", can_wish_and_spirit_bomb)

GOKU_BOSSES = [
    GOKU_RADITZ_CLEAR, GOKU_NAPPA_CLEAR, GOKU_VEGETA_1_CLEAR, GOKU_RECOOME_CLEAR, GOKU_GINYU_CLEAR, GOKU_FRIEZA_1_CLEAR,
    GOKU_FRIEZA_2_CLEAR, GOKU_COOLER_CLEAR, GOKU_CELL_CLEAR, GOKU_MAJIN_VEGETA_CLEAR, GOKU_MAJIN_BUU_CLEAR,
    GOKU_SUPER_BUU_1_CLEAR, GOKU_SUPER_BUU_2_CLEAR, GOKU_KID_BUU_CLEAR, GOKU_UUB_CLEAR, GOKU_COOLER_2_CLEAR,
    GOKU_METAL_COOLER_CLEAR, GOKU_VEGETA_2_CLEAR, GOKU_COOLER_3_CLEAR, GOKU_BROLY_CLEAR, GOKU_GOTENKS_CLEAR,
    GOKU_OMEGA_CLEAR
]

## Kid Gohan
KGOHAN_PICCOLO_CLEAR = LocationData(23, "Kid Gohan - Saiyan Saga - Defeat Piccolo", can_kid_gohan)
KGOHAN_SAIBAMEN_CLEAR = LocationData(24, "Kid Gohan - Saiyan Saga - Defeat Saibamen", can_kid_gohan)
KGOHAN_NAPPA_CLEAR = LocationData(25, "Kid Gohan - Saiyan Saga - Defeat Nappa", can_kid_gohan)
KGOHAN_RECOOME_CLEAR = LocationData(26, "Kid Gohan - Namek Saga - Defeat Recoome", can_kid_gohan)
KGOHAN_FRIEZA_CLEAR = LocationData(27, "Kid Gohan - Namek Saga - Defeat Third Form Frieza", can_kid_gohan)
KGOHAN_GOKU_CLEAR = LocationData(28, "Kid Gohan 2 - Saiyan Saga - Defeat Goku", can_wish_kid_gohan)
KGOHAN_GINYU_GOKU_CLEAR = LocationData(29, "Kid Gohan 2 - Namek Saga - Defeat Goku w/ Scouter", can_wish_kid_gohan)
KGOHAN_COOLER_CLEAR = LocationData(30, "Kid Gohan 2 - Namek Saga - Defeat Cooler", can_wish_kid_gohan)

KID_GOHAN_BOSSES = [
    KGOHAN_PICCOLO_CLEAR, KGOHAN_SAIBAMEN_CLEAR, KGOHAN_NAPPA_CLEAR, KGOHAN_RECOOME_CLEAR,KGOHAN_FRIEZA_CLEAR,
    KGOHAN_GOKU_CLEAR, KGOHAN_GINYU_GOKU_CLEAR, KGOHAN_COOLER_CLEAR
]

## Teen Gohan
TGOHAN_PICCOLO_CLEAR = LocationData(31, "Teen Gohan - Defeat Piccolo", can_teen_gohan)
TGOHAN_KRILLIN_CLEAR = LocationData(32, "Teen Gohan - Defeat Krillin", can_teen_gohan)
TGOHAN_GOKU_CLEAR = LocationData(33, "Teen Gohan - Defeat Super Saiyan Goku", can_teen_gohan)
TGOHAN_CELL_1_CLEAR = LocationData(34, "Teen Gohan - Defeat Perfect Cell", can_teen_gohan)
TGOHAN_CELL_2_CLEAR = LocationData(35, "Teen Gohan - Defeat Super Perfect Cell", can_teen_gohan)
TGOHAN_TIEN_CLEAR = LocationData(36, "Teen Gohan 2 - Defeat Tien", can_wish_teen_gohan)
TGOHAN_YAMCHA_CLEAR = LocationData(37, "Teen Gohan 2 - Defeat Yamcha", can_wish_teen_gohan)

TEEN_GOHAN_BOSSES = [
    TGOHAN_PICCOLO_CLEAR, TGOHAN_KRILLIN_CLEAR, TGOHAN_GOKU_CLEAR, TGOHAN_CELL_1_CLEAR, TGOHAN_CELL_2_CLEAR,
    TGOHAN_TIEN_CLEAR, TGOHAN_YAMCHA_CLEAR
]

## Gohan
GOHAN_GOTEN_CLEAR = LocationData(38, "Gohan - Defeat Goten", can_gohan)
GOHAN_VIDEL_CLEAR = LocationData(39, "Gohan - Defeat Videl", can_gohan)
GOHAN_PICCOLO_CLEAR = LocationData(40, "Gohan - Defeat Piccolo", can_gohan)
GOHAN_DABURA_CLEAR = LocationData(41, "Gohan - Defeat Dabura", can_gohan)
GOHAN_MAJIN_BUU_CLEAR = LocationData(42, "Gohan - Defeat Majin Buu", can_gohan)
GOHAN_VEGETA_CLEAR = LocationData(43, "Gohan 2 - Defeat Vegeta", can_wish_gohan)
GOHAN_MAJIN_VEGETA_CLEAR = LocationData(44, "Gohan 2 - Defeat Majin Vegeta", can_wish_gohan)
GOHAN_KID_BUU_CLEAR = LocationData(45, "Gohan 2 - Defeat Kid Buu", can_wish_gohan)
GOHAN_BROLY_CLEAR = LocationData(46, "Gohan 2 - Defeat Broly", can_wish_gohan)

GOHAN_BOSSES = [
    GOHAN_GOTEN_CLEAR, GOHAN_VIDEL_CLEAR, GOHAN_PICCOLO_CLEAR, GOHAN_DABURA_CLEAR, GOHAN_MAJIN_BUU_CLEAR,
    GOHAN_VEGETA_CLEAR, GOHAN_MAJIN_VEGETA_CLEAR, GOHAN_KID_BUU_CLEAR, GOHAN_BROLY_CLEAR
]

## Vegeta
VEGETA_GOKU_1_CLEAR = LocationData(47, "Vegeta - Saiyan Saga - Defeat Goku", can_vegeta)
VEGETA_KID_GOHAN_CLEAR = LocationData(48, "Vegeta - Saiyan Saga - Defeat Kid Gohan", can_vegeta)
VEGETA_RECOOME_CLEAR = LocationData(49, "Vegeta - Namek Saga - Defeat Recoome", can_vegeta)
VEGETA_FRIEZA_1_CLEAR = LocationData(50, "Vegeta - Namek Saga - Defeat First Form Frieza", can_vegeta)
VEGETA_FRIEZA_2_CLEAR = LocationData(51, "Vegeta - Namek Saga - Defeat Final Form Frieza", can_vegeta)
VEGETA_ANDROID_17_CLEAR = LocationData(52, "Vegeta - Android Saga - Defeat Android 17", can_vegeta)
VEGETA_ANDROID_18_CLEAR = LocationData(53, "Vegeta - Android Saga - Defeat Android 18", can_vegeta)
VEGETA_CELL_1_CLEAR = LocationData(54, "Vegeta - Android Saga - Defeat Cell (17 Absorbed)", can_vegeta)
VEGETA_CELL_2_CLEAR = LocationData(55, "Vegeta - Android Saga - Defeat Perfect Cell", can_vegeta)
VEGETA_GOKU_2_CLEAR = LocationData(56, "Vegeta - Buu Saga - Defeat Super Saiyan 2 Goku", can_vegeta)
VEGETA_MAJIN_BUU_CLEAR = LocationData(57, "Vegeta - Buu Saga - Defeat Majin Buu", can_vegeta)
VEGETA_SUPER_BUU_1_CLEAR = LocationData(58, "Vegeta - Buu Saga - Defeat Super Buu (Gohan)", can_vegeta)
VEGETA_SUPER_BUU_2_CLEAR = LocationData(59, "Vegeta - Buu Saga - Defeat Super Buu", can_vegeta)
VEGETA_KID_BUU_CLEAR = LocationData(60, "Vegeta - Buu Saga - Defeat Kid Buu", can_vegeta)
VEGETA_METAL_COOLER_CLEAR = LocationData(61, "Vegeta 2 - Namek Saga - Defeat Metal Cooler", can_wish_vegeta)
VEGETA_BROLY_CLEAR = LocationData(62, "Vegeta 2 - Buu Saga - Defeat Broly", can_wish_vegeta)
VEGETA_GOTENKS_CLEAR = LocationData(63, "Vegeta 2 - Extra Saga - Defeat Gotenks", can_wish_vegeta)
VEGETA_GOKU_3_CLEAR = LocationData(64, "Vegeta 2 - Extra Saga - Defeat Super Saiyan 4 Goku", can_wish_vegeta)

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
KRILLIN_GINYU_GOKU_CLEAR = LocationData(68, "Krillin - Namek Saga - Defeat Goku w/ Scouter", can_krillin)
KRILLIN_FRIEZA_1_CLEAR = LocationData(69, "Krillin - Namek Saga - Defeat Second Form Frieza", can_krillin)
KRILLIN_FRIEZA_2_CLEAR = LocationData(70, "Krillin - Namek Saga - Defeat Final Form Frieza", can_krillin)
KRILLIN_CELL_CLEAR = LocationData(71, "Krillin 2 - Android Saga - Defeat Perfect Form Cell", can_wish_krillin)

KRILLIN_BOSSES = [
    KRILLIN_SAIBAMEN_CLEAR, KRILLIN_NAPPA_CLEAR, KRILLIN_RECOOME_CLEAR, KRILLIN_GINYU_GOKU_CLEAR, KRILLIN_FRIEZA_1_CLEAR,
    KRILLIN_FRIEZA_2_CLEAR, KRILLIN_CELL_CLEAR
]

## Piccolo
PICCOLO_RADITZ_CLEAR = LocationData(72, "Piccolo - Saiyan Saga - Defeat Raditz", can_piccolo)
PICCOLO_KID_GOHAN_CLEAR = LocationData(73, "Piccolo - Saiyan Saga - Defeat Kid Gohan", can_piccolo)
PICCOLO_SAIBAMEN_CLEAR = LocationData(74, "Piccolo - Saiyan Saga - Defeat Saibamen", can_piccolo)
PICCOLO_NAPPA_CLEAR = LocationData(75, "Piccolo - Saiyan Saga - Defeat Nappa", can_piccolo)
PICCOLO_FRIEZA_1_CLEAR = LocationData(76, "Piccolo - Namek Saga - Defeat Second Form Frieza", can_piccolo)
PICCOLO_FRIEZA_2_CLEAR = LocationData(77, "Piccolo - Namek Saga - Defeat Third Form Frieza", can_piccolo)
PICCOLO_DR_GERO_CLEAR = LocationData(78, "Piccolo - Android Saga - Defeat Dr Gero", can_piccolo)
PICCOLO_CELL_1_CLEAR = LocationData(79, "Piccolo - Android Saga - Defeat Cell", can_piccolo)
PICCOLO_ANDROID_17_CLEAR = LocationData(80, "Piccolo - Android Saga - Defeat Android 17", can_piccolo)
PICCOLO_SUPER_BUU_CLEAR = LocationData(81, "Piccolo - Buu Saga - Defeat Super Buu", can_piccolo)
PICCOLO_GOKU_CLEAR = LocationData(82, "Piccolo 2 - Saiyan Saga - Defeat Goku", can_wish_piccolo)
PICCOLO_VEGETA_CLEAR = LocationData(83, "Piccolo 2 - Saiyan Saga - Defeat Vegeta", can_wish_piccolo)
PICCOLO_COOLER_CLEAR = LocationData(84, "Piccolo 2 - Namek Saga - Defeat Cooler", can_wish_piccolo)
PICCOLO_METAL_COOLER_CLEAR = LocationData(85, "Piccolo 2 - Namek Saga - Defeat Metal Cooler", can_wish_piccolo)
PICCOLO_FRIEZA_3_CLEAR = LocationData(86, "Piccolo 2 - Namek Saga - Defeat Final Form Frieza", can_wish_piccolo)
PICCOLO_CELL_2_CLEAR = LocationData(87, "Piccolo 2 - Android Saga - Defeat Perfect Cell", can_wish_piccolo)
PICCOLO_DABURA_CLEAR = LocationData(88, "Piccolo 2 - Buu Saga - Defeat Dabura", can_wish_piccolo)
PICCOLO_BROLY_CLEAR = LocationData(89, "Piccolo 2 - Buu Saga - Defeat Broly", can_wish_piccolo)

PICCOLO_BOSSES = [
    PICCOLO_RADITZ_CLEAR, PICCOLO_KID_GOHAN_CLEAR, PICCOLO_SAIBAMEN_CLEAR, PICCOLO_NAPPA_CLEAR, PICCOLO_FRIEZA_1_CLEAR,
    PICCOLO_FRIEZA_2_CLEAR, PICCOLO_DR_GERO_CLEAR, PICCOLO_CELL_1_CLEAR, PICCOLO_ANDROID_17_CLEAR, PICCOLO_SUPER_BUU_CLEAR,
    PICCOLO_GOKU_CLEAR, PICCOLO_VEGETA_CLEAR, PICCOLO_COOLER_CLEAR, PICCOLO_METAL_COOLER_CLEAR, PICCOLO_FRIEZA_3_CLEAR,
    PICCOLO_CELL_2_CLEAR, PICCOLO_DABURA_CLEAR, PICCOLO_BROLY_CLEAR
]

## Tien
TIEN_SAIBAMEN_CLEAR = LocationData(90, "Tien - Saiyan Saga - Defeat Saibamen", can_tien)
TIEN_NAPPA_CLEAR = LocationData(91, "Tien - Saiyan Saga - Defeat Nappa", can_tien)
TIEN_CELL_CLEAR = LocationData(92, "Tien - Android Saga - Defeat Second Form Cell", can_tien)
TIEN_CELL_JR_CLEAR = LocationData(93, "Tien - Android Saga - Defeat Cell Jr", can_tien)
TIEN_SUPER_BUU_CLEAR = LocationData(94, "Tien - Buu Saga - Defeat Super Buu (Gotenks)", can_tien)
TIEN_YAMCHA_CLEAR = LocationData(95, "Tien 2 - Extra Saga - Defeat Yamcha", can_wish_tien)

TIEN_BOSSES = [
    TIEN_SAIBAMEN_CLEAR, TIEN_NAPPA_CLEAR, TIEN_CELL_CLEAR, TIEN_CELL_JR_CLEAR, TIEN_SUPER_BUU_CLEAR, TIEN_YAMCHA_CLEAR
]

## Yamcha
YAMCHA_SAIBAMEN_CLEAR = LocationData(96, "Yamcha - Saiyan Saga - Defeat Saibamen", can_yamcha)
YAMCHA_DR_GERO_CLEAR = LocationData(97, "Yamcha - Android Saga - Defeat Dr Gero", can_yamcha)
YAMCHA_TIEN_CLEAR = LocationData(98, "Yamcha - Extra Saga - Defeat Tien", can_yamcha)
YAMCHA_VEGETA_CLEAR = LocationData(99, "Yamcha 2 - Extra Saga - Defeat Vegeta", can_wish_yamcha)

YAMCHA_BOSSES = [
    YAMCHA_SAIBAMEN_CLEAR, YAMCHA_DR_GERO_CLEAR, YAMCHA_TIEN_CLEAR, YAMCHA_VEGETA_CLEAR
]

## Uub
UUB_GOKU_1_CLEAR = LocationData(100, "Uub - Defeat Goku at World Tournament", can_uub)
UUB_VEGETA_CLEAR = LocationData(101, "Uub - Defeat Vegeta", can_uub)
UUB_MAJIN_BUU_CLEAR = LocationData(102, "Uub - Defeat Majin Buu", can_uub)
UUB_GOKU_2_CLEAR = LocationData(103, "Uub - Defeat Goku at Archipelago", can_uub)
UUB_OMEGA_SHENRON_CLEAR = LocationData(104, "Uub - Defeat Omega Shenron", can_uub)

UUB_BOSSES = [
    UUB_GOKU_1_CLEAR, UUB_VEGETA_CLEAR, UUB_MAJIN_BUU_CLEAR, UUB_GOKU_2_CLEAR, UUB_OMEGA_SHENRON_CLEAR
]

## Broly
BROLY_KRILLIN_CLEAR = LocationData(105, "Broly - Defeat Krillin", can_broly)
BROLY_PICCOLO_CLEAR = LocationData(106, "Broly - Defeat Piccolo", can_broly)
BROLY_VEGETA_CLEAR = LocationData(107, "Broly - Defeat Vegeta", can_broly)
BROLY_VIDEL_CLEAR = LocationData(108, "Broly - Defeat Videl", can_broly)
BROLY_KID_TRUNKS_CLEAR = LocationData(109, "Broly - Defeat Kid Trunks", can_broly)
BROLY_GOTEN_CLEAR = LocationData(110, "Broly - Defeat Goten", can_broly)
BROLY_GOHAN_1_CLEAR = LocationData(111, "Broly - Defeat Gohan 1", can_broly)
BROLY_GOHAN_2_CLEAR = LocationData(112, "Broly - Defeat Gohan 2", can_broly)
BROLY_GOKU_CLEAR = LocationData(113, "Broly 2 - Defeat Goku", can_wish_broly)

BROLY_BOSSES = [
    BROLY_KRILLIN_CLEAR, BROLY_PICCOLO_CLEAR, BROLY_VEGETA_CLEAR, BROLY_VIDEL_CLEAR, BROLY_KID_TRUNKS_CLEAR,
    BROLY_GOTEN_CLEAR, BROLY_GOHAN_1_CLEAR, BROLY_GOHAN_1_CLEAR, BROLY_GOHAN_2_CLEAR, BROLY_GOHAN_2_CLEAR
]

DW_BOSSES = [
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
REENACTMENT_12 = LocationData(126, "Vegeta: Defeat Majin Buu with Perfect Explosion", can_complete_reenactment_12)
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

DW_REENACTMENTS = [
    REENACTMENT_0, REENACTMENT_1, REENACTMENT_2, REENACTMENT_3, REENACTMENT_4, REENACTMENT_5, REENACTMENT_6, REENACTMENT_7,
    REENACTMENT_8, REENACTMENT_9, REENACTMENT_10, REENACTMENT_11, REENACTMENT_12, REENACTMENT_13, REENACTMENT_14,
    REENACTMENT_15, REENACTMENT_16, REENACTMENT_17, REENACTMENT_18, REENACTMENT_19, REENACTMENT_20
]

## Difficulty-related
VERY_HARD_CLEAR = LocationData(135, "Clear DW on Very Hard")
Z1_CLEAR = LocationData(136, "Clear DW on Z1", has_z_hard)
Z2_CLEAR = LocationData(137, "Clear DW on Z2", has_z_hard)
Z3_CLEAR = LocationData(138, "Clear DW on Z3", has_z_hard_3)

DW_DIFFICULTIES = [VERY_HARD_CLEAR, Z1_CLEAR, Z2_CLEAR, Z3_CLEAR]

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

DW_WISHES = [
    GOKU_WISH_1, GOKU_WISH_2, GOKU_WISH_3, KGOHAN_WISH_1, KGOHAN_WISH_2, KGOHAN_WISH_3, TGOHAN_WISH_1, TGOHAN_WISH_2,
    TGOHAN_WISH_3, GOHAN_WISH_1, GOHAN_WISH_2, GOHAN_WISH_3, VEGETA_WISH_1, VEGETA_WISH_2, VEGETA_WISH_3, KRILLIN_WISH_1,
    KRILLIN_WISH_2, KRILLIN_WISH_3, PICCOLO_WISH_1, PICCOLO_WISH_2, PICCOLO_WISH_3, TIEN_WISH_1, TIEN_WISH_2, TIEN_WISH_3,
    YAMCHA_WISH_1, YAMCHA_WISH_2, YAMCHA_WISH_3, UUB_WISH_1, UUB_WISH_2, UUB_WISH_3, BROLY_WISH_1, BROLY_WISH_2,
    BROLY_WISH_3
]

## DW Static Capsules
GOKU_CAPSULE_1 = LocationData(172, "Goku - Saiyan Saga - Starting Capsule", has_goku)
GOKU_CAPSULE_2 = LocationData(173, "Goku - Saiyan Saga - Capsule at Plains Marker", can_goku)
GOKU_CAPSULE_3 = LocationData(174, "Goku - Saiyan Saga - Capsule at Plains", can_goku)
GOKU_CAPSULE_4 = LocationData(175, "Goku - Saiyan Saga - Vegeta Reward", can_goku)
GOKU_CAPSULE_5 = LocationData(176, "Goku - Namek Saga - Capsule at Capsule House", can_goku)
GOKU_CAPSULE_6 = LocationData(177, "Goku - Namek Saga - Recoome Reward 1", can_goku)
GOKU_CAPSULE_7 = LocationData(178, "Goku - Namek Saga - Recoome Reward 2", can_goku)
GOKU_CAPSULE_8 = LocationData(179, "Goku - Namek Saga - Ginyu Reward", can_goku)
GOKU_CAPSULE_9 = LocationData(180, "Goku - Namek Saga - Capsule given before 100% Final Power Frieza Battle", can_goku)
GOKU_CAPSULE_10 = LocationData(181, "Goku - Namek Saga - 100% Full Power Frieza Reward", can_goku)
GOKU_CAPSULE_11 = LocationData(182, "Goku - Android Saga - Capsule at Plains near Cell Ring", can_goku)
GOKU_CAPSULE_12 = LocationData(183, "Goku - Android Saga - Capsule near Baba's House", can_goku)
GOKU_CAPSULE_13 = LocationData(184, "Goku - Android Saga - Perfect Form Cell Reward", can_goku)
GOKU_CAPSULE_14 = LocationData(185, "Goku - Buu Saga - Capsule given in Saga Intro", can_goku)
GOKU_CAPSULE_15 = LocationData(186, "Goku - Buu Saga - Capsule at Forest near West City", can_goku)
GOKU_CAPSULE_16 = LocationData(187, "Goku - Buu Saga - Capsule at North City", can_goku)
GOKU_CAPSULE_17 = LocationData(188, "Goku - Buu Saga - Capsule given before Majin Buu Battle", can_goku)
GOKU_CAPSULE_18 = LocationData(189, "Goku - Buu Saga - Majin Buu Reward", can_goku)
GOKU_CAPSULE_19 = LocationData(190, "Goku - Buu Saga - Capsule given before Super Buu (Gohan) Battle at ??? Marker", can_goku)
GOKU_CAPSULE_20 = LocationData(191, "Goku - Buu Saga - Super Buu (Gohan) Reward", can_goku)
GOKU_CAPSULE_21 = LocationData(192, "Goku - Buu Saga - Super Buu Reward", can_goku)
GOKU_CAPSULE_22 = LocationData(193, "Goku - Buu Saga - Kid Buu Reward", can_goku)
GOKU_CAPSULE_23 = LocationData(194, "Goku - Extra Saga - Capsule at ??? in SE Islands", can_super_spirit_bomb)
GOKU_CAPSULE_24 = LocationData(195, "Goku - Extra Saga - Uub Reward", can_super_spirit_bomb)
GOKU_CAPSULE_25 = LocationData(196, "Goku 2 - Saiyan Saga - Capsule at Saiyan's Spaceship near East City", can_wish_goku)
GOKU_CAPSULE_26 = LocationData(197, "Goku 2 - Saiyan Saga - Capsule at Grandpa Gohan's House", can_wish_goku)
GOKU_CAPSULE_27 = LocationData(198, "Goku 2 - Saiyan Saga - Capsule at Korin's Tower", can_wish_goku)
GOKU_CAPSULE_28 = LocationData(199, "Goku 2 - Namek Saga - Capsule at ??? on Lone Central Island", can_wish_goku)
GOKU_CAPSULE_29 = LocationData(200, "Goku 2 - Namek Saga - Capsule at Namek Village in Southwest Continent", can_wish_goku)
GOKU_CAPSULE_30 = LocationData(201, "Goku 2 - Namek Saga - Capsule given at ??? Marker after Cooler Battle", can_wish_goku)
GOKU_CAPSULE_31 = LocationData(202, "Goku 2 - Namek Saga - Cooler Reward (Cooler Battle after Vegeta Battle)", can_wish_goku_vegeta)
GOKU_CAPSULE_32 = LocationData(203, "Goku 2 - Buu Saga - Broly Reward", can_wish_goku)
GOKU_CAPSULE_33 = LocationData(204, "Goku 2 - Extra Saga - Capsule given before Gotenks Battle at World Tournament", can_super_spirit_bomb)
GOKU_CAPSULE_34 = LocationData(205, "Goku 2 - Extra Saga - Capsule given before Omega Shenron Battle at Central City", can_super_spirit_bomb)
GOKU_CAPSULE_35 = LocationData(206, "Goku 2 - Extra Saga - Omega Shenron Reward", can_super_spirit_bomb)
KID_GOHAN_CAPSULE_1 = LocationData(207, "Kid Gohan - Saiyan Saga - Capsule at Mountains near Baba's Palace", has_kid_gohan)
KID_GOHAN_CAPSULE_2 = LocationData(208, "Kid Gohan - Namek Saga - Capsule at Guru's House", can_kid_gohan)
KID_GOHAN_CAPSULE_3 = LocationData(209, "Kid Gohan - Namek Saga - Recoome Reward", can_kid_gohan)
KID_GOHAN_CAPSULE_4 = LocationData(210, "Kid Gohan - Namek Saga - Capsule given upon Completion", can_kid_gohan)
KID_GOHAN_CAPSULE_5 = LocationData(211, "Kid Gohan 2 - Saiyan Saga - Goku Reward", can_wish_kid_gohan)
TEEN_GOHAN_CAPSULE_1 = LocationData(212, "Teen Gohan - Starting Capsule", has_teen_gohan)
TEEN_GOHAN_CAPSULE_2 = LocationData(213, "Teen Gohan - Capsule at Central City", can_teen_gohan)
TEEN_GOHAN_CAPSULE_3 = LocationData(214, "Teen Gohan - Capsule at Kami's Lookout", can_teen_gohan)
TEEN_GOHAN_CAPSULE_4 = LocationData(215, "Teen Gohan - Capsule 1 at Cell Ring", can_teen_gohan)
TEEN_GOHAN_CAPSULE_5 = LocationData(216, "Teen Gohan - Capsule 2 at Cell Ring", can_teen_gohan)
TEEN_GOHAN_CAPSULE_6 = LocationData(217, "Teen Gohan - Super Perfect Cell Reward", can_teen_gohan)
TEEN_GOHAN_CAPSULE_7 = LocationData(218, "Teen Gohan - Capsule given upon Completion", can_teen_gohan)
TEEN_GOHAN_CAPSULE_8 = LocationData(219, "Teen Gohan 2 - Capsule at Goku's House", can_wish_teen_gohan)
GOHAN_CAPSULE_1 = LocationData(220, "Gohan - Starting Capsule 1", has_gohan)
GOHAN_CAPSULE_2 = LocationData(221, "Gohan - Starting Capsule 2", has_gohan)
GOHAN_CAPSULE_3 = LocationData(222, "Gohan - Capsule at Goku's House 1", can_gohan)
GOHAN_CAPSULE_4 = LocationData(223, "Gohan - Goten Reward", can_gohan)
GOHAN_CAPSULE_5 = LocationData(224, "Gohan - Capsule at End of Videl Story Quest", can_gohan)
GOHAN_CAPSULE_6 = LocationData(225, "Gohan - Capsule at Mountains Marker near Babidi's Spaceship", can_gohan)
GOHAN_CAPSULE_7 = LocationData(226, "Gohan - Capsule at Goku's House 2", can_gohan)
GOHAN_CAPSULE_8 = LocationData(227, "Gohan - Dabura Reward", can_gohan)
GOHAN_CAPSULE_9 = LocationData(228, "Gohan - Capsule given before Majin Buu Battle at Forest Marker", can_gohan)
GOHAN_CAPSULE_10 = LocationData(229, "Gohan - Capsule given after Majin Buu Battle", can_gohan)
GOHAN_CAPSULE_11 = LocationData(230, "Gohan - Capsule at ??? in Snowy Continent", can_gohan)
GOHAN_CAPSULE_12 = LocationData(231, "Gohan - Capsule given upon Completion", can_gohan)
GOHAN_CAPSULE_13 = LocationData(232, "Gohan 2 - Capsule at Plains near Central City", can_wish_gohan)
GOHAN_CAPSULE_14 = LocationData(233, "Gohan 2 - Capsule at Forest North of Kami's Lookout", can_wish_gohan)
VEGETA_CAPSULE_1 = LocationData(234, "Vegeta - Saiyan Saga - Starting Capsule", has_vegeta)
VEGETA_CAPSULE_2 = LocationData(235, "Vegeta - Namek Saga - Capsule at Planet Namek in Northwest Continent", can_vegeta)
VEGETA_CAPSULE_3 = LocationData(236, "Vegeta - Namek Saga - Recoome Reward", can_vegeta)
VEGETA_CAPSULE_4 = LocationData(237, "Vegeta - Android Saga - Capsule given in Saga Intro 1", can_vegeta)
VEGETA_CAPSULE_5 = LocationData(238, "Vegeta - Android Saga - Capsule given in Saga Intro 2", can_vegeta)
VEGETA_CAPSULE_6 = LocationData(239, "Vegeta - Android Saga - Capsule at West City", can_vegeta)
VEGETA_CAPSULE_7 = LocationData(240, "Vegeta - Buu Saga - Capsule given in Saga Intro", can_vegeta)
VEGETA_CAPSULE_8 = LocationData(241, "Vegeta - Buu Saga - Capsule given before Super Saiyan 2 Goku Battle at Plains Marker", can_vegeta)
VEGETA_CAPSULE_9 = LocationData(242, "Vegeta - Buu Saga - Capsule given after Majin Buu Battle", can_vegeta)
VEGETA_CAPSULE_10 = LocationData(243, "Vegeta - Buu Saga - Capsule given before Super Buu (Gohan) Battle at Plains Marker", can_vegeta)
VEGETA_CAPSULE_11 = LocationData(244, "Vegeta - Buu Saga - Super Buu Reward", can_vegeta)
VEGETA_CAPSULE_12 = LocationData(245, "Vegeta - Buu Saga - Kid Buu Reward", can_vegeta)
VEGETA_CAPSULE_13 = LocationData(246, "Vegeta - Capsule given upon Completion", can_vegeta)
VEGETA_CAPSULE_14 = LocationData(247, "Vegeta 2 - Buu Saga - Broly Reward", can_wish_vegeta)
VEGETA_CAPSULE_15 = LocationData(248, "Vegeta 2 - Extra Saga - Capsule given before Gotenks Battle at World Tournament Marker", can_wish_vegeta)
VEGETA_CAPSULE_16 = LocationData(249, "Vegeta 2 - Extra Saga - Capsule at ??? Marker", can_wish_vegeta)
VEGETA_CAPSULE_17 = LocationData(250, "Vegeta 2 - Extra Saga - Goku Reward", can_wish_vegeta)
KRILLIN_CAPSULE_1 = LocationData(251, "Krillin - Saiyan Saga - Starting Capsule", can_krillin)
KRILLIN_CAPSULE_2 = LocationData(252, "Krillin - Saiyan Saga - Capsule at Mountains in Southwest", can_krillin)
KRILLIN_CAPSULE_3 = LocationData(253, "Krillin - Namek Saga - Capsule at Guru's House", can_krillin)
KRILLIN_CAPSULE_4 = LocationData(254, "Krillin - Namek Saga - Recoome Reward", can_krillin)
KRILLIN_CAPSULE_5 = LocationData(255, "Krillin - Namek Saga - Capsule given before Third Form Frieza Battle", can_krillin)
KRILLIN_CAPSULE_6 = LocationData(256, "Krillin - Capsule given upon Completion", can_krillin)
KRILLIN_CAPSULE_7 = LocationData(257, "Krillin 2 - Android Saga - Capsule at South City", can_wish_krillin)
KRILLIN_CAPSULE_8 = LocationData(258, "Krillin 2 - Android Saga - Capsule at West City at end of Android 16 Quest", can_wish_krillin)
PICCOLO_CAPSULE_1 = LocationData(259, "Piccolo - Saiyan Saga - Starting Capsule", has_piccolo)
PICCOLO_CAPSULE_2 = LocationData(260, "Piccolo - Saiyan Saga - Capsule given before Raditz Battle at Plains Marker", can_piccolo)
PICCOLO_CAPSULE_3 = LocationData(261, "Piccolo - Saiyan Saga - Capsule at Mountains in Northwest Continent", can_piccolo)
PICCOLO_CAPSULE_4 = LocationData(262, "Piccolo - Namek Saga - Capsule given in Saga Intro", can_piccolo)
PICCOLO_CAPSULE_5 = LocationData(263, "Piccolo - Namek Saga - Capsule at ??? in Southwest Island", can_piccolo)
PICCOLO_CAPSULE_6 = LocationData(264, "Piccolo - Namek Saga - Second Form Frieza Reward", can_piccolo)
PICCOLO_CAPSULE_7 = LocationData(265, "Piccolo - Android Saga - Capsule at Kami's Lookout", can_piccolo)
PICCOLO_CAPSULE_8 = LocationData(266, "Piccolo - Android Saga - Capsule given before Android 17 Battle at Kame House", can_piccolo)
PICCOLO_CAPSULE_9 = LocationData(267, "Piccolo - Android Saga - Android 17 Reward", can_piccolo)
PICCOLO_CAPSULE_10 = LocationData(268, "Piccolo - Buu Saga - Capsule at Central City at end of Hercule Quest", can_piccolo)
PICCOLO_CAPSULE_11 = LocationData(269, "Piccolo - Buu Saga - Capsule at Mountains in Northwest Continent", can_piccolo)
PICCOLO_CAPSULE_12 = LocationData(270, "Piccolo 2 - Namek Saga - Capsule at Rightmost Red Marker after Defeating Second Form Frieza", can_wish_piccolo)
TIEN_CAPSULE_1 = LocationData(271, "Tien - Saiyan Saga - Starting Capsule", has_tien)
TIEN_CAPSULE_2 = LocationData(272, "Tien - Saiyan Saga - Capsule at Plains near West City", can_tien)
TIEN_CAPSULE_3 = LocationData(273, "Tien - Saiyan Saga - Capsule after Saibamen Battle", can_tien)
TIEN_CAPSULE_4 = LocationData(274, "Tien - Android Saga - Capsule at Kami's Lookout", can_tien)
YAMCHA_CAPSULE_1 = LocationData(275, "Yamcha - Saiyan Saga - Starting Capsule", has_yamcha)
YAMCHA_CAPSULE_2 = LocationData(276, "Yamcha - Saiyan Saga - Capsule at End of Break-up Quest", can_yamcha)
YAMCHA_CAPSULE_3 = LocationData(277, "Yamcha - Saiyan Saga - Capsule at Plains Red Marker", can_yamcha)
YAMCHA_CAPSULE_4 = LocationData(278, "Yamcha - Android Saga - Dr Gero Reward", can_yamcha)
YAMCHA_CAPSULE_5 = LocationData(279, "Yamcha 2 - Saiyan Saga - Capsule after Saibamen Battle", can_wish_yamcha)
UUB_CAPSULE_1 = LocationData(280, "Uub - Starting Capsule", has_uub)
BROLY_CAPSULE_1 = LocationData(281, "Broly - Starting Capsule", has_broly)
BROLY_CAPSULE_2 = LocationData(282, "Broly - Capsule at Grandpa Gohan's House", can_broly)
BROLY_CAPSULE_3 = LocationData(283, "Broly - Capsule at ??? near Kami's Lookout", can_broly)
BROLY_CAPSULE_4 = LocationData(284, "Broly - Capsule Given Before Gohan 1", can_broly)
BROLY_CAPSULE_5 = LocationData(285, "Broly - Capsule Given upon Completion", can_broly)
BROLY_CAPSULE_6 = LocationData(286, "Broly 2 - Capsule at Plains near Northern Mountains", can_wish_broly)
### everything else are random capsules. Some of these locations give a specified capsule once and then a random capsule afterward

DW_STATIC_CAPSULES = [
    GOKU_CAPSULE_1, GOKU_CAPSULE_2, GOKU_CAPSULE_3, GOKU_CAPSULE_4, GOKU_CAPSULE_5, GOKU_CAPSULE_6, GOKU_CAPSULE_7,
    GOKU_CAPSULE_8, GOKU_CAPSULE_9, GOKU_CAPSULE_10, GOKU_CAPSULE_11, GOKU_CAPSULE_12, GOKU_CAPSULE_13, GOKU_CAPSULE_14,
    GOKU_CAPSULE_15, GOKU_CAPSULE_16, GOKU_CAPSULE_17, GOKU_CAPSULE_18, GOKU_CAPSULE_19, GOKU_CAPSULE_20, GOKU_CAPSULE_21,
    GOKU_CAPSULE_22, GOKU_CAPSULE_23, GOKU_CAPSULE_24, GOKU_CAPSULE_25, GOKU_CAPSULE_26, GOKU_CAPSULE_27, GOKU_CAPSULE_28,
    GOKU_CAPSULE_29, GOKU_CAPSULE_30, GOKU_CAPSULE_31, GOKU_CAPSULE_32, GOKU_CAPSULE_33, GOKU_CAPSULE_34, GOKU_CAPSULE_35,
    KID_GOHAN_CAPSULE_1, KID_GOHAN_CAPSULE_2, KID_GOHAN_CAPSULE_3, KID_GOHAN_CAPSULE_4, KID_GOHAN_CAPSULE_5,
    TEEN_GOHAN_CAPSULE_1, TEEN_GOHAN_CAPSULE_2, TEEN_GOHAN_CAPSULE_3, TEEN_GOHAN_CAPSULE_4, TEEN_GOHAN_CAPSULE_5,
    TEEN_GOHAN_CAPSULE_6, TEEN_GOHAN_CAPSULE_7, TEEN_GOHAN_CAPSULE_8, GOHAN_CAPSULE_1, GOHAN_CAPSULE_2, GOHAN_CAPSULE_3,
    GOHAN_CAPSULE_4, GOHAN_CAPSULE_5, GOHAN_CAPSULE_6, GOHAN_CAPSULE_7, GOHAN_CAPSULE_8, GOHAN_CAPSULE_9, GOHAN_CAPSULE_10,
    GOHAN_CAPSULE_11, GOHAN_CAPSULE_12, GOHAN_CAPSULE_13, GOHAN_CAPSULE_14, VEGETA_CAPSULE_1, VEGETA_CAPSULE_2,
    VEGETA_CAPSULE_3, VEGETA_CAPSULE_4, VEGETA_CAPSULE_5, VEGETA_CAPSULE_6, VEGETA_CAPSULE_7, VEGETA_CAPSULE_8,
    VEGETA_CAPSULE_9, VEGETA_CAPSULE_10, VEGETA_CAPSULE_11, VEGETA_CAPSULE_12, VEGETA_CAPSULE_13, VEGETA_CAPSULE_14,
    VEGETA_CAPSULE_15, VEGETA_CAPSULE_16, VEGETA_CAPSULE_17, KRILLIN_CAPSULE_1, KRILLIN_CAPSULE_2, KRILLIN_CAPSULE_3,
    KRILLIN_CAPSULE_4, KRILLIN_CAPSULE_5, KRILLIN_CAPSULE_6, KRILLIN_CAPSULE_7, KRILLIN_CAPSULE_8, PICCOLO_CAPSULE_1,
    PICCOLO_CAPSULE_2, PICCOLO_CAPSULE_3, PICCOLO_CAPSULE_4, PICCOLO_CAPSULE_5, PICCOLO_CAPSULE_6, PICCOLO_CAPSULE_7,
    PICCOLO_CAPSULE_8, PICCOLO_CAPSULE_9, PICCOLO_CAPSULE_10, PICCOLO_CAPSULE_11, PICCOLO_CAPSULE_12, TIEN_CAPSULE_1,
    TIEN_CAPSULE_2, TIEN_CAPSULE_3, TIEN_CAPSULE_4, YAMCHA_CAPSULE_1, YAMCHA_CAPSULE_2, YAMCHA_CAPSULE_3,
    YAMCHA_CAPSULE_4, YAMCHA_CAPSULE_5, UUB_CAPSULE_1, BROLY_CAPSULE_1, BROLY_CAPSULE_2, BROLY_CAPSULE_3,
    BROLY_CAPSULE_4, BROLY_CAPSULE_5, BROLY_CAPSULE_6
]

DRAGON_WORLD_LOCS = [
    *DW_BOSSES, *DW_REENACTMENTS, *DW_DIFFICULTIES, *DW_WISHES, *DW_STATIC_CAPSULES
]

# Dragon Arena Checks
GOKU_BREAK_IN = LocationData(300, "Dragon Arena - Defeat Break-In Challenger - Goku", has_dragon_arena)
KGOKU_BREAK_IN = LocationData(301, "Dragon Arena - Defeat Break-In Challenger - Kid Goku", has_dragon_arena)
KGOHAN_BREAK_IN = LocationData(302, "Dragon Arena - Defeat Break-In Challenger - Kid Gohan", has_dragon_arena)
TGOHAN_BREAK_IN = LocationData(303, "Dragon Arena - Defeat Break-In Challenger - Teen Gohan", has_dragon_arena)
GOHAN_BREAK_IN  = LocationData(304, "Dragon Arena - Defeat Break-In Challenger - Gohan", has_dragon_arena)
GTS_BREAK_IN = LocationData(305, "Dragon Arena - Defeat Break-In Challenger - Gt Saiyaman", has_dragon_arena)
GOTEN_BREAK_IN = LocationData(306, "Dragon Arena - Defeat Break-In Challenger - Goten", has_dragon_arena)
VEGETA_BREAK_IN = LocationData(307, "Dragon Arena - Defeat Break-In Challenger - Vegeta", has_dragon_arena)
TRUNKS_BREAK_IN = LocationData(308, "Dragon Arena - Defeat Break-In Challenger - Trunks", has_dragon_arena)
KTRUNKS_BREAK_IN = LocationData(309, "Dragon Arena - Defeat Break-In Challenger - Kid Trunks", has_dragon_arena)
KRILLIN_BREAK_IN = LocationData(310, "Dragon Arena - Defeat Break-In Challenger - Krillin", has_dragon_arena)
PICCOLO_BREAK_IN = LocationData(311, "Dragon Arena - Defeat Break-In Challenger - Piccolo", has_dragon_arena)
TIEN_BREAK_IN = LocationData(312, "Dragon Arena - Defeat Break-In Challenger - Tien", has_dragon_arena)
YAMCHA_BREAK_IN = LocationData(313, "Dragon Arena - Defeat Break-In Challenger - Yamcha", has_dragon_arena)
VIDEL_BREAK_IN = LocationData(314, "Dragon Arena - Defeat Break-In Challenger - Videl", has_dragon_arena)
HERCULE_BREAK_IN = LocationData(315, "Dragon Arena - Defeat Break-In Challenger - Hercule", has_dragon_arena)
SUPREME_KAI_BREAK_IN = LocationData(316, "Dragon Arena - Defeat Break-In Challenger - Supreme Kai", has_dragon_arena)
UUB_BREAK_IN = LocationData(317, "Dragon Arena - Defeat Break-In Challenger - Uub", has_dragon_arena)
RADITZ_BREAK_IN = LocationData(318, "Dragon Arena - Defeat Break-In Challenger - Raditz", has_dragon_arena)
NAPPA_BREAK_IN = LocationData(319, "Dragon Arena - Defeat Break-In Challenger - Nappa", has_dragon_arena)
GINYU_BREAK_IN = LocationData(320, "Dragon Arena - Defeat Break-In Challenger - Ginyu", has_dragon_arena)
RECOOME_BREAK_IN = LocationData(321, "Dragon Arena - Defeat Break-In Challenger - Recoome", has_dragon_arena)
FRIEZA_BREAK_IN = LocationData(322, "Dragon Arena - Defeat Break-In Challenger - Frieza", has_dragon_arena)
ANDROID_16_BREAK_IN = LocationData(323, "Dragon Arena - Defeat Break-In Challenger - Android 16", has_dragon_arena)
ANDROID_17_BREAK_IN = LocationData(324, "Dragon Arena - Defeat Break-In Challenger - Android 17", has_dragon_arena)
ANDROID_18_BREAK_IN = LocationData(325, "Dragon Arena - Defeat Break-In Challenger - Android 18", has_dragon_arena)
DR_GERO_BREAK_IN = LocationData(326, "Dragon Arena - Defeat Break-In Challenger - Dr Gero", has_dragon_arena)
CELL_BREAK_IN = LocationData(327, "Dragon Arena - Defeat Break-In Challenger - Cell", has_dragon_arena)
MAJIN_BUU_BREAK_IN = LocationData(328, "Dragon Arena - Defeat Break-In Challenger - Majin Buu", has_dragon_arena)
SUPER_BUU_BREAK_IN = LocationData(329, "Dragon Arena - Defeat Break-In Challenger - Super Buu", has_dragon_arena)
KID_BUU_BREAK_IN = LocationData(330, "Dragon Arena - Defeat Break-In Challenger - Kid Buu", has_dragon_arena)
DABURA_BREAK_IN = LocationData(331, "Dragon Arena - Defeat Break-In Challenger - Dabura", has_dragon_arena)
COOLER_BREAK_IN = LocationData(332, "Dragon Arena - Defeat Break-In Challenger - Cooler", has_dragon_arena)
BARDOCK_BREAK_IN = LocationData(333, "Dragon Arena - Defeat Break-In Challenger - Bardock", has_dragon_arena)
BROLY_BREAK_IN = LocationData(334, "Dragon Arena - Defeat Break-In Challenger - Broly", has_dragon_arena)
OMEGA_BREAK_IN = LocationData(335, "Dragon Arena - Defeat Break-In Challenger - Omega", has_dragon_arena)
SAIBAMEN_BREAK_IN = LocationData(336, "Dragon Arena - Defeat Break-In Challenger - Saibamen", has_dragon_arena)
CELL_JR_BREAK_IN = LocationData(337, "Dragon Arena - Defeat Break-In Challenger - Cell Jr", has_dragon_arena)

DRAGON_ARENA_LOCS = [
    GOKU_BREAK_IN, KGOKU_BREAK_IN, KGOHAN_BREAK_IN, TGOHAN_BREAK_IN, GOHAN_BREAK_IN, GTS_BREAK_IN, GOTEN_BREAK_IN,
    VEGETA_BREAK_IN, TRUNKS_BREAK_IN, KTRUNKS_BREAK_IN, KRILLIN_BREAK_IN, PICCOLO_BREAK_IN, TIEN_BREAK_IN, YAMCHA_BREAK_IN,
    VIDEL_BREAK_IN, HERCULE_BREAK_IN, SUPREME_KAI_BREAK_IN, UUB_BREAK_IN, RADITZ_BREAK_IN, NAPPA_BREAK_IN, GINYU_BREAK_IN,
    RECOOME_BREAK_IN, FRIEZA_BREAK_IN, ANDROID_16_BREAK_IN, ANDROID_17_BREAK_IN, ANDROID_18_BREAK_IN, DR_GERO_BREAK_IN,
    CELL_BREAK_IN, MAJIN_BUU_BREAK_IN, SUPER_BUU_BREAK_IN, KID_BUU_BREAK_IN, DABURA_BREAK_IN, COOLER_BREAK_IN,
    BARDOCK_BREAK_IN, BROLY_BREAK_IN, OMEGA_BREAK_IN, SAIBAMEN_BREAK_IN, CELL_JR_BREAK_IN
]

# Training Mode Checks
TRAINING_1_COMPLETED = LocationData(400, "Training Mode - Complete Training 1", has_training_1)
TRAINING_2_COMPLETED = LocationData(401, "Training Mode - Complete Training 2", has_training_2)
TRAINING_3_COMPLETED = LocationData(402, "Training Mode - Complete Training 3", has_training_3)
TRAINING_4_COMPLETED = LocationData(403, "Training Mode - Complete Training 4", has_training_4)
TRAINING_5_COMPLETED = LocationData(404, "Training Mode - Complete Training 5", has_training_5)
TRAINING_6_COMPLETED = LocationData(405, "Training Mode - Complete Training 6", has_training_6)
TRAINING_7_COMPLETED = LocationData(406, "Training Mode - Complete Training 7", has_training_7)
TRAINING_8_COMPLETED = LocationData(407, "Training Mode - Complete Training 8", has_training_8)
TRAINING_9_COMPLETED = LocationData(408, "Training Mode - Complete Training 9", has_training_9)
TRAINING_10_COMPLETED = LocationData(409, "Training Mode - Complete Training 10", has_training_10)
TRAINING_11_COMPLETED = LocationData(410, "Training Mode - Complete Training 11", has_training_11)
TRAINING_12_COMPLETED = LocationData(411, "Training Mode - Complete Training 12", has_training_12)

TRAINING_LOCS = [
    TRAINING_1_COMPLETED,TRAINING_2_COMPLETED,TRAINING_3_COMPLETED,TRAINING_4_COMPLETED, TRAINING_5_COMPLETED,
    TRAINING_6_COMPLETED,TRAINING_7_COMPLETED,TRAINING_8_COMPLETED,TRAINING_9_COMPLETED,TRAINING_10_COMPLETED,
    TRAINING_11_COMPLETED,TRAINING_12_COMPLETED
]

# World Tournament Checks
NOVICE_CLEARED = LocationData(420, "World Tournament - Novice Tournament Champion", has_tournament_novice)
ADEPT_CLEARED = LocationData(421, "World Tournament - Adept Tournament Champion", has_tournament_adept)
ADVANCED_CLEARED = LocationData(422, "World Tournament - Advanced Tournament Champion", has_tournament_advanced)

WT_LOCS = [
    NOVICE_CLEARED, ADEPT_CLEARED, ADVANCED_CLEARED
]

# Shop Checks
SHOP_ITEMS={}
x = 1
while x < 100:
    SHOP_ITEMS[f"Shop Item {x}"] = 499 + x
    x += 1

SHOP_LOCS = []
for key, value in SHOP_ITEMS:
  SHOP_LOCS.append(LocationData(value, key))

LOCATIONS = [
    *DRAGON_WORLD_LOCS,
    *DRAGON_ARENA_LOCS,
    *TRAINING_LOCS,
    *WT_LOCS,
    *SHOP_LOCS
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