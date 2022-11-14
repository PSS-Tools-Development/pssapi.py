"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import List as _List

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class SeasonDesignRaw:
    XML_NODE_NAME: str = 'SeasonDesign'

    def __init__(self, season_design_info: _EntityInfo) -> None:
        self.background_sprite_id: int = _parse.pss_int(season_design_info.get('BackgroundSpriteId'))
        self.banner_background_sprite_id: int = _parse.pss_int(season_design_info.get('BannerBackgroundSpriteId'))
        self.banner_sprite_id: int = _parse.pss_int(season_design_info.get('BannerSpriteId'))
        self.button_sprite_id: int = _parse.pss_int(season_design_info.get('ButtonSpriteId'))
        self.close_button_sprite_id: int = _parse.pss_int(season_design_info.get('CloseButtonSpriteId'))
        self.end_date: _datetime = _parse.pss__datetime(season_design_info.get('EndDate'))
        self.from_date: _datetime = _parse.pss__datetime(season_design_info.get('FromDate'))
        self.icon_sprite_id: int = _parse.pss_int(season_design_info.get('IconSpriteId'))
        self.metadata: str = _parse.pss_str(season_design_info.get('Metadata'))
        self.prologue_description: str = _parse.pss_str(season_design_info.get('PrologueDescription'))
        self.requirement_string: str = _parse.pss_str(season_design_info.get('RequirementString'))
        self.reward_string: str = _parse.pss_str(season_design_info.get('RewardString'))
        self.season_description: str = _parse.pss_str(season_design_info.get('SeasonDescription'))
        self.season_design_id: int = _parse.pss_int(season_design_info.get('SeasonDesignId'))
        self.season_name: str = _parse.pss_str(season_design_info.get('SeasonName'))
        self.season_sprite_id: int = _parse.pss_int(season_design_info.get('SeasonSpriteId'))
        self.season_type: str = _parse.pss_str(season_design_info.get('SeasonType'))
        self.sub_title: str = _parse.pss_str(season_design_info.get('SubTitle'))
        self.subtitle_sprite_id: int = _parse.pss_int(season_design_info.get('SubtitleSpriteId'))
        self.text_frame_sprite_id: int = _parse.pss_int(season_design_info.get('TextFrameSpriteId'))
        self.title_sprite_id: int = _parse.pss_int(season_design_info.get('TitleSpriteId'))
