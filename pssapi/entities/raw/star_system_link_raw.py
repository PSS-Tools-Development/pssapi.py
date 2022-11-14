"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import List as _List

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class StarSystemLinkRaw:
    XML_NODE_NAME: str = 'StarSystemLink'

    def __init__(self, star_system_link_info: _EntityInfo) -> None:
        self.from_star_system_id: int = _parse.pss_int(star_system_link_info.get('FromStarSystemId'))
        self.is_two_way: bool = _parse.pss_bool(star_system_link_info.get('IsTwoWay'))
        self.star_system_link_id: int = _parse.pss_int(star_system_link_info.get('StarSystemLinkId'))
        self.to_star_system_id: int = _parse.pss_int(star_system_link_info.get('ToStarSystemId'))
        self.travel_time: int = _parse.pss_int(star_system_link_info.get('TravelTime'))
