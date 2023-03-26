from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import HistoryRaw as _HistoryRaw


class History(_HistoryRaw, _EntityWithIdBase):
    def __init__(self, history_info: _EntityInfo) -> None:
        super().__init__(history_info)

    @property
    def id(self) -> int:
        return self.history_id
