from typing import NamedTuple, Optional, Callable, Dict, Any
from Items import GRAY_CAPSULES
from ..Logic import *

class LocationData(NamedTuple):
    location_id: Optional[int]
    name: str
    access_rule: Optional[Callable[[CollectionState, int], bool]] = None


# Dragon World Checks
## Goku
GOKU_RADITZ_CLEAR = LocationData(location_id=1, name="Goku - Saiyan Saga - Defeat Raditz")
GOKU_NAPPA_CLEAR = LocationData(location_id=2, name="Goku - Saiyan Saga - Defeat Nappa")
GOKU_VEGETA_1_CLEAR = LocationData(location_id=3, name="Goku - Saiyan Saga - Defeat Vegeta")
GOKU_RECOOME_CLEAR = LocationData(location_id=4, name="Goku - Namek Saga - Defeat Recoome")
GOKU_GINYU_CLEAR = LocationData(location_id=5, name="Goku - Namek Saga - Defeat Ginyu")
GOKU_FRIEZA_1_CLEAR = LocationData(location_id=6, name="Goku - Namek Saga - Defeat Final Form Frieza")
GOKU_FRIEZA_2_CLEAR = LocationData(location_id=7, name="Goku - Namek Saga - Defeat 100% Final Form Frieza")
GOKU_COOLER_CLEAR = LocationData(location_id=8, name="Goku - Android Saga - Defeat Cooler")
GOKU_CELL_CLEAR = LocationData(location_id=9, name="Goku - Android Saga - Defeat Cell")
GOKU_MAJIN_VEGETA_CLEAR = LocationData(location_id=10, name="Goku - Buu Saga - Defeat Majin Vegeta")
GOKU_MAJIN_BUU_CLEAR = LocationData(location_id=11, name="Goku - Buu Saga - Defeat Majin Buu")
GOKU_SUPER_BUU_1_CLEAR = LocationData(location_id=12, name="Goku - Buu Saga - Defeat Super Buu (Gohan)")
GOKU_SUPER_BUU_2_CLEAR = LocationData(location_id=13, name="Goku - Buu Saga - Defeat Super Buu")
GOKU_KID_BUU_CLEAR = LocationData(location_id=14, name="Goku - Buu Saga - Defeat Kid Buu")
GOKU_UUB_CLEAR = LocationData(location_id=15, name="Goku - Extra Saga - Defeat Uub") # Must have defeated Kid Buu with a
                                                                                     # successful Super Spirit Bomb
GOKU_COOLER_2_CLEAR = LocationData(location_id=16, name="Goku 2 - Namek Saga - Defeat Cooler")
GOKU_METAL_COOLER_CLEAR = LocationData(location_id=17, name="Goku 2 - Namek Saga - Defeat Metal Cooler")
GOKU_VEGETA_2_CLEAR = LocationData(location_id=18, name="Goku 2 - Namek Saga - Defeat Super Saiyan Vegeta")
GOKU_COOLER_3_CLEAR = LocationData(location_id=19, name="Goku 2 - Namek Saga - Defeat Cooler after Vegeta")
GOKU_BROLY_CLEAR = LocationData(location_id=20, name="Goku 2 - Buu Saga - Defeat Broly")
GOKU_GOTENKS_CLEAR = LocationData(location_id=21, name="Goku 2 - Extra Saga - Defeat Gotenks")
GOKU_OMEGA_CLEAR = LocationData(location_id=22, name="Goku 2 - Extra Saga - Defeat Omega Shenron")

GOKU_BOSSES = [
    GOKU_RADITZ_CLEAR, GOKU_NAPPA_CLEAR, GOKU_VEGETA_1_CLEAR, GOKU_RECOOME_CLEAR, GOKU_GINYU_CLEAR, GOKU_FRIEZA_1_CLEAR,
    GOKU_FRIEZA_2_CLEAR, GOKU_COOLER_CLEAR, GOKU_CELL_CLEAR, GOKU_MAJIN_VEGETA_CLEAR, GOKU_MAJIN_BUU_CLEAR,
    GOKU_SUPER_BUU_1_CLEAR, GOKU_SUPER_BUU_2_CLEAR, GOKU_KID_BUU_CLEAR, GOKU_UUB_CLEAR, GOKU_COOLER_2_CLEAR,
    GOKU_METAL_COOLER_CLEAR, GOKU_VEGETA_2_CLEAR, GOKU_COOLER_3_CLEAR, GOKU_BROLY_CLEAR, GOKU_GOTENKS_CLEAR,
    GOKU_OMEGA_CLEAR
]

## Kid Gohan
KGOHAN_PICCOLO_CLEAR = LocationData(location_id=23, name="Kid Gohan - Saiyan Saga - Defeat Piccolo")
KGOHAN_SAIBAMEN_CLEAR = LocationData(location_id=24, name="Kid Gohan - Saiyan Saga - Defeat Saibamen")
KGOHAN_NAPPA_CLEAR = LocationData(location_id=25, name="Kid Gohan - Saiyan Saga - Defeat Nappa")
KGOHAN_RECOOME_CLEAR = LocationData(location_id=26, name="Kid Gohan - Namek Saga - Defeat Recoome")
KGOHAN_FRIEZA_CLEAR = LocationData(location_id=27, name="Kid Gohan - Namek Saga - Defeat Third Form Frieza")
KGOHAN_GOKU_CLEAR = LocationData(location_id=28, name="Kid Gohan 2 - Saiyan Saga - Defeat Goku")
KGOHAN_GINYU_GOKU_CLEAR = LocationData(location_id=29, name="Kid Gohan 2 - Namek Saga - Defeat Goku w/ Scouter")
KGOHAN_COOLER_CLEAR = LocationData(location_id=30, name="Kid Gohan 2 - Namek Saga - Defeat Cooler")

KID_GOHAN_BOSSES = [
    KGOHAN_PICCOLO_CLEAR, KGOHAN_SAIBAMEN_CLEAR, KGOHAN_NAPPA_CLEAR, KGOHAN_RECOOME_CLEAR,KGOHAN_FRIEZA_CLEAR,
    KGOHAN_GOKU_CLEAR, KGOHAN_GINYU_GOKU_CLEAR, KGOHAN_COOLER_CLEAR
]

## Teen Gohan
TGOHAN_PICCOLO_CLEAR = LocationData(location_id=31, name="Teen Gohan - Defeat Piccolo")
TGOHAN_KRILLIN_CLEAR = LocationData(location_id=32, name="Teen Gohan - Defeat Krillin")
TGOHAN_GOKU_CLEAR = LocationData(location_id=33, name="Teen Gohan - Defeat Super Saiyan Goku")
TGOHAN_CELL_1_CLEAR = LocationData(location_id=34, name="Teen Gohan - Defeat Perfect Cell")
TGOHAN_CELL_2_CLEAR = LocationData(location_id=35, name="Teen Gohan - Defeat Super Perfect Cell")
TGOHAN_TIEN_CLEAR = LocationData(location_id=36, name="Teen Gohan 2 - Defeat Tien")
TGOHAN_YAMCHA_CLEAR = LocationData(location_id=37, name="Teen Gohan 2 - Defeat Yamcha")

TEEN_GOHAN_BOSSES = [
    TGOHAN_PICCOLO_CLEAR, TGOHAN_KRILLIN_CLEAR, TGOHAN_GOKU_CLEAR, TGOHAN_CELL_1_CLEAR, TGOHAN_CELL_2_CLEAR,
    TGOHAN_TIEN_CLEAR, TGOHAN_YAMCHA_CLEAR
]

## Gohan
GOHAN_GOTEN_CLEAR = LocationData(location_id=38, name="Gohan - Defeat Goten")
GOHAN_VIDEL_CLEAR = LocationData(location_id=39, name="Gohan - Defeat Videl")
GOHAN_PICCOLO_CLEAR = LocationData(location_id=40, name="Gohan - Defeat Piccolo")
GOHAN_DABURA_CLEAR = LocationData(location_id=41, name="Gohan - Defeat Dabura")
GOHAN_MAJIN_BUU_CLEAR = LocationData(location_id=42, name="Gohan - Defeat Majin Buu")
GOHAN_VEGETA_CLEAR = LocationData(location_id=43, name="Gohan 2 - Defeat Vegeta")
GOHAN_MAJIN_VEGETA_CLEAR = LocationData(location_id=44, name="Gohan 2 - Defeat Majin Vegeta")
GOHAN_KID_BUU_CLEAR = LocationData(location_id=45, name="Gohan 2 - Defeat Kid Buu")
GOHAN_BROLY_CLEAR = LocationData(location_id=46, name="Gohan 2 - Defeat Broly")

GOHAN_BOSSES = [
    GOHAN_GOTEN_CLEAR, GOHAN_VIDEL_CLEAR, GOHAN_PICCOLO_CLEAR, GOHAN_DABURA_CLEAR, GOHAN_MAJIN_BUU_CLEAR,
    GOHAN_VEGETA_CLEAR, GOHAN_MAJIN_VEGETA_CLEAR, GOHAN_KID_BUU_CLEAR, GOHAN_BROLY_CLEAR
]

## Vegeta
VEGETA_GOKU_1_CLEAR = LocationData(location_id=47, name="Vegeta - Saiyan Saga - Defeat Goku")
VEGETA_KID_GOHAN_CLEAR = LocationData(location_id=48, name="Vegeta - Saiyan Saga - Defeat Kid Gohan")
VEGETA_RECOOME_CLEAR = LocationData(location_id=49, name="Vegeta - Namek Saga - Defeat Recoome")
VEGETA_FRIEZA_1_CLEAR = LocationData(location_id=50, name="Vegeta - Namek Saga - Defeat First Form Frieza")
VEGETA_FRIEZA_2_CLEAR = LocationData(location_id=51, name="Vegeta - Namek Saga - Defeat Final Form Frieza")
VEGETA_ANDROID_17_CLEAR = LocationData(location_id=52, name="Vegeta - Android Saga - Defeat Android 17")
VEGETA_ANDROID_18_CLEAR = LocationData(location_id=53, name="Vegeta - Android Saga - Defeat Android 18")
VEGETA_CELL_1_CLEAR = LocationData(location_id=54, name="Vegeta - Android Saga - Defeat Cell (17 Absorbed)")
VEGETA_CELL_2_CLEAR = LocationData(location_id=55, name="Vegeta - Android Saga - Defeat Perfect Cell")
VEGETA_GOKU_2_CLEAR = LocationData(location_id=56, name="Vegeta - Buu Saga - Defeat Super Saiyan 2 Goku")
VEGETA_MAJIN_BUU_CLEAR = LocationData(location_id=57, name="Vegeta - Buu Saga - Defeat Majin Buu")
VEGETA_SUPER_BUU_1_CLEAR = LocationData(location_id=58, name="Vegeta - Buu Saga - Defeat Super Buu (Gohan)")
VEGETA_SUPER_BUU_2_CLEAR = LocationData(location_id=59, name="Vegeta - Buu Saga - Defeat Super Buu")
VEGETA_KID_BUU_CLEAR = LocationData(location_id=60, name="Vegeta - Buu Saga - Defeat Kid Buu")
VEGETA_METAL_COOLER_CLEAR = LocationData(location_id=61, name="Vegeta 2 - Namek Saga - Defeat Metal Cooler")
VEGETA_BROLY_CLEAR = LocationData(location_id=62, name="Vegeta 2 - Buu Saga - Defeat Broly")
VEGETA_GOTENKS_CLEAR = LocationData(location_id=63, name="Vegeta 2 - Extra Saga - Defeat Gotenks")
VEGETA_GOKU_3_CLEAR = LocationData(location_id=64, name="Vegeta 2 - Extra Saga - Defeat Super Saiyan 4 Goku")

VEGETA_BOSSES = [
    VEGETA_GOKU_1_CLEAR, VEGETA_KID_GOHAN_CLEAR, VEGETA_RECOOME_CLEAR, VEGETA_FRIEZA_1_CLEAR, VEGETA_FRIEZA_2_CLEAR,
    VEGETA_ANDROID_17_CLEAR, VEGETA_ANDROID_18_CLEAR, VEGETA_CELL_1_CLEAR, VEGETA_CELL_2_CLEAR, VEGETA_GOKU_2_CLEAR,
    VEGETA_MAJIN_BUU_CLEAR, VEGETA_SUPER_BUU_1_CLEAR, VEGETA_SUPER_BUU_2_CLEAR, VEGETA_KID_BUU_CLEAR,
    VEGETA_METAL_COOLER_CLEAR, VEGETA_BROLY_CLEAR, VEGETA_GOTENKS_CLEAR, VEGETA_GOKU_3_CLEAR
]

## Krillin
KRILLIN_SAIBAMEN_CLEAR = LocationData(location_id=65, name="Krillin - Saiyan Saga - Defeat Saibamen")
KRILLIN_NAPPA_CLEAR = LocationData(location_id=66, name="Krillin - Saiyan Saga - Defeat Nappa")
KRILLIN_RECOOME_CLEAR = LocationData(location_id=67, name="Krillin - Namek Saga - Defeat Recoome")
KRILLIN_GINYU_GOKU_CLEAR = LocationData(location_id=68, name="Krillin - Namek Saga - Defeat Goku w/ Scouter")
KRILLIN_FRIEZA_1_CLEAR = LocationData(location_id=69, name="Krillin - Namek Saga - Defeat Second Form Frieza")
KRILLIN_FRIEZA_2_CLEAR = LocationData(location_id=70, name="Krillin - Namek Saga - Defeat Final Form Frieza")
KRILLIN_CELL_CLEAR = LocationData(location_id=71, name="Krillin 2 - Android Saga - Defeat Perfect Form Cell")

KRILLIN_BOSSES = [
    KRILLIN_SAIBAMEN_CLEAR, KRILLIN_NAPPA_CLEAR, KRILLIN_RECOOME_CLEAR, KRILLIN_GINYU_GOKU_CLEAR, KRILLIN_FRIEZA_1_CLEAR,
    KRILLIN_FRIEZA_2_CLEAR, KRILLIN_CELL_CLEAR
]

## Piccolo
PICCOLO_RADITZ_CLEAR = LocationData(location_id=72, name="Piccolo - Saiyan Saga - Defeat Raditz")
PICCOLO_KID_GOHAN_CLEAR = LocationData(location_id=73, name="Piccolo - Saiyan Saga - Defeat Kid Gohan")
PICCOLO_SAIBAMEN_CLEAR = LocationData(location_id=74, name="Piccolo - Saiyan Saga - Defeat Saibamen")
PICCOLO_NAPPA_CLEAR = LocationData(location_id=75, name="Piccolo - Saiyan Saga - Defeat Nappa")
PICCOLO_FRIEZA_1_CLEAR = LocationData(location_id=76, name="Piccolo - Namek Saga - Defeat Second Form Frieza")
PICCOLO_FRIEZA_2_CLEAR = LocationData(location_id=77, name="Piccolo - Namek Saga - Defeat Third Form Frieza")
PICCOLO_DR_GERO_CLEAR = LocationData(location_id=78, name="Piccolo - Android Saga - Defeat Dr Gero")
PICCOLO_CELL_1_CLEAR = LocationData(location_id=79, name="Piccolo - Android Saga - Defeat Cell")
PICCOLO_ANDROID_17_CLEAR = LocationData(location_id=80, name="Piccolo - Android Saga - Defeat Android 17")
PICCOLO_SUPER_BUU_CLEAR = LocationData(location_id=81, name="Piccolo - Buu Saga - Defeat Super Buu")
PICCOLO_GOKU_CLEAR = LocationData(location_id=82, name="Piccolo 2 - Saiyan Saga - Defeat Goku")
PICCOLO_VEGETA_CLEAR = LocationData(location_id=83, name="Piccolo 2 - Saiyan Saga - Defeat Vegeta")
PICCOLO_COOLER_CLEAR = LocationData(location_id=84, name="Piccolo 2 - Namek Saga - Defeat Cooler")
PICCOLO_METAL_COOLER_CLEAR = LocationData(location_id=85, name="Piccolo 2 - Namek Saga - Defeat Metal Cooler")
PICCOLO_FRIEZA_3_CLEAR = LocationData(location_id=86, name="Piccolo 2 - Namek Saga - Defeat Final Form Frieza")
PICCOLO_CELL_2_CLEAR = LocationData(location_id=87, name="Piccolo 2 - Android Saga - Defeat Perfect Cell")
PICCOLO_DABURA_CLEAR = LocationData(location_id=88, name="Piccolo 2 - Buu Saga - Defeat Dabura")
PICCOLO_BROLY_CLEAR = LocationData(location_id=89, name="Piccolo 2 - Buu Saga - Defeat Broly")

PICCOLO_BOSSES = [
    PICCOLO_RADITZ_CLEAR, PICCOLO_KID_GOHAN_CLEAR, PICCOLO_SAIBAMEN_CLEAR, PICCOLO_NAPPA_CLEAR, PICCOLO_FRIEZA_1_CLEAR,
    PICCOLO_FRIEZA_2_CLEAR, PICCOLO_DR_GERO_CLEAR, PICCOLO_CELL_1_CLEAR, PICCOLO_ANDROID_17_CLEAR, PICCOLO_SUPER_BUU_CLEAR,
    PICCOLO_GOKU_CLEAR, PICCOLO_VEGETA_CLEAR, PICCOLO_COOLER_CLEAR, PICCOLO_METAL_COOLER_CLEAR, PICCOLO_FRIEZA_3_CLEAR,
    PICCOLO_CELL_2_CLEAR, PICCOLO_DABURA_CLEAR, PICCOLO_BROLY_CLEAR
]

## Tien
TIEN_SAIBAMEN_CLEAR = LocationData(location_id=90, name="Tien - Saiyan Saga - Defeat Saibamen")
TIEN_NAPPA_CLEAR = LocationData(location_id=91, name="Tien - Saiyan Saga - Defeat Nappa")
TIEN_CELL_CLEAR = LocationData(location_id=92, name="Tien - Android Saga - Defeat Second Form Cell")
TIEN_CELL_JR_CLEAR = LocationData(location_id=93, name="Tien - Android Saga - Defeat Cell Jr")
TIEN_SUPER_BUU_CLEAR = LocationData(location_id=94, name="Tien - Buu Saga - Defeat Super Buu (Gotenks)")
TIEN_YAMCHA_CLEAR = LocationData(location_id=95, name="Tien 2 - Extra Saga - Defeat Yamcha")

TIEN_BOSSES = [
    TIEN_SAIBAMEN_CLEAR, TIEN_NAPPA_CLEAR, TIEN_CELL_CLEAR, TIEN_CELL_JR_CLEAR, TIEN_SUPER_BUU_CLEAR, TIEN_YAMCHA_CLEAR
]

## Yamcha
YAMCHA_SAIBAMEN_CLEAR = LocationData(location_id=96, name="Yamcha - Saiyan Saga - Defeat Saibamen")
YAMCHA_DR_GERO_CLEAR = LocationData(location_id=97, name="Yamcha - Android Saga - Defeat Dr Gero")
YAMCHA_TIEN_CLEAR = LocationData(location_id=98, name="Yamcha - Extra Saga - Defeat Tien")
YAMCHA_VEGETA_CLEAR = LocationData(location_id=99, name="Yamcha 2 - Extra Saga - Defeat Vegeta")

YAMCHA_BOSSES = [
    YAMCHA_SAIBAMEN_CLEAR, YAMCHA_DR_GERO_CLEAR, YAMCHA_TIEN_CLEAR, YAMCHA_VEGETA_CLEAR
]

## Uub
UUB_GOKU_1_CLEAR = LocationData(location_id=100, name="Uub - Defeat Goku at World Tournament")
UUB_VEGETA_CLEAR = LocationData(location_id=101, name="Uub - Defeat Vegeta")
UUB_MAJIN_BUU_CLEAR = LocationData(location_id=102, name="Uub - Defeat Majin Buu")
UUB_GOKU_2_CLEAR = LocationData(location_id=103, name="Uub - Defeat Goku at Archipelago")
UUB_OMEGA_SHENRON_CLEAR = LocationData(location_id=104, name="Uub - Defeat Omega Shenron")

UUB_BOSSES = [
    UUB_GOKU_1_CLEAR, UUB_VEGETA_CLEAR, UUB_MAJIN_BUU_CLEAR, UUB_GOKU_2_CLEAR, UUB_OMEGA_SHENRON_CLEAR
]

## Broly
BROLY_KRILLIN_CLEAR = LocationData(location_id=105, name="Broly - Defeat Krillin")
BROLY_PICCOLO_CLEAR = LocationData(location_id=106, name="Broly - Defeat Piccolo")
BROLY_VEGETA_CLEAR = LocationData(location_id=107, name="Broly - Defeat Vegeta")
BROLY_VIDEL_CLEAR = LocationData(location_id=108, name="Broly - Defeat Videl")
BROLY_KID_TRUNKS_CLEAR = LocationData(location_id=109, name="Broly - Defeat Kid Trunks")
BROLY_GOTEN_CLEAR = LocationData(location_id=110, name="Broly - Defeat Goten")
BROLY_GOHAN_1_CLEAR = LocationData(location_id=111, name="Broly - Defeat Gohan 1")
BROLY_GOHAN_2_CLEAR = LocationData(location_id=112, name="Broly - Defeat Gohan 2")
BROLY_GOKU_CLEAR = LocationData(location_id=113, name="Broly 2 - Defeat Goku")

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
REENACTMENT_0 = LocationData(location_id=114, name = "Reenactment 00") # Goku - Use Kamehameha against Raditz
REENACTMENT_1 = LocationData(location_id=115, name = "Reenactment 01") # Piccolo - Use Special Beam Cannon against Raditz
REENACTMENT_2 = LocationData(location_id=116, name = "Reenactment 02") # Tien - Use Ki Blast Cannon against Nappa
REENACTMENT_3 = LocationData(location_id=117, name = "Reenactment 03") # Kid Gohan - Use Masenko against Nappa
REENACTMENT_4 = LocationData(location_id=118, name = "Reenactment 04") # Krillin - Use Destructo Disc against Frieza (Second Form)
REENACTMENT_5 = LocationData(location_id=119, name = "Reenactment 05") # Goku - Use Super Saiyan against Frieza (Final Form)
REENACTMENT_6 = LocationData(location_id=120, name = "Reenactment 06") # Yamcha - Use Senzu Bean during battle with Dr Gero
REENACTMENT_7 = LocationData(location_id=121, name = "Reenactment 07") # Piccolo - Use Fuse with Kami against Cell
REENACTMENT_8 = LocationData(location_id=122, name = "Reenactment 08") # Vegeta - Have 2500 HP or more at end of Cell (17 Absorbed) fight
REENACTMENT_9 = LocationData(location_id=123, name = "Reenactment 09") # Vegeta - Use Final Flash against Cell (Perfect)
REENACTMENT_10 = LocationData(location_id=124, name = "Reenactment 10") # Teen Gohan - Use Super Saiyan against Goku
REENACTMENT_11 = LocationData(location_id=125, name = "Reenactment 11") # Teen Gohan - Defeat Cell (Super Perfect Form) with Father-Son Kamehameha
                                                        # You do not have to exceed Cell's meter during the charging segment
REENACTMENT_12 = LocationData(location_id=126, name = "Reenactment 12") # Vegeta - Defeat Majin Buu with Perfect Explosion
REENACTMENT_13 = LocationData(location_id=127, name = "Reenactment 13") # Goku - Use Super Saiyan 3 against Majin Buu
REENACTMENT_14 = LocationData(location_id=128, name = "Reenactment 14") # Piccolo - Defeat Super Buu after 60 seconds have elapsed
REENACTMENT_15 = LocationData(location_id=129, name = "Reenactment 15") # Gohan - Use Elder Kai Unlock Ability against Super Buu
REENACTMENT_16 = LocationData(location_id=130, name = "Reenactment 16") # Goku - Defeat Kid Buu with Super Spirit Bomb
                                                        # To do this, you must already be base Goku or Kaioken and have
                                                        # Super Saiyan in your tray. If you use Spirit Bomb, it will
                                                        # become Super Spirit Bomb. Defeat Kid Buu by filling your meter
                                                        # more than he does.
REENACTMENT_17 = LocationData(location_id=131, name = "Reenactment 17") # Vegeta - Use Super Saiyan 4 against Super Saiyan 4 Goku
REENACTMENT_18 = LocationData(location_id=132, name = "Reenactment 18") # Goku - Defeat Omega Shenron with 100X Big Bang Kamehameha
REENACTMENT_19 = LocationData(location_id=133, name = "Reenactment 19") # Broly - Use fully-powered Gigantic Meteor against Gohan 1
REENACTMENT_20 = LocationData(location_id=134, name = "Reenactment 20") # Uub - Use Ki Cannon against Goku 1

DW_REENACTMENTS = [
    REENACTMENT_0, REENACTMENT_1, REENACTMENT_2, REENACTMENT_3, REENACTMENT_4, REENACTMENT_5, REENACTMENT_6, REENACTMENT_7,
    REENACTMENT_8, REENACTMENT_9, REENACTMENT_10, REENACTMENT_11, REENACTMENT_12, REENACTMENT_13, REENACTMENT_14,
    REENACTMENT_15, REENACTMENT_16, REENACTMENT_17, REENACTMENT_18, REENACTMENT_19, REENACTMENT_20
]

## Difficulty-related
VERY_HARD_CLEAR = LocationData(location_id=135, name="Clear DW on Very Hard")
Z1_CLEAR = LocationData(location_id=136, name="Clear DW on Z1")
Z2_CLEAR = LocationData(location_id=137, name="Clear DW on Z2")
Z3_CLEAR = LocationData(location_id=138, name="Clear DW on Z3")

DW_DIFFICULTIES = [VERY_HARD_CLEAR, Z1_CLEAR, Z2_CLEAR, Z3_CLEAR]

## Wishes
GOKU_WISH_1 = LocationData(location_id=139, name="Goku Wish 1 - Breakthrough")
GOKU_WISH_2 = LocationData(location_id=140, name="Goku Wish 2 - Memories of Goku")
GOKU_WISH_3 = LocationData(location_id=141, name="Goku Wish 3 - Mysterious Vest")
KGOHAN_WISH_1 = LocationData(location_id=142, name="Kid Gohan Wish 1 - Breakthrough")
KGOHAN_WISH_2 = LocationData(location_id=143, name="Kid Gohan Wish 2 - Memories of Kid Gohan")
KGOHAN_WISH_3 = LocationData(location_id=144, name="Kid Gohan Wish 3 - Mysterious Evil Uniform")
TGOHAN_WISH_1 = LocationData(location_id=145, name="Teen Gohan Wish 1 - Breakthrough")
TGOHAN_WISH_2 = LocationData(location_id=146, name="Teen Gohan Wish 2 - Memories of Teen Gohan")
TGOHAN_WISH_3 = LocationData(location_id=147, name="Teen Gohan Wish 3 - Evil Mystery Uniform")
GOHAN_WISH_1 = LocationData(location_id=148, name="Gohan Wish 1 - Breakthrough")
GOHAN_WISH_2 = LocationData(location_id=149, name="Gohan Wish 2 - Memories of Gohan")
GOHAN_WISH_3 = LocationData(location_id=150, name="Gohan Wish 3 - Supreme Kai's Outfit")
VEGETA_WISH_1 = LocationData(location_id=151, name="Vegeta Wish 1 - Breakthrough")
VEGETA_WISH_2 = LocationData(location_id=152, name="Vegeta Wish 2 - Memories of Vegeta")
VEGETA_WISH_3 = LocationData(location_id=153, name="Vegeta Wish 1 - Bulma's Armor")
KRILLIN_WISH_1 = LocationData(location_id=154, name="Krillin Wish 1 - Breakthrough")
KRILLIN_WISH_2 = LocationData(location_id=155, name="Krillin Wish 2 - Memories of Krillin")
KRILLIN_WISH_3 = LocationData(location_id=156, name="Krillin Wish 3 - Mysterious Vest")
PICCOLO_WISH_1 = LocationData(location_id=157, name="Piccolo Wish 1 - Breakthrough")
PICCOLO_WISH_2 = LocationData(location_id=158, name="Piccolo Wish 2 - Memories of Piccolo")
PICCOLO_WISH_3 = LocationData(location_id=159, name="Piccolo Wish 3 - Evil Mystery Uniform")
TIEN_WISH_1 = LocationData(location_id=160, name="Tien Wish 1 - Breakthrough")
TIEN_WISH_2 = LocationData(location_id=161, name="Tien Wish 2 - Memories of Tien")
TIEN_WISH_3 = LocationData(location_id=162, name="Tien Wish 3 - Mysterious Vest")
YAMCHA_WISH_1 = LocationData(location_id=163, name="Yamcha Wish 1 - Breakthrough")
YAMCHA_WISH_2 = LocationData(location_id=164, name="Yamcha Wish 2 - Memories of Yamcha")
YAMCHA_WISH_3 = LocationData(location_id=165, name="Yamcha Wish 3 - Mysterious Vest")
UUB_WISH_1 = LocationData(location_id=166, name="Uub Wish 1 - Breakthrough")
UUB_WISH_2 = LocationData(location_id=167, name="Uub Wish 2 - Memories of Uub")
UUB_WISH_3 = LocationData(location_id=168, name="Uub Wish 3 - Majin Belt")
BROLY_WISH_1 = LocationData(location_id=169, name="Broly Wish 1 - Breakthrough")
BROLY_WISH_2 = LocationData(location_id=170, name="Broly Wish 2 - Memories of Broly")
BROLY_WISH_3 = LocationData(location_id=171, name="Broly Wish 3 - Legendary Body Wrap")

DW_WISHES = [
    GOKU_WISH_1, GOKU_WISH_2, GOKU_WISH_3, KGOHAN_WISH_1, KGOHAN_WISH_2, KGOHAN_WISH_3, TGOHAN_WISH_1, TGOHAN_WISH_2,
    TGOHAN_WISH_3, GOHAN_WISH_1, GOHAN_WISH_2, GOHAN_WISH_3, VEGETA_WISH_1, VEGETA_WISH_2, VEGETA_WISH_3, KRILLIN_WISH_1,
    KRILLIN_WISH_2, KRILLIN_WISH_3, PICCOLO_WISH_1, PICCOLO_WISH_2, PICCOLO_WISH_3, TIEN_WISH_1, TIEN_WISH_2, TIEN_WISH_3,
    YAMCHA_WISH_1, YAMCHA_WISH_2, YAMCHA_WISH_3, UUB_WISH_1, UUB_WISH_2, UUB_WISH_3, BROLY_WISH_1, BROLY_WISH_2,
    BROLY_WISH_3
]

## DW Static Capsules
GOKU_CAPSULE_1 = LocationData(location_id=172, name="Goku - Saiyan Saga - Starting Capsule")
GOKU_CAPSULE_2 = LocationData(location_id=173, name="Goku - Saiyan Saga - Capsule at Plains Marker")
GOKU_CAPSULE_3 = LocationData(location_id=174, name="Goku - Saiyan Saga - Capsule at Plains")
GOKU_CAPSULE_4 = LocationData(location_id=175, name="Goku - Saiyan Saga - Vegeta Reward")
GOKU_CAPSULE_5 = LocationData(location_id=176, name="Goku - Namek Saga - Capsule at Capsule House")
GOKU_CAPSULE_6 = LocationData(location_id=177, name="Goku - Namek Saga - Recoome Reward 1")
GOKU_CAPSULE_7 = LocationData(location_id=178, name="Goku - Namek Saga - Recoome Reward 2")
GOKU_CAPSULE_8 = LocationData(location_id=179, name="Goku - Namek Saga - Ginyu Reward")
GOKU_CAPSULE_9 = LocationData(location_id=180, name="Goku - Namek Saga - Capsule given before 100% Final Power Frieza Battle")
GOKU_CAPSULE_10 = LocationData(location_id=181, name="Goku - Namek Saga - 100% Full Power Frieza Reward")
GOKU_CAPSULE_11 = LocationData(location_id=182, name="Goku - Android Saga - Capsule at Plains near Cell Ring")
GOKU_CAPSULE_12 = LocationData(location_id=183, name="Goku - Android Saga - Capsule near Baba's House")
GOKU_CAPSULE_13 = LocationData(location_id=184, name="Goku - Android Saga - Perfect Form Cell Reward")
GOKU_CAPSULE_14 = LocationData(location_id=185, name="Goku - Buu Saga - Capsule given in Saga Intro")
GOKU_CAPSULE_15 = LocationData(location_id=186, name="Goku - Buu Saga - Capsule at Forest near West City")
GOKU_CAPSULE_16 = LocationData(location_id=187, name="Goku - Buu Saga - Capsule at North City")
GOKU_CAPSULE_17 = LocationData(location_id=188, name="Goku - Buu Saga - Capsule given before Majin Buu Battle")
GOKU_CAPSULE_18 = LocationData(location_id=189, name="Goku - Buu Saga - Majin Buu Reward")
GOKU_CAPSULE_19 = LocationData(location_id=190, name="Goku - Buu Saga - Capsule given before Super Buu (Gohan) Battle at ??? Marker")
GOKU_CAPSULE_20 = LocationData(location_id=191, name="Goku - Buu Saga - Super Buu (Gohan) Reward")
GOKU_CAPSULE_21 = LocationData(location_id=192, name="Goku - Buu Saga - Super Buu Reward")
GOKU_CAPSULE_22 = LocationData(location_id=193, name="Goku - Buu Saga - Kid Buu Reward")
GOKU_CAPSULE_23 = LocationData(location_id=194, name="Goku - Extra Saga - Capsule at ??? in SE Islands")
GOKU_CAPSULE_24 = LocationData(location_id=195, name="Goku - Extra Saga - Uub Reward")
GOKU_CAPSULE_25 = LocationData(location_id=196, name="Goku 2 - Saiyan Saga - Capsule at Saiyan's Spaceship near East City")
GOKU_CAPSULE_26 = LocationData(location_id=197, name="Goku 2 - Saiyan Saga - Capsule at Grandpa Gohan's House")
GOKU_CAPSULE_27 = LocationData(location_id=198, name="Goku 2 - Saiyan Saga - Capsule at Korin's Tower")
GOKU_CAPSULE_28 = LocationData(location_id=199, name="Goku 2 - Namek Saga - Capsule at ??? on Lone Central Island")
GOKU_CAPSULE_29 = LocationData(location_id=200, name="Goku 2 - Namek Saga - Capsule at Namek Village in Southwest Continent")
GOKU_CAPSULE_30 = LocationData(location_id=201, name="Goku 2 - Namek Saga - Capsule given at ??? Marker after Cooler Battle")
GOKU_CAPSULE_31 = LocationData(location_id=202, name="Goku 2 - Namek Saga - Cooler Reward (Cooler Battle after Vegeta Battle)")
GOKU_CAPSULE_32 = LocationData(location_id=203, name="Goku 2 - Buu Saga - Broly Reward")
GOKU_CAPSULE_33 = LocationData(location_id=204, name="Goku 2 - Extra Saga - Capsule given before Gotenks Battle at World Tournament")
GOKU_CAPSULE_34 = LocationData(location_id=205, name="Goku 2 - Extra Saga - Capsule given before Omega Shenron Battle at Central City")
GOKU_CAPSULE_35 = LocationData(location_id=206, name="Goku 2 - Extra Saga - Omega Shenron Reward")
KID_GOHAN_CAPSULE_1 = LocationData(location_id=207, name="Kid Gohan - Saiyan Saga - Capsule at Mountains near Baba's Palace")
KID_GOHAN_CAPSULE_2 = LocationData(location_id=208, name="Kid Gohan - Namek Saga - Capsule at Guru's House")
KID_GOHAN_CAPSULE_3 = LocationData(location_id=209, name="Kid Gohan - Namek Saga - Recoome Reward")
KID_GOHAN_CAPSULE_4 = LocationData(location_id=210, name="Kid Gohan - Namek Saga - Capsule given upon Completion")
KID_GOHAN_CAPSULE_5 = LocationData(location_id=211, name="Kid Gohan 2 - Saiyan Saga - Goku Reward")
TEEN_GOHAN_CAPSULE_1 = LocationData(location_id=212, name="Teen Gohan - Starting Capsule")
TEEN_GOHAN_CAPSULE_2 = LocationData(location_id=213, name="Teen Gohan - Capsule at Central City")
TEEN_GOHAN_CAPSULE_3 = LocationData(location_id=214, name="Teen Gohan - Capsule at Kami's Lookout")
TEEN_GOHAN_CAPSULE_4 = LocationData(location_id=215, name="Teen Gohan - Capsule 1 at Cell Ring")
TEEN_GOHAN_CAPSULE_5 = LocationData(location_id=216, name="Teen Gohan - Capsule 2 at Cell Ring")
TEEN_GOHAN_CAPSULE_6 = LocationData(location_id=217, name="Teen Gohan - Super Perfect Cell Reward")
TEEN_GOHAN_CAPSULE_7 = LocationData(location_id=218, name="Teen Gohan - Capsule given upon Completion")
TEEN_GOHAN_CAPSULE_8 = LocationData(location_id=219, name="Teen Gohan 2 - Capsule at Goku's House")
GOHAN_CAPSULE_1 = LocationData(location_id=220, name="Gohan - Starting Capsule 1")
GOHAN_CAPSULE_2 = LocationData(location_id=221, name="Gohan - Starting Capsule 2")
GOHAN_CAPSULE_3 = LocationData(location_id=222, name="Gohan - Capsule at Goku's House 1")
GOHAN_CAPSULE_4 = LocationData(location_id=223, name="Gohan - Goten Reward")
GOHAN_CAPSULE_5 = LocationData(location_id=224, name="Gohan - Capsule at End of Videl Story Quests")
GOHAN_CAPSULE_6 = LocationData(location_id=225, name="Gohan - Capsule at Mountains Marker near Babidi's Spaceship")
GOHAN_CAPSULE_7 = LocationData(location_id=226, name="Gohan - Capsule at Goku's House 2")
GOHAN_CAPSULE_8 = LocationData(location_id=227, name="Gohan - Dabura Reward")
GOHAN_CAPSULE_9 = LocationData(location_id=228, name="Gohan - Capsule given before Majin Buu Battle at Forest Marker")
GOHAN_CAPSULE_10 = LocationData(location_id=229, name="Gohan - Capsule given after Majin Buu Battle")
GOHAN_CAPSULE_11 = LocationData(location_id=230, name="Gohan - Capsule at ??? in Snowy Continent")
GOHAN_CAPSULE_12 = LocationData(location_id=231, name="Gohan - Capsule given upon Completion")
GOHAN_CAPSULE_13 = LocationData(location_id=232, name="Gohan 2 - Capsule at Plains near Central City")
GOHAN_CAPSULE_14 = LocationData(location_id=233, name="Gohan 2 - Capsule at Forest North of Kami's Lookout")
VEGETA_CAPSULE_1 = LocationData(location_id=234, name="Vegeta - Saiyan Saga - Starting Capsule")
VEGETA_CAPSULE_2 = LocationData(location_id=235, name="Vegeta - Namek Saga - Capsule at Planet Namek in Northwest Continent")
VEGETA_CAPSULE_3 = LocationData(location_id=236, name="Vegeta - Namek Saga - Recoome Reward")
VEGETA_CAPSULE_4 = LocationData(location_id=237, name="Vegeta - Android Saga - Capsule given in Saga Intro 1")
VEGETA_CAPSULE_5 = LocationData(location_id=238, name="Vegeta - Android Saga - Capsule given in Saga Intro 2")
VEGETA_CAPSULE_6 = LocationData(location_id=239, name="Vegeta - Android Saga - Capsule at West City")
VEGETA_CAPSULE_7 = LocationData(location_id=240, name="Vegeta - Buu Saga - Capsule given in Saga Intro")
VEGETA_CAPSULE_8 = LocationData(location_id=241, name="Vegeta - Buu Saga - Capsule given before Super Saiyan 2 Goku Battle at Plains Marker")
VEGETA_CAPSULE_9 = LocationData(location_id=242, name="Vegeta - Buu Saga - Capsule given after Majin Buu Battle")
VEGETA_CAPSULE_10 = LocationData(location_id=243, name="Vegeta - Buu Saga - Capsule given before Super Buu (Gohan) Battle at Plains Marker")
VEGETA_CAPSULE_11 = LocationData(location_id=244, name="Vegeta - Buu Saga - Super Buu Reward")
VEGETA_CAPSULE_12 = LocationData(location_id=245, name="Vegeta - Buu Saga - Kid Buu Reward")
VEGETA_CAPSULE_13 = LocationData(location_id=246, name="Vegeta - Capsule given upon Completion")
VEGETA_CAPSULE_14 = LocationData(location_id=247, name="Vegeta 2 - Buu Saga - Broly Reward")
VEGETA_CAPSULE_15 = LocationData(location_id=248, name="Vegeta 2 - Extra Saga - Capsule given before Gotenks Battle at World Tournament Marker")
VEGETA_CAPSULE_16 = LocationData(location_id=249, name="Vegeta 2 - Extra Saga - Capsule at ??? Marker")
VEGETA_CAPSULE_17 = LocationData(location_id=250, name="Vegeta 2 - Extra Saga - Goku Reward")
KRILLIN_CAPSULE_1 = LocationData(location_id=251, name="Krillin - Saiyan Saga - Starting Capsule")
KRILLIN_CAPSULE_2 = LocationData(location_id=252, name="Krillin - Saiyan Saga - Capsule at Mountains in Southwest")
KRILLIN_CAPSULE_3 = LocationData(location_id=253, name="Krillin - Namek Saga - Capsule at Guru's House")
KRILLIN_CAPSULE_4 = LocationData(location_id=254, name="Krillin - Namek Saga - Recoome Reward")
KRILLIN_CAPSULE_5 = LocationData(location_id=255, name="Krillin - Namek Saga - Capsule given before Third Form Frieza Battle")
KRILLIN_CAPSULE_6 = LocationData(location_id=256, name="Krillin - Capsule given upon Completion")
KRILLIN_CAPSULE_7 = LocationData(location_id=257, name="Krillin 2 - Android Saga - Capsule at South City")
KRILLIN_CAPSULE_8 = LocationData(location_id=258, name="Krillin 2 - Android Saga - Capsule at West City after Rescuing Android 16 at Plains near World Tournament Ring")
PICCOLO_CAPSULE_1 = LocationData(location_id=259, name="Piccolo - Saiyan Saga - Starting Capsule")
PICCOLO_CAPSULE_2 = LocationData(location_id=260, name="Piccolo - Saiyan Saga - Capsule given before Raditz Battle at Plains Marker")
PICCOLO_CAPSULE_3 = LocationData(location_id=261, name="Piccolo - Saiyan Saga - Capsule at Mountains in Northwest Continent")
PICCOLO_CAPSULE_4 = LocationData(location_id=262, name="Piccolo - Namek Saga - Capsule given in Saga Intro")
PICCOLO_CAPSULE_5 = LocationData(location_id=263, name="Piccolo - Namek Saga - Capsule at ??? in Southwest Island")
PICCOLO_CAPSULE_6 = LocationData(location_id=264, name="Piccolo - Namek Saga - Second Form Frieza Reward")
PICCOLO_CAPSULE_7 = LocationData(location_id=265, name="Piccolo - Android Saga - Capsule at Kami's Lookout")
PICCOLO_CAPSULE_8 = LocationData(location_id=266, name="Piccolo - Android Saga - Capsule given before Android 17 Battle at Kame House")
PICCOLO_CAPSULE_9 = LocationData(location_id=267, name="Piccolo - Android Saga - Android 17 Reward")
PICCOLO_CAPSULE_10 = LocationData(location_id=268, name="Piccolo - Buu Saga - Capsule at Central City after Rescuing Hercule at Desert in Southwest")
PICCOLO_CAPSULE_11 = LocationData(location_id=269, name="Piccolo - Buu Saga - Capsule at Mountains in Northwest Continent")
PICCOLO_CAPSULE_12 = LocationData(location_id=270, name="Piccolo 2 - Namek Saga - Capsule at Rightmost Red Marker after Defeating Second Form Frieza")
TIEN_CAPSULE_1 = LocationData(location_id=271, name="Tien - Saiyan Saga - Starting Capsule")
TIEN_CAPSULE_2 = LocationData(location_id=272, name="Tien - Saiyan Saga - Capsule at Plains near West City")
TIEN_CAPSULE_3 = LocationData(location_id=273, name="Tien - Saiyan Saga - Capsule after Saibamen Battle")
TIEN_CAPSULE_4 = LocationData(location_id=274, name="Tien - Android Saga - Capsule at Kami's Lookout")
YAMCHA_CAPSULE_1 = LocationData(location_id=275, name="Yamcha - Saiyan Saga - Starting Capsule")
YAMCHA_CAPSULE_2 = LocationData(location_id=276, name="Yamcha - Saiyan Saga - Capsule at End of Break-up Side-Story")
YAMCHA_CAPSULE_3 = LocationData(location_id=277, name="Yamcha - Saiyan Saga - Capsule at Plains Red Marker")
YAMCHA_CAPSULE_4 = LocationData(location_id=278, name="Yamcha - Android Saga - Dr Gero Reward")
YAMCHA_CAPSULE_5 = LocationData(location_id=279, name="Yamcha 2 - Saiyan Saga - Capsule after Saibamen Battle")
UUB_CAPSULE_1 = LocationData(location_id=280, name="Uub - Starting Capsule")
BROLY_CAPSULE_1 = LocationData(location_id=281, name="Broly - Starting Capsule")
BROLY_CAPSULE_2 = LocationData(location_id=282, name="Broly - Capsule at Grandpa Gohan's House")
BROLY_CAPSULE_3 = LocationData(location_id=283, name="Broly - Capsule at ??? near Kami's Lookout")
BROLY_CAPSULE_4 = LocationData(location_id=284, name="Broly - Capsule Given Before Gohan 1")
BROLY_CAPSULE_5 = LocationData(location_id=285, name="Broly - Capsule Given upon Completion")
BROLY_CAPSULE_6 = LocationData(location_id=286, name="Broly 2 - Capsule at Plains near Northern Mountains")
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
GOKU_BREAK_IN = LocationData(location_id=300, name="Dragon Arena - Defeat Break-In Challenger - Goku")
KGOKU_BREAK_IN = LocationData(location_id=301, name="Dragon Arena - Defeat Break-In Challenger - Kid Goku")
KGOHAN_BREAK_IN = LocationData(location_id=302, name="Dragon Arena - Defeat Break-In Challenger - Kid Gohan")
TGOHAN_BREAK_IN = LocationData(location_id=303, name="Dragon Arena - Defeat Break-In Challenger - Teen Gohan")
GOHAN_BREAK_IN  = LocationData(location_id=304, name="Dragon Arena - Defeat Break-In Challenger - Gohan")
GTS_BREAK_IN = LocationData(location_id=305, name="Dragon Arena - Defeat Break-In Challenger - Gt Saiyaman")
GOTEN_BREAK_IN = LocationData(location_id=306, name="Dragon Arena - Defeat Break-In Challenger - Goten")
VEGETA_BREAK_IN = LocationData(location_id=307, name="Dragon Arena - Defeat Break-In Challenger - Vegeta")
TRUNKS_BREAK_IN = LocationData(location_id=308, name="Dragon Arena - Defeat Break-In Challenger - Trunks")
KTRUNKS_BREAK_IN = LocationData(location_id=309, name="Dragon Arena - Defeat Break-In Challenger - Kid Trunks")
KRILLIN_BREAK_IN = LocationData(location_id=310, name="Dragon Arena - Defeat Break-In Challenger - Krillin")
PICCOLO_BREAK_IN = LocationData(location_id=311, name="Dragon Arena - Defeat Break-In Challenger - Piccolo")
TIEN_BREAK_IN = LocationData(location_id=312, name="Dragon Arena - Defeat Break-In Challenger - Tien")
YAMCHA_BREAK_IN = LocationData(location_id=313, name="Dragon Arena - Defeat Break-In Challenger - Yamcha")
VIDEL_BREAK_IN = LocationData(location_id=314, name="Dragon Arena - Defeat Break-In Challenger - Videl")
HERCULE_BREAK_IN = LocationData(location_id=315, name="Dragon Arena - Defeat Break-In Challenger - Hercule")
SUPREME_KAI_BREAK_IN = LocationData(location_id=316, name="Dragon Arena - Defeat Break-In Challenger - Supreme Kai")
UUB_BREAK_IN = LocationData(location_id=317, name="Dragon Arena - Defeat Break-In Challenger - Uub")
RADITZ_BREAK_IN = LocationData(location_id=318, name="Dragon Arena - Defeat Break-In Challenger - Raditz")
NAPPA_BREAK_IN = LocationData(location_id=319, name="Dragon Arena - Defeat Break-In Challenger - Nappa")
GINYU_BREAK_IN = LocationData(location_id=320, name="Dragon Arena - Defeat Break-In Challenger - Ginyu")
RECOOME_BREAK_IN = LocationData(location_id=321, name="Dragon Arena - Defeat Break-In Challenger - Recoome")
FRIEZA_BREAK_IN = LocationData(location_id=322, name="Dragon Arena - Defeat Break-In Challenger - Frieza")
ANDROID_16_BREAK_IN = LocationData(location_id=323, name="Dragon Arena - Defeat Break-In Challenger - Android 16")
ANDROID_17_BREAK_IN = LocationData(location_id=324, name="Dragon Arena - Defeat Break-In Challenger - Android 17")
ANDROID_18_BREAK_IN = LocationData(location_id=325, name="Dragon Arena - Defeat Break-In Challenger - Android 18")
DR_GERO_BREAK_IN = LocationData(location_id=326, name="Dragon Arena - Defeat Break-In Challenger - Dr Gero")
CELL_BREAK_IN = LocationData(location_id=327, name="Dragon Arena - Defeat Break-In Challenger - Cell")
MAJIN_BUU_BREAK_IN = LocationData(location_id=328, name="Dragon Arena - Defeat Break-In Challenger - Majin Buu")
SUPER_BUU_BREAK_IN = LocationData(location_id=329, name="Dragon Arena - Defeat Break-In Challenger - Super Buu")
KID_BUU_BREAK_IN = LocationData(location_id=330, name="Dragon Arena - Defeat Break-In Challenger - Kid Buu")
DABURA_BREAK_IN = LocationData(location_id=331, name="Dragon Arena - Defeat Break-In Challenger - Dabura")
COOLER_BREAK_IN = LocationData(location_id=332, name="Dragon Arena - Defeat Break-In Challenger - Cooler")
BARDOCK_BREAK_IN = LocationData(location_id=333, name="Dragon Arena - Defeat Break-In Challenger - Bardock")
BROLY_BREAK_IN = LocationData(location_id=334, name="Dragon Arena - Defeat Break-In Challenger - Broly")
OMEGA_BREAK_IN = LocationData(location_id=335, name="Dragon Arena - Defeat Break-In Challenger - Omega")
SAIBAMEN_BREAK_IN = LocationData(location_id=336, name="Dragon Arena - Defeat Break-In Challenger - Saibamen")
CELL_JR_BREAK_IN = LocationData(location_id=337, name="Dragon Arena - Defeat Break-In Challenger - Cell Jr")

DRAGON_ARENA_LOCS = [
    GOKU_BREAK_IN, KGOKU_BREAK_IN, KGOHAN_BREAK_IN, TGOHAN_BREAK_IN, GOHAN_BREAK_IN, GTS_BREAK_IN, GOTEN_BREAK_IN,
    VEGETA_BREAK_IN, TRUNKS_BREAK_IN, KTRUNKS_BREAK_IN, KRILLIN_BREAK_IN, PICCOLO_BREAK_IN, TIEN_BREAK_IN, YAMCHA_BREAK_IN,
    VIDEL_BREAK_IN, HERCULE_BREAK_IN, SUPREME_KAI_BREAK_IN, UUB_BREAK_IN, RADITZ_BREAK_IN, NAPPA_BREAK_IN, GINYU_BREAK_IN,
    RECOOME_BREAK_IN, FRIEZA_BREAK_IN, ANDROID_16_BREAK_IN, ANDROID_17_BREAK_IN, ANDROID_18_BREAK_IN, DR_GERO_BREAK_IN,
    CELL_BREAK_IN, MAJIN_BUU_BREAK_IN, SUPER_BUU_BREAK_IN, KID_BUU_BREAK_IN, DABURA_BREAK_IN, COOLER_BREAK_IN,
    BARDOCK_BREAK_IN, BROLY_BREAK_IN, OMEGA_BREAK_IN, SAIBAMEN_BREAK_IN, CELL_JR_BREAK_IN
]

# Training Mode Checks
TRAINING_1_COMPLETED = LocationData(location_id=400, name="Training Mode - Complete Training 1")
TRAINING_2_COMPLETED = LocationData(location_id=401, name="Training Mode - Complete Training 2")
TRAINING_3_COMPLETED = LocationData(location_id=402, name="Training Mode - Complete Training 3")
TRAINING_4_COMPLETED = LocationData(location_id=403, name="Training Mode - Complete Training 4")
TRAINING_5_COMPLETED = LocationData(location_id=404, name="Training Mode - Complete Training 5")
TRAINING_6_COMPLETED = LocationData(location_id=405, name="Training Mode - Complete Training 6")
TRAINING_7_COMPLETED = LocationData(location_id=406, name="Training Mode - Complete Training 7")
TRAINING_8_COMPLETED = LocationData(location_id=407, name="Training Mode - Complete Training 8")
TRAINING_9_COMPLETED = LocationData(location_id=408, name="Training Mode - Complete Training 9")
TRAINING_10_COMPLETED = LocationData(location_id=409, name="Training Mode - Complete Training 10")
TRAINING_11_COMPLETED = LocationData(location_id=410, name="Training Mode - Complete Training 11")
TRAINING_12_COMPLETED = LocationData(location_id=411, name="Training Mode - Complete Training 12")

TRAINING_LOCS = [
    TRAINING_1_COMPLETED,TRAINING_2_COMPLETED,TRAINING_3_COMPLETED,TRAINING_4_COMPLETED, TRAINING_5_COMPLETED,
    TRAINING_6_COMPLETED,TRAINING_7_COMPLETED,TRAINING_8_COMPLETED,TRAINING_9_COMPLETED,TRAINING_10_COMPLETED,
    TRAINING_11_COMPLETED,TRAINING_12_COMPLETED
]

# World Tournament Checks
NOVICE_CLEARED = LocationData(location_id=420, name="World Tournament - Novice Tournament Champion")
ADEPT_CLEARED = LocationData(location_id=421, name="World Tournament - Adept Tournament Champion")
ADVANCED_CLEARED = LocationData(location_id=422, name="World Tournament - Advanced Tournament Champion")

WT_LOCS = [
    NOVICE_CLEARED, ADEPT_CLEARED, ADVANCED_CLEARED
]

# Shop Checks
SHOP_ITEMS={}
x = 1
while x < 100:
    SHOP_ITEMS[f"Shop Item {x}"] = 499 + x
    x = x + 1

SHOP_LOCS = []
for key, value in SHOP_ITEMS:
  SHOP_LOCS.append(LocationData(location_id = value, name=key))

LOCATIONS = [
    *DRAGON_WORLD_LOCS,
    *DRAGON_ARENA_LOCS,
    *TRAINING_LOCS,
    *WT_LOCS,
    *SHOP_LOCS
]


def location_name_pairs() -> Dict[str, int]:
    locations = {}
    for location in LOCATIONS:
        locations[location.name] = location.id
    return locations


def location_id_pairs() -> Dict[int, str]:
    locations = {}
    for location in LOCATIONS:
        locations[location.id] = location.name
    return locations


LOC_NAME_PAIRS = location_name_pairs()
LOC_ID_PAIRS = location_id_pairs()


def location_name_to_id(name: str) -> int:
    return LOC_NAME_PAIRS[name]


def location_id_to_name(id: int) -> str:
    return LOC_ID_PAIRS[id]