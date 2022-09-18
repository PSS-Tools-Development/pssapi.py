
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import TaskDesignRaw as _TaskDesignRaw
from ..types import EntityInfo as _EntityInfo


class TaskDesign(_EntityWithIdBase, _TaskDesignRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<TaskDesign {self.id}: {self.name}>'

    def __str__(self) -> str:
        return f'<TaskDesign {self.id}: {self.name}>'

    @property
    def id(self) -> int:
        return self.task_design_id
