####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class StarSystemLinkRaw():
    XML_NODE_NAME: str = 'StarSystemLink'

    def __init__(self, star_system_link_info: _EntityInfo) -> None:
        self.__star_system_link_id: int = _parse.pss_int(star_system_link_info.get('StarSystemLinkId'))
        self.__from_star_system_id: int = _parse.pss_int(star_system_link_info.get('FromStarSystemId'))
        self.__to_star_system_id: int = _parse.pss_int(star_system_link_info.get('ToStarSystemId'))
        self.__is_two_way: bool = _parse.pss_bool(star_system_link_info.get('IsTwoWay'))
        self.__travel_time: int = _parse.pss_int(star_system_link_info.get('TravelTime'))

    @property
    def star_system_link_id(self) -> int:
        return self.__star_system_link_id

    @property
    def from_star_system_id(self) -> int:
        return self.__from_star_system_id

    @property
    def to_star_system_id(self) -> int:
        return self.__to_star_system_id

    @property
    def is_two_way(self) -> bool:
        return self.__is_two_way

    @property
    def travel_time(self) -> int:
        return self.__travel_time
