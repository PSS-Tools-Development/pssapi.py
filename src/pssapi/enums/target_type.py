from .str_enum_base import StrEnumBase as _StrEnumBase

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class TargetType(_StrEnumBase):
    NONE = "None"
    CRAFT = "Craft"
    RANDOM_ROOM = "RandomRoom"
    SINGLE_ROOM = "SingleRoom"
