from enum import IntFlag as _IntFlag

from .int_flag_object_base import IntFlagObjectBase as _IntFlagObjectBase


class MissionEventFlag(_IntFlag):
    NONE = 0
    SHOW_OPTION_IF_REQUIREMENT_NOT_MET = 1


class MissionEventFlagObject(_IntFlagObjectBase):
    def __init__(self, mission_event_flag: MissionEventFlag):
        super().__init__(mission_event_flag)

    @property
    def show_option_if_requirement_not_met(self) -> bool:
        return bool(self.value & MissionEventFlag.SHOW_OPTION_IF_REQUIREMENT_NOT_MET)

    @property
    def value(self) -> MissionEventFlag:
        return self._value
