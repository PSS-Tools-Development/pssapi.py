from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import SituationRaw as _SituationRaw


class Situation(_SituationRaw, _EntityWithIdBase):
    def __init__(self, situation_info: _EntityInfo) -> None:
        super().__init__(situation_info)

    @property
    def id(self) -> int:
        return self.situation_id
