
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import LiveOpsRaw as _LiveOpsRaw
from ..types import EntityInfo as _EntityInfo


class LiveOps(_EntityWithIdBase, _LiveOpsRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<LiveOps {self.id}: {self.name}>'

    def __str__(self) -> str:
        return f'<LiveOps {self.id}: {self.name}>'

    @property
    def id(self) -> int:
        return self.live_ops_id
