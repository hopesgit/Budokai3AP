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


class RAMAddress(Address):
    pass


class ROMAddress(Address):
    pass


class Function(Address):
    is_function = True


P1HP = RAMAddress(0x497B60, 4, name="P1 HP")
Function(0x1003e0, 16) # runs at all times
