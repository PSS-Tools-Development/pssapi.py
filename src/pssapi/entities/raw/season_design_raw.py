"""
This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class SeasonDesignRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "SeasonDesign"

    def __init__(self, season_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._background_sprite_id: int = _parse.pss_int(season_design_info.pop("BackgroundSpriteId", None))
        self._banner_background_sprite_id: int = _parse.pss_int(season_design_info.pop("BannerBackgroundSpriteId", None))
        self._banner_sprite_id: int = _parse.pss_int(season_design_info.pop("BannerSpriteId", None))
        self._button_sprite_id: int = _parse.pss_int(season_design_info.pop("ButtonSpriteId", None))
        self._close_button_sprite_id: int = _parse.pss_int(season_design_info.pop("CloseButtonSpriteId", None))
        self._end_date: _datetime = _parse.pss_datetime(season_design_info.pop("EndDate", None))
        self._from_date: _datetime = _parse.pss_datetime(season_design_info.pop("FromDate", None))
        self._icon_sprite_id: int = _parse.pss_int(season_design_info.pop("IconSpriteId", None))
        self._metadata: str = _parse.pss_str(season_design_info.pop("Metadata", None))
        self._premium_reward_string: str = _parse.pss_str(season_design_info.pop("PremiumRewardString", None))
        self._prologue_description: str = _parse.pss_str(season_design_info.pop("PrologueDescription", None))
        self._repeat_reward_string: str = _parse.pss_str(season_design_info.pop("RepeatRewardString", None))
        self._requirement_string: str = _parse.pss_str(season_design_info.pop("RequirementString", None))
        self._reward_string: str = _parse.pss_str(season_design_info.pop("RewardString", None))
        self._season_description: str = _parse.pss_str(season_design_info.pop("SeasonDescription", None))
        self._season_design_id: int = _parse.pss_int(season_design_info.pop("SeasonDesignId", None))
        self._season_name: str = _parse.pss_str(season_design_info.pop("SeasonName", None))
        self._season_sprite_id: int = _parse.pss_int(season_design_info.pop("SeasonSpriteId", None))
        self._season_type: str = _parse.pss_str(season_design_info.pop("SeasonType", None))
        self._sub_title: str = _parse.pss_str(season_design_info.pop("SubTitle", None))
        self._subtitle_sprite_id: int = _parse.pss_int(season_design_info.pop("SubtitleSpriteId", None))
        self._text_frame_sprite_id: int = _parse.pss_int(season_design_info.pop("TextFrameSpriteId", None))
        self._title_sprite_id: int = _parse.pss_int(season_design_info.pop("TitleSpriteId", None))
        super().__init__(season_design_info)

    @property
    def background_sprite_id(self) -> int:
        return self._background_sprite_id

    @property
    def banner_background_sprite_id(self) -> int:
        return self._banner_background_sprite_id

    @property
    def banner_sprite_id(self) -> int:
        return self._banner_sprite_id

    @property
    def button_sprite_id(self) -> int:
        return self._button_sprite_id

    @property
    def close_button_sprite_id(self) -> int:
        return self._close_button_sprite_id

    @property
    def end_date(self) -> _datetime:
        return self._end_date

    @property
    def from_date(self) -> _datetime:
        return self._from_date

    @property
    def icon_sprite_id(self) -> int:
        return self._icon_sprite_id

    @property
    def metadata(self) -> str:
        return self._metadata

    @property
    def premium_reward_string(self) -> str:
        return self._premium_reward_string

    @property
    def prologue_description(self) -> str:
        return self._prologue_description

    @property
    def repeat_reward_string(self) -> str:
        return self._repeat_reward_string

    @property
    def requirement_string(self) -> str:
        return self._requirement_string

    @property
    def reward_string(self) -> str:
        return self._reward_string

    @property
    def season_description(self) -> str:
        return self._season_description

    @property
    def season_design_id(self) -> int:
        return self._season_design_id

    @property
    def season_name(self) -> str:
        return self._season_name

    @property
    def season_sprite_id(self) -> int:
        return self._season_sprite_id

    @property
    def season_type(self) -> str:
        return self._season_type

    @property
    def sub_title(self) -> str:
        return self._sub_title

    @property
    def subtitle_sprite_id(self) -> int:
        return self._subtitle_sprite_id

    @property
    def text_frame_sprite_id(self) -> int:
        return self._text_frame_sprite_id

    @property
    def title_sprite_id(self) -> int:
        return self._title_sprite_id

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

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "BackgroundSpriteId": self.background_sprite_id,
                "BannerBackgroundSpriteId": self.banner_background_sprite_id,
                "BannerSpriteId": self.banner_sprite_id,
                "ButtonSpriteId": self.button_sprite_id,
                "CloseButtonSpriteId": self.close_button_sprite_id,
                "EndDate": self.end_date,
                "FromDate": self.from_date,
                "IconSpriteId": self.icon_sprite_id,
                "Metadata": self.metadata,
                "PremiumRewardString": self.premium_reward_string,
                "PrologueDescription": self.prologue_description,
                "RepeatRewardString": self.repeat_reward_string,
                "RequirementString": self.requirement_string,
                "RewardString": self.reward_string,
                "SeasonDescription": self.season_description,
                "SeasonDesignId": self.season_design_id,
                "SeasonName": self.season_name,
                "SeasonSpriteId": self.season_sprite_id,
                "SeasonType": self.season_type,
                "SubTitle": self.sub_title,
                "SubtitleSpriteId": self.subtitle_sprite_id,
                "TextFrameSpriteId": self.text_frame_sprite_id,
                "TitleSpriteId": self.title_sprite_id,
            }
            self._dict.update(super().__dict__())

        return self._dict
