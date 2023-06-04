from enum import IntFlag as _IntFlag

from .int_flag_object_base import IntFlagObjectBase as _IntFlagObjectBase


class GenerationFlags(_IntFlag):
    NONE = 0


class GenerationFlagsObject(_IntFlagObjectBase):
    def __init__(self, generation_flags: GenerationFlags):
        super().__init__(generation_flags)

    @property
    def value(self) -> GenerationFlags:
        return self._value
