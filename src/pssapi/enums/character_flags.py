from enum import IntFlag as _IntFlag

from .int_flag_object_base import IntFlagObjectBase as _IntFlagObjectBase


class CharacterFlags(_IntFlag):
    NONE = 0
    FAVOURITE = 1


class CharacterFlagsObject(_IntFlagObjectBase):
    def __init__(self, character_flags: CharacterFlags):
        super().__init__(character_flags)

    @property
    def favourite(self) -> bool:
        return bool(self.value & CharacterFlags.FAVOURITE)

    @property
    def value(self) -> CharacterFlags:
        return self._value
