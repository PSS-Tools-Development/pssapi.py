from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import SeasonDesignRaw as _SeasonDesignRaw


class SeasonDesign(_SeasonDesignRaw, _EntityWithIdBase):
    def __init__(self, season_design_info: _EntityInfo) -> None:
        super().__init__(season_design_info)

    @property
    def id(self) -> int:
        return self.season_design_id
