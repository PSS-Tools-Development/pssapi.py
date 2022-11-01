"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class AchievementDesignRaw:
    XML_NODE_NAME: str = 'AchievementDesign'

    def __init__(self, achievement_design_info: _EntityInfo) -> None:
        self.__achievement_type: str = _parse.pss_str(
            achievement_design_info.get('AchievementType'))
        self.__achievement_design_id: int = _parse.pss_int(
            achievement_design_info.get('AchievementDesignId'))
        self.__order_index: int = _parse.pss_int(
            achievement_design_info.get('OrderIndex'))
        self.__achievement_reward: int = _parse.pss_int(
            achievement_design_info.get('AchievementReward'))
        self.__is_hidden: bool = _parse.pss_bool(
            achievement_design_info.get('IsHidden'))
        self.__guide_argument: int = _parse.pss_int(
            achievement_design_info.get('GuideArgument'))
        self.__achievement_title: str = _parse.pss_str(
            achievement_design_info.get('AchievementTitle'))
        self.__mineral_reward: int = _parse.pss_int(
            achievement_design_info.get('MineralReward'))
        self.__gas_reward: int = _parse.pss_int(
            achievement_design_info.get('GasReward'))
        self.__guide_type: str = _parse.pss_str(
            achievement_design_info.get('GuideType'))
        self.__parent_achievement_design_id: int = _parse.pss_int(
            achievement_design_info.get('ParentAchievementDesignId'))
        self.__sprite_id: int = _parse.pss_int(
            achievement_design_info.get('SpriteId'))
        self.__achievement_description: str = _parse.pss_str(
            achievement_design_info.get('AchievementDescription'))
        self.__root_achievement_design_id: int = _parse.pss_int(
            achievement_design_info.get('RootAchievementDesignId'))
        self.__duration_type: str = _parse.pss_str(
            achievement_design_info.get('DurationType'))
        self.__achievement_goal: int = _parse.pss_int(
            achievement_design_info.get('AchievementGoal'))
        self.__achievement_key: str = _parse.pss_str(
            achievement_design_info.get('AchievementKey'))
        self.__reward_string: str = _parse.pss_str(
            achievement_design_info.get('RewardString'))

    @property
    def achievement_type(self) -> str:
        return self.__achievement_type

    @property
    def achievement_design_id(self) -> int:
        return self.__achievement_design_id

    @property
    def order_index(self) -> int:
        return self.__order_index

    @property
    def achievement_reward(self) -> int:
        return self.__achievement_reward

    @property
    def is_hidden(self) -> bool:
        return self.__is_hidden

    @property
    def guide_argument(self) -> int:
        return self.__guide_argument

    @property
    def achievement_title(self) -> str:
        return self.__achievement_title

    @property
    def mineral_reward(self) -> int:
        return self.__mineral_reward

    @property
    def gas_reward(self) -> int:
        return self.__gas_reward

    @property
    def guide_type(self) -> str:
        return self.__guide_type

    @property
    def parent_achievement_design_id(self) -> int:
        return self.__parent_achievement_design_id

    @property
    def sprite_id(self) -> int:
        return self.__sprite_id

    @property
    def achievement_description(self) -> str:
        return self.__achievement_description

    @property
    def root_achievement_design_id(self) -> int:
        return self.__root_achievement_design_id

    @property
    def duration_type(self) -> str:
        return self.__duration_type

    @property
    def achievement_goal(self) -> int:
        return self.__achievement_goal

    @property
    def achievement_key(self) -> str:
        return self.__achievement_key

    @property
    def reward_string(self) -> str:
        return self.__reward_string
