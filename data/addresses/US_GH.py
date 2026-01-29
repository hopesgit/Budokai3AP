from ..Addresses import RAMAddress, Function, ROMAddress, Address

VERSION = "SLUS-20998GH"

CURRENT_SCREEN = RAMAddress(0x46a5b0, 2, "Current Screen")
DU_GOKU_X_COORD = RAMAddress(0x49d260, 4) # read as float
DU_GOKU_Y_COORD = RAMAddress(0x49d268, 4) # read as float
DU_GOKU_SAGA = RAMAddress(0x49d27c, 1, "DU: Goku's Saga")
# 0x00 for Saiyan, 0x01 for Namek, 0x02 for Android, 0x03 for Buu
DU_GOKU_DBS = RAMAddress(0x49d284, 1, "DU: Goku's Dragon Ball collection")
# E7654321 (bit order)
DU_GOKU_RADAR = RAMAddress(0x49d285, 1, "DU: Goku has radar?")
# 0x00 for no, 0x01 for yes
DU_GOKU_LEVEL = RAMAddress(0x49d287, 1, "DU: Goku's Level")
DU_GOKU_HEALTH = RAMAddress(0x49d288, 1, "DU: Goku's Health stat")
DU_GOKU_KI = RAMAddress(0x49d289, 1)
DU_GOKU_ATTACK = RAMAddress(0x49d28a, 1)
DU_GOKU_GUARD = RAMAddress(0x49d28b, 1)
DU_GOKU_ARTS = RAMAddress(0x49d28d, 1)
DU_GOKU_COM = RAMAddress(0x49d28e, 1)
DU_GOKU_SLOT1 = RAMAddress(0x49d290, 2)
DU_GOKU_SLOT2 = RAMAddress(0x49d292, 2)
DU_GOKU_SLOT3 = RAMAddress(0x49d294, 2)
DU_GOKU_SLOT4 = RAMAddress(0x49d296, 2)
DU_GOKU_SLOT5 = RAMAddress(0x49d298, 2)
DU_GOKU_SLOT6 = RAMAddress(0x49d29a, 2)
DU_GOKU_SLOT7 = RAMAddress(0x49d29c, 2)
# slots are weird. if something takes up more than one slot, 
# the next capsule still uses the spot that is "skipped"

DU_UUB_X_COORD = RAMAddress(0x4b0570, 4)
DU_UUB_Y_COORD = RAMAddress(0x4b0578, 4)