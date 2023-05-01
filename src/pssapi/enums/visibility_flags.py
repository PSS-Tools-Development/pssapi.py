from enum import IntEnum as _IntEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class VisibilityFlags(_IntEnum):
    NONE = 0
    HIDE_WHEN_NOT_SATISFIED = 1
    SHOW_WHEN_NOT_SATISFIED = 2
    ALWAYS_SHOW = 3
    ALWAYS_HIDE = 4
