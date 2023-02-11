from enum import StrEnum as _StrEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""

class SpecialAbilityType(_StrEnum):
        HEAL_SELF_HP = 'HealSelfHp'
        HEAL_SAME_ROOM_CHARACTERS = 'HealSameRoomCharacters'
        ADD_RELOAD = 'AddReload'
        DEDUCT_RELOAD = 'DeductReload'
        HEAL_ROOM_HP = 'HealRoomHp'
        DAMAGE_TO_ROOM = 'DamageToRoom'
        DAMAGE_TO_SAME_ROOM_CHARACTERS = 'DamageToSameRoomCharacters'
        DAMAGE_TO_CURRENT_ENEMY = 'DamageToCurrentEnemy'
        SET_FIRE = 'SetFire'
        TELEPORT = 'Teleport'
        FREEZE = 'Freeze'
        FIRE_WALK = 'FireWalk'
        CLONE = 'Clone'
        POLYMORPH = 'Polymorph'
        MIMIC = 'Mimic'
        SUMMON = 'Summon'
        INVULNERABILITY = 'Invulnerability'
        PROTECT_ROOM = 'ProtectRoom'
        BLOODLUST = 'Bloodlust'
    