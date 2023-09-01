from .str_enum_base import StrEnumBase as _StrEnumBase

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class TriggerType(_StrEnumBase):
    NONE = "None"
    COLLECT_RESOURCES = "CollectResources"
    PV_P = "PvP"
    SCAN_SHIP = "ScanShip"
