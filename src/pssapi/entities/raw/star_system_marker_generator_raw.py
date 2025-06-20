"""
This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class StarSystemMarkerGeneratorRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "StarSystemMarkerGenerator"

    def __init__(self, star_system_marker_generator_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._behavior_flags: int = _parse.pss_int(star_system_marker_generator_info.pop("BehaviorFlags", None))
        self._completion_original_value: int = _parse.pss_int(star_system_marker_generator_info.pop("CompletionOriginalValue", None))
        self._completion_value_type: str = _parse.pss_str(star_system_marker_generator_info.pop("CompletionValueType", None))
        self._cost_string: str = _parse.pss_str(star_system_marker_generator_info.pop("CostString", None))
        self._cost_type: str = _parse.pss_str(star_system_marker_generator_info.pop("CostType", None))
        self._description: str = _parse.pss_str(star_system_marker_generator_info.pop("Description", None))
        self._end_date: _datetime = _parse.pss_datetime(star_system_marker_generator_info.pop("EndDate", None))
        self._from_star_system_id: int = _parse.pss_int(star_system_marker_generator_info.pop("FromStarSystemId", None))
        self._generation_flags: int = _parse.pss_int(star_system_marker_generator_info.pop("GenerationFlags", None))
        self._generation_interval: int = _parse.pss_int(star_system_marker_generator_info.pop("GenerationInterval", None))
        self._marker_design_id: int = _parse.pss_int(star_system_marker_generator_info.pop("MarkerDesignId", None))
        self._marker_duration: int = _parse.pss_int(star_system_marker_generator_info.pop("MarkerDuration", None))
        self._marker_flags: int = _parse.pss_int(star_system_marker_generator_info.pop("MarkerFlags", None))
        self._marker_requirement_string: str = _parse.pss_str(star_system_marker_generator_info.pop("MarkerRequirementString", None))
        self._marker_type: str = _parse.pss_str(star_system_marker_generator_info.pop("MarkerType", None))
        self._max_active_markers: int = _parse.pss_int(star_system_marker_generator_info.pop("MaxActiveMarkers", None))
        self._metadata: str = _parse.pss_str(star_system_marker_generator_info.pop("Metadata", None))
        self._movement_type: str = _parse.pss_str(star_system_marker_generator_info.pop("MovementType", None))
        self._name: str = _parse.pss_str(star_system_marker_generator_info.pop("Name", None))
        self._next_star_system_id: int = _parse.pss_int(star_system_marker_generator_info.pop("NextStarSystemId", None))
        self._number_of_markers: int = _parse.pss_int(star_system_marker_generator_info.pop("NumberOfMarkers", None))
        self._number_of_ships: int = _parse.pss_int(star_system_marker_generator_info.pop("NumberOfShips", None))
        self._origin_next_star_system_id: int = _parse.pss_int(star_system_marker_generator_info.pop("OriginNextStarSystemId", None))
        self._origin_star_system_id: int = _parse.pss_int(star_system_marker_generator_info.pop("OriginStarSystemId", None))
        self._requirement_string: str = _parse.pss_str(star_system_marker_generator_info.pop("RequirementString", None))
        self._reward_string: str = _parse.pss_str(star_system_marker_generator_info.pop("RewardString", None))
        self._ship_ids: str = _parse.pss_str(star_system_marker_generator_info.pop("ShipIds", None))
        self._ship_tags: str = _parse.pss_str(star_system_marker_generator_info.pop("ShipTags", None))
        self._slots: str = _parse.pss_str(star_system_marker_generator_info.pop("Slots", None))
        self._sprite_id: int = _parse.pss_int(star_system_marker_generator_info.pop("SpriteId", None))
        self._star_system_id: int = _parse.pss_int(star_system_marker_generator_info.pop("StarSystemId", None))
        self._star_system_marker_generator_id: int = _parse.pss_int(star_system_marker_generator_info.pop("StarSystemMarkerGeneratorId", None))
        self._start_date: _datetime = _parse.pss_datetime(star_system_marker_generator_info.pop("StartDate", None))
        self._tags: str = _parse.pss_str(star_system_marker_generator_info.pop("Tags", None))
        self._title: str = _parse.pss_str(star_system_marker_generator_info.pop("Title", None))
        self._travel_cool_down_time: int = _parse.pss_int(star_system_marker_generator_info.pop("TravelCoolDownTime", None))
        self._travel_duration: int = _parse.pss_int(star_system_marker_generator_info.pop("TravelDuration", None))
        self._travel_start_date: _datetime = _parse.pss_datetime(star_system_marker_generator_info.pop("TravelStartDate", None))
        self._travel_time_multiplier: int = _parse.pss_int(star_system_marker_generator_info.pop("TravelTimeMultiplier", None))
        super().__init__(star_system_marker_generator_info)

    @property
    def behavior_flags(self) -> int:
        return self._behavior_flags

    @property
    def completion_original_value(self) -> int:
        return self._completion_original_value

    @property
    def completion_value_type(self) -> str:
        return self._completion_value_type

    @property
    def cost_string(self) -> str:
        return self._cost_string

    @property
    def cost_type(self) -> str:
        return self._cost_type

    @property
    def description(self) -> str:
        return self._description

    @property
    def end_date(self) -> _datetime:
        return self._end_date

    @property
    def from_star_system_id(self) -> int:
        return self._from_star_system_id

    @property
    def generation_flags(self) -> int:
        return self._generation_flags

    @property
    def generation_interval(self) -> int:
        return self._generation_interval

    @property
    def marker_design_id(self) -> int:
        return self._marker_design_id

    @property
    def marker_duration(self) -> int:
        return self._marker_duration

    @property
    def marker_flags(self) -> int:
        return self._marker_flags

    @property
    def marker_requirement_string(self) -> str:
        return self._marker_requirement_string

    @property
    def marker_type(self) -> str:
        return self._marker_type

    @property
    def max_active_markers(self) -> int:
        return self._max_active_markers

    @property
    def metadata(self) -> str:
        return self._metadata

    @property
    def movement_type(self) -> str:
        return self._movement_type

    @property
    def name(self) -> str:
        return self._name

    @property
    def next_star_system_id(self) -> int:
        return self._next_star_system_id

    @property
    def number_of_markers(self) -> int:
        return self._number_of_markers

    @property
    def number_of_ships(self) -> int:
        return self._number_of_ships

    @property
    def origin_next_star_system_id(self) -> int:
        return self._origin_next_star_system_id

    @property
    def origin_star_system_id(self) -> int:
        return self._origin_star_system_id

    @property
    def requirement_string(self) -> str:
        return self._requirement_string

    @property
    def reward_string(self) -> str:
        return self._reward_string

    @property
    def ship_ids(self) -> str:
        return self._ship_ids

    @property
    def ship_tags(self) -> str:
        return self._ship_tags

    @property
    def slots(self) -> str:
        return self._slots

    @property
    def sprite_id(self) -> int:
        return self._sprite_id

    @property
    def star_system_id(self) -> int:
        return self._star_system_id

    @property
    def star_system_marker_generator_id(self) -> int:
        return self._star_system_marker_generator_id

    @property
    def start_date(self) -> _datetime:
        return self._start_date

    @property
    def tags(self) -> str:
        return self._tags

    @property
    def title(self) -> str:
        return self._title

    @property
    def travel_cool_down_time(self) -> int:
        return self._travel_cool_down_time

    @property
    def travel_duration(self) -> int:
        return self._travel_duration

    @property
    def travel_start_date(self) -> _datetime:
        return self._travel_start_date

    @property
    def travel_time_multiplier(self) -> int:
        return self._travel_time_multiplier

    def _key(self):
        return (
            self.behavior_flags,
            self.completion_original_value,
            self.completion_value_type,
            self.cost_string,
            self.cost_type,
            self.description,
            self.end_date,
            self.from_star_system_id,
            self.generation_flags,
            self.generation_interval,
            self.marker_design_id,
            self.marker_duration,
            self.marker_flags,
            self.marker_requirement_string,
            self.marker_type,
            self.max_active_markers,
            self.metadata,
            self.movement_type,
            self.name,
            self.next_star_system_id,
            self.number_of_markers,
            self.number_of_ships,
            self.origin_next_star_system_id,
            self.origin_star_system_id,
            self.requirement_string,
            self.reward_string,
            self.ship_ids,
            self.ship_tags,
            self.slots,
            self.sprite_id,
            self.star_system_id,
            self.star_system_marker_generator_id,
            self.start_date,
            self.tags,
            self.title,
            self.travel_cool_down_time,
            self.travel_duration,
            self.travel_start_date,
            self.travel_time_multiplier,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "BehaviorFlags": self.behavior_flags,
                "CompletionOriginalValue": self.completion_original_value,
                "CompletionValueType": self.completion_value_type,
                "CostString": self.cost_string,
                "CostType": self.cost_type,
                "Description": self.description,
                "EndDate": self.end_date,
                "FromStarSystemId": self.from_star_system_id,
                "GenerationFlags": self.generation_flags,
                "GenerationInterval": self.generation_interval,
                "MarkerDesignId": self.marker_design_id,
                "MarkerDuration": self.marker_duration,
                "MarkerFlags": self.marker_flags,
                "MarkerRequirementString": self.marker_requirement_string,
                "MarkerType": self.marker_type,
                "MaxActiveMarkers": self.max_active_markers,
                "Metadata": self.metadata,
                "MovementType": self.movement_type,
                "Name": self.name,
                "NextStarSystemId": self.next_star_system_id,
                "NumberOfMarkers": self.number_of_markers,
                "NumberOfShips": self.number_of_ships,
                "OriginNextStarSystemId": self.origin_next_star_system_id,
                "OriginStarSystemId": self.origin_star_system_id,
                "RequirementString": self.requirement_string,
                "RewardString": self.reward_string,
                "ShipIds": self.ship_ids,
                "ShipTags": self.ship_tags,
                "Slots": self.slots,
                "SpriteId": self.sprite_id,
                "StarSystemId": self.star_system_id,
                "StarSystemMarkerGeneratorId": self.star_system_marker_generator_id,
                "StartDate": self.start_date,
                "Tags": self.tags,
                "Title": self.title,
                "TravelCoolDownTime": self.travel_cool_down_time,
                "TravelDuration": self.travel_duration,
                "TravelStartDate": self.travel_start_date,
                "TravelTimeMultiplier": self.travel_time_multiplier,
            }
            self._dict.update(super().__dict__())

        return self._dict
