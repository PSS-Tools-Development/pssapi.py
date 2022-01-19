from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import LiveOpsRaw as _LiveOpsRaw


class LiveOps(_LiveOpsRaw, _EntityWithIdBase):
    def __init__(self, live_ops_info: _EntityInfo) -> None:
        super().__init__(live_ops_info)

    @property
    def id(self) -> int:
        return self.live_ops_id
