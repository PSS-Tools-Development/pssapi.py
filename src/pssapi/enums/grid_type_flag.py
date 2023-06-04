from enum import IntFlag as _IntFlag

from .int_flag_object_base import IntFlagObjectBase as _IntFlagObjectBase


class GridTypeFlag(_IntFlag):
    NONE = 0
    A = 1
    B = 2


class GridTypeFlagObject(_IntFlagObjectBase):
    def __init__(self, grid_type_flag: GridTypeFlag):
        super().__init__(grid_type_flag)

    @property
    def a(self) -> bool:
        return bool(self.value & GridTypeFlag.A)

    @property
    def b(self) -> bool:
        return bool(self.value & GridTypeFlag.B)

    @property
    def value(self) -> GridTypeFlag:
        return self._value
