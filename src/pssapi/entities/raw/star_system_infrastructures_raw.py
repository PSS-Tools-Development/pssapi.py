"""
This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class StarSystemInfrastructuresRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "StarSystemInfrastructures"

    def __init__(self, star_system_infrastructures_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._investment_end_date: _datetime = _parse.pss_datetime(star_system_infrastructures_info.pop("InvestmentEndDate", None))
        self._investment_level: int = _parse.pss_int(star_system_infrastructures_info.pop("InvestmentLevel", None))
        self._star_system_id: int = _parse.pss_int(star_system_infrastructures_info.pop("StarSystemId", None))
        self._star_system_infrastructure_design_id: int = _parse.pss_int(star_system_infrastructures_info.pop("StarSystemInfrastructureDesignId", None))
        self._star_system_infrastructure_id: int = _parse.pss_int(star_system_infrastructures_info.pop("StarSystemInfrastructureId", None))
        super().__init__(star_system_infrastructures_info)

    @property
    def investment_end_date(self) -> _datetime:
        return self._investment_end_date

    @property
    def investment_level(self) -> int:
        return self._investment_level

    @property
    def star_system_id(self) -> int:
        return self._star_system_id

    @property
    def star_system_infrastructure_design_id(self) -> int:
        return self._star_system_infrastructure_design_id

    @property
    def star_system_infrastructure_id(self) -> int:
        return self._star_system_infrastructure_id

    def _key(self):
        return (
            self.investment_end_date,
            self.investment_level,
            self.star_system_id,
            self.star_system_infrastructure_design_id,
            self.star_system_infrastructure_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "InvestmentEndDate": self.investment_end_date,
                "InvestmentLevel": self.investment_level,
                "StarSystemId": self.star_system_id,
                "StarSystemInfrastructureDesignId": self.star_system_infrastructure_design_id,
                "StarSystemInfrastructureId": self.star_system_infrastructure_id,
            }
            self._dict.update(super().__dict__())

        return self._dict
