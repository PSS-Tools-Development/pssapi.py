"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class HistoryRaw:
    XML_NODE_NAME: str = "History"

    def __init__(self, history_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._argument: int = _parse.pss_int(history_info.get("Argument"))
        self._date: _datetime = _parse.pss_datetime(history_info.get("Date"))
        self._history_id: int = _parse.pss_int(history_info.get("HistoryId"))
        self._history_type: str = _parse.pss_str(history_info.get("HistoryType"))
        self._value: int = _parse.pss_int(history_info.get("Value"))

    @property
    def argument(self) -> int:
        return self._argument

    @property
    def date(self) -> _datetime:
        return self._date

    @property
    def history_id(self) -> int:
        return self._history_id

    @property
    def history_type(self) -> str:
        return self._history_type

    @property
    def value(self) -> int:
        return self._value

    def _key(self):
        return (
            self.argument,
            self.date,
            self.history_id,
            self.history_type,
            self.value,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "Argument": self.argument,
                "Date": self.date,
                "HistoryId": self.history_id,
                "HistoryType": self.history_type,
                "Value": self.value,
            }

        return self._dict
