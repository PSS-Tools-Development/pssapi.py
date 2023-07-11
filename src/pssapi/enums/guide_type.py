from .str_enum_base import StrEnumBase as _StrEnumBase

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class GuideType(_StrEnumBase):
    NONE = "None"
    BUY_CHARACTER = "BuyCharacter"
    BUY_ROOM = "BuyRoom"
    BUY_SHIP = "BuyShip"
    PVP = "PVP"
    START_GUIDE = "StartGuide"
    UPGRADE_CHARACTER = "UpgradeCharacter"
    UPGRADE_ROOM = "UpgradeRoom"
