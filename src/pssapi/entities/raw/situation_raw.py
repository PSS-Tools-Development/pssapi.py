"""
This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class SituationRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "Situation"

    def __init__(self, situation_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._end_date: _datetime = _parse.pss_datetime(situation_info.pop("EndDate", None))
        self._from_date: _datetime = _parse.pss_datetime(situation_info.pop("FromDate", None))
        self._remaining_count: int = _parse.pss_int(situation_info.pop("RemainingCount", None))
        self._reset_date: _datetime = _parse.pss_datetime(situation_info.pop("ResetDate", None))
        self._situation_category: str = _parse.pss_str(situation_info.pop("SituationCategory", None))
        self._situation_design_id: int = _parse.pss_int(situation_info.pop("SituationDesignId", None))
        self._situation_id: int = _parse.pss_int(situation_info.pop("SituationId", None))
        self._user_id: int = _parse.pss_int(situation_info.pop("UserId", None))
        super().__init__(situation_info)

    @property
    def end_date(self) -> _datetime:
        return self._end_date

    @property
    def from_date(self) -> _datetime:
        return self._from_date

    @property
    def remaining_count(self) -> int:
        return self._remaining_count

    @property
    def reset_date(self) -> _datetime:
        return self._reset_date

    @property
    def situation_category(self) -> str:
        return self._situation_category

    @property
    def situation_design_id(self) -> int:
        return self._situation_design_id

    @property
    def situation_id(self) -> int:
        return self._situation_id

    @property
    def user_id(self) -> int:
        return self._user_id

    def _key(self):
        return (
            self.end_date,
            self.from_date,
            self.remaining_count,
            self.reset_date,
            self.situation_category,
            self.situation_design_id,
            self.situation_id,
            self.user_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "EndDate": self.end_date,
                "FromDate": self.from_date,
                "RemainingCount": self.remaining_count,
                "ResetDate": self.reset_date,
                "SituationCategory": self.situation_category,
                "SituationDesignId": self.situation_design_id,
                "SituationId": self.situation_id,
                "UserId": self.user_id,
            }
            self._dict.update(super().__dict__())

        return self._dict
