"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

import pssapi.entities as _entities

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class UserLoginRaw:
    XML_NODE_NAME: str = "UserLogin"

    def __init__(self, user_login_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._previous_last_login_date: _datetime = _parse.pss_datetime(user_login_info.get("PreviousLastLoginDate"))
        self._user: _entities.User = _entities.User(user_login_info.get("User")) if user_login_info.get("User") else None
        self._user_id: int = _parse.pss_int(user_login_info.get("UserId"))
        self._access_token: str = _parse.pss_str(user_login_info.get("accessToken"))

    @property
    def previous_last_login_date(self) -> _datetime:
        return self._previous_last_login_date

    @property
    def user(self) -> "_entities.User":
        return self._user

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def access_token(self) -> str:
        return self._access_token

    def _key(self):
        return (
            self.previous_last_login_date,
            self.user._key() if self.user else None,
            self.user_id,
            self.access_token,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "PreviousLastLoginDate": self.previous_last_login_date,
                "User": dict(self.user) if self.user else None,
                "UserId": self.user_id,
                "accessToken": self.access_token,
            }

        return self._dict
