"""
    This file has been generated automatically
"""

from datetime import datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class NewsDesignRaw:
    XML_NODE_NAME: str = 'NewsDesign'

    def __init__(self, news_design_info: _EntityInfo) -> None:
        self.__news_design_id: int = _parse.pss_int(
            news_design_info.get('NewsDesignId'))
        self.__title: str = _parse.pss_str(news_design_info.get('Title'))
        self.__description: str = _parse.pss_str(
            news_design_info.get('Description'))
        self.__user_id: int = _parse.pss_int(news_design_info.get('UserId'))
        self.__update_date: datetime = _parse.pss_datetime(
            news_design_info.get('UpdateDate'))
        self.__link: str = _parse.pss_str(news_design_info.get('Link'))
        self.__sprite_id: int = _parse.pss_int(
            news_design_info.get('SpriteId'))
        self.__expiry_date: datetime = _parse.pss_datetime(
            news_design_info.get('ExpiryDate'))
        self.__from_date: datetime = _parse.pss_datetime(
            news_design_info.get('FromDate'))

    @property
    def news_design_id(self) -> int:
        return self.__news_design_id

    @property
    def title(self) -> str:
        return self.__title

    @property
    def description(self) -> str:
        return self.__description

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def update_date(self) -> datetime:
        return self.__update_date

    @property
    def link(self) -> str:
        return self.__link

    @property
    def sprite_id(self) -> int:
        return self.__sprite_id

    @property
    def expiry_date(self) -> datetime:
        return self.__expiry_date

    @property
    def from_date(self) -> datetime:
        return self.__from_date
