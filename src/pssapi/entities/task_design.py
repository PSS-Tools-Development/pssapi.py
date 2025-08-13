from .entity_base import EntityWithIdBase
from .raw import TaskDesignRaw


class TaskDesign(TaskDesignRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.task_design_id


__all__ = [
    "TaskDesign",
]
