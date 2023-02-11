"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import List as _List

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class AchievementDesignRaw:
    XML_NODE_NAME: str = 'AchievementDesign'

    def __init__(self, achievement_design_info: _EntityInfo) -> None:
        self.achievement_description: str = _parse.pss_str(achievement_design_info.get('AchievementDescription'))
        self.achievement_design_id: int = _parse.pss_int(achievement_design_info.get('AchievementDesignId'))
        self.achievement_goal: int = _parse.pss_int(achievement_design_info.get('AchievementGoal'))
        self.achievement_key: str = _parse.pss_str(achievement_design_info.get('AchievementKey'))
        self.achievement_reward: int = _parse.pss_int(achievement_design_info.get('AchievementReward'))
        self.achievement_title: str = _parse.pss_str(achievement_design_info.get('AchievementTitle'))
        self.achievement_type: str = _parse.pss_str(achievement_design_info.get('AchievementType'))
        self.duration_type: str = _parse.pss_str(achievement_design_info.get('DurationType'))
        self.gas_reward: int = _parse.pss_int(achievement_design_info.get('GasReward'))
        self.guide_argument: int = _parse.pss_int(achievement_design_info.get('GuideArgument'))
        self.guide_type: str = _parse.pss_str(achievement_design_info.get('GuideType'))
        self.is_hidden: bool = _parse.pss_bool(achievement_design_info.get('IsHidden'))
        self.mineral_reward: int = _parse.pss_int(achievement_design_info.get('MineralReward'))
        self.order_index: int = _parse.pss_int(achievement_design_info.get('OrderIndex'))
        self.parent_achievement_design_id: int = _parse.pss_int(achievement_design_info.get('ParentAchievementDesignId'))
        self.reward_string: str = _parse.pss_str(achievement_design_info.get('RewardString'))
        self.root_achievement_design_id: int = _parse.pss_int(achievement_design_info.get('RootAchievementDesignId'))
        self.sprite_id: int = _parse.pss_int(achievement_design_info.get('SpriteId'))
