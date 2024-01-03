"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class UserFleetCollectionRaw:
    XML_NODE_NAME: str = "UserFleetCollection"

    def __init__(self, user_fleet_collection_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._collection_date: _datetime = _parse.pss_datetime(user_fleet_collection_info.get("CollectionDate"))
        self._rewards_string: str = _parse.pss_str(user_fleet_collection_info.get("RewardsString"))
        self._room_id: int = _parse.pss_int(user_fleet_collection_info.get("RoomId"))
        self._start_date: _datetime = _parse.pss_datetime(user_fleet_collection_info.get("StartDate"))
        self._user_fleet_collection_id: int = _parse.pss_int(user_fleet_collection_info.get("UserFleetCollectionId"))
        self._user_id: int = _parse.pss_int(user_fleet_collection_info.get("UserId"))

    @property
    def collection_date(self) -> _datetime:
        return self._collection_date

    @property
    def rewards_string(self) -> str:
        return self._rewards_string

    @property
    def room_id(self) -> int:
        return self._room_id

    @property
    def start_date(self) -> _datetime:
        return self._start_date

    @property
    def user_fleet_collection_id(self) -> int:
        return self._user_fleet_collection_id

    @property
    def user_id(self) -> int:
        return self._user_id

    def _key(self):
        return (
            self.collection_date,
            self.rewards_string,
            self.room_id,
            self.start_date,
            self.user_fleet_collection_id,
            self.user_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "CollectionDate": self.collection_date,
                "RewardsString": self.rewards_string,
                "RoomId": self.room_id,
                "StartDate": self.start_date,
                "UserFleetCollectionId": self.user_fleet_collection_id,
                "UserId": self.user_id,
            }

        return self._dict
