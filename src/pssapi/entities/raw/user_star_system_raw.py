"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class UserStarSystemRaw:
    XML_NODE_NAME: str = "UserStarSystem"

    def __init__(self, user_star_system_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._exploration_percentage: int = _parse.pss_int(user_star_system_info.get("ExplorationPercentage"))
        self._star_system_id: int = _parse.pss_int(user_star_system_info.get("StarSystemId"))
        self._user_id: int = _parse.pss_int(user_star_system_info.get("UserId"))
        self._user_star_system_id: int = _parse.pss_int(user_star_system_info.get("UserStarSystemId"))

    @property
    def exploration_percentage(self) -> int:
        return self._exploration_percentage

    @property
    def star_system_id(self) -> int:
        return self._star_system_id

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def user_star_system_id(self) -> int:
        return self._user_star_system_id

    def _key(self):
        return (
            self.exploration_percentage,
            self.star_system_id,
            self.user_id,
            self.user_star_system_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "ExplorationPercentage": self.exploration_percentage,
                "StarSystemId": self.star_system_id,
                "UserId": self.user_id,
                "UserStarSystemId": self.user_star_system_id,
            }

        return self._dict
