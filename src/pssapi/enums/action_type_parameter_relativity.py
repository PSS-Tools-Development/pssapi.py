from enum import StrEnum as _StrEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class ActionTypeParameterRelativity(_StrEnum):
    RELATIVE = "Relative"
    ABSOLUTE = "Absolute"
    PERCENTAGE = "Percentage"
    HIGHEST = "Highest"
    LOWEST = "Lowest"
