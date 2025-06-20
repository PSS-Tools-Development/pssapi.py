"""
This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class DivisionDesignRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "DivisionDesign"

    def __init__(self, division_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._background_sprite_id: int = _parse.pss_int(division_design_info.pop("BackgroundSpriteId", None))
        self._banner_sprite_ids: str = _parse.pss_str(division_design_info.pop("BannerSpriteIds", None))
        self._division_design_id: int = _parse.pss_int(division_design_info.pop("DivisionDesignId", None))
        self._division_name: str = _parse.pss_str(division_design_info.pop("DivisionName", None))
        self._division_type: str = _parse.pss_str(division_design_info.pop("DivisionType", None))
        self._finals_immunity_percentage: int = _parse.pss_int(division_design_info.pop("FinalsImmunityPercentage", None))
        self._logo_sprite_id: int = _parse.pss_int(division_design_info.pop("LogoSpriteId", None))
        self._max_rank: int = _parse.pss_int(division_design_info.pop("MaxRank", None))
        self._min_rank: int = _parse.pss_int(division_design_info.pop("MinRank", None))
        self._monthly_achievement_design_ids: str = _parse.pss_str(division_design_info.pop("MonthlyAchievementDesignIds", None))
        self._reward_strings: str = _parse.pss_str(division_design_info.pop("RewardStrings", None))
        self._yearly_achievement_design_ids: str = _parse.pss_str(division_design_info.pop("YearlyAchievementDesignIds", None))
        super().__init__(division_design_info)

    @property
    def background_sprite_id(self) -> int:
        return self._background_sprite_id

    @property
    def banner_sprite_ids(self) -> str:
        return self._banner_sprite_ids

    @property
    def division_design_id(self) -> int:
        return self._division_design_id

    @property
    def division_name(self) -> str:
        return self._division_name

    @property
    def division_type(self) -> str:
        return self._division_type

    @property
    def finals_immunity_percentage(self) -> int:
        return self._finals_immunity_percentage

    @property
    def logo_sprite_id(self) -> int:
        return self._logo_sprite_id

    @property
    def max_rank(self) -> int:
        return self._max_rank

    @property
    def min_rank(self) -> int:
        return self._min_rank

    @property
    def monthly_achievement_design_ids(self) -> str:
        return self._monthly_achievement_design_ids

    @property
    def reward_strings(self) -> str:
        return self._reward_strings

    @property
    def yearly_achievement_design_ids(self) -> str:
        return self._yearly_achievement_design_ids

    def _key(self):
        return (
            self.background_sprite_id,
            self.banner_sprite_ids,
            self.division_design_id,
            self.division_name,
            self.division_type,
            self.finals_immunity_percentage,
            self.logo_sprite_id,
            self.max_rank,
            self.min_rank,
            self.monthly_achievement_design_ids,
            self.reward_strings,
            self.yearly_achievement_design_ids,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "BackgroundSpriteId": self.background_sprite_id,
                "BannerSpriteIds": self.banner_sprite_ids,
                "DivisionDesignId": self.division_design_id,
                "DivisionName": self.division_name,
                "DivisionType": self.division_type,
                "FinalsImmunityPercentage": self.finals_immunity_percentage,
                "LogoSpriteId": self.logo_sprite_id,
                "MaxRank": self.max_rank,
                "MinRank": self.min_rank,
                "MonthlyAchievementDesignIds": self.monthly_achievement_design_ids,
                "RewardStrings": self.reward_strings,
                "YearlyAchievementDesignIds": self.yearly_achievement_design_ids,
            }
            self._dict.update(super().__dict__())

        return self._dict
