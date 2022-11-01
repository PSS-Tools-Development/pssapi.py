
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import SeasonDesignRaw as _SeasonDesignRaw
from ..types import EntityInfo as _EntityInfo


class SeasonDesign(_EntityWithIdBase, _SeasonDesignRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<SeasonDesign {self.id}>'

    def __str__(self) -> str:
        return f'<SeasonDesign {self.id}>'

    @property
    def id(self) -> int:
        return self.season_design_id
