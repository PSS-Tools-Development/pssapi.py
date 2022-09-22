"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import User as _User


class LadderServiceRaw:

    SERVICE_NAME = 'LadderService'
    LIST_USERS_BY_CHAMPIONSHIP_SCORE_RANKING_BASE_PATH: str = 'LadderService/ListUsersByChampionshipScoreRanking'
    LIST_USERS_BY_RANKING_BASE_PATH: str = 'LadderService/ListUsersByRanking'

    @staticmethod
    async def _list_users_by_championship_score_ranking(production_server: str, from_: int, to: int, access_token: str, **params) -> _List[_User]:
        params = {
            'from': from_,
            'to': to,
            'accessToken': access_token,
            **params
        }

        result = await _core.get_entities_from_path(_User, 'Users', production_server, LadderServiceRaw.LIST_USERS_BY_CHAMPIONSHIP_SCORE_RANKING_BASE_PATH, **params)
        return result

    @staticmethod
    async def _list_users_by_ranking(production_server: str, from_: int, to: int, access_token: str, **params) -> _List[_User]:
        params = {
            'from': from_,
            'to': to,
            'accessToken': access_token,
            **params
        }

        result = await _core.get_entities_from_path(_User, 'Users', production_server, LadderServiceRaw.LIST_USERS_BY_RANKING_BASE_PATH, **params)
        return result
