from typing import NamedTuple, Optional, Callable, Dict, Any
from Items import GRAY_CAPSULES
from ..Logic import *

class LocationData(NamedTuple):
    location_id: Optional[int]
    name: str
    access_rule: Optional[Callable[[CollectionState, int], bool]] = None
    checked_flag_address: Optional[Callable[["Addresses"], int]] = None
    enable_if: Optional[Callable[[Dict[str, Any]], bool]] = None
    is_vendor: bool = False

# todo: add all capsule locations?
# Dragon World Checks
## Goku
### Saiyan Saga
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

## Kid Gohan
KGOHAN_PICCOLO_CLEAR = LocationData(location_id=23, name="Kid Gohan - Saiyan Saga - Defeat Piccolo")
KGOHAN_SAIBAMEN_CLEAR = LocationData(location_id=24, name="Kid Gohan - Saiyan Saga - Defeat Saibamen")
KGOHAN_NAPPA_CLEAR = LocationData(location_id=25, name="Kid Gohan - Saiyan Saga - Defeat Nappa")
KGOHAN_RECOOME_CLEAR = LocationData(location_id=26, name="Kid Gohan - Namek Saga - Defeat Recoome")
KGOHAN_FRIEZA_CLEAR = LocationData(location_id=27, name="Kid Gohan - Namek Saga - Defeat Third Form Frieza")
KGOHAN_GOKU_CLEAR = LocationData(location_id=28, name="Kid Gohan 2 - Saiyan Saga - Defeat Goku")
KGOHAN_GINYU_GOKU_CLEAR = LocationData(location_id=29, name="Kid Gohan 2 - Namek Saga - Defeat Goku w/ Scouter")
KGOHAN_COOLER_CLEAR = LocationData(location_id=30, name="Kid Gohan 2 - Namek Saga - Defeat Cooler")

## Teen Gohan
TGOHAN_PICCOLO_CLEAR = LocationData(location_id=31, name="Teen Gohan - Defeat Piccolo")
TGOHAN_KRILLIN_CLEAR = LocationData(location_id=32, name="Teen Gohan - Defeat Krillin")
TGOHAN_GOKU_CLEAR = LocationData(location_id=33, name="Teen Gohan - Defeat Super Saiyan Goku")
TGOHAN_CELL_1_CLEAR = LocationData(location_id=34, name="Teen Gohan - Defeat Perfect Cell")
TGOHAN_CELL_2_CLEAR = LocationData(location_id=35, name="Teen Gohan - Defeat Super Perfect Cell")
TGOHAN_TIEN_CLEAR = LocationData(location_id=36, name="Teen Gohan 2 - Defeat Tien")
TGOHAN_YAMCHA_CLEAR = LocationData(location_id=37, name="Teen Gohan 2 - Defeat Yamcha")

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

## Krillin
KRILLIN_SAIBAMEN_CLEAR = LocationData(location_id=65, name="Krillin - Saiyan Saga - Defeat Saibamen")
KRILLIN_NAPPA_CLEAR = LocationData(location_id=66, name="Krillin - Saiyan Saga - Defeat Nappa")
KRILLIN_RECOOME_CLEAR = LocationData(location_id=67, name="Krillin - Namek Saga - Defeat Recoome")
KRILLIN_GINYU_GOKU_CLEAR = LocationData(location_id=68, name="Krillin - Namek Saga - Defeat Goku w/ Scouter")
KRILLIN_FRIEZA_1_CLEAR = LocationData(location_id=69, name="Krillin - Namek Saga - Defeat Second Form Frieza")
KRILLIN_FRIEZA_2_CLEAR = LocationData(location_id=70, name="Krillin - Namek Saga - Defeat Final Form Frieza")
KRILLIN_CELL_CLEAR = LocationData(location_id=71, name="Krillin 2 - Android Saga - Defeat Perfect Form Cell")

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

## Tien
TIEN_SAIBAMEN_CLEAR = LocationData(location_id=90, name="Tien - Saiyan Saga - Defeat Saibamen")
TIEN_NAPPA_CLEAR = LocationData(location_id=91, name="Tien - Saiyan Saga - Defeat Nappa")
TIEN_CELL_CLEAR = LocationData(location_id=92, name="Tien - Android Saga - Defeat Second Form Cell")
TIEN_CELL_JR_CLEAR = LocationData(location_id=93, name="Tien - Android Saga - Defeat Cell Jr")
TIEN_SUPER_BUU_CLEAR = LocationData(location_id=94, name="Tien - Buu Saga - Defeat Super Buu (Gotenks)")
TIEN_YAMCHA_CLEAR = LocationData(location_id=95, name="Tien 2 - Extra Saga - Defeat Yamcha")

## Yamcha
YAMCHA_SAIBAMEN_CLEAR = LocationData(location_id=96, name="Yamcha - Saiyan Saga - Defeat Saibamen")
YAMCHA_DR_GERO_CLEAR = LocationData(location_id=97, name="Yamcha - Android Saga - Defeat Dr Gero")
YAMCHA_TIEN_CLEAR = LocationData(location_id=98, name="Yamcha - Extra Saga - Defeat Tien")
YAMCHA_VEGETA_CLEAR = LocationData(location_id=99, name="Yamcha 2 - Extra Saga - Defeat Vegeta")

## Uub
UUB_GOKU_1_CLEAR = LocationData(location_id=100, name="Uub - Defeat Goku at World Tournament")
UUB_VEGETA_CLEAR = LocationData(location_id=101, name="Uub - Defeat Vegeta")
UUB_MAJIN_BUU_CLEAR = LocationData(location_id=102, name="Uub - Defeat Majin Buu")
UUB_GOKU_2_CLEAR = LocationData(location_id=103, name="Uub - Defeat Goku at Archipelago")
UUB_OMEGA_SHENRON_CLEAR = LocationData(location_id=104, name="Uub - Defeat Omega Shenron")

## Broly
BROLY_KRILLIN_CLEAR = LocationData(location_id=105, name="Broly - Defeat Krillin")
BROLY_PICCOLO_CLEAR_= LocationData(location_id=106, name="Broly - Defeat Piccolo")
BROLY_VEGETA_CLEAR = LocationData(location_id=107, name="Broly - Defeat Vegeta")
BROLY_VIDEL_CLEAR = LocationData(location_id=108, name="Broly - Defeat Videl")
BROLY_KID_TRUNKS_CLEAR = LocationData(location_id=109, name="Broly - Defeat Kid Trunks")
BROLY_GOTEN_CLEAR = LocationData(location_id=110, name="Broly - Defeat Goten")
BROLY_GOHAN_1_CLEAR = LocationData(location_id=111, name="Broly - Defeat Gohan 1")
BROLY_GOHAN_2_CLEAR = LocationData(location_id=112, name="Broly - Defeat Gohan 2")
BROLY_GOKU_CLEAR = LocationData(location_id=113, name="Broly 2 - Defeat Goku")

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

## Difficulty-related
VERY_HARD_CLEAR = LocationData(location_id=135, name="Clear DW on Very Hard")
Z1_CLEAR = LocationData(location_id=136, name="Clear DW on Z1")
Z2_CLEAR = LocationData(location_id=137, name="Clear DW on Z2")
Z3_CLEAR = LocationData(location_id=138, name="Clear DW on Z3")

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

## DW Static Capsules
GOKU_CAPSULE_1 = LocationData(location_id=, name="Goku - Saiyan Saga - Starting Capsule")
GOKU_CAPSULE_2 = LocationData(location_id=, name="Goku - Saiyan Saga - Capsule at Plains Marker")
GOKU_CAPSULE_3 = LocationData(location_id=, name="Goku - Saiyan Saga - Capsule at Plains")
GOKU_CAPSULE_4 = LocationData(location_id=, name="Goku - Saiyan Saga - Vegeta Reward")
GOKU_CAPSULE_5 = LocationData(location_id=, name="Goku - Namek Saga - Capsule at Capsule House")
GOKU_CAPSULE_6 = LocationData(location_id=, name="Goku - Namek Saga - Recoome Reward 1")
GOKU_CAPSULE_7 = LocationData(location_id=, name="Goku - Namek Saga - Recoome Reward 2")
GOKU_CAPSULE_8 = LocationData(location_id=, name="Goku - Namek Saga - Ginyu Reward")
GOKU_CAPSULE_9 = LocationData(location_id=, name="Goku - Namek Saga - Capsule given before 100% Final Power Frieza Battle")
GOKU_CAPSULE_10 = LocationData(location_id=, name="Goku - Namek Saga - 100% Full Power Frieza Reward")
GOKU_CAPSULE_11 = LocationData(location_id=, name="Goku - Android Saga - Capsule at Plains near Cell Ring")
GOKU_CAPSULE_12 = LocationData(location_id=, name="Goku - Android Saga - Capsule near Baba's House")
GOKU_CAPSULE_13 = LocationData(location_id=, name="Goku - Android Saga - Perfect Form Cell Reward")
GOKU_CAPSULE_14 = LocationData(location_id=, name="Goku - Buu Saga - Capsule given in Saga Intro")
GOKU_CAPSULE_15 = LocationData(location_id=, name="Goku - Buu Saga - Capsule at Forest near West City")
GOKU_CAPSULE_16 = LocationData(location_id=, name="Goku - Buu Saga - Capsule at North City")
GOKU_CAPSULE_17 = LocationData(location_id=, name="Goku - Buu Saga - Capsule given before Majin Buu Battle")
GOKU_CAPSULE_18 = LocationData(location_id=, name="Goku - Buu Saga - Majin Buu Reward")
GOKU_CAPSULE_19 = LocationData(location_id=, name="Goku - Buu Saga - Capsule given before Super Buu (Gohan) Battle at ??? Marker")
GOKU_CAPSULE_20 = LocationData(location_id=, name="Goku - Buu Saga - Super Buu (Gohan) Reward")
GOKU_CAPSULE_21 = LocationData(location_id=, name="Goku - Buu Saga - Super Buu Reward")
GOKU_CAPSULE_22 = LocationData(location_id=, name="Goku - Buu Saga - Kid Buu Reward")
GOKU_CAPSULE_23 = LocationData(location_id=, name="Goku - Extra Saga - Capsule at ??? in SE Islands")
GOKU_CAPSULE_24 = LocationData(location_id=, name="Goku - Extra Saga - Uub Reward")
GOKU_CAPSULE_25 = LocationData(location_id=, name="Goku 2 - Saiyan Saga - Capsule at Saiyan's Spaceship near East City")
GOKU_CAPSULE_26 = LocationData(location_id=, name="Goku 2 - Saiyan Saga - Capsule at Grandpa Gohan's House")
GOKU_CAPSULE_27 = LocationData(location_id=, name="Goku 2 - Saiyan Saga - Capsule at Korin's Tower")
GOKU_CAPSULE_28 = LocationData(location_id=, name="Goku 2 - Namek Saga - Capsule at ??? on Lone Central Island")
GOKU_CAPSULE_29 = LocationData(location_id=, name="Goku 2 - Namek Saga - Capsule at Namek Village in Southwest Continent")
GOKU_CAPSULE_30 = LocationData(location_id=, name="Goku 2 - Namek Saga - Capsule given at ??? Marker after Cooler Battle")
GOKU_CAPSULE_31 = LocationData(location_id=, name="Goku 2 - Namek Saga - Cooler Reward (Cooler Battle after Vegeta Battle)")
GOKU_CAPSULE_32 = LocationData(location_id=, name="Goku 2 - Buu Saga - Broly Reward")
GOKU_CAPSULE_33 = LocationData(location_id=, name="Goku 2 - Extra Saga - Capsule given before Gotenks Battle at World Tournament")
GOKU_CAPSULE_34 = LocationData(location_id=, name="Goku 2 - Extra Saga - Capsule given before Omega Shenron Battle at Central City")
GOKU_CAPSULE_35 = LocationData(location_id=, name="Goku 2 - Extra Saga - Omega Shenron Reward")
"Kid Gohan - Saiyan Saga - Capsule at Mountains near Baba's Palace"
"Kid Gohan - Namek Saga - Capsule at Guru's House"
"Kid Gohan - Namek Saga - Recoome Reward"
"Kid Gohan - Namek Saga - Capsule given upon Completion"
"Kid Gohan 2 - Saiyan Saga - Goku Reward"
"Teen Gohan - Starting Capsule"
"Teen Gohan - Capsule at Central City"
"Teen Gohan - Capsule at Kami's Lookout"
"Teen Gohan - Capsule 1 at Cell Ring"
"Teen Gohan - Capsule 2 at Cell Ring"
"Teen Gohan - Super Perfect Cell Reward"
"Teen Gohan - Capsule given upon Completion"
"Teen Gohan 2 - Chi-Chi's Wish Capsule at Goku's House"
"Gohan - Starting Capsule 1"
"Gohan - Starting Capsule 2"
"Gohan - Capsule at Goku's House 1"
"Gohan - Goten Reward"
"Gohan - Capsule at End of Videl Story Quests"
"Gohan - Capsule at Mountains Marker near Babidi's Spaceship"
"Gohan - Capsule at Goku's House 2"
"Gohan - Dabura Reward"
"Gohan - Capsule given before Majin Buu Battle at Forest Marker"
"Gohan - Capsule given after Majin Buu Battle"
"Gohan - Capsule at ??? in Snowy Continent"
"Gohan - Capsule given upon Completion"
"Gohan 2 - Capsule at Plains near Central City"
"Gohan 2 - Capsule at Forest North of Kami's Lookout"
"Vegeta - Saiyan Saga - Starting Capsule"
"Vegeta - Namek Saga - Capsule at Planet Namek in Northwest Continent"
"Vegeta - Namek Saga - Recoome Reward"
"Vegeta - Android Saga - Capsule given in Saga Intro 1"
"Vegeta - Android Saga - Capsule given in Saga Intro 2"
"Vegeta - Android Saga - Capsule at West City"
"Vegeta - Buu Saga - Capsule given in Saga Intro"
"Vegeta - Buu Saga - Capsule given before Super Saiyan 2 Goku Battle at Plains Marker"
"Vegeta - Buu Saga - Capsule given after Majin Buu Battle"
"Vegeta - Buu Saga - Capsule given before Super Buu (Gohan) Battle at Plains Marker"
"Vegeta - Buu Saga - Super Buu Reward"
"Vegeta - Buu Saga - Kid Buu Reward"
"Vegeta - Capsule given upon Completion"
"Vegeta 2 - Buu Saga - Broly Reward"
"Vegeta 2 - Extra Saga - Capsule given before Gotenks Battle at World Tournament Marker"
"Vegeta 2 - Extra Saga - Capsule at ??? Marker"
"Vegeta 2 - Extra Saga - Goku Reward"
"Krillin - Saiyan Saga - Starting Capsule"
"Krillin - Saiyan Saga - Capsule at Mountains in Southwest"
"Krillin - Namek Saga - Capsule at Guru's House"
"Krillin - Namek Saga - Recoome Reward"
"Krillin - Namek Saga - Capsule given before Third Form Frieza Battle"
"Krillin - Capsule given upon Completion"
"Krillin 2 - Android Saga - Capsule at South City"
"Krillin 2 - Android Saga - Capsule at West City after Rescuing Android 16 at Plains near World Tournament Ring"
"Piccolo - Saiyan Saga - Starting Capsule"
"Piccolo - Saiyan Saga - Capsule given before Raditz Battle at Plains Marker"
"Piccolo - Saiyan Saga - Capsule at Mountains in Northwest Continent"
"Piccolo - Namek Saga - Capsule given in Saga Intro"
"Piccolo - Namek Saga - Capsule at ??? in Southwest Island"
"Piccolo - Namek Saga - Second Form Frieza Reward"
"Piccolo - Android Saga - Capsule at Kami's Lookout"
"Piccolo - Android Saga - Capsule given before Android 17 Battle at Kame House"
"Piccolo - Android Saga - Android 17 Reward"
"Piccolo - Buu Saga - Capsule at Central City after Rescuing Hercule at Desert in Southwest"
"Piccolo - Buu Saga - Capsule at Mountains in Northwest Continent"
"Piccolo 2 - Namek Saga - Capsule at Rightmost Red Marker after Defeating Second Form Frieza"
"Tien - Saiyan Saga - Starting Capsule"
"Tien - Saiyan Saga - Capsule at Plains near West City"
"Tien - Saiyan Saga - Capsule after Saibamen Battle"
"Tien - Android Saga - Capsule at Kami's Lookout"
"Yamcha - Saiyan Saga - Starting Capsule"
"Yamcha - Saiyan Saga - Capsule at End of Break-up Side-Story"
"Yamcha - Saiyan Saga - Capsule at Plains Red Marker"
"Yamcha - Android Saga - Dr Gero Reward"
"Yamcha 2 - Saiyan Saga - Capsule after Saibamen Battle"
"Uub - Starting Capsule"
"Broly - Starting Capsule"
"Broly - Capsule at Grandpa Gohan's House"
"Broly - Capsule at ??? near Kami's Lookout"
"Broly - Capsule Given Before Gohan 1"
"Broly - Capsule Given upon Completion"
"Broly 2 - Capsule at Plains near Northern Mountains"
### everything else are random capsules. Some of these locations give a specified capsule once and then a random capsule afterward

# Dragon Arena Checks
GOKU_BREAK_IN = LocationData(location_id=200, name="Dragon Arena - Defeat Break-In Challenger - Goku")
KGOKU_BREAK_IN = LocationData(location_id=201, name="Dragon Arena - Defeat Break-In Challenger - Kid Goku")
KGOHAN_BREAK_IN = LocationData(location_id=202, name="Dragon Arena - Defeat Break-In Challenger - Kid Gohan")
TGOHAN_BREAK_IN = LocationData(location_id=203, name="Dragon Arena - Defeat Break-In Challenger - Teen Gohan")
GOHAN_BREAK_IN  = LocationData(location_id=204, name="Dragon Arena - Defeat Break-In Challenger - Gohan")
GTS_BREAK_IN = LocationData(location_id=205, name="Dragon Arena - Defeat Break-In Challenger - Gt Saiyaman")
GOTEN_BREAK_IN = LocationData(location_id=206, name="Dragon Arena - Defeat Break-In Challenger - Goten")
VEGETA_BREAK_IN = LocationData(location_id=207, name="Dragon Arena - Defeat Break-In Challenger - Vegeta")
TRUNKS_BREAK_IN = LocationData(location_id=208, name="Dragon Arena - Defeat Break-In Challenger - Trunks")
KTRUNKS_BREAK_IN = LocationData(location_id=209, name="Dragon Arena - Defeat Break-In Challenger - Kid Trunks")
KRILLIN_BREAK_IN = LocationData(location_id=210, name="Dragon Arena - Defeat Break-In Challenger - Krillin")
PICCOLO_BREAK_IN = LocationData(location_id=211, name="Dragon Arena - Defeat Break-In Challenger - Piccolo")
TIEN_BREAK_IN = LocationData(location_id=212, name="Dragon Arena - Defeat Break-In Challenger - Tien")
YAMCHA_BREAK_IN = LocationData(location_id=213, name="Dragon Arena - Defeat Break-In Challenger - Yamcha")
VIDEL_BREAK_IN = LocationData(location_id=214, name="Dragon Arena - Defeat Break-In Challenger - Videl")
HERCULE_BREAK_IN = LocationData(location_id=215, name="Dragon Arena - Defeat Break-In Challenger - Hercule")
SUPREME_KAI_BREAK_IN = LocationData(location_id=216, name="Dragon Arena - Defeat Break-In Challenger - Supreme Kai")
UUB_BREAK_IN = LocationData(location_id=217, name="Dragon Arena - Defeat Break-In Challenger - Uub")
RADITZ_BREAK_IN = LocationData(location_id=218, name="Dragon Arena - Defeat Break-In Challenger - Raditz")
NAPPA_BREAK_IN = LocationData(location_id=219, name="Dragon Arena - Defeat Break-In Challenger - Nappa")
GINYU_BREAK_IN = LocationData(location_id=220, name="Dragon Arena - Defeat Break-In Challenger - Ginyu")
RECOOME_BREAK_IN = LocationData(location_id=221, name="Dragon Arena - Defeat Break-In Challenger - Recoome")
FRIEZA_BREAK_IN = LocationData(location_id=222, name="Dragon Arena - Defeat Break-In Challenger - Frieza")
ANDROID_16_BREAK_IN = LocationData(location_id=223, name="Dragon Arena - Defeat Break-In Challenger - Android 16")
ANDROID_17_BREAK_IN = LocationData(location_id=224, name="Dragon Arena - Defeat Break-In Challenger - Android 17")
ANDROID_18_BREAK_IN = LocationData(location_id=225, name="Dragon Arena - Defeat Break-In Challenger - Android 18")
DR_GERO_BREAK_IN = LocationData(location_id=226, name="Dragon Arena - Defeat Break-In Challenger - Dr Gero")
CELL_BREAK_IN = LocationData(location_id=227, name="Dragon Arena - Defeat Break-In Challenger - Cell")
MAJIN_BUU_BREAK_IN = LocationData(location_id=228, name="Dragon Arena - Defeat Break-In Challenger - Majin Buu")
SUPER_BUU_BREAK_IN = LocationData(location_id=229, name="Dragon Arena - Defeat Break-In Challenger - Super Buu")
KID_BUU_BREAK_IN = LocationData(location_id=230, name="Dragon Arena - Defeat Break-In Challenger - Kid Buu")
DABURA_BREAK_IN = LocationData(location_id=231, name="Dragon Arena - Defeat Break-In Challenger - Dabura")
COOLER_BREAK_IN = LocationData(location_id=232, name="Dragon Arena - Defeat Break-In Challenger - Cooler")
BARDOCK_BREAK_IN = LocationData(location_id=233, name="Dragon Arena - Defeat Break-In Challenger - Bardock")
BROLY_BREAK_IN = LocationData(location_id=234, name="Dragon Arena - Defeat Break-In Challenger - Broly")
OMEGA_BREAK_IN = LocationData(location_id=235, name="Dragon Arena - Defeat Break-In Challenger - Omega")
SAIBAMEN_BREAK_IN = LocationData(location_id=236, name="Dragon Arena - Defeat Break-In Challenger - Saibamen")
CELL_JR_BREAK_IN = LocationData(location_id=237, name="Dragon Arena - Defeat Break-In Challenger - Cell Jr")


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

# World Tournament Checks
NOVICE_CLEARED = LocationData(location_id=420, name="World Tournament - Novice Tournament Champion")
ADEPT_CLEARED = LocationData(location_id=421, name="World Tournament - Adept Tournament Champion")
ADVANCED_CLEARED = LocationData(location_id=422, name="World Tournament - Advanced Tournament Champion")
