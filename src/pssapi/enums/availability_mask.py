from enum import IntFlag as _IntFlag

from .int_flag_object_base import IntFlagObjectBase as _IntFlagObjectBase


class AvailabilityMask(_IntFlag):
    NONE = 0
    PLAYER = 1
    """Available on a player's ship."""
    ALLIANCE = 2
    """Available on a fleet's starbase."""


class AvailabilityMaskObject(_IntFlagObjectBase):
    def __init__(self, availability_mask: AvailabilityMask):
        super().__init__(availability_mask)

    @property
    def player(self) -> bool:
        return bool(self.value & AvailabilityMask.PLAYER)

    @property
    def alliance(self) -> bool:
        return bool(self.value & AvailabilityMask.ALLIANCE)

    @property
    def value(self) -> AvailabilityMask:
        return self._value
