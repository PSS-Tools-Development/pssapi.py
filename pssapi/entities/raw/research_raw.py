"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import List as _List

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ResearchRaw:
    XML_NODE_NAME: str = 'Research'

    def __init__(self, research_info: _EntityInfo) -> None:
        self.research_design_id: int = _parse.pss_int(research_info.get('ResearchDesignId'))
        self.research_id: int = _parse.pss_int(research_info.get('ResearchId'))
        self.research_start_date: _datetime = _parse.pss__datetime(research_info.get('ResearchStartDate'))
        self.research_state: str = _parse.pss_str(research_info.get('ResearchState'))
        self.ship_id: int = _parse.pss_int(research_info.get('ShipId'))
