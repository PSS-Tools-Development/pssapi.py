from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import HistoryRaw as _HistoryRaw


class History(_HistoryRaw, _EntityWithIdBase):
    def __init__(self, history_info: _EntityInfo) -> None:
        super().__init__(history_info)
        self._history_type_enum: _enums.HistoryType = _parse.pss_str_enum(self.history_type, _enums.HistoryType)

    @property
    def id(self) -> int:
        return self.history_id

    @property
    def history_type_enum(self) -> "_enums.HistoryType":
        return self._history_type_enum
