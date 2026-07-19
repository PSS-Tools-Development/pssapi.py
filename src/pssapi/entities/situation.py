from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import SituationRaw as _SituationRaw


class Situation(_SituationRaw, _EntityWithIdBase):
    def __init__(self, situation_info: _EntityInfo) -> None:
        super().__init__(situation_info)
        self._situation_category_enum: _enums.SituationCategory = _parse.pss_str_enum(self.situation_category, _enums.SituationCategory)

    @property
    def id(self) -> int:
        return self.situation_id

    @property
    def situation_category_enum(self) -> _enums.SituationCategory:
        return self._situation_category_enum
