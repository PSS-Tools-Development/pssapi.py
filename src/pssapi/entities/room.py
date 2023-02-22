
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import RoomRaw as _RoomRaw
from ..types import EntityInfo as _EntityInfo


class Room(_RoomRaw, _EntityWithIdBase):
    def __init__(self, room_info: _EntityInfo) -> None:
        super().__init__(room_info)

    @property
    def id(self) -> int:
        return self.room_id
