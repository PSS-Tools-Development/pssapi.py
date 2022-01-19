from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import MissileDesignRaw as _MissileDesignRaw


class MissileDesign(_MissileDesignRaw, _EntityWithIdBase):
    def __init__(self, missile_design_info: _EntityInfo) -> None:
        super().__init__(missile_design_info)

    @property
    def id(self) -> int:
        return self.missile_design_id
