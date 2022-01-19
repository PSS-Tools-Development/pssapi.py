"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class UserSeasonRaw:
    XML_NODE_NAME: str = "UserSeason"

    def __init__(self, user_season_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._points: int = _parse.pss_int(user_season_info.get("Points"))
        self._purchase_vip_date: _datetime = _parse.pss_datetime(user_season_info.get("PurchaseVIPDate"))
        self._purchase_vip_status: str = _parse.pss_str(user_season_info.get("PurchaseVIPStatus"))
        self._season_design_id: int = _parse.pss_int(user_season_info.get("SeasonDesignId"))
        self._unlocked_reward_design_ids: str = _parse.pss_str(user_season_info.get("UnlockedRewardDesignIds"))
        self._user_id: int = _parse.pss_int(user_season_info.get("UserId"))
        self._user_season_id: int = _parse.pss_int(user_season_info.get("UserSeasonId"))

    @property
    def points(self) -> int:
        return self._points

    @property
    def purchase_vip_date(self) -> _datetime:
        return self._purchase_vip_date

    @property
    def purchase_vip_status(self) -> str:
        return self._purchase_vip_status

    @property
    def season_design_id(self) -> int:
        return self._season_design_id

    @property
    def unlocked_reward_design_ids(self) -> str:
        return self._unlocked_reward_design_ids

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def user_season_id(self) -> int:
        return self._user_season_id

    def _key(self):
        return (
            self.points,
            self.purchase_vip_date,
            self.purchase_vip_status,
            self.season_design_id,
            self.unlocked_reward_design_ids,
            self.user_id,
            self.user_season_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "Points": self.points,
                "PurchaseVIPDate": self.purchase_vip_date,
                "PurchaseVIPStatus": self.purchase_vip_status,
                "SeasonDesignId": self.season_design_id,
                "UnlockedRewardDesignIds": self.unlocked_reward_design_ids,
                "UserId": self.user_id,
                "UserSeasonId": self.user_season_id,
            }

        return self._dict
