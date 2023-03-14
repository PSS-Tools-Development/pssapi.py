from enum import StrEnum as _StrEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class MessageType(_StrEnum):
    PUBLIC = "Public"
    PRIVATE = "Private"
    SYSTEM = "System"
    ALLIANCE = "Alliance"
    MOMENTS = "Moments"
    MARKET = "Market"
    CATALOG = "Catalog"
    BATTLE = "Battle"
    TOURNAMENT = "Tournament"
    MISSION = "Mission"
    TASK = "Task"
    GLOBAL = "Global"
