"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import Alliance as _Alliance
from ...entities import Message as _Message

# ---------- Constants ----------

LIST_ALLIANCES_BY_CHAMPIONSHIP_SCORE_RANKING_BASE_PATH: str = 'AllianceService/ListAlliancesByChampionshipScoreRanking'
LIST_ALLIANCES_BY_RANKING_BASE_PATH: str = 'AllianceService/ListAlliancesByRanking'
LIST_USERS_2_BASE_PATH: str = 'AllianceService/ListUsers2'
SEARCH_ALLIANCES_BASE_PATH: str = 'AllianceService/SearchAlliances'


# ---------- Endpoints ----------

async def list_alliances_by_championship_score_ranking(production_server: str, from_: int, to: int, access_token: str, **params) -> _List[_Alliance]:
    params = {
        'from': from_,
        'to': to,
        'accessToken': access_token,
        **params
    }
    result = await _core.get_entities_from_path(_Alliance, 'Alliances', production_server, LIST_ALLIANCES_BY_CHAMPIONSHIP_SCORE_RANKING_BASE_PATH, **params)
    return result


async def list_alliances_by_ranking(production_server: str, take: int, skip: int, **params) -> _List[_Alliance]:
    params = {
        'take': take,
        'skip': skip,
        **params
    }
    result = await _core.get_entities_from_path(_Alliance, 'Alliances', production_server, LIST_ALLIANCES_BY_RANKING_BASE_PATH, **params)
    return result


async def list_users_2(production_server: str, take: int, skip: int, access_token: str, alliance_id: int, **params) -> _List[_Message]:
    params = {
        'take': take,
        'skip': skip,
        'accessToken': access_token,
        'allianceId': alliance_id,
        **params
    }
    result = await _core.get_entities_from_path(_Message, 'Messages', production_server, LIST_USERS_2_BASE_PATH, **params)
    return result


async def search_alliances(production_server: str, take: int, skip: int, access_token: str, name: str, **params) -> _List[_Alliance]:
    params = {
        'take': take,
        'skip': skip,
        'accessToken': access_token,
        'name': name,
        **params
    }
    result = await _core.get_entities_from_path(_Alliance, 'Alliances', production_server, SEARCH_ALLIANCES_BASE_PATH, **params)
    return result
