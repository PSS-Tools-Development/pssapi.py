from enum import StrEnum as _StrEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class BattleType(_StrEnum):
    ALLIANCE = "Alliance"
    FRIENDLY = "Friendly"
    MISSION = "Mission"
    PVE = "PVE"
    PVP = "PVP"
    PVP_LOCKED = "PVPLocked"
    PVP_REVENGE = "PVPRevenge"
    RAID = "Raid"
