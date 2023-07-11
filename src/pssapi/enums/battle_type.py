from .str_enum_base import StrEnumBase as _StrEnumBase

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class BattleType(_StrEnumBase):
    ALLIANCE = "Alliance"
    FRIENDLY = "Friendly"
    MISSION = "Mission"
    PVE = "PVE"
    PVP = "PVP"
    PVP_LOCKED = "PVPLocked"
    PVP_REVENGE = "PVPRevenge"
    RAID = "Raid"
