from .str_enum_base import StrEnumBase as _StrEnumBase

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class ConditionTypeCategory(_StrEnumBase):
    NONE = "None"
    CURRENT = "Current"
    CURRENT_ROOM = "CurrentRoom"
    ENEMY_CHARACTER = "EnemyCharacter"
    ENEMY_CRAFT = "EnemyCraft"
    ENEMY_ROOM = "EnemyRoom"
    ENEMY_SHIP = "EnemyShip"
    ORIGIN_ROOM = "OriginRoom"
    TARGET_ROOM = "TargetRoom"
    YOUR_CHARACTER = "YourCharacter"
    YOUR_CRAFT = "YourCraft"
    YOUR_ROOM = "YourRoom"
    YOUR_SHIP = "YourShip"
