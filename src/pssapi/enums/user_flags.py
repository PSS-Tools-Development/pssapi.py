from enum import IntFlag as _IntFlag

from .int_flag_object_base import IntFlagObjectBase as _IntFlagObjectBase


class UserFlags(_IntFlag):
    NONE = 0
    ALLOW_FORCE_B_TEST = 1


class UserFlagsObject(_IntFlagObjectBase):
    def __init__(self, user_flags: UserFlags):
        super().__init__(user_flags)

    @property
    def allow_force_b_test(self) -> bool:
        return bool(self.value & UserFlags.ALLOW_FORCE_B_TEST)

    @property
    def value(self) -> UserFlags:
        return self._value
