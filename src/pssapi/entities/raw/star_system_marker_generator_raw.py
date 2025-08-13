"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class StarSystemMarkerGeneratorRaw(EntityBaseRaw, tag="StarSystemMarkerGenerator"):
    XML_NODE_NAME: str = "StarSystemMarkerGenerator"

    behavior_flags: Optional[int] = attr(name="BehaviorFlags", default=None)
    completion_original_value: Optional[int] = attr(name="CompletionOriginalValue", default=None)
    completion_value_type: Optional[str] = attr(name="CompletionValueType", default=None)
    cost_string: Optional[str] = attr(name="CostString", default=None)
    cost_type: Optional[str] = attr(name="CostType", default=None)
    description: Optional[str] = attr(name="Description", default=None)
    end_date: Optional[datetime] = attr(name="EndDate", default=None)
    from_star_system_id: Optional[int] = attr(name="FromStarSystemId", default=None)
    generation_flags: Optional[int] = attr(name="GenerationFlags", default=None)
    generation_interval: Optional[int] = attr(name="GenerationInterval", default=None)
    marker_design_id: Optional[int] = attr(name="MarkerDesignId", default=None)
    marker_duration: Optional[int] = attr(name="MarkerDuration", default=None)
    marker_flags: Optional[int] = attr(name="MarkerFlags", default=None)
    marker_requirement_string: Optional[str] = attr(name="MarkerRequirementString", default=None)
    marker_type: Optional[str] = attr(name="MarkerType", default=None)
    max_active_markers: Optional[int] = attr(name="MaxActiveMarkers", default=None)
    metadata: Optional[str] = attr(name="Metadata", default=None)
    movement_type: Optional[str] = attr(name="MovementType", default=None)
    name: Optional[str] = attr(name="Name", default=None)
    next_star_system_id: Optional[int] = attr(name="NextStarSystemId", default=None)
    number_of_markers: Optional[int] = attr(name="NumberOfMarkers", default=None)
    number_of_ships: Optional[int] = attr(name="NumberOfShips", default=None)
    origin_next_star_system_id: Optional[int] = attr(name="OriginNextStarSystemId", default=None)
    origin_star_system_id: Optional[int] = attr(name="OriginStarSystemId", default=None)
    requirement_string: Optional[str] = attr(name="RequirementString", default=None)
    reward_string: Optional[str] = attr(name="RewardString", default=None)
    ship_ids: Optional[str] = attr(name="ShipIds", default=None)
    ship_tags: Optional[str] = attr(name="ShipTags", default=None)
    slots: Optional[str] = attr(name="Slots", default=None)
    sprite_id: Optional[int] = attr(name="SpriteId", default=None)
    star_system_id: Optional[int] = attr(name="StarSystemId", default=None)
    star_system_marker_generator_id: Optional[int] = attr(name="StarSystemMarkerGeneratorId", default=None)
    start_date: Optional[datetime] = attr(name="StartDate", default=None)
    tags: Optional[str] = attr(name="Tags", default=None)
    title: Optional[str] = attr(name="Title", default=None)
    travel_cool_down_time: Optional[int] = attr(name="TravelCoolDownTime", default=None)
    travel_duration: Optional[int] = attr(name="TravelDuration", default=None)
    travel_start_date: Optional[datetime] = attr(name="TravelStartDate", default=None)
    travel_time_multiplier: Optional[int] = attr(name="TravelTimeMultiplier", default=None)

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


__all__ = [
    "StarSystemMarkerGeneratorRaw",
]
