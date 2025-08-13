from .entity_base import EntityWithIdBase
from .raw import MissionEventRaw


class MissionEvent(MissionEventRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.mission_event_id


__all__ = [
    "MissionEvent",
]
