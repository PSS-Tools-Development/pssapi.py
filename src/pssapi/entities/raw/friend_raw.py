"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class FriendRaw:
    XML_NODE_NAME: str = "Friend"

    def __init__(self, friend_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._date_updated: _datetime = _parse.pss_datetime(friend_info.get("DateUpdated"))
        self._friend_icon_sprite_id: int = _parse.pss_int(friend_info.get("FriendIconSpriteId"))
        self._friend_trophy: int = _parse.pss_int(friend_info.get("FriendTrophy"))
        self._friend_type: str = _parse.pss_str(friend_info.get("FriendType"))
        self._friend_user_id: int = _parse.pss_int(friend_info.get("FriendUserId"))
        self._id_: int = _parse.pss_int(friend_info.get("Id"))
        self._last_interaction_date: _datetime = _parse.pss_datetime(friend_info.get("LastInteractionDate"))
        self._last_login_date: _datetime = _parse.pss_datetime(friend_info.get("LastLoginDate"))
        self._level: int = _parse.pss_int(friend_info.get("Level"))
        self._name: str = _parse.pss_str(friend_info.get("Name"))
        self._unread_messages: int = _parse.pss_int(friend_info.get("UnreadMessages"))

    @property
    def date_updated(self) -> _datetime:
        return self._date_updated

    @property
    def friend_icon_sprite_id(self) -> int:
        return self._friend_icon_sprite_id

    @property
    def friend_trophy(self) -> int:
        return self._friend_trophy

    @property
    def friend_type(self) -> str:
        return self._friend_type

    @property
    def friend_user_id(self) -> int:
        return self._friend_user_id

    @property
    def id_(self) -> int:
        return self._id_

    @property
    def last_interaction_date(self) -> _datetime:
        return self._last_interaction_date

    @property
    def last_login_date(self) -> _datetime:
        return self._last_login_date

    @property
    def level(self) -> int:
        return self._level

    @property
    def name(self) -> str:
        return self._name

    @property
    def unread_messages(self) -> int:
        return self._unread_messages

    def _key(self):
        return (
            self.date_updated,
            self.friend_icon_sprite_id,
            self.friend_trophy,
            self.friend_type,
            self.friend_user_id,
            self.id_,
            self.last_interaction_date,
            self.last_login_date,
            self.level,
            self.name,
            self.unread_messages,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "DateUpdated": self.date_updated,
                "FriendIconSpriteId": self.friend_icon_sprite_id,
                "FriendTrophy": self.friend_trophy,
                "FriendType": self.friend_type,
                "FriendUserId": self.friend_user_id,
                "Id": self.id_,
                "LastInteractionDate": self.last_interaction_date,
                "LastLoginDate": self.last_login_date,
                "Level": self.level,
                "Name": self.name,
                "UnreadMessages": self.unread_messages,
            }

        return self._dict
