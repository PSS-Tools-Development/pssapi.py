from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import MissionEventRaw as _MissionEventRaw


class MissionEvent(_MissionEventRaw, _EntityWithIdBase):
    def __init__(self, mission_event_info: _EntityInfo) -> None:
        super().__init__(mission_event_info)

    @property
    def id(self) -> int:
        return self.mission_event_id
