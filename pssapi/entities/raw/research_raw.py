"""
    This file has been generated automatically
"""

from datetime import datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ResearchRaw:
    XML_NODE_NAME: str = 'Research'

    def __init__(self, research_info: _EntityInfo) -> None:
        self.__research_id: int = _parse.pss_int(
            research_info.get('ResearchId'))
        self.__ship_id: int = _parse.pss_int(research_info.get('ShipId'))
        self.__research_start_date: datetime = _parse.pss_datetime(
            research_info.get('ResearchStartDate'))
        self.__research_design_id: int = _parse.pss_int(
            research_info.get('ResearchDesignId'))
        self.__research_state: str = _parse.pss_str(
            research_info.get('ResearchState'))

    @property
    def research_id(self) -> int:
        return self.__research_id

    @property
    def ship_id(self) -> int:
        return self.__ship_id

    @property
    def research_start_date(self) -> datetime:
        return self.__research_start_date

    @property
    def research_design_id(self) -> int:
        return self.__research_design_id

    @property
    def research_state(self) -> str:
        return self.__research_state
