from abc import ABC
from typing import List


class Instruction(ABC):
    bytes = bytes()
    def __init__(self):
        pass


class Address(ABC):
    start_offset: int = 0x0
    end_offset: int = 0x0
    instructions: List[Instruction] = []
    name: str = ''
    is_function: bool = False
    length: int

    def __init__(self, start_offset, length = 0, name='', is_function=False, instructions: List[Instruction] = []):
        self.start_offset = start_offset
        self.end_offset = start_offset + length 
        self.name = name
        self.is_function = is_function
        self.length = length
        self.instructions = instructions

    @classmethod
    def from_address_list(cls, addresses: List, name=''):
        if addresses:
            start_offset = addresses[0].start_offset
            length = 0
            for addr in addresses:
                length += addr.length
            end_offset = addresses[-1].end_offset
            cls.start_offset = start_offset
            cls.length = length
            cls.end_offset = end_offset
            cls.name = name


class RAMAddress(Address):
    pass


class ROMAddress(Address):
    pass


class Function(Address):
    is_function = True



class Addresses:
    child = None
    
    def __init__(self, game_version: str):
        from .addresses import US, US_GH, PAL, PAL_CE, JP, JP_BS
        match game_version:
            case US.VERSION:
                self.child = US
            case US_GH.VERSION:
                self.child = US_GH
            case PAL.VERSION:
                self.child = PAL
            case PAL_CE.VERSION:
                self.child = PAL_CE
            case JP.VERSION:
                self.child = JP
            case JP_BS.VERSION:
                self.child = JP_BS
            case _:
                self.child = US

    def current_screen(self):
        return self.child.CURRENT_SCREEN

    def p1_hp(self):
        return self.child.P1HP
    
    def p2_hp(self):
        return self.child.P2HP