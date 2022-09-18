
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import RoomRaw as _RoomRaw
from ..types import EntityInfo as _EntityInfo


class Room(_EntityWithIdBase, _RoomRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<Room {self.id}: {self.name}>'

    def __str__(self) -> str:
        return f'<Room {self.id}: {self.name}>'

    @property
    def id(self) -> int:
        return self.room_id
