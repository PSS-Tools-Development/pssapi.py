from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import RoomActionRaw as _RoomActionRaw


class RoomAction(_RoomActionRaw, _EntityWithIdBase):
    def __init__(self, room_action_info: _EntityInfo) -> None:
        super().__init__(room_action_info)

    @property
    def id(self) -> int:
        return self.room_action_id
