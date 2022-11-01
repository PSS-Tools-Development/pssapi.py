"""
    This file has been generated automatically
"""

from datetime import datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class StarSystemMarkerGeneratorRaw:
    XML_NODE_NAME: str = 'StarSystemMarkerGenerator'

    def __init__(self, star_system_marker_generator_info: _EntityInfo) -> None:
        self.__description: str = _parse.pss_str(
            star_system_marker_generator_info.get('Description'))
        self.__marker_design_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('MarkerDesignId'))
        self.__tags: str = _parse.pss_str(
            star_system_marker_generator_info.get('Tags'))
        self.__requirement_string: str = _parse.pss_str(
            star_system_marker_generator_info.get('RequirementString'))
        self.__slots: str = _parse.pss_str(
            star_system_marker_generator_info.get('Slots'))
        self.__travel_start_date: datetime = _parse.pss_datetime(
            star_system_marker_generator_info.get('TravelStartDate'))
        self.__name: str = _parse.pss_str(
            star_system_marker_generator_info.get('Name'))
        self.__end_date: datetime = _parse.pss_datetime(
            star_system_marker_generator_info.get('EndDate'))
        self.__metadata: str = _parse.pss_str(
            star_system_marker_generator_info.get('Metadata'))
        self.__sprite_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('SpriteId'))
        self.__origin_next_star_system_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('OriginNextStarSystemId'))
        self.__cost_string: str = _parse.pss_str(
            star_system_marker_generator_info.get('CostString'))
        self.__star_system_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('StarSystemId'))
        self.__ship_tags: str = _parse.pss_str(
            star_system_marker_generator_info.get('ShipTags'))
        self.__reward_string: str = _parse.pss_str(
            star_system_marker_generator_info.get('RewardString'))
        self.__origin_star_system_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('OriginStarSystemId'))
        self.__ship_ids: str = _parse.pss_str(
            star_system_marker_generator_info.get('ShipIds'))
        self.__start_date: datetime = _parse.pss_datetime(
            star_system_marker_generator_info.get('StartDate'))
        self.__completion_value_type: str = _parse.pss_str(
            star_system_marker_generator_info.get('CompletionValueType'))
        self.__marker_flags: int = _parse.pss_int(
            star_system_marker_generator_info.get('MarkerFlags'))
        self.__behavior_flags: int = _parse.pss_int(
            star_system_marker_generator_info.get('BehaviorFlags'))
        self.__max_active_markers: int = _parse.pss_int(
            star_system_marker_generator_info.get('MaxActiveMarkers'))
        self.__marker_requirement_string: str = _parse.pss_str(
            star_system_marker_generator_info.get('MarkerRequirementString'))
        self.__marker_duration: int = _parse.pss_int(
            star_system_marker_generator_info.get('MarkerDuration'))
        self.__marker_type: str = _parse.pss_str(
            star_system_marker_generator_info.get('MarkerType'))
        self.__next_star_system_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('NextStarSystemId'))
        self.__title: str = _parse.pss_str(
            star_system_marker_generator_info.get('Title'))
        self.__travel_duration: int = _parse.pss_int(
            star_system_marker_generator_info.get('TravelDuration'))
        self.__movement_type: str = _parse.pss_str(
            star_system_marker_generator_info.get('MovementType'))
        self.__number_of_markers: int = _parse.pss_int(
            star_system_marker_generator_info.get('NumberOfMarkers'))
        self.__from_star_system_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('FromStarSystemId'))
        self.__travel_time_multiplier: int = _parse.pss_int(
            star_system_marker_generator_info.get('TravelTimeMultiplier'))
        self.__star_system_marker_generator_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('StarSystemMarkerGeneratorId'))
        self.__generation_flags: int = _parse.pss_int(
            star_system_marker_generator_info.get('GenerationFlags'))
        self.__number_of_ships: int = _parse.pss_int(
            star_system_marker_generator_info.get('NumberOfShips'))
        self.__generation_interval: int = _parse.pss_int(
            star_system_marker_generator_info.get('GenerationInterval'))
        self.__travel_cool_down_time: int = _parse.pss_int(
            star_system_marker_generator_info.get('TravelCoolDownTime'))
        self.__completion_original_value: int = _parse.pss_int(
            star_system_marker_generator_info.get('CompletionOriginalValue'))
        self.__cost_type: str = _parse.pss_str(
            star_system_marker_generator_info.get('CostType'))

    @property
    def description(self) -> str:
        return self.__description

    @property
    def marker_design_id(self) -> int:
        return self.__marker_design_id

    @property
    def tags(self) -> str:
        return self.__tags

    @property
    def requirement_string(self) -> str:
        return self.__requirement_string

    @property
    def slots(self) -> str:
        return self.__slots

    @property
    def travel_start_date(self) -> datetime:
        return self.__travel_start_date

    @property
    def name(self) -> str:
        return self.__name

    @property
    def end_date(self) -> datetime:
        return self.__end_date

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
    def ship_tags(self) -> str:
        return self.__ship_tags

    @property
    def reward_string(self) -> str:
        return self.__reward_string

    @property
    def origin_star_system_id(self) -> int:
        return self.__origin_star_system_id

    @property
    def ship_ids(self) -> str:
        return self.__ship_ids

    @property
    def start_date(self) -> datetime:
        return self.__start_date

    @property
    def completion_value_type(self) -> str:
        return self.__completion_value_type

    @property
    def marker_flags(self) -> int:
        return self.__marker_flags

    @property
    def behavior_flags(self) -> int:
        return self.__behavior_flags

    @property
    def max_active_markers(self) -> int:
        return self.__max_active_markers

    @property
    def marker_requirement_string(self) -> str:
        return self.__marker_requirement_string

    @property
    def marker_duration(self) -> int:
        return self.__marker_duration

    @property
    def marker_type(self) -> str:
        return self.__marker_type

    @property
    def next_star_system_id(self) -> int:
        return self.__next_star_system_id

    @property
    def title(self) -> str:
        return self.__title

    @property
    def travel_duration(self) -> int:
        return self.__travel_duration

    @property
    def movement_type(self) -> str:
        return self.__movement_type

    @property
    def number_of_markers(self) -> int:
        return self.__number_of_markers

    @property
    def from_star_system_id(self) -> int:
        return self.__from_star_system_id

    @property
    def travel_time_multiplier(self) -> int:
        return self.__travel_time_multiplier

    @property
    def star_system_marker_generator_id(self) -> int:
        return self.__star_system_marker_generator_id

    @property
    def generation_flags(self) -> int:
        return self.__generation_flags

    @property
    def number_of_ships(self) -> int:
        return self.__number_of_ships

    @property
    def generation_interval(self) -> int:
        return self.__generation_interval

    @property
    def travel_cool_down_time(self) -> int:
        return self.__travel_cool_down_time

    @property
    def completion_original_value(self) -> int:
        return self.__completion_original_value

    @property
    def cost_type(self) -> str:
        return self.__cost_type
