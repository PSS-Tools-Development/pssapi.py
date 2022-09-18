"""
    This file has been generated automatically
"""

from datetime import datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class SeasonDesignRaw:
    XML_NODE_NAME: str = 'SeasonDesign'

    def __init__(self, season_design_info: _EntityInfo) -> None:
        self.__season_design_id: int = _parse.pss_int(
            season_design_info.get('SeasonDesignId'))
        self.__season_name: str = _parse.pss_str(
            season_design_info.get('SeasonName'))
        self.__season_description: str = _parse.pss_str(
            season_design_info.get('SeasonDescription'))
        self.__season_type: str = _parse.pss_str(
            season_design_info.get('SeasonType'))
        self.__requirement_string: str = _parse.pss_str(
            season_design_info.get('RequirementString'))
        self.__metadata: str = _parse.pss_str(
            season_design_info.get('Metadata'))
        self.__sub_title: str = _parse.pss_str(
            season_design_info.get('SubTitle'))
        self.__prologue_description: str = _parse.pss_str(
            season_design_info.get('PrologueDescription'))
        self.__reward_string: str = _parse.pss_str(
            season_design_info.get('RewardString'))
        self.__from_date: datetime = _parse.pss_datetime(
            season_design_info.get('FromDate'))
        self.__end_date: datetime = _parse.pss_datetime(
            season_design_info.get('EndDate'))
        self.__icon_sprite_id: int = _parse.pss_int(
            season_design_info.get('IconSpriteId'))
        self.__background_sprite_id: int = _parse.pss_int(
            season_design_info.get('BackgroundSpriteId'))
        self.__season_sprite_id: int = _parse.pss_int(
            season_design_info.get('SeasonSpriteId'))
        self.__title_sprite_id: int = _parse.pss_int(
            season_design_info.get('TitleSpriteId'))
        self.__close_button_sprite_id: int = _parse.pss_int(
            season_design_info.get('CloseButtonSpriteId'))
        self.__button_sprite_id: int = _parse.pss_int(
            season_design_info.get('ButtonSpriteId'))
        self.__text_frame_sprite_id: int = _parse.pss_int(
            season_design_info.get('TextFrameSpriteId'))
        self.__banner_sprite_id: int = _parse.pss_int(
            season_design_info.get('BannerSpriteId'))
        self.__banner_background_sprite_id: int = _parse.pss_int(
            season_design_info.get('BannerBackgroundSpriteId'))
        self.__subtitle_sprite_id: int = _parse.pss_int(
            season_design_info.get('SubtitleSpriteId'))

    @property
    def season_design_id(self) -> int:
        return self.__season_design_id

    @property
    def season_name(self) -> str:
        return self.__season_name

    @property
    def season_description(self) -> str:
        return self.__season_description

    @property
    def season_type(self) -> str:
        return self.__season_type

    @property
    def requirement_string(self) -> str:
        return self.__requirement_string

    @property
    def metadata(self) -> str:
        return self.__metadata

    @property
    def sub_title(self) -> str:
        return self.__sub_title

    @property
    def prologue_description(self) -> str:
        return self.__prologue_description

    @property
    def reward_string(self) -> str:
        return self.__reward_string

    @property
    def from_date(self) -> datetime:
        return self.__from_date

    @property
    def end_date(self) -> datetime:
        return self.__end_date

    @property
    def icon_sprite_id(self) -> int:
        return self.__icon_sprite_id

    @property
    def background_sprite_id(self) -> int:
        return self.__background_sprite_id

    @property
    def season_sprite_id(self) -> int:
        return self.__season_sprite_id

    @property
    def title_sprite_id(self) -> int:
        return self.__title_sprite_id

    @property
    def close_button_sprite_id(self) -> int:
        return self.__close_button_sprite_id

    @property
    def button_sprite_id(self) -> int:
        return self.__button_sprite_id

    @property
    def text_frame_sprite_id(self) -> int:
        return self.__text_frame_sprite_id

    @property
    def banner_sprite_id(self) -> int:
        return self.__banner_sprite_id

    @property
    def banner_background_sprite_id(self) -> int:
        return self.__banner_background_sprite_id

    @property
    def subtitle_sprite_id(self) -> int:
        return self.__subtitle_sprite_id
