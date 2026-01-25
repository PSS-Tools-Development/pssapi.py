from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import AllianceTaskRaw as _AllianceTaskRaw


class AllianceTask(_AllianceTaskRaw, _EntityWithIdBase):
    def __init__(self, alliance_task_info: _EntityInfo) -> None:
        super().__init__(alliance_task_info)

    @property
    def id(self) -> int:
        return self.alliance_task_id
