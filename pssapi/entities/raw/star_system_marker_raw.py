"""
    This file has been generated automatically
"""

from datetime import datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class StarSystemMarkerRaw:
    XML_NODE_NAME: str = 'StarSystemMarker'

    def __init__(self, star_system_marker_info: _EntityInfo) -> None:
        self.__is_repeatable: bool = _parse.pss_bool(
            star_system_marker_info.get('IsRepeatable'))
        self.__is_collected: bool = _parse.pss_bool(
            star_system_marker_info.get('IsCollected'))
        self.__title: str = _parse.pss_str(
            star_system_marker_info.get('Title'))
        self.__description: str = _parse.pss_str(
            star_system_marker_info.get('Description'))
        self.__marker_design_id: int = _parse.pss_int(
            star_system_marker_info.get('MarkerDesignId'))
        self.__movement_type: str = _parse.pss_str(
            star_system_marker_info.get('MovementType'))
        self.__requirement_string: str = _parse.pss_str(
            star_system_marker_info.get('RequirementString'))
        self.__star_system_arrival_date: datetime = _parse.pss_datetime(
            star_system_marker_info.get('StarSystemArrivalDate'))
        self.__completion_remaining_value: int = _parse.pss_int(
            star_system_marker_info.get('CompletionRemainingValue'))
        self.__from_star_system_id: int = _parse.pss_int(
            star_system_marker_info.get('FromStarSystemId'))
        self.__completion_date: datetime = _parse.pss_datetime(
            star_system_marker_info.get('CompletionDate'))
        self.__travel_start_date: datetime = _parse.pss_datetime(
            star_system_marker_info.get('TravelStartDate'))
        self.__travel_time_multiplier: int = _parse.pss_int(
            star_system_marker_info.get('TravelTimeMultiplier'))
        self.__mission_design_id: int = _parse.pss_int(
            star_system_marker_info.get('MissionDesignId'))
        self.__metadata: str = _parse.pss_str(
            star_system_marker_info.get('Metadata'))
        self.__sprite_id: int = _parse.pss_int(
            star_system_marker_info.get('SpriteId'))
        self.__origin_next_star_system_id: int = _parse.pss_int(
            star_system_marker_info.get('OriginNextStarSystemId'))
        self.__cost_string: str = _parse.pss_str(
            star_system_marker_info.get('CostString'))
        self.__star_system_id: int = _parse.pss_int(
            star_system_marker_info.get('StarSystemId'))
        self.__expiry_date: datetime = _parse.pss_datetime(
            star_system_marker_info.get('ExpiryDate'))
        self.__reward_string: str = _parse.pss_str(
            star_system_marker_info.get('RewardString'))
        self.__last_update_date: datetime = _parse.pss_datetime(
            star_system_marker_info.get('LastUpdateDate'))
        self.__ship_id: int = _parse.pss_int(
            star_system_marker_info.get('ShipId'))
        self.__origin_star_system_id: int = _parse.pss_int(
            star_system_marker_info.get('OriginStarSystemId'))
        self.__mission_event_id: int = _parse.pss_int(
            star_system_marker_info.get('MissionEventId'))
        self.__ship_ids: str = _parse.pss_str(
            star_system_marker_info.get('ShipIds'))
        self.__completion_value_type: str = _parse.pss_str(
            star_system_marker_info.get('CompletionValueType'))
        self.__marker_flags: int = _parse.pss_int(
            star_system_marker_info.get('MarkerFlags'))
        self.__star_system_marker_id: int = _parse.pss_int(
            star_system_marker_info.get('StarSystemMarkerId'))
        self.__purchase_flags: int = _parse.pss_int(
            star_system_marker_info.get('PurchaseFlags'))
        self.__travel_cool_down_time: int = _parse.pss_int(
            star_system_marker_info.get('TravelCoolDownTime'))
        self.__user_id: int = _parse.pss_int(
            star_system_marker_info.get('UserId'))
        self.__completion_original_value: int = _parse.pss_int(
            star_system_marker_info.get('CompletionOriginalValue'))
        self.__marker_type: str = _parse.pss_str(
            star_system_marker_info.get('MarkerType'))
        self.__next_star_system_id: int = _parse.pss_int(
            star_system_marker_info.get('NextStarSystemId'))
        self.__cost_type: str = _parse.pss_str(
            star_system_marker_info.get('CostType'))

    @property
    def is_repeatable(self) -> bool:
        return self.__is_repeatable

    @property
    def is_collected(self) -> bool:
        return self.__is_collected

    @property
    def title(self) -> str:
        return self.__title

    @property
    def description(self) -> str:
        return self.__description

    @property
    def marker_design_id(self) -> int:
        return self.__marker_design_id

    @property
    def movement_type(self) -> str:
        return self.__movement_type

    @property
    def requirement_string(self) -> str:
        return self.__requirement_string

    @property
    def star_system_arrival_date(self) -> datetime:
        return self.__star_system_arrival_date

    @property
    def completion_remaining_value(self) -> int:
        return self.__completion_remaining_value

    @property
    def from_star_system_id(self) -> int:
        return self.__from_star_system_id

    @property
    def completion_date(self) -> datetime:
        return self.__completion_date

    @property
    def travel_start_date(self) -> datetime:
        return self.__travel_start_date

    @property
    def travel_time_multiplier(self) -> int:
        return self.__travel_time_multiplier

    @property
    def mission_design_id(self) -> int:
        return self.__mission_design_id

    @property
    def metadata(self) -> str:
        return self.__metadata

    @property
    def sprite_id(self) -> int:
        return self.__sprite_id

    @property
    def origin_next_star_system_id(self) -> int:
        return self.__origin_next_star_system_id

    @property
    def cost_string(self) -> str:
        return self.__cost_string

    @property
    def star_system_id(self) -> int:
        return self.__star_system_id

    @property
    def expiry_date(self) -> datetime:
        return self.__expiry_date

    @property
    def reward_string(self) -> str:
        return self.__reward_string

    @property
    def last_update_date(self) -> datetime:
        return self.__last_update_date

    @property
    def ship_id(self) -> int:
        return self.__ship_id

    @property
    def origin_star_system_id(self) -> int:
        return self.__origin_star_system_id

    @property
    def mission_event_id(self) -> int:
        return self.__mission_event_id

    @property
    def ship_ids(self) -> str:
        return self.__ship_ids

    @property
    def completion_value_type(self) -> str:
        return self.__completion_value_type

    @property
    def marker_flags(self) -> int:
        return self.__marker_flags

    @property
    def star_system_marker_id(self) -> int:
        return self.__star_system_marker_id

    @property
    def purchase_flags(self) -> int:
        return self.__purchase_flags

    @property
    def travel_cool_down_time(self) -> int:
        return self.__travel_cool_down_time

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def completion_original_value(self) -> int:
        return self.__completion_original_value

    @property
    def marker_type(self) -> str:
        return self.__marker_type

    @property
    def next_star_system_id(self) -> int:
        return self.__next_star_system_id

    @property
    def cost_type(self) -> str:
        return self.__cost_type
