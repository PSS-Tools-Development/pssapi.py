from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import TaskRaw as _TaskRaw


class Task(_TaskRaw, _EntityWithIdBase):
    def __init__(self, task_info: _EntityInfo) -> None:
        super().__init__(task_info)

    @property
    def id(self) -> int:
        return self.task_id
