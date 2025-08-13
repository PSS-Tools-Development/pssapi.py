from .entity_base import EntityWithIdBase
from .raw import RoomActionRaw


class RoomAction(RoomActionRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.room_action_id


__all__ = [
    "RoomAction",
]
