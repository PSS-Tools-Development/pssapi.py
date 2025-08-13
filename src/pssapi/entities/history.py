from .entity_base import EntityWithIdBase
from .raw import HistoryRaw


class History(HistoryRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.history_id


__all__ = [
    "History",
]
