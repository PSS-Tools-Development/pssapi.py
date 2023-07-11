from .str_enum_base import StrEnumBase as _StrEnumBase

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class ConditionTypeComparison(_StrEnumBase):
    EQUAL = "Equal"
    EQUAL_PERCENTAGE = "EqualPercentage"
    HIGHER = "Higher"
    HIGHER_OR_EQUAL_PERCENTAGE = "HigherOrEqualPercentage"
    HIGHER_PERCENTAGE = "HigherPercentage"
    LOWER = "Lower"
    LOWER_OR_EQUAL_PERCENTAGE = "LowerOrEqualPercentage"
    LOWER_PERCENTAGE = "LowerPercentage"
    NOT_EQUAL = "NotEqual"
