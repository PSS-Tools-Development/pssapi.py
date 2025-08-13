"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class SeasonDesignRaw(EntityBaseRaw, tag="SeasonDesign"):
    XML_NODE_NAME: str = "SeasonDesign"

    background_sprite_id: Optional[int] = attr(name="BackgroundSpriteId", default=None)
    banner_background_sprite_id: Optional[int] = attr(name="BannerBackgroundSpriteId", default=None)
    banner_sprite_id: Optional[int] = attr(name="BannerSpriteId", default=None)
    button_sprite_id: Optional[int] = attr(name="ButtonSpriteId", default=None)
    close_button_sprite_id: Optional[int] = attr(name="CloseButtonSpriteId", default=None)
    end_date: Optional[datetime] = attr(name="EndDate", default=None)
    from_date: Optional[datetime] = attr(name="FromDate", default=None)
    icon_sprite_id: Optional[int] = attr(name="IconSpriteId", default=None)
    metadata: Optional[str] = attr(name="Metadata", default=None)
    premium_reward_string: Optional[str] = attr(name="PremiumRewardString", default=None)
    prologue_description: Optional[str] = attr(name="PrologueDescription", default=None)
    repeat_reward_string: Optional[str] = attr(name="RepeatRewardString", default=None)
    requirement_string: Optional[str] = attr(name="RequirementString", default=None)
    reward_string: Optional[str] = attr(name="RewardString", default=None)
    season_description: Optional[str] = attr(name="SeasonDescription", default=None)
    season_design_id: Optional[int] = attr(name="SeasonDesignId", default=None)
    season_name: Optional[str] = attr(name="SeasonName", default=None)
    season_sprite_id: Optional[int] = attr(name="SeasonSpriteId", default=None)
    season_type: Optional[str] = attr(name="SeasonType", default=None)
    sub_title: Optional[str] = attr(name="SubTitle", default=None)
    subtitle_sprite_id: Optional[int] = attr(name="SubtitleSpriteId", default=None)
    text_frame_sprite_id: Optional[int] = attr(name="TextFrameSpriteId", default=None)
    title_sprite_id: Optional[int] = attr(name="TitleSpriteId", default=None)

    def _key(self):
        return (
            self.background_sprite_id,
            self.banner_background_sprite_id,
            self.banner_sprite_id,
            self.button_sprite_id,
            self.close_button_sprite_id,
            self.end_date,
            self.from_date,
            self.icon_sprite_id,
            self.metadata,
            self.premium_reward_string,
            self.prologue_description,
            self.repeat_reward_string,
            self.requirement_string,
            self.reward_string,
            self.season_description,
            self.season_design_id,
            self.season_name,
            self.season_sprite_id,
            self.season_type,
            self.sub_title,
            self.subtitle_sprite_id,
            self.text_frame_sprite_id,
            self.title_sprite_id,
        )


__all__ = [
    "SeasonDesignRaw",
]
