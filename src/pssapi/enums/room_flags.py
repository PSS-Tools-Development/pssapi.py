from enum import IntFlag as _IntFlag

from .int_flag_object_base import IntFlagObjectBase as _IntFlagObjectBase


class RoomFlags(_IntFlag):
    NONE = 0
    REQUIRE_POWER = 1
    REQUIRE_TARGET = 2
    REQUIRE_ITEM = 4
    ALLOW_DESIGN_SWITCH = 8
    DISPLAY_WHEN_MISSING_REQUIREMENTS = 16
    DONT_ALLOW_UPGRADE = 32


class RoomFlagsObject(_IntFlagObjectBase):
    def __init__(self, room_flags: RoomFlags):
        super().__init__(room_flags)

    @property
    def allow_design_switch(self) -> bool:
        return bool(self.value & RoomFlags.ALLOW_DESIGN_SWITCH)

    @property
    def display_when_missing_requirements(self) -> bool:
        return bool(self.value & RoomFlags.DISPLAY_WHEN_MISSING_REQUIREMENTS)

    @property
    def dont_allow_upgrade(self) -> bool:
        return bool(self.value & RoomFlags.DONT_ALLOW_UPGRADE)

    @property
    def require_item(self) -> bool:
        return bool(self.value & RoomFlags.REQUIRE_ITEM)

    @property
    def require_power(self) -> bool:
        return bool(self.value & RoomFlags.REQUIRE_POWER)

    @property
    def require_target(self) -> bool:
        return bool(self.value & RoomFlags.REQUIRE_TARGET)

    @property
    def value(self) -> RoomFlags:
        return self._value
