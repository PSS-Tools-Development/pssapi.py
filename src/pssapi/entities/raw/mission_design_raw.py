"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class MissionDesignRaw(EntityBaseRaw, tag="MissionDesign"):
    XML_NODE_NAME: str = "MissionDesign"

    available_every_x_days: Optional[int] = attr(name="AvailableEveryXDays", default=None)
    available_from: Optional[datetime] = attr(name="AvailableFrom", default=None)
    available_to: Optional[datetime] = attr(name="AvailableTo", default=None)
    background_sprite_id: Optional[int] = attr(name="BackgroundSpriteId", default=None)
    chance: Optional[int] = attr(name="Chance", default=None)
    condition: Optional[str] = attr(name="Condition", default=None)
    exploration_percentage: Optional[int] = attr(name="ExplorationPercentage", default=None)
    flags: Optional[int] = attr(name="Flags", default=None)
    is_single_play: Optional[bool] = attr(name="IsSinglePlay", default=None)
    max_attempts_per_day: Optional[int] = attr(name="MaxAttemptsPerDay", default=None)
    max_ship_level: Optional[int] = attr(name="MaxShipLevel", default=None)
    metadata: Optional[str] = attr(name="Metadata", default=None)
    min_duration_since_last_event: Optional[int] = attr(name="MinDurationSinceLastEvent", default=None)
    min_ship_level: Optional[int] = attr(name="MinShipLevel", default=None)
    mission_description: Optional[str] = attr(name="MissionDescription", default=None)
    mission_design_id: Optional[int] = attr(name="MissionDesignId", default=None)
    mission_design_status: Optional[str] = attr(name="MissionDesignStatus", default=None)
    mission_design_type: Optional[str] = attr(name="MissionDesignType", default=None)
    mission_title: Optional[str] = attr(name="MissionTitle", default=None)
    required_mission_design_id: Optional[int] = attr(name="RequiredMissionDesignId", default=None)
    requirement_description: Optional[str] = attr(name="RequirementDescription", default=None)
    requirement_string: Optional[str] = attr(name="RequirementString", default=None)
    star_system_id: Optional[int] = attr(name="StarSystemId", default=None)
    story_animation_id: Optional[int] = attr(name="StoryAnimationId", default=None)
    story_description: Optional[str] = attr(name="StoryDescription", default=None)
    weight: Optional[int] = attr(name="Weight", default=None)

    def _key(self):
        return (
            self.available_every_x_days,
            self.available_from,
            self.available_to,
            self.background_sprite_id,
            self.chance,
            self.condition,
            self.exploration_percentage,
            self.flags,
            self.is_single_play,
            self.max_attempts_per_day,
            self.max_ship_level,
            self.metadata,
            self.min_duration_since_last_event,
            self.min_ship_level,
            self.mission_description,
            self.mission_design_id,
            self.mission_design_status,
            self.mission_design_type,
            self.mission_title,
            self.required_mission_design_id,
            self.requirement_description,
            self.requirement_string,
            self.star_system_id,
            self.story_animation_id,
            self.story_description,
            self.weight,
        )


__all__ = [
    "MissionDesignRaw",
]
