from .entity_base import EntityWithIdBase
from .raw import RoomDesignRaw


class RoomDesign(RoomDesignRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.room_design_id


__all__ = [
    "RoomDesign",
]
