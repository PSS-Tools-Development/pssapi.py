from .str_enum_base import StrEnumBase as _StrEnumBase

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class ExplosionType(_StrEnumBase):
    ALL = "All"
    LINE = "Line"
    RADIUS = "Radius"
    RANDOM = "Random"
    RANDOM_UNIQUE = "RandomUnique"
    SINGLE = "Single"
