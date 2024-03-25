"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


from .entity_base_raw import EntityBaseRaw

class ResearchRaw(EntityBaseRaw):
    XML_NODE_NAME: str = "Research"

    def __init__(self, research_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._research_design_id: int = _parse.pss_int(research_info.pop("ResearchDesignId", None))
        self._research_id: int = _parse.pss_int(research_info.pop("ResearchId", None))
        self._research_start_date: _datetime = _parse.pss_datetime(research_info.pop("ResearchStartDate", None))
        self._research_state: str = _parse.pss_str(research_info.pop("ResearchState", None))
        self._ship_id: int = _parse.pss_int(research_info.pop("ShipId", None))
        super().__init__(research_info)

    @property
    def research_design_id(self) -> int:
        return self._research_design_id

    @property
    def research_id(self) -> int:
        return self._research_id

    @property
    def research_start_date(self) -> _datetime:
        return self._research_start_date

    @property
    def research_state(self) -> str:
        return self._research_state

    @property
    def ship_id(self) -> int:
        return self._ship_id

    def _key(self):
        return (
            self.research_design_id,
            self.research_id,
            self.research_start_date,
            self.research_state,
            self.ship_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "ResearchDesignId": self.research_design_id,
                "ResearchId": self.research_id,
                "ResearchStartDate": self.research_start_date,
                "ResearchState": self.research_state,
                "ShipId": self.ship_id,
            }
            self._dict.update(super().__dict__())

        return self._dict
