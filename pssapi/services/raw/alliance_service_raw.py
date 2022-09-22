"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import Alliance as _Alliance
from ...entities import User as _User


class AllianceServiceRaw:

    SERVICE_NAME = 'AllianceService'
    LIST_ALLIANCES_BY_CHAMPIONSHIP_SCORE_RANKING_BASE_PATH: str = 'AllianceService/ListAlliancesByChampionshipScoreRanking'
    LIST_ALLIANCES_BY_RANKING_BASE_PATH: str = 'AllianceService/ListAlliancesByRanking'
    LIST_USERS_2_BASE_PATH: str = 'AllianceService/ListUsers2'
    SEARCH_ALLIANCES_BASE_PATH: str = 'AllianceService/SearchAlliances'

    @staticmethod
    async def _list_alliances_by_championship_score_ranking(production_server: str, from_: int, to: int, access_token: str, **params) -> _List[_Alliance]:
        params = {
            'from': from_,
            'to': to,
            'accessToken': access_token,
            **params
        }

        result = await _core.get_entities_from_path(_Alliance, 'Alliances', production_server, AllianceServiceRaw.LIST_ALLIANCES_BY_CHAMPIONSHIP_SCORE_RANKING_BASE_PATH, **params)
        return result

    @staticmethod
    async def _list_alliances_by_ranking(production_server: str, skip: int, take: int, **params) -> _List[_Alliance]:
        params = {
            'skip': skip,
            'take': take,
            **params
        }

        result = await _core.get_entities_from_path(_Alliance, 'Alliances', production_server, AllianceServiceRaw.LIST_ALLIANCES_BY_RANKING_BASE_PATH, **params)
        return result

    @staticmethod
    async def _list_users_2(production_server: str, alliance_id: int, skip: int, take: int, access_token: str, **params) -> _List[_User]:
        params = {
            'allianceId': alliance_id,
            'skip': skip,
            'take': take,
            'accessToken': access_token,
            **params
        }

        result = await _core.get_entities_from_path(_User, 'Users', production_server, AllianceServiceRaw.LIST_USERS_2_BASE_PATH, **params)
        return result

    @staticmethod
    async def _search_alliances(production_server: str, name: str, skip: int, take: int, access_token: str, **params) -> _List[_Alliance]:
        params = {
            'name': name,
            'skip': skip,
            'take': take,
            'accessToken': access_token,
            **params
        }

        result = await _core.get_entities_from_path(_Alliance, 'Alliances', production_server, AllianceServiceRaw.SEARCH_ALLIANCES_BASE_PATH, **params)
        return result
