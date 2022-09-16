####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class StarSystemMarkerRaw():
    XML_NODE_NAME: str = 'StarSystemMarker'

    def __init__(self, star_system_marker_info: _EntityInfo) -> None:
        self.__star_system_marker_id: int = _parse.pss_int(star_system_marker_info.get('StarSystemMarkerId'))
        self.__star_system_id: int = _parse.pss_int(star_system_marker_info.get('StarSystemId'))
        self.__from_star_system_id: int = _parse.pss_int(star_system_marker_info.get('FromStarSystemId'))
        self.__next_star_system_id: int = _parse.pss_int(star_system_marker_info.get('NextStarSystemId'))
        self.__origin_star_system_id: int = _parse.pss_int(star_system_marker_info.get('OriginStarSystemId'))
        self.__origin_next_star_system_id: int = _parse.pss_int(star_system_marker_info.get('OriginNextStarSystemId'))
        self.__marker_flags: int = _parse.pss_int(star_system_marker_info.get('MarkerFlags'))
        self.__marker_type: str = _parse.pss_str(star_system_marker_info.get('MarkerType'))
        self.__cost_string: str = _parse.pss_str(star_system_marker_info.get('CostString'))
        self.__reward_string: str = _parse.pss_str(star_system_marker_info.get('RewardString'))
        self.__is_collected: bool = _parse.pss_bool(star_system_marker_info.get('IsCollected'))
        self.__is_repeatable: bool = _parse.pss_bool(star_system_marker_info.get('IsRepeatable'))
        self.__title: str = _parse.pss_str(star_system_marker_info.get('Title'))
        self.__star_system_arrival_date: datetime = _parse.pss_datetime(star_system_marker_info.get('StarSystemArrivalDate'))
        self.__expiry_date: datetime = _parse.pss_datetime(star_system_marker_info.get('ExpiryDate'))
        self.__user_id: int = _parse.pss_int(star_system_marker_info.get('UserId'))
        self.__mission_design_id: int = _parse.pss_int(star_system_marker_info.get('MissionDesignId'))
        self.__completion_date: datetime = _parse.pss_datetime(star_system_marker_info.get('CompletionDate'))
        self.__sprite_id: int = _parse.pss_int(star_system_marker_info.get('SpriteId'))
        self.__mission_event_id: int = _parse.pss_int(star_system_marker_info.get('MissionEventId'))

    @property
    def star_system_marker_id(self) -> int:
        return self.__star_system_marker_id

    @property
    def star_system_id(self) -> int:
        return self.__star_system_id

    @property
    def from_star_system_id(self) -> int:
        return self.__from_star_system_id

    @property
    def next_star_system_id(self) -> int:
        return self.__next_star_system_id

    @property
    def origin_star_system_id(self) -> int:
        return self.__origin_star_system_id

    @property
    def origin_next_star_system_id(self) -> int:
        return self.__origin_next_star_system_id

    @property
    def marker_flags(self) -> int:
        return self.__marker_flags

    @property
    def marker_type(self) -> str:
        return self.__marker_type

    @property
    def cost_string(self) -> str:
        return self.__cost_string

    @property
    def reward_string(self) -> str:
        return self.__reward_string

    @property
    def is_collected(self) -> bool:
        return self.__is_collected

    @property
    def is_repeatable(self) -> bool:
        return self.__is_repeatable

    @property
    def title(self) -> str:
        return self.__title

    @property
    def star_system_arrival_date(self) -> datetime:
        return self.__star_system_arrival_date

    @property
    def expiry_date(self) -> datetime:
        return self.__expiry_date

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def mission_design_id(self) -> int:
        return self.__mission_design_id

    @property
    def completion_date(self) -> datetime:
        return self.__completion_date

    @property
    def sprite_id(self) -> int:
        return self.__sprite_id

    @property
    def mission_event_id(self) -> int:
        return self.__mission_event_id
