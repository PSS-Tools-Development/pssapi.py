"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class UserSeasonRaw(EntityBaseRaw, tag="UserSeason"):
    XML_NODE_NAME: str = "UserSeason"

    points: Optional[int] = attr(name="Points", default=None)
    purchase_vip_date: Optional[datetime] = attr(name="PurchaseVIPDate", default=None)
    purchase_vip_status: Optional[str] = attr(name="PurchaseVIPStatus", default=None)
    season_design_id: Optional[int] = attr(name="SeasonDesignId", default=None)
    unlocked_reward_design_ids: Optional[str] = attr(name="UnlockedRewardDesignIds", default=None)
    user_id: Optional[int] = attr(name="UserId", default=None)
    user_season_id: Optional[int] = attr(name="UserSeasonId", default=None)

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


__all__ = [
    "UserSeasonRaw",
]
