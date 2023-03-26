from enum import StrEnum as _StrEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class TaskCategory(_StrEnum):
    NONE = "None"
    STANDARD = "1"
    COMPETITION = "2"
    GLOBAL = "3"
    BATTLE_PASS_DAILY = "4"
    BATTLE_PASS_SEASON = "5"
    BATTLE_PASS_DAILY_TEMPLATE = "6"
    BATTLE_PASS_SEASON_TEMPLATE = "7"
    BATTLE_PASS_DAILY_REROLL = "8"
