from typing import TYPE_CHECKING

from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes

# from .Budokai3Client import Budokai3Context

if TYPE_CHECKING:
    pass

NOP = bytes([0x00, 0x00, 0x00, 0x00])

class Budokai3ProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "DBZ Budokai 3"
    patch_file_ending = '.apdbzb3'
    result_file_ending = '.iso'
    procedure = [
        ('apply_bsdiff4', ["base_patch.bsdiff4"]),
        ("apply_tokens", ["token_data.bin"])
    ]
    md5 = "225b94da75fa16da774e4fcf18f82d0f"

