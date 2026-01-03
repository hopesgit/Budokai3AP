from abc import ABC
from typing import Optional


class Address(ABC):
    start_offset: int = 0x0
    end_offset: int = 0x0
    instruction: Optional[bytes] = None
    name: str = ''
    is_function: bool = False
    length: int

    def __init__(self, start_offset=0x0, end_offset=0x0, instruction='', name='', is_function=False):
        self.start_offset = start_offset
        self.end_offset = end_offset | start_offset
        self.expected_instruction = instruction
        self.name = name
        self.is_function = is_function
        self.length = end_offset - start_offset


class RAMAddress(Address):
    pass


class ROMAddress(Address):
    pass


class Function(Address):
    is_function = True


Function(start_offset=0x1003e0, instruction=bytes(0x3C02003F), name="Main?")
