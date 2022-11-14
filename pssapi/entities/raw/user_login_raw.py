"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import List as _List

from ...entities import User as _User
from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class UserLoginRaw:
    XML_NODE_NAME: str = 'UserLogin'

    def __init__(self, user_login_info: _EntityInfo) -> None:
        self.previous_last_login_date: _datetime = _parse.pss__datetime(user_login_info.get('PreviousLastLoginDate'))
        self.user: _User = _User(user_login_info.get('User'))
        self.user_id: int = _parse.pss_int(user_login_info.get('UserId'))
        self.access_token: str = _parse.pss_str(user_login_info.get('accessToken'))
