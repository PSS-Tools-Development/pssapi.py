from enum import StrEnum as _StrEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""

class ConditionTypeCategory(_StrEnum):
        YOUR_SHIP = 'YourShip'
        YOUR_ROOM = 'YourRoom'
        YOUR_CHARACTER = 'YourCharacter'
        ENEMY_SHIP = 'EnemyShip'
        ENEMY_ROOM = 'EnemyRoom'
        ENEMY_CHARACTER = 'EnemyCharacter'
        CURRENT = 'Current'
        ENEMY_CRAFT = 'EnemyCraft'
        TARGET_ROOM = 'TargetRoom'
        YOUR_CRAFT = 'YourCraft'
        CURRENT_ROOM = 'CurrentRoom'
        ORIGIN_ROOM = 'OriginRoom'
    