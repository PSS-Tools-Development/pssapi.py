
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import SituationDesignRaw as _SituationDesignRaw
from ..types import EntityInfo as _EntityInfo


class SituationDesign(_EntityWithIdBase, _SituationDesignRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<SituationDesign {self.id}: {self.name}>'

    def __str__(self) -> str:
        return f'<SituationDesign {self.id}: {self.name}>'

    @property
    def id(self) -> int:
        return self.situation_design_id
