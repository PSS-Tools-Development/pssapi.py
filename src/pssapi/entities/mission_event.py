from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import MissionEventRaw as _MissionEventRaw


class MissionEvent(_MissionEventRaw, _EntityWithIdBase):
    def __init__(self, mission_event_info: _EntityInfo) -> None:
        super().__init__(mission_event_info)
        self._flags_enum: _enums.MissionEventFlag = _parse.pss_int_flag(self.flags, _enums.MissionEventFlag)
        self._mission_event_type_enum: _enums.MissionEventType = _parse.pss_str_enum(self.mission_event_type, _enums.MissionEventType)

    @property
    def id(self) -> int:
        return self.mission_event_id

    @property
    def flags_enum(self) -> "_enums.MissionEventFlag":
        return self._flags_enum

    @property
    def mission_event_type_enum(self) -> "_enums.MissionEventType":
        return self._mission_event_type_enum
