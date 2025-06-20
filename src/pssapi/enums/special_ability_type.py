from .str_enum_base import StrEnumBase as _StrEnumBase


"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class SpecialAbilityType(_StrEnumBase):
    NONE = "None"
    ADD_RELOAD = "AddReload"
    """Rush"""
    BLOODLUST = "Bloodlust"
    """Bloodlust"""
    CLONE = "Clone"
    DAMAGE_TO_CURRENT_ENEMY = "DamageToCurrentEnemy"
    """Critical Strike"""
    DAMAGE_TO_ROOM = "DamageToRoom"
    """Ultra Dismantle"""
    DAMAGE_TO_SAME_ROOM_CHARACTERS = "DamageToSameRoomCharacters"
    """Poison Gas"""
    DEDUCT_RELOAD = "DeductReload"
    """System Hack"""
    FIRE_WALK = "FireWalk"
    """Fire walk"""
    FREEZE = "Freeze"
    """Freeze"""
    HEAL_ROOM_HP = "HealRoomHp"
    """Urgent Repair"""
    HEAL_SAME_ROOM_CHARACTERS = "HealSameRoomCharacters"
    """Healing Rain"""
    HEAL_SELF_HP = "HealSelfHp"
    """First Aid"""
    INVULNERABILITY = "Invulnerability"
    """Phase Shift"""
    MIMIC = "Mimic"
    POLYMORPH = "Polymorph"
    PROTECT_ROOM = "ProtectRoom"
    """Stasis Shield"""
    SET_FIRE = "SetFire"
    """Arson"""
    SUMMON = "Summon"
    TELEPORT = "Teleport"
