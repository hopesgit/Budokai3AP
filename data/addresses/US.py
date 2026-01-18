from ..Addresses import RAMAddress, Function, ROMAddress, Address

VERSION = "SLUS-20998"

P1HP = RAMAddress(0x497B60, 4, name="P1 HP")
P1Ki = RAMAddress(0x497B70, 4, name="P1 Ki")
P2HP = RAMAddress(0x499B80, 4, name="P2 HP")
P2Ki = RAMAddress(0x499B90, 4, name="P2 Ki")
# until mentioned otherwise, vals are 00 when unpressed, FF when pressed
Controller_DPad_Right = RAMAddress(0x492EC8, 1, name="Dpad Right")
Controller_DPad_Left = RAMAddress(0x492EC9, 1, name="Dpad Left")
Controller_DPad_Up = RAMAddress(0x492ECA, 1, name="Dpad Up")
Controller_DPad_Down = RAMAddress(0x492ECB, 1, name="Dpad Down")
dpad = [Controller_DPad_Right, Controller_DPad_Left, Controller_DPad_Up, Controller_DPad_Down]
Controller_DPad = RAMAddress.from_address_list(dpad, name="Dpad")

Controller_Triangle = RAMAddress(0x492ECC, 1, name="Triangle")
Controller_Circle = RAMAddress(0x492ECD, 1, name="Circle")
Controller_Cross = RAMAddress(0x492ECE, 1, name="Cross")
Controller_Square = RAMAddress(0x492ECF, 1, name="Square")
face = [Controller_Triangle, Controller_Circle, Controller_Cross, Controller_Square]
Controller_Face_Buttons = RAMAddress.from_address_list(face, name="Face Buttons")

Controller_L1 = RAMAddress(0x492ED0, 1, name="L1")
Controller_R1 = RAMAddress(0x492ED1, 1, name="R1")
Controller_L2 = RAMAddress(0x492ED2, 1, name="L2")
Controller_R2 = RAMAddress(0x492ED3, 1, name="R2")
top = [Controller_L1, Controller_R1, Controller_L2, Controller_R2]
Controller_Shoulder_Buttons = RAMAddress.from_address_list(top, name="Shoulder Buttons")

Controller_Select = RAMAddress(0x492EC2, 1, name="Select") # When Sel is pressed, val changes from FF to FE
Controller_Start = RAMAddress(0x492EC2, 1, name="Start") # When Sta is presser, value changes from FF to F7
Controller_L3 = RAMAddress(0x492EC2, 1, name="L3") # value is normally FF; while pressed, it becomes FD
Controller_R3 = RAMAddress(0x492EC2, 1, name="R3") # value is normally FF; while pressed, it becomes FB
# Sel + Start is a reset hotkey in PCSX2. Don't press that without intent.
# L3 plus R3? 0x492EC2 is F9
# L3 plus R3 plus Select? F8
# L3 plus R3 plus Start? F1

Controller_RStick = RAMAddress(0x492EC4, 2, name="Right Stick") # value is 7F7F;
# Left-right movment is stored in 0x492EC4; leftward moves toward 00 while rightward moves toward FF
# Up-down movement is stored in 0x492EC5; upward moves toward 00 and downwards moves toward FF
Controller_LStick = RAMAddress(0x492EC6, 2, name="Left Stick") # value is 7F7F; 
# Left-right movement is stored in 0x492EC6; leftward moves toward 00 while rightward moves toward FF
# Up-down movement is stored in 0x492EC7; upward moves toward 00 and downwards moves toward FF


CURRENT_SCREEN = RAMAddress(0x4B4B40, 16, name="Current Screen")
Function(0x1003e0, 16) # runs at all times