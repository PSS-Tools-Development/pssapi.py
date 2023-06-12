from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .metadata import RoomDesignMetadata as _RoomDesignMetadata
from .raw import RoomDesignRaw as _RoomDesignRaw


class RoomDesign(_RoomDesignRaw, _EntityWithIdBase):
    def __init__(self, room_design_info: _EntityInfo) -> None:
        super().__init__(room_design_info)
        self._room_design_metadata: _RoomDesignMetadata = _RoomDesignMetadata(self.metadata)

    @property
    def id(self) -> int:
        return self.room_design_id

    @property
    def room_design_metadata(self) -> _RoomDesignMetadata:
        return self._room_design_metadata
