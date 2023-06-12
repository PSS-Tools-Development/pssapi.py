from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .metadata import MissileDesignMetadata as _MissileDesignMetadata
from .raw import MissileDesignRaw as _MissileDesignRaw


class MissileDesign(_MissileDesignRaw, _EntityWithIdBase):
    def __init__(self, missile_design_info: _EntityInfo) -> None:
        super().__init__(missile_design_info)
        self._missile_design_metadata: _MissileDesignMetadata = _MissileDesignMetadata(self.metadata)

    @property
    def id(self) -> int:
        return self.missile_design_id

    @property
    def missile_design_metadata(self) -> _MissileDesignMetadata:
        return self._missile_design_metadata
