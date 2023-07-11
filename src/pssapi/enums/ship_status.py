from .str_enum_base import StrEnumBase as _StrEnumBase

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class ShipStatus(_StrEnumBase):
    ATTACKING = "Attacking"
    DEFENDING = "Defending"
    OFFLINE = "Offline"
    ONLINE = "Online"
    SEARCHING = "Searching"
