from enum import IntFlag as _IntFlag

from .int_flag_object_base import IntFlagObjectBase as _IntFlagObjectBase

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class BehaviorFlags(_IntFlag):
    NONE = 0


class BehaviorFlagsObject(_IntFlagObjectBase):
    def __init__(self, behavior_flags: BehaviorFlags):
        super().__init__(behavior_flags)

    @property
    def value(self) -> BehaviorFlags:
        return self._value
