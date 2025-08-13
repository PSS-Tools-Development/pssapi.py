"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class AchievementDesignRaw(EntityBaseRaw, tag="AchievementDesign"):
    XML_NODE_NAME: str = "AchievementDesign"

    achievement_description: Optional[str] = attr(name="AchievementDescription", default=None)
    achievement_design_id: Optional[int] = attr(name="AchievementDesignId", default=None)
    achievement_goal: Optional[int] = attr(name="AchievementGoal", default=None)
    achievement_key: Optional[str] = attr(name="AchievementKey", default=None)
    achievement_reward: Optional[int] = attr(name="AchievementReward", default=None)
    achievement_title: Optional[str] = attr(name="AchievementTitle", default=None)
    achievement_type: Optional[str] = attr(name="AchievementType", default=None)
    duration_type: Optional[str] = attr(name="DurationType", default=None)
    gas_reward: Optional[int] = attr(name="GasReward", default=None)
    guide_argument: Optional[int] = attr(name="GuideArgument", default=None)
    guide_type: Optional[str] = attr(name="GuideType", default=None)
    is_hidden: Optional[bool] = attr(name="IsHidden", default=None)
    mineral_reward: Optional[int] = attr(name="MineralReward", default=None)
    order_index: Optional[int] = attr(name="OrderIndex", default=None)
    parent_achievement_design_id: Optional[int] = attr(name="ParentAchievementDesignId", default=None)
    reward_string: Optional[str] = attr(name="RewardString", default=None)
    root_achievement_design_id: Optional[int] = attr(name="RootAchievementDesignId", default=None)
    sprite_id: Optional[int] = attr(name="SpriteId", default=None)

    def _key(self):
        return (
            self.achievement_description,
            self.achievement_design_id,
            self.achievement_goal,
            self.achievement_key,
            self.achievement_reward,
            self.achievement_title,
            self.achievement_type,
            self.duration_type,
            self.gas_reward,
            self.guide_argument,
            self.guide_type,
            self.is_hidden,
            self.mineral_reward,
            self.order_index,
            self.parent_achievement_design_id,
            self.reward_string,
            self.root_achievement_design_id,
            self.sprite_id,
        )


__all__ = [
    "AchievementDesignRaw",
]
