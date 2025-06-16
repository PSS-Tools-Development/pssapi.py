"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class AchievementDesignRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "AchievementDesign"

    def __init__(self, achievement_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._achievement_description: str = _parse.pss_str(achievement_design_info.pop("AchievementDescription", None))
        self._achievement_design_id: int = _parse.pss_int(achievement_design_info.pop("AchievementDesignId", None))
        self._achievement_goal: int = _parse.pss_int(achievement_design_info.pop("AchievementGoal", None))
        self._achievement_key: str = _parse.pss_str(achievement_design_info.pop("AchievementKey", None))
        self._achievement_reward: int = _parse.pss_int(achievement_design_info.pop("AchievementReward", None))
        self._achievement_title: str = _parse.pss_str(achievement_design_info.pop("AchievementTitle", None))
        self._achievement_type: str = _parse.pss_str(achievement_design_info.pop("AchievementType", None))
        self._duration_type: str = _parse.pss_str(achievement_design_info.pop("DurationType", None))
        self._gas_reward: int = _parse.pss_int(achievement_design_info.pop("GasReward", None))
        self._guide_argument: int = _parse.pss_int(achievement_design_info.pop("GuideArgument", None))
        self._guide_type: str = _parse.pss_str(achievement_design_info.pop("GuideType", None))
        self._is_hidden: bool = _parse.pss_bool(achievement_design_info.pop("IsHidden", None))
        self._mineral_reward: int = _parse.pss_int(achievement_design_info.pop("MineralReward", None))
        self._order_index: int = _parse.pss_int(achievement_design_info.pop("OrderIndex", None))
        self._parent_achievement_design_id: int = _parse.pss_int(achievement_design_info.pop("ParentAchievementDesignId", None))
        self._reward_string: str = _parse.pss_str(achievement_design_info.pop("RewardString", None))
        self._root_achievement_design_id: int = _parse.pss_int(achievement_design_info.pop("RootAchievementDesignId", None))
        self._sprite_id: int = _parse.pss_int(achievement_design_info.pop("SpriteId", None))
        super().__init__(achievement_design_info)

    @property
    def achievement_description(self) -> str:
        return self._achievement_description

    @property
    def achievement_design_id(self) -> int:
        return self._achievement_design_id

    @property
    def achievement_goal(self) -> int:
        return self._achievement_goal

    @property
    def achievement_key(self) -> str:
        return self._achievement_key

    @property
    def achievement_reward(self) -> int:
        return self._achievement_reward

    @property
    def achievement_title(self) -> str:
        return self._achievement_title

    @property
    def achievement_type(self) -> str:
        return self._achievement_type

    @property
    def duration_type(self) -> str:
        return self._duration_type

    @property
    def gas_reward(self) -> int:
        return self._gas_reward

    @property
    def guide_argument(self) -> int:
        return self._guide_argument

    @property
    def guide_type(self) -> str:
        return self._guide_type

    @property
    def is_hidden(self) -> bool:
        return self._is_hidden

    @property
    def mineral_reward(self) -> int:
        return self._mineral_reward

    @property
    def order_index(self) -> int:
        return self._order_index

    @property
    def parent_achievement_design_id(self) -> int:
        return self._parent_achievement_design_id

    @property
    def reward_string(self) -> str:
        return self._reward_string

    @property
    def root_achievement_design_id(self) -> int:
        return self._root_achievement_design_id

    @property
    def sprite_id(self) -> int:
        return self._sprite_id

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

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "AchievementDescription": self.achievement_description,
                "AchievementDesignId": self.achievement_design_id,
                "AchievementGoal": self.achievement_goal,
                "AchievementKey": self.achievement_key,
                "AchievementReward": self.achievement_reward,
                "AchievementTitle": self.achievement_title,
                "AchievementType": self.achievement_type,
                "DurationType": self.duration_type,
                "GasReward": self.gas_reward,
                "GuideArgument": self.guide_argument,
                "GuideType": self.guide_type,
                "IsHidden": self.is_hidden,
                "MineralReward": self.mineral_reward,
                "OrderIndex": self.order_index,
                "ParentAchievementDesignId": self.parent_achievement_design_id,
                "RewardString": self.reward_string,
                "RootAchievementDesignId": self.root_achievement_design_id,
                "SpriteId": self.sprite_id,
            }
            self._dict.update(super().__dict__())

        return self._dict
