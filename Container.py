import shutil
import hashlib
import mmap
from typing import TYPE_CHECKING, Callable, Any, Optional

from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes

from Budokai3Client import Budokai3Context
from .Budokai3Options import Budokai3Options
from . import MIPS, TextManager

if TYPE_CHECKING:
    from . import Budokai3World

NOP = bytes([0x00, 0x00, 0x00, 0x00])

class Budokai3ProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "DBZ Budokai 3"
    patch_file_ending = '.apdbzb3'
    result_file_ending = '.iso'
    procedure = [
        ("apply_bsdiff4", ["base_patch.bsdiff4"]),
        ("apply_tokens", ["token_data.bin"])
    ]
    md5 = "225b94da75fa16da774e4fcf18f82d0f"


    def __init__(self, ctx: Budokai3Context):