"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class SituationDesignRaw(EntityBaseRaw, tag="SituationDesign"):
    XML_NODE_NAME: str = "SituationDesign"

    chance: Optional[int] = attr(name="Chance", default=None)
    change_argument_string: Optional[str] = attr(name="ChangeArgumentString", default=None)
    change_type: Optional[str] = attr(name="ChangeType", default=None)
    daily_occurrence_limit: Optional[int] = attr(name="DailyOccurrenceLimit", default=None)
    end_date: Optional[datetime] = attr(name="EndDate", default=None)
    flags: Optional[int] = attr(name="Flags", default=None)
    from_date: Optional[datetime] = attr(name="FromDate", default=None)
    icon_sprite_id: Optional[int] = attr(name="IconSpriteId", default=None)
    requirement_string: Optional[str] = attr(name="RequirementString", default=None)
    situation_description: Optional[str] = attr(name="SituationDescription", default=None)
    situation_design_id: Optional[int] = attr(name="SituationDesignId", default=None)
    situation_name: Optional[str] = attr(name="SituationName", default=None)
    situation_tags: Optional[str] = attr(name="SituationTags", default=None)
    situation_type: Optional[str] = attr(name="SituationType", default=None)
    trigger_type: Optional[str] = attr(name="TriggerType", default=None)

    def _key(self):
        return (
            self.chance,
            self.change_argument_string,
            self.change_type,
            self.daily_occurrence_limit,
            self.end_date,
            self.flags,
            self.from_date,
            self.icon_sprite_id,
            self.requirement_string,
            self.situation_description,
            self.situation_design_id,
            self.situation_name,
            self.situation_tags,
            self.situation_type,
            self.trigger_type,
        )


__all__ = [
    "SituationDesignRaw",
]
