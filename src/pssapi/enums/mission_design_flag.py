from enum import IntFlag as _IntFlag

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class MissionDesignFlag(_IntFlag):
    NONE = 0
    HIDE_WHEN_REQUIREMENT_NOT_SATISFIED = 1
    GALAXY_EXCLUSIVE = 2
    SHOWN_WHEN_UNEXPLORED = 4
    DISABLE_HP_CHECK = 8
    VOTES = 16
    IGNORE_STAR_SYSTEM = 32
