"""
This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class TaskRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "Task"

    def __init__(self, task_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._collected: bool = _parse.pss_bool(task_info.pop("Collected", None))
        self._progress_value: int = _parse.pss_int(task_info.pop("ProgressValue", None))
        self._task_design_id: int = _parse.pss_int(task_info.pop("TaskDesignId", None))
        self._task_id: int = _parse.pss_int(task_info.pop("TaskId", None))
        self._user_id: int = _parse.pss_int(task_info.pop("UserId", None))
        super().__init__(task_info)

    @property
    def collected(self) -> bool:
        return self._collected

    @property
    def progress_value(self) -> int:
        return self._progress_value

    @property
    def task_design_id(self) -> int:
        return self._task_design_id

    @property
    def task_id(self) -> int:
        return self._task_id

    @property
    def user_id(self) -> int:
        return self._user_id

    def _key(self):
        return (
            self.collected,
            self.progress_value,
            self.task_design_id,
            self.task_id,
            self.user_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "Collected": self.collected,
                "ProgressValue": self.progress_value,
                "TaskDesignId": self.task_design_id,
                "TaskId": self.task_id,
                "UserId": self.user_id,
            }
            self._dict.update(super().__dict__())

        return self._dict
