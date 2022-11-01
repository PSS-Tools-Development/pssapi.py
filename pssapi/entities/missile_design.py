
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import MissileDesignRaw as _MissileDesignRaw
from ..types import EntityInfo as _EntityInfo


class MissileDesign(_EntityWithIdBase, _MissileDesignRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<MissileDesign {self.id}>'

    def __str__(self) -> str:
        return f'<MissileDesign {self.id}>'

    @property
    def id(self) -> int:
        return self.missile_design_id
