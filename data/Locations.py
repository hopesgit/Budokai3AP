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
