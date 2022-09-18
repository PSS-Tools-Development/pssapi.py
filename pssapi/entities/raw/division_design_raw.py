"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class DivisionDesignRaw:
    XML_NODE_NAME: str = 'DivisionDesign'

    def __init__(self, division_design_info: _EntityInfo) -> None:
        self.__division_design_id: int = _parse.pss_int(
            division_design_info.get('DivisionDesignId'))
        self.__division_name: str = _parse.pss_str(
            division_design_info.get('DivisionName'))
        self.__min_rank: int = _parse.pss_int(
            division_design_info.get('MinRank'))
        self.__max_rank: int = _parse.pss_int(
            division_design_info.get('MaxRank'))
        self.__reward_strings: str = _parse.pss_str(
            division_design_info.get('RewardStrings'))
        self.__division_type: str = _parse.pss_str(
            division_design_info.get('DivisionType'))
        self.__banner_sprite_ids: str = _parse.pss_str(
            division_design_info.get('BannerSpriteIds'))
        self.__monthly_achievement_design_ids: str = _parse.pss_str(
            division_design_info.get('MonthlyAchievementDesignIds'))
        self.__yearly_achievement_design_ids: str = _parse.pss_str(
            division_design_info.get('YearlyAchievementDesignIds'))
        self.__finals_immunity_percentage: int = _parse.pss_int(
            division_design_info.get('FinalsImmunityPercentage'))
        self.__logo_sprite_id: int = _parse.pss_int(
            division_design_info.get('LogoSpriteId'))
        self.__background_sprite_id: int = _parse.pss_int(
            division_design_info.get('BackgroundSpriteId'))

    @property
    def division_design_id(self) -> int:
        return self.__division_design_id

    @property
    def division_name(self) -> str:
        return self.__division_name

    @property
    def min_rank(self) -> int:
        return self.__min_rank

    @property
    def max_rank(self) -> int:
        return self.__max_rank

    @property
    def reward_strings(self) -> str:
        return self.__reward_strings

    @property
    def division_type(self) -> str:
        return self.__division_type

    @property
    def banner_sprite_ids(self) -> str:
        return self.__banner_sprite_ids

    @property
    def monthly_achievement_design_ids(self) -> str:
        return self.__monthly_achievement_design_ids

    @property
    def yearly_achievement_design_ids(self) -> str:
        return self.__yearly_achievement_design_ids

    @property
    def finals_immunity_percentage(self) -> int:
        return self.__finals_immunity_percentage

    @property
    def logo_sprite_id(self) -> int:
        return self.__logo_sprite_id

    @property
    def background_sprite_id(self) -> int:
        return self.__background_sprite_id
