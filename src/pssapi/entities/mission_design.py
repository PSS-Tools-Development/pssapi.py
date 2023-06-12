from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .metadata import MissionDesignMetadata as _MissionDesignMetadata
from .raw import MissionDesignRaw as _MissionDesignRaw


class MissionDesign(_MissionDesignRaw, _EntityWithIdBase):
    def __init__(self, mission_design_info: _EntityInfo) -> None:
        super().__init__(mission_design_info)
        self._mission_design_metadata: _MissionDesignMetadata = _MissionDesignMetadata(self.metadata)

    @property
    def id(self) -> int:
        return self.mission_design_id

    @property
    def mission_design_metadata(self) -> _MissionDesignMetadata:
        return self._mission_design_metadata
