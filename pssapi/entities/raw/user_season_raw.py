####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class UserSeasonRaw():
    XML_NODE_NAME: str = 'UserSeason'

    def __init__(self, user_season_info: _EntityInfo) -> None:
        self.__unlocked_reward_design_ids: str = _parse.pss_str(user_season_info.get('UnlockedRewardDesignIds'))
        self.__user_season_id: int = _parse.pss_int(user_season_info.get('UserSeasonId'))
        self.__points: int = _parse.pss_int(user_season_info.get('Points'))
        self.__purchase_vip_date: datetime = _parse.pss_datetime(user_season_info.get('PurchaseVIPDate'))
        self.__season_design_id: int = _parse.pss_int(user_season_info.get('SeasonDesignId'))
        self.__purchase_vip_status: str = _parse.pss_str(user_season_info.get('PurchaseVIPStatus'))
        self.__user_id: int = _parse.pss_int(user_season_info.get('UserId'))

    @property
    def unlocked_reward_design_ids(self) -> str:
        return self.__unlocked_reward_design_ids

    @property
    def user_season_id(self) -> int:
        return self.__user_season_id

    @property
    def points(self) -> int:
        return self.__points

    @property
    def purchase_vip_date(self) -> datetime:
        return self.__purchase_vip_date

    @property
    def season_design_id(self) -> int:
        return self.__season_design_id

    @property
    def purchase_vip_status(self) -> str:
        return self.__purchase_vip_status

    @property
    def user_id(self) -> int:
        return self.__user_id