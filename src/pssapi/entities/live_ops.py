from .entity_base import EntityWithIdBase
from .raw import LiveOpsRaw


class LiveOps(LiveOpsRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.live_ops_id


__all__ = [
    "LiveOps",
]
