from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import TaskDesignRaw as _TaskDesignRaw


class TaskDesign(_TaskDesignRaw, _EntityWithIdBase):
    def __init__(self, task_design_info: _EntityInfo) -> None:
        super().__init__(task_design_info)
        self._flags_enum: _enums.TaskDesignFlagsType = _parse.pss_int_flag(self.flags, _enums.TaskDesignFlagsType)
        self._objective_type_enum: _enums.ObjectiveType = _parse.pss_str_enum(self.objective_type, _enums.ObjectiveType)
        self._task_category_enum: _enums.TaskCategory = _parse.pss_str_enum(self.task_category, _enums.TaskCategory)

    @property
    def id(self) -> int:
        return self.task_design_id

    @property
    def flags_enum(self) -> "_enums.TaskDesignFlagsType":
        return self._flags_enum

    @property
    def objective_type_enum(self) -> "_enums.ObjectiveType":
        return self._objective_type_enum

    @property
    def task_category_enum(self) -> "_enums.TaskCategory":
        return self._task_category_enum
