"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class NewsDesignRaw:
    XML_NODE_NAME: str = "NewsDesign"

    def __init__(self, news_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._description: str = _parse.pss_str(news_design_info.get("Description"))
        self._expiry_date: _datetime = _parse.pss_datetime(news_design_info.get("ExpiryDate"))
        self._from_date: _datetime = _parse.pss_datetime(news_design_info.get("FromDate"))
        self._link: str = _parse.pss_str(news_design_info.get("Link"))
        self._news_design_id: int = _parse.pss_int(news_design_info.get("NewsDesignId"))
        self._sprite_id: int = _parse.pss_int(news_design_info.get("SpriteId"))
        self._title: str = _parse.pss_str(news_design_info.get("Title"))
        self._update_date: _datetime = _parse.pss_datetime(news_design_info.get("UpdateDate"))
        self._user_id: int = _parse.pss_int(news_design_info.get("UserId"))

    @property
    def description(self) -> str:
        return self._description

    @property
    def expiry_date(self) -> _datetime:
        return self._expiry_date

    @property
    def from_date(self) -> _datetime:
        return self._from_date

    @property
    def link(self) -> str:
        return self._link

    @property
    def news_design_id(self) -> int:
        return self._news_design_id

    @property
    def sprite_id(self) -> int:
        return self._sprite_id

    @property
    def title(self) -> str:
        return self._title

    @property
    def update_date(self) -> _datetime:
        return self._update_date

    @property
    def user_id(self) -> int:
        return self._user_id

    def _key(self):
        return (
            self.description,
            self.expiry_date,
            self.from_date,
            self.link,
            self.news_design_id,
            self.sprite_id,
            self.title,
            self.update_date,
            self.user_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "Description": self.description,
                "ExpiryDate": self.expiry_date,
                "FromDate": self.from_date,
                "Link": self.link,
                "NewsDesignId": self.news_design_id,
                "SpriteId": self.sprite_id,
                "Title": self.title,
                "UpdateDate": self.update_date,
                "UserId": self.user_id,
            }

        return self._dict
