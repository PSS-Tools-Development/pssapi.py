"""
    This file has been generated automatically
"""

from datetime import datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class StarSystemMarkerGeneratorRaw:
    XML_NODE_NAME: str = 'StarSystemMarkerGenerator'

    def __init__(self, star_system_marker_generator_info: _EntityInfo) -> None:
        self.__cost_type: str = _parse.pss_str(
            star_system_marker_generator_info.get('CostType'))
        self.__from_star_system_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('FromStarSystemId'))
        self.__origin_star_system_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('OriginStarSystemId'))
        self.__movement_type: str = _parse.pss_str(
            star_system_marker_generator_info.get('MovementType'))
        self.__marker_requirement_string: str = _parse.pss_str(
            star_system_marker_generator_info.get('MarkerRequirementString'))
        self.__reward_string: str = _parse.pss_str(
            star_system_marker_generator_info.get('RewardString'))
        self.__title: str = _parse.pss_str(
            star_system_marker_generator_info.get('Title'))
        self.__description: str = _parse.pss_str(
            star_system_marker_generator_info.get('Description'))
        self.__generation_flags: int = _parse.pss_int(
            star_system_marker_generator_info.get('GenerationFlags'))
        self.__star_system_marker_generator_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('StarSystemMarkerGeneratorId'))
        self.__name: str = _parse.pss_str(
            star_system_marker_generator_info.get('Name'))
        self.__marker_flags: int = _parse.pss_int(
            star_system_marker_generator_info.get('MarkerFlags'))
        self.__number_of_ships: int = _parse.pss_int(
            star_system_marker_generator_info.get('NumberOfShips'))
        self.__travel_cool_down_time: int = _parse.pss_int(
            star_system_marker_generator_info.get('TravelCoolDownTime'))
        self.__generation_interval: int = _parse.pss_int(
            star_system_marker_generator_info.get('GenerationInterval'))
        self.__slots: str = _parse.pss_str(
            star_system_marker_generator_info.get('Slots'))
        self.__completion_value_type: str = _parse.pss_str(
            star_system_marker_generator_info.get('CompletionValueType'))
        self.__tags: str = _parse.pss_str(
            star_system_marker_generator_info.get('Tags'))
        self.__completion_original_value: int = _parse.pss_int(
            star_system_marker_generator_info.get('CompletionOriginalValue'))
        self.__origin_next_star_system_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('OriginNextStarSystemId'))
        self.__travel_start_date: datetime = _parse.pss_datetime(
            star_system_marker_generator_info.get('TravelStartDate'))
        self.__next_star_system_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('NextStarSystemId'))
        self.__star_system_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('StarSystemId'))
        self.__travel_time_multiplier: int = _parse.pss_int(
            star_system_marker_generator_info.get('TravelTimeMultiplier'))
        self.__ship_ids: str = _parse.pss_str(
            star_system_marker_generator_info.get('ShipIds'))
        self.__behavior_flags: int = _parse.pss_int(
            star_system_marker_generator_info.get('BehaviorFlags'))
        self.__cost_string: str = _parse.pss_str(
            star_system_marker_generator_info.get('CostString'))
        self.__end_date: datetime = _parse.pss_datetime(
            star_system_marker_generator_info.get('EndDate'))
        self.__sprite_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('SpriteId'))
        self.__travel_duration: int = _parse.pss_int(
            star_system_marker_generator_info.get('TravelDuration'))
        self.__ship_tags: str = _parse.pss_str(
            star_system_marker_generator_info.get('ShipTags'))
        self.__marker_design_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('MarkerDesignId'))
        self.__metadata: str = _parse.pss_str(
            star_system_marker_generator_info.get('Metadata'))
        self.__marker_duration: int = _parse.pss_int(
            star_system_marker_generator_info.get('MarkerDuration'))
        self.__number_of_markers: int = _parse.pss_int(
            star_system_marker_generator_info.get('NumberOfMarkers'))
        self.__max_active_markers: int = _parse.pss_int(
            star_system_marker_generator_info.get('MaxActiveMarkers'))
        self.__start_date: datetime = _parse.pss_datetime(
            star_system_marker_generator_info.get('StartDate'))
        self.__requirement_string: str = _parse.pss_str(
            star_system_marker_generator_info.get('RequirementString'))
        self.__marker_type: str = _parse.pss_str(
            star_system_marker_generator_info.get('MarkerType'))

    @property
    def cost_type(self) -> str:
        return self.__cost_type

    @property
    def from_star_system_id(self) -> int:
        return self.__from_star_system_id

    @property
    def origin_star_system_id(self) -> int:
        return self.__origin_star_system_id

    @property
    def movement_type(self) -> str:
        return self.__movement_type

    @property
    def marker_requirement_string(self) -> str:
        return self.__marker_requirement_string

    @property
    def reward_string(self) -> str:
        return self.__reward_string

    @property
    def title(self) -> str:
        return self.__title

    @property
    def description(self) -> str:
        return self.__description

    @property
    def generation_flags(self) -> int:
        return self.__generation_flags

    @property
    def star_system_marker_generator_id(self) -> int:
        return self.__star_system_marker_generator_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def marker_flags(self) -> int:
        return self.__marker_flags

    @property
    def number_of_ships(self) -> int:
        return self.__number_of_ships

    @property
    def travel_cool_down_time(self) -> int:
        return self.__travel_cool_down_time

    @property
    def generation_interval(self) -> int:
        return self.__generation_interval

    @property
    def slots(self) -> str:
        return self.__slots

    @property
    def completion_value_type(self) -> str:
        return self.__completion_value_type

    @property
    def tags(self) -> str:
        return self.__tags

    @property
    def completion_original_value(self) -> int:
        return self.__completion_original_value

    @property
    def origin_next_star_system_id(self) -> int:
        return self.__origin_next_star_system_id

    @property
    def travel_start_date(self) -> datetime:
        return self.__travel_start_date

    @property
    def next_star_system_id(self) -> int:
        return self.__next_star_system_id

    @property
    def star_system_id(self) -> int:
        return self.__star_system_id

    @property
    def travel_time_multiplier(self) -> int:
        return self.__travel_time_multiplier

    @property
    def ship_ids(self) -> str:
        return self.__ship_ids

    @property
    def behavior_flags(self) -> int:
        return self.__behavior_flags

    @property
    def cost_string(self) -> str:
        return self.__cost_string

    @property
    def end_date(self) -> datetime:
        return self.__end_date

    @property
    def sprite_id(self) -> int:
        return self.__sprite_id

    @property
    def travel_duration(self) -> int:
        return self.__travel_duration

    @property
    def ship_tags(self) -> str:
        return self.__ship_tags

    @property
    def marker_design_id(self) -> int:
        return self.__marker_design_id

    @property
    def metadata(self) -> str:
        return self.__metadata

    @property
    def marker_duration(self) -> int:
        return self.__marker_duration

    @property
    def number_of_markers(self) -> int:
        return self.__number_of_markers

    @property
    def max_active_markers(self) -> int:
        return self.__max_active_markers

    @property
    def start_date(self) -> datetime:
        return self.__start_date

    @property
    def requirement_string(self) -> str:
        return self.__requirement_string

    @property
    def marker_type(self) -> str:
        return self.__marker_type
