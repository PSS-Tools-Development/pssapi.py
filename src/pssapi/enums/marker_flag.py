from enum import IntFlag as _IntFlag

from .int_flag_object_base import IntFlagObjectBase as _IntFlagObjectBase


class MarkerFlag(_IntFlag):
    NONE = 0
    GLOBAL = 1
    USER = 2
    DISPLAY_ON_MISSION = 4
    DISPLAY_ON_SYSTEM_INFO = 8
    CREATE_MARKER_IF_EXISTS = 16
    CREATE_MARKER_IF_EXISTS_KEEP_EXISTING = 32
    USE_TRAVEL_MULTIPLIER = 64
    DELETE_SHIP_ID_AFTER_DEFEAT = 128


class MarkerFlagObject(_IntFlagObjectBase):
    def __init__(self, marker_flag: MarkerFlag):
        super().__init__(marker_flag)

    @property
    def create_marker_if_exists(self) -> bool:
        return bool(self.value & MarkerFlag.CREATE_MARKER_IF_EXISTS)

    @property
    def create_marker_if_exists_keep_existing(self) -> bool:
        return bool(self.value & MarkerFlag.CREATE_MARKER_IF_EXISTS_KEEP_EXISTING)

    @property
    def delete_ship_id_after_defeat(self) -> bool:
        return bool(self.value & MarkerFlag.DELETE_SHIP_ID_AFTER_DEFEAT)

    @property
    def display_on_mission(self) -> bool:
        return bool(self.value & MarkerFlag.DISPLAY_ON_MISSION)

    @property
    def display_on_system_info(self) -> bool:
        return bool(self.value & MarkerFlag.DISPLAY_ON_SYSTEM_INFO)

    @property
    def global_(self) -> bool:
        return bool(self.value & MarkerFlag.GLOBAL)

    @property
    def use_travel_multiplier(self) -> bool:
        return bool(self.value & MarkerFlag.USE_TRAVEL_MULTIPLIER)

    @property
    def user(self) -> bool:
        return bool(self.value & MarkerFlag.USER)

    @property
    def value(self) -> MarkerFlag:
        return self._value
