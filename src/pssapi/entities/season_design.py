from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .metadata import SeasonDesignMetadata as _SeasonDesignMetadata
from .raw import SeasonDesignRaw as _SeasonDesignRaw


class SeasonDesign(_SeasonDesignRaw, _EntityWithIdBase):
    def __init__(self, season_design_info: _EntityInfo) -> None:
        super().__init__(season_design_info)
        self._season_design_metadata: _SeasonDesignMetadata = _SeasonDesignMetadata(self.metadata)

    @property
    def id(self) -> int:
        return self.season_design_id

    @property
    def season_design_metadata(self) -> _SeasonDesignMetadata:
        return self._season_design_metadata
