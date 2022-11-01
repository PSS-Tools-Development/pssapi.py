from enum import StrEnum as _StrEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class ConditionTypeComparison(_StrEnum):
    HIGHER = 'Higher'
    LOWER = 'Lower'
    EQUAL = 'Equal'
    HIGHER_PERCENTAGE = 'HigherPercentage'
    LOWER_PERCENTAGE = 'LowerPercentage'
    EQUAL_PERCENTAGE = 'EqualPercentage'
    NOT_EQUAL = 'NotEqual'
    HIGHER_OR_EQUAL_PERCENTAGE = 'HigherOrEqualPercentage'
    LOWER_OR_EQUAL_PERCENTAGE = 'LowerOrEqualPercentage'
