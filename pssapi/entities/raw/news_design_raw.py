"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import List as _List

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class NewsDesignRaw:
    XML_NODE_NAME: str = 'NewsDesign'

    def __init__(self, news_design_info: _EntityInfo) -> None:
        self.description: str = _parse.pss_str(news_design_info.get('Description'))
        self.expiry_date: _datetime = _parse.pss_datetime(news_design_info.get('ExpiryDate'))
        self.from_date: _datetime = _parse.pss_datetime(news_design_info.get('FromDate'))
        self.link: str = _parse.pss_str(news_design_info.get('Link'))
        self.news_design_id: int = _parse.pss_int(news_design_info.get('NewsDesignId'))
        self.sprite_id: int = _parse.pss_int(news_design_info.get('SpriteId'))
        self.title: str = _parse.pss_str(news_design_info.get('Title'))
        self.update_date: _datetime = _parse.pss_datetime(news_design_info.get('UpdateDate'))
        self.user_id: int = _parse.pss_int(news_design_info.get('UserId'))
