"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class UserSeasonRaw:
    XML_NODE_NAME: str = 'UserSeason'

    def __init__(self, user_season_info: _EntityInfo) -> None:
        self.points: int = _parse.pss_int(user_season_info.get('Points'))
        self.purchase_vip_date: _datetime = _parse.pss_datetime(user_season_info.get('PurchaseVIPDate'))
        self.purchase_vip_status: str = _parse.pss_str(user_season_info.get('PurchaseVIPStatus'))
        self.season_design_id: int = _parse.pss_int(user_season_info.get('SeasonDesignId'))
        self.unlocked_reward_design_ids: str = _parse.pss_str(user_season_info.get('UnlockedRewardDesignIds'))
        self.user_id: int = _parse.pss_int(user_season_info.get('UserId'))
        self.user_season_id: int = _parse.pss_int(user_season_info.get('UserSeasonId'))
