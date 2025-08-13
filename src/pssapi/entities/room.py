from .entity_base import EntityWithIdBase
from .raw import RoomRaw


class Room(RoomRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.room_id


__all__ = [
    "Room",
]
