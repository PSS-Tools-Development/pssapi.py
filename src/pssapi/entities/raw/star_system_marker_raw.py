"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as EntityBaseRaw


class StarSystemMarkerRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "StarSystemMarker"

    def __init__(self, star_system_marker_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._completion_date: _datetime = _parse.pss_datetime(star_system_marker_info.pop("CompletionDate", None))
        self._completion_original_value: int = _parse.pss_int(star_system_marker_info.pop("CompletionOriginalValue", None))
        self._completion_remaining_value: int = _parse.pss_int(star_system_marker_info.pop("CompletionRemainingValue", None))
        self._completion_value_type: str = _parse.pss_str(star_system_marker_info.pop("CompletionValueType", None))
        self._cost_string: str = _parse.pss_str(star_system_marker_info.pop("CostString", None))
        self._cost_type: str = _parse.pss_str(star_system_marker_info.pop("CostType", None))
        self._description: str = _parse.pss_str(star_system_marker_info.pop("Description", None))
        self._expiry_date: _datetime = _parse.pss_datetime(star_system_marker_info.pop("ExpiryDate", None))
        self._from_star_system_id: int = _parse.pss_int(star_system_marker_info.pop("FromStarSystemId", None))
        self._is_collected: bool = _parse.pss_bool(star_system_marker_info.pop("IsCollected", None))
        self._is_repeatable: bool = _parse.pss_bool(star_system_marker_info.pop("IsRepeatable", None))
        self._last_update_date: _datetime = _parse.pss_datetime(star_system_marker_info.pop("LastUpdateDate", None))
        self._marker_design_id: int = _parse.pss_int(star_system_marker_info.pop("MarkerDesignId", None))
        self._marker_flags: int = _parse.pss_int(star_system_marker_info.pop("MarkerFlags", None))
        self._marker_type: str = _parse.pss_str(star_system_marker_info.pop("MarkerType", None))
        self._metadata: str = _parse.pss_str(star_system_marker_info.pop("Metadata", None))
        self._mission_design_id: int = _parse.pss_int(star_system_marker_info.pop("MissionDesignId", None))
        self._mission_event_id: int = _parse.pss_int(star_system_marker_info.pop("MissionEventId", None))
        self._movement_type: str = _parse.pss_str(star_system_marker_info.pop("MovementType", None))
        self._next_star_system_id: int = _parse.pss_int(star_system_marker_info.pop("NextStarSystemId", None))
        self._origin_next_star_system_id: int = _parse.pss_int(star_system_marker_info.pop("OriginNextStarSystemId", None))
        self._origin_star_system_id: int = _parse.pss_int(star_system_marker_info.pop("OriginStarSystemId", None))
        self._purchase_flags: int = _parse.pss_int(star_system_marker_info.pop("PurchaseFlags", None))
        self._requirement_string: str = _parse.pss_str(star_system_marker_info.pop("RequirementString", None))
        self._reward_string: str = _parse.pss_str(star_system_marker_info.pop("RewardString", None))
        self._ship_id: int = _parse.pss_int(star_system_marker_info.pop("ShipId", None))
        self._ship_ids: str = _parse.pss_str(star_system_marker_info.pop("ShipIds", None))
        self._sprite_id: int = _parse.pss_int(star_system_marker_info.pop("SpriteId", None))
        self._star_system_arrival_date: _datetime = _parse.pss_datetime(star_system_marker_info.pop("StarSystemArrivalDate", None))
        self._star_system_id: int = _parse.pss_int(star_system_marker_info.pop("StarSystemId", None))
        self._star_system_marker_generator_id: int = _parse.pss_int(star_system_marker_info.pop("StarSystemMarkerGeneratorId", None))
        self._star_system_marker_id: int = _parse.pss_int(star_system_marker_info.pop("StarSystemMarkerId", None))
        self._title: str = _parse.pss_str(star_system_marker_info.pop("Title", None))
        self._travel_cool_down_time: int = _parse.pss_int(star_system_marker_info.pop("TravelCoolDownTime", None))
        self._travel_start_date: _datetime = _parse.pss_datetime(star_system_marker_info.pop("TravelStartDate", None))
        self._travel_time_multiplier: int = _parse.pss_int(star_system_marker_info.pop("TravelTimeMultiplier", None))
        self._user_id: int = _parse.pss_int(star_system_marker_info.pop("UserId", None))
        super().__init__(star_system_marker_info)

    @property
    def completion_date(self) -> _datetime:
        return self._completion_date

    @property
    def completion_original_value(self) -> int:
        return self._completion_original_value

    @property
    def completion_remaining_value(self) -> int:
        return self._completion_remaining_value

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
    def expiry_date(self) -> _datetime:
        return self._expiry_date

    @property
    def from_star_system_id(self) -> int:
        return self._from_star_system_id

    @property
    def is_collected(self) -> bool:
        return self._is_collected

    @property
    def is_repeatable(self) -> bool:
        return self._is_repeatable

    @property
    def last_update_date(self) -> _datetime:
        return self._last_update_date

    @property
    def marker_design_id(self) -> int:
        return self._marker_design_id

    @property
    def marker_flags(self) -> int:
        return self._marker_flags

    @property
    def marker_type(self) -> str:
        return self._marker_type

    @property
    def metadata(self) -> str:
        return self._metadata

    @property
    def mission_design_id(self) -> int:
        return self._mission_design_id

    @property
    def mission_event_id(self) -> int:
        return self._mission_event_id

    @property
    def movement_type(self) -> str:
        return self._movement_type

    @property
    def next_star_system_id(self) -> int:
        return self._next_star_system_id

    @property
    def origin_next_star_system_id(self) -> int:
        return self._origin_next_star_system_id

    @property
    def origin_star_system_id(self) -> int:
        return self._origin_star_system_id

    @property
    def purchase_flags(self) -> int:
        return self._purchase_flags

    @property
    def requirement_string(self) -> str:
        return self._requirement_string

    @property
    def reward_string(self) -> str:
        return self._reward_string

    @property
    def ship_id(self) -> int:
        return self._ship_id

    @property
    def ship_ids(self) -> str:
        return self._ship_ids

    @property
    def sprite_id(self) -> int:
        return self._sprite_id

    @property
    def star_system_arrival_date(self) -> _datetime:
        return self._star_system_arrival_date

    @property
    def star_system_id(self) -> int:
        return self._star_system_id

    @property
    def star_system_marker_generator_id(self) -> int:
        return self._star_system_marker_generator_id

    @property
    def star_system_marker_id(self) -> int:
        return self._star_system_marker_id

    @property
    def title(self) -> str:
        return self._title

    @property
    def travel_cool_down_time(self) -> int:
        return self._travel_cool_down_time

    @property
    def travel_start_date(self) -> _datetime:
        return self._travel_start_date

    @property
    def travel_time_multiplier(self) -> int:
        return self._travel_time_multiplier

    @property
    def user_id(self) -> int:
        return self._user_id

    def _key(self):
        return (
            self.completion_date,
            self.completion_original_value,
            self.completion_remaining_value,
            self.completion_value_type,
            self.cost_string,
            self.cost_type,
            self.description,
            self.expiry_date,
            self.from_star_system_id,
            self.is_collected,
            self.is_repeatable,
            self.last_update_date,
            self.marker_design_id,
            self.marker_flags,
            self.marker_type,
            self.metadata,
            self.mission_design_id,
            self.mission_event_id,
            self.movement_type,
            self.next_star_system_id,
            self.origin_next_star_system_id,
            self.origin_star_system_id,
            self.purchase_flags,
            self.requirement_string,
            self.reward_string,
            self.ship_id,
            self.ship_ids,
            self.sprite_id,
            self.star_system_arrival_date,
            self.star_system_id,
            self.star_system_marker_generator_id,
            self.star_system_marker_id,
            self.title,
            self.travel_cool_down_time,
            self.travel_start_date,
            self.travel_time_multiplier,
            self.user_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "CompletionDate": self.completion_date,
                "CompletionOriginalValue": self.completion_original_value,
                "CompletionRemainingValue": self.completion_remaining_value,
                "CompletionValueType": self.completion_value_type,
                "CostString": self.cost_string,
                "CostType": self.cost_type,
                "Description": self.description,
                "ExpiryDate": self.expiry_date,
                "FromStarSystemId": self.from_star_system_id,
                "IsCollected": self.is_collected,
                "IsRepeatable": self.is_repeatable,
                "LastUpdateDate": self.last_update_date,
                "MarkerDesignId": self.marker_design_id,
                "MarkerFlags": self.marker_flags,
                "MarkerType": self.marker_type,
                "Metadata": self.metadata,
                "MissionDesignId": self.mission_design_id,
                "MissionEventId": self.mission_event_id,
                "MovementType": self.movement_type,
                "NextStarSystemId": self.next_star_system_id,
                "OriginNextStarSystemId": self.origin_next_star_system_id,
                "OriginStarSystemId": self.origin_star_system_id,
                "PurchaseFlags": self.purchase_flags,
                "RequirementString": self.requirement_string,
                "RewardString": self.reward_string,
                "ShipId": self.ship_id,
                "ShipIds": self.ship_ids,
                "SpriteId": self.sprite_id,
                "StarSystemArrivalDate": self.star_system_arrival_date,
                "StarSystemId": self.star_system_id,
                "StarSystemMarkerGeneratorId": self.star_system_marker_generator_id,
                "StarSystemMarkerId": self.star_system_marker_id,
                "Title": self.title,
                "TravelCoolDownTime": self.travel_cool_down_time,
                "TravelStartDate": self.travel_start_date,
                "TravelTimeMultiplier": self.travel_time_multiplier,
                "UserId": self.user_id,
            }
            self._dict.update(super().__dict__())

        return self._dict
