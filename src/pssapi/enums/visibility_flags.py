from enum import IntFlag as _IntFlag

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class VisibilityFlags(_IntFlag):
    NONE = 0
    HIDE_WHEN_NOT_SATISFIED = 1
    SHOW_WHEN_NOT_SATISFIED = 2
    ALWAYS_SHOW = 3
    ALWAYS_HIDE = 4
