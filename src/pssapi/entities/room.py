from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import RoomRaw as _RoomRaw


class Room(_RoomRaw, _EntityWithIdBase):
    def __init__(self, room_info: _EntityInfo) -> None:
        super().__init__(room_info)
        self._room_status_enum: _enums.RoomStatus = _parse.pss_str_enum(self.room_status, _enums.RoomStatus)

    @property
    def id(self) -> int:
        return self.room_id

    @property
    def room_status_enum(self) -> "_enums.RoomStatus":
        return self._room_status_enum
