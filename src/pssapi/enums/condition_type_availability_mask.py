from enum import IntFlag as _IntFlag

from .int_flag_object_base import IntFlagObjectBase as _IntFlagObjectBase


class ConditionTypeAvailabilityMask(_IntFlag):
    NONE = 0
    TARGET_ROOM = 1
    TARGET_CHARACTER = 2


class ConditionTypeAvailabilityMaskObject(_IntFlagObjectBase):
    def __init__(self, character_flags: ConditionTypeAvailabilityMask):
        super().__init__(character_flags)

    @property
    def target_character(self) -> bool:
        return bool(self.value & ConditionTypeAvailabilityMask.TARGET_CHARACTER)

    @property
    def target_room(self) -> bool:
        return bool(self.value & ConditionTypeAvailabilityMask.TARGET_ROOM)

    @property
    def value(self) -> ConditionTypeAvailabilityMask:
        return self._value
