from .str_enum_base import StrEnumBase as _StrEnumBase

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class ActionTypeParameterRelativity(_StrEnumBase):
    NONE = "None"
    ABSOLUTE = "Absolute"
    HIGHEST = "Highest"
    LOWEST = "Lowest"
    PERCENTAGE = "Percentage"
    RELATIVE = "Relative"
