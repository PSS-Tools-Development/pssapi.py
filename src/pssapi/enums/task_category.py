from .str_enum_base import StrEnumBase as _StrEnumBase

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class TaskCategory(_StrEnumBase):
    NONE = "None"
    STANDARD = "Standard"
    COMPETITION = "Competition"
    GLOBAL = "Global"
    BATTLE_PASS_DAILY = "BattlePassDaily"
    BATTLE_PASS_SEASON = "BattlePassSeason"
    BATTLE_PASS_DAILY_TEMPLATE = "BattlePassDailyTemplate"
    BATTLE_PASS_SEASON_TEMPLATE = "BattlePassSeasonTemplate"
    BATTLE_PASS_DAILY_REROLL = "BattlePassDailyReroll"
