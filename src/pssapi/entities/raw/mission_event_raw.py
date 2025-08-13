"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class MissionEventRaw(EntityBaseRaw, tag="MissionEvent"):
    XML_NODE_NAME: str = "MissionEvent"

    background_id: Optional[int] = attr(name="BackgroundId", default=None)
    background_sprite_id: Optional[int] = attr(name="BackgroundSpriteId", default=None)
    cost_string: Optional[str] = attr(name="CostString", default=None)
    end_description: Optional[str] = attr(name="EndDescription", default=None)
    event_xml_string: Optional[str] = attr(name="EventXmlString", default=None)
    flags: Optional[int] = attr(name="Flags", default=None)
    function_string: Optional[str] = attr(name="FunctionString", default=None)
    is_single_play: Optional[bool] = attr(name="IsSinglePlay", default=None)
    mission_design_id: Optional[int] = attr(name="MissionDesignId", default=None)
    mission_event_id: Optional[int] = attr(name="MissionEventId", default=None)
    mission_event_type: Optional[str] = attr(name="MissionEventType", default=None)
    parent_mission_event_id: Optional[int] = attr(name="ParentMissionEventId", default=None)
    percent_weight: Optional[int] = attr(name="PercentWeight", default=None)
    requirement_description: Optional[str] = attr(name="RequirementDescription", default=None)
    requirement_string: Optional[str] = attr(name="RequirementString", default=None)
    reward_string: Optional[str] = attr(name="RewardString", default=None)
    ship_id: Optional[int] = attr(name="ShipId", default=None)
    start_description: Optional[str] = attr(name="StartDescription", default=None)
    time_limit: Optional[int] = attr(name="TimeLimit", default=None)
    title: Optional[str] = attr(name="Title", default=None)

    def _key(self):
        return (
            self.background_id,
            self.background_sprite_id,
            self.cost_string,
            self.end_description,
            self.event_xml_string,
            self.flags,
            self.function_string,
            self.is_single_play,
            self.mission_design_id,
            self.mission_event_id,
            self.mission_event_type,
            self.parent_mission_event_id,
            self.percent_weight,
            self.requirement_description,
            self.requirement_string,
            self.reward_string,
            self.ship_id,
            self.start_description,
            self.time_limit,
            self.title,
        )


__all__ = [
    "MissionEventRaw",
]
