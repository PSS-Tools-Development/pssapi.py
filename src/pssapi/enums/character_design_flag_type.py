from enum import IntFlag as _IntFlag

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class CharacterDesignFlagType(_IntFlag):
    NONE = 0
    IS_CREW = 1
    CAN_CREATE_VIA_PRESTIGE = 2
    IS_PRIZE = 4
    IS_CAPTAIN = 8
    AVAILABLE_IN_DROPSHIP = 16
