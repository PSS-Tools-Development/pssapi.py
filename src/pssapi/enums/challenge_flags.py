from enum import IntFlag as _IntFlag

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class ChallengeFlags(_IntFlag):
    NONE = 0
    IS_REAL_TIME = 1
    IS_FIRST_FREE = 2
    IS_SINGLE_PLAY = 4
    IS_MANUAL_COMMAND_ENABLED = 8
