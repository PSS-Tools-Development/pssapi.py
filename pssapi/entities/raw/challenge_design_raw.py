"""
    This file has been generated automatically
"""

from datetime import datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ChallengeDesignRaw:
    XML_NODE_NAME: str = 'ChallengeDesign'

    def __init__(self, challenge_design_info: _EntityInfo) -> None:
        self.__is_realtime: bool = _parse.pss_bool(
            challenge_design_info.get('IsRealtime'))
        self.__is_first_free: bool = _parse.pss_bool(
            challenge_design_info.get('IsFirstFree'))
        self.__challenge_design_id: int = _parse.pss_int(
            challenge_design_info.get('ChallengeDesignId'))
        self.__name: str = _parse.pss_str(challenge_design_info.get('Name'))
        self.__description: str = _parse.pss_str(
            challenge_design_info.get('Description'))
        self.__challenge_argument: int = _parse.pss_int(
            challenge_design_info.get('ChallengeArgument'))
        self.__challenge_scoring_argument: int = _parse.pss_int(
            challenge_design_info.get('ChallengeScoringArgument'))
        self.__lives: int = _parse.pss_int(challenge_design_info.get('Lives'))
        self.__entry_fee: int = _parse.pss_int(
            challenge_design_info.get('EntryFee'))
        self.__base_prize: int = _parse.pss_int(
            challenge_design_info.get('BasePrize'))
        self.__min_battle_prize: int = _parse.pss_int(
            challenge_design_info.get('MinBattlePrize'))
        self.__max_battle_prize: int = _parse.pss_int(
            challenge_design_info.get('MaxBattlePrize'))
        self.__special_rule_argument: int = _parse.pss_int(
            challenge_design_info.get('SpecialRuleArgument'))
        self.__opponent_ship_ids: str = _parse.pss_str(
            challenge_design_info.get('OpponentShipIds'))
        self.__flags: int = _parse.pss_int(challenge_design_info.get('Flags'))
        self.__reward_string: str = _parse.pss_str(
            challenge_design_info.get('RewardString'))
        self.__requirement_string: str = _parse.pss_str(
            challenge_design_info.get('RequirementString'))
        self.__challenge_design_metadata: str = _parse.pss_str(
            challenge_design_info.get('ChallengeDesignMetadata'))
        self.__special_rule_type: str = _parse.pss_str(
            challenge_design_info.get('SpecialRuleType'))
        self.__challenge_scoring_type: str = _parse.pss_str(
            challenge_design_info.get('ChallengeScoringType'))
        self.__challenge_type: str = _parse.pss_str(
            challenge_design_info.get('ChallengeType'))
        self.__button_animation_id: int = _parse.pss_int(
            challenge_design_info.get('ButtonAnimationId'))
        self.__start_date: datetime = _parse.pss_datetime(
            challenge_design_info.get('StartDate'))
        self.__end_date: datetime = _parse.pss_datetime(
            challenge_design_info.get('EndDate'))
        self.__root_achievement_design_id: int = _parse.pss_int(
            challenge_design_info.get('RootAchievementDesignId'))
        self.__poster_sprite_id: int = _parse.pss_int(
            challenge_design_info.get('PosterSpriteId'))

    @property
    def is_realtime(self) -> bool:
        return self.__is_realtime

    @property
    def is_first_free(self) -> bool:
        return self.__is_first_free

    @property
    def challenge_design_id(self) -> int:
        return self.__challenge_design_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def challenge_argument(self) -> int:
        return self.__challenge_argument

    @property
    def challenge_scoring_argument(self) -> int:
        return self.__challenge_scoring_argument

    @property
    def lives(self) -> int:
        return self.__lives

    @property
    def entry_fee(self) -> int:
        return self.__entry_fee

    @property
    def base_prize(self) -> int:
        return self.__base_prize

    @property
    def min_battle_prize(self) -> int:
        return self.__min_battle_prize

    @property
    def max_battle_prize(self) -> int:
        return self.__max_battle_prize

    @property
    def special_rule_argument(self) -> int:
        return self.__special_rule_argument

    @property
    def opponent_ship_ids(self) -> str:
        return self.__opponent_ship_ids

    @property
    def flags(self) -> int:
        return self.__flags

    @property
    def reward_string(self) -> str:
        return self.__reward_string

    @property
    def requirement_string(self) -> str:
        return self.__requirement_string

    @property
    def challenge_design_metadata(self) -> str:
        return self.__challenge_design_metadata

    @property
    def special_rule_type(self) -> str:
        return self.__special_rule_type

    @property
    def challenge_scoring_type(self) -> str:
        return self.__challenge_scoring_type

    @property
    def challenge_type(self) -> str:
        return self.__challenge_type

    @property
    def button_animation_id(self) -> int:
        return self.__button_animation_id

    @property
    def start_date(self) -> datetime:
        return self.__start_date

    @property
    def end_date(self) -> datetime:
        return self.__end_date

    @property
    def root_achievement_design_id(self) -> int:
        return self.__root_achievement_design_id

    @property
    def poster_sprite_id(self) -> int:
        return self.__poster_sprite_id
