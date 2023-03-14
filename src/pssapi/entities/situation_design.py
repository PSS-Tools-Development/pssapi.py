from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import SituationDesignRaw as _SituationDesignRaw


class SituationDesign(_SituationDesignRaw, _EntityWithIdBase):
    def __init__(self, situation_design_info: _EntityInfo) -> None:
        super().__init__(situation_design_info)

    @property
    def id(self) -> int:
        return self.situation_design_id
