from enum import IntFlag as _IntFlag

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class SituationDesignFlag(_IntFlag):
    NONE = 0
    AFFECT_ATTACKING_SHIP = 1
    AFFECT_DEFENDING_SHIP = 2
    AFFECT_PV_P = 4
    AFFECT_PV_E = 8
    VOTES = 16
    AFFECT_TOURNAMENT = 32
