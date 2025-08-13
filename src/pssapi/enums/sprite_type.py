from enum import IntEnum as _IntEnum


"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class SpriteType(_IntEnum):
    NONE = 0
    INTERIOR = 1
    EXTERIOR = 2
    INTERIOR_DESTROYED = 3
    EXTERIOR_DESTROYED = 4
    INTERIOR_ACTIVATE = 5
    EXTERIOR_ACTIVATE = 6
    LOADING = 7
