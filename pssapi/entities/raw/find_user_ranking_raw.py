####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class FindUserRankingRaw():
    XML_NODE_NAME: str = 'FindUserRanking'

    def __init__(self, find_user_ranking_info: _EntityInfo) -> None:
        self.__user_id: int = _parse.pss_int(find_user_ranking_info.get('UserId'))
        self.__ranking: int = _parse.pss_int(find_user_ranking_info.get('Ranking'))
        self.__total_users: int = _parse.pss_int(find_user_ranking_info.get('TotalUsers'))
        self.__total_active_users: int = _parse.pss_int(find_user_ranking_info.get('TotalActiveUsers'))

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def ranking(self) -> int:
        return self.__ranking

    @property
    def total_users(self) -> int:
        return self.__total_users

    @property
    def total_active_users(self) -> int:
        return self.__total_active_users
