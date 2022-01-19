from enum import StrEnum as _StrEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class ShipStatus(_StrEnum):
    ATTACKING = "Attacking"
    DEFENDING = "Defending"
    OFFLINE = "Offline"
    ONLINE = "Online"
    SEARCHING = "Searching"
