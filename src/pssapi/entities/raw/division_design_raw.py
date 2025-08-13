"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class DivisionDesignRaw(EntityBaseRaw, tag="DivisionDesign"):
    XML_NODE_NAME: str = "DivisionDesign"

    background_sprite_id: Optional[int] = attr(name="BackgroundSpriteId", default=None)
    banner_sprite_ids: Optional[str] = attr(name="BannerSpriteIds", default=None)
    division_design_id: Optional[int] = attr(name="DivisionDesignId", default=None)
    division_name: Optional[str] = attr(name="DivisionName", default=None)
    division_type: Optional[str] = attr(name="DivisionType", default=None)
    finals_immunity_percentage: Optional[int] = attr(name="FinalsImmunityPercentage", default=None)
    logo_sprite_id: Optional[int] = attr(name="LogoSpriteId", default=None)
    max_rank: Optional[int] = attr(name="MaxRank", default=None)
    min_rank: Optional[int] = attr(name="MinRank", default=None)
    monthly_achievement_design_ids: Optional[str] = attr(name="MonthlyAchievementDesignIds", default=None)
    reward_strings: Optional[str] = attr(name="RewardStrings", default=None)
    yearly_achievement_design_ids: Optional[str] = attr(name="YearlyAchievementDesignIds", default=None)

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


__all__ = [
    "DivisionDesignRaw",
]
