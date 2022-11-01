from enum import StrEnum as _StrEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class ConditionTypeParameter(_StrEnum):
    HP = 'Hp'
    SHIELD = 'Shield'
    COUNT = 'Count'
    FRIENDLY_COUNT = 'FriendlyCount'
    ENEMY_COUNT = 'EnemyCount'
    CLOAKING_DURATION = 'CloakingDuration'
    SYSTEM_DAMAGE = 'SystemDamage'
    HULL_DAMAGE = 'HullDamage'
    STUN_LENGTH = 'StunLength'
    EMP_LENGTH = 'EMPLength'
    CHARACTER_DAMAGE = 'CharacterDamage'
    FIRE_LENGTH = 'FireLength'
    BREACH_CHANCE = 'BreachChance'
    SPEED = 'Speed'
    DIRECT_SYSTEM_DAMAGE = 'DirectSystemDamage'
    SHIELD_DAMAGE = 'ShieldDamage'
    COST = 'Cost'
