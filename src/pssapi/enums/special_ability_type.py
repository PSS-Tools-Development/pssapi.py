from enum import StrEnum as _StrEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class SpecialAbilityType(_StrEnum):
    NONE = "None"
    ADD_RELOAD = "AddReload"
    BLOODLUST = "Bloodlust"
    CLONE = "Clone"
    DAMAGE_TO_CURRENT_ENEMY = "DamageToCurrentEnemy"
    DAMAGE_TO_ROOM = "DamageToRoom"
    DAMAGE_TO_SAME_ROOM_CHARACTERS = "DamageToSameRoomCharacters"
    DEDUCT_RELOAD = "DeductReload"
    FIRE_WALK = "FireWalk"
    FREEZE = "Freeze"
    HEAL_ROOM_HP = "HealRoomHp"
    HEAL_SAME_ROOM_CHARACTERS = "HealSameRoomCharacters"
    HEAL_SELF_HP = "HealSelfHp"
    INVULNERABILITY = "Invulnerability"
    MIMIC = "Mimic"
    POLYMORPH = "Polymorph"
    PROTECT_ROOM = "ProtectRoom"
    SET_FIRE = "SetFire"
    SUMMON = "Summon"
    TELEPORT = "Teleport"
