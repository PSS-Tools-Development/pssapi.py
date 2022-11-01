
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import RoomDesignRaw as _RoomDesignRaw
from ..types import EntityInfo as _EntityInfo


class RoomDesign(_EntityWithIdBase, _RoomDesignRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<RoomDesign {self.id}>'

    def __str__(self) -> str:
        return f'<RoomDesign {self.id}>'

    @property
    def id(self) -> int:
        return self.room_design_id
