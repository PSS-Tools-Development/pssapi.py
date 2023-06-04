from enum import IntFlag as _IntFlag

from .int_flag_object_base import IntFlagObjectBase as _IntFlagObjectBase

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class CharacterDesignFlagType(_IntFlag):
    NONE = 0
    IS_CREW = 1
    CAN_CREATE_VIA_PRESTIGE = 2
    IS_PRIZE = 4
    IS_CAPTAIN = 8
    AVAILABLE_IN_DROPSHIP = 16


class CharacterDesignFlagTypeObject(_IntFlagObjectBase):
    def __init__(self, character_design_flag_type: CharacterDesignFlagType):
        super().__init__(character_design_flag_type)

    @property
    def available_in_dropship(self) -> bool:
        return self.value & CharacterDesignFlagType.AVAILABLE_IN_DROPSHIP or False

    @property
    def can_create_via_prestige(self) -> bool:
        return self.value & CharacterDesignFlagType.CAN_CREATE_VIA_PRESTIGE or False

    @property
    def is_captain(self) -> bool:
        return self.value & CharacterDesignFlagType.IS_CAPTAIN or False

    @property
    def is_crew(self) -> bool:
        return self.value & CharacterDesignFlagType.IS_CREW or False

    @property
    def is_prize(self) -> bool:
        return self.value & CharacterDesignFlagType.IS_PRIZE or False

    @property
    def value(self) -> CharacterDesignFlagType:
        return self._value
