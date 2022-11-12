"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class DivisionDesignRaw:
    XML_NODE_NAME: str = 'DivisionDesign'

    def __init__(self, division_design_info: _EntityInfo) -> None:
        self.background_sprite_id: int = _parse.pss_int(
            division_design_info.get('BackgroundSpriteId'))
        self.banner_sprite_ids: str = _parse.pss_str(
            division_design_info.get('BannerSpriteIds'))
        self.division_design_id: int = _parse.pss_int(
            division_design_info.get('DivisionDesignId'))
        self.division_name: str = _parse.pss_str(
            division_design_info.get('DivisionName'))
        self.division_type: str = _parse.pss_str(
            division_design_info.get('DivisionType'))
        self.finals_immunity_percentage: int = _parse.pss_int(
            division_design_info.get('FinalsImmunityPercentage'))
        self.logo_sprite_id: int = _parse.pss_int(
            division_design_info.get('LogoSpriteId'))
        self.max_rank: int = _parse.pss_int(
            division_design_info.get('MaxRank'))
        self.min_rank: int = _parse.pss_int(
            division_design_info.get('MinRank'))
        self.monthly_achievement_design_ids: str = _parse.pss_str(
            division_design_info.get('MonthlyAchievementDesignIds'))
        self.reward_strings: str = _parse.pss_str(
            division_design_info.get('RewardStrings'))
        self.yearly_achievement_design_ids: str = _parse.pss_str(
            division_design_info.get('YearlyAchievementDesignIds'))
