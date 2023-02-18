from enum import StrEnum as _StrEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class RoomStatus(_StrEnum):
    BUILDING = 'Building'
    NORMAL = 'Normal'
    INVENTORY = 'Inventory'
    UPGRADING = 'Upgrading'
