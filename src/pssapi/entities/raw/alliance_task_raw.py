"""
This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class AllianceTaskRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "AllianceTask"

    def __init__(self, alliance_task_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._alliance_id: int = _parse.pss_int(alliance_task_info.pop("AllianceId", None))
        self._alliance_task_id: int = _parse.pss_int(alliance_task_info.pop("AllianceTaskId", None))
        self._progress_value: int = _parse.pss_int(alliance_task_info.pop("ProgressValue", None))
        self._task_design_id: int = _parse.pss_int(alliance_task_info.pop("TaskDesignId", None))
        self._update_date: _datetime = _parse.pss_datetime(alliance_task_info.pop("UpdateDate", None))
        super().__init__(alliance_task_info)

    @property
    def alliance_id(self) -> int:
        return self._alliance_id

    @property
    def alliance_task_id(self) -> int:
        return self._alliance_task_id

    @property
    def progress_value(self) -> int:
        return self._progress_value

    @property
    def task_design_id(self) -> int:
        return self._task_design_id

    @property
    def update_date(self) -> _datetime:
        return self._update_date

    def _key(self):
        return (
            self.alliance_id,
            self.alliance_task_id,
            self.progress_value,
            self.task_design_id,
            self.update_date,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "AllianceId": self.alliance_id,
                "AllianceTaskId": self.alliance_task_id,
                "ProgressValue": self.progress_value,
                "TaskDesignId": self.task_design_id,
                "UpdateDate": self.update_date,
            }
            self._dict.update(super().__dict__())

        return self._dict
