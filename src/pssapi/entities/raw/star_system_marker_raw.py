"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class StarSystemMarkerRaw(EntityBaseRaw, tag="StarSystemMarker"):
    XML_NODE_NAME: str = "StarSystemMarker"

    completion_date: Optional[datetime] = attr(name="CompletionDate", default=None)
    completion_original_value: Optional[int] = attr(name="CompletionOriginalValue", default=None)
    completion_remaining_value: Optional[int] = attr(name="CompletionRemainingValue", default=None)
    completion_value_type: Optional[str] = attr(name="CompletionValueType", default=None)
    cost_string: Optional[str] = attr(name="CostString", default=None)
    cost_type: Optional[str] = attr(name="CostType", default=None)
    description: Optional[str] = attr(name="Description", default=None)
    expiry_date: Optional[datetime] = attr(name="ExpiryDate", default=None)
    from_star_system_id: Optional[int] = attr(name="FromStarSystemId", default=None)
    is_collected: Optional[bool] = attr(name="IsCollected", default=None)
    is_repeatable: Optional[bool] = attr(name="IsRepeatable", default=None)
    last_update_date: Optional[datetime] = attr(name="LastUpdateDate", default=None)
    marker_design_id: Optional[int] = attr(name="MarkerDesignId", default=None)
    marker_flags: Optional[int] = attr(name="MarkerFlags", default=None)
    marker_type: Optional[str] = attr(name="MarkerType", default=None)
    metadata: Optional[str] = attr(name="Metadata", default=None)
    mission_design_id: Optional[int] = attr(name="MissionDesignId", default=None)
    mission_event_id: Optional[int] = attr(name="MissionEventId", default=None)
    movement_type: Optional[str] = attr(name="MovementType", default=None)
    next_star_system_id: Optional[int] = attr(name="NextStarSystemId", default=None)
    origin_next_star_system_id: Optional[int] = attr(name="OriginNextStarSystemId", default=None)
    origin_star_system_id: Optional[int] = attr(name="OriginStarSystemId", default=None)
    purchase_flags: Optional[int] = attr(name="PurchaseFlags", default=None)
    requirement_string: Optional[str] = attr(name="RequirementString", default=None)
    reward_string: Optional[str] = attr(name="RewardString", default=None)
    ship_id: Optional[int] = attr(name="ShipId", default=None)
    ship_ids: Optional[str] = attr(name="ShipIds", default=None)
    sprite_id: Optional[int] = attr(name="SpriteId", default=None)
    star_system_arrival_date: Optional[datetime] = attr(name="StarSystemArrivalDate", default=None)
    star_system_id: Optional[int] = attr(name="StarSystemId", default=None)
    star_system_marker_generator_id: Optional[int] = attr(name="StarSystemMarkerGeneratorId", default=None)
    star_system_marker_id: Optional[int] = attr(name="StarSystemMarkerId", default=None)
    title: Optional[str] = attr(name="Title", default=None)
    travel_cool_down_time: Optional[int] = attr(name="TravelCoolDownTime", default=None)
    travel_start_date: Optional[datetime] = attr(name="TravelStartDate", default=None)
    travel_time_multiplier: Optional[int] = attr(name="TravelTimeMultiplier", default=None)
    user_id: Optional[int] = attr(name="UserId", default=None)

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


__all__ = [
    "StarSystemMarkerRaw",
]
