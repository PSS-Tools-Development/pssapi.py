from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import TaskDesignRaw as _TaskDesignRaw


class TaskDesign(_TaskDesignRaw, _EntityWithIdBase):
    def __init__(self, task_design_info: _EntityInfo) -> None:
        super().__init__(task_design_info)

    @property
    def id(self) -> int:
        return self.task_design_id
