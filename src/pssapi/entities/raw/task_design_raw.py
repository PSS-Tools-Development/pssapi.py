"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class TaskDesignRaw(EntityBaseRaw, tag="TaskDesign"):
    XML_NODE_NAME: str = "TaskDesign"

    available_from: Optional[datetime] = attr(name="AvailableFrom", default=None)
    available_to: Optional[datetime] = attr(name="AvailableTo", default=None)
    description: Optional[str] = attr(name="Description", default=None)
    flags: Optional[int] = attr(name="Flags", default=None)
    global_progress: Optional[int] = attr(name="GlobalProgress", default=None)
    icon_sprite_id: Optional[int] = attr(name="IconSpriteId", default=None)
    name: Optional[str] = attr(name="Name", default=None)
    objective_amount: Optional[int] = attr(name="ObjectiveAmount", default=None)
    objective_argument: Optional[str] = attr(name="ObjectiveArgument", default=None)
    objective_type: Optional[str] = attr(name="ObjectiveType", default=None)
    requirement_string: Optional[str] = attr(name="RequirementString", default=None)
    reward_distribution_string: Optional[str] = attr(name="RewardDistributionString", default=None)
    reward_string: Optional[str] = attr(name="RewardString", default=None)
    season_design_id: Optional[int] = attr(name="SeasonDesignId", default=None)
    task_category: Optional[str] = attr(name="TaskCategory", default=None)
    task_design_id: Optional[int] = attr(name="TaskDesignId", default=None)

    def _key(self):
        return (
            self.available_from,
            self.available_to,
            self.description,
            self.flags,
            self.global_progress,
            self.icon_sprite_id,
            self.name,
            self.objective_amount,
            self.objective_argument,
            self.objective_type,
            self.requirement_string,
            self.reward_distribution_string,
            self.reward_string,
            self.season_design_id,
            self.task_category,
            self.task_design_id,
        )


__all__ = [
    "TaskDesignRaw",
]
