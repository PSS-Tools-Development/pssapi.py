"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict
from typing import List as _List

import pssapi.entities as _entities

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ListFriendsRaw:
    XML_NODE_NAME: str = "ListFriends"

    def __init__(self, list_friends_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._friends: _List[_entities.Friend] = [_entities.Friend(child_info) for child_info in list_friends_info.get("Friends")] if list_friends_info.get("Friends") else []
        self._user_id: int = _parse.pss_int(list_friends_info.get("UserId"))

    @property
    def friends(self) -> _List["_entities.Friend"]:
        return self._friends

    @property
    def user_id(self) -> int:
        return self._user_id

    def _key(self):
        return (
            tuple(child._key() for child in self.friends),
            self.user_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "Friends": [dict(child) for child in self.friends],
                "UserId": self.user_id,
            }

        return self._dict
