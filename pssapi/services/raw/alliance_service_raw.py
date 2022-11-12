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

async def list_alliances_by_championship_score_ranking(production_server: str, access_token: str, from_: int, to: int, **params) -> _List[_Alliance]:
    params = {
        'accessToken': access_token,
        'from': from_,
        'to': to,
        **params
    }
    content = None
    result = await _core.get_entities_from_path(_Alliance, 'Alliances', production_server, LIST_ALLIANCES_BY_CHAMPIONSHIP_SCORE_RANKING_BASE_PATH, 'GET', request_content=content, **params)
    return result


async def list_alliances_by_ranking(production_server: str, skip: int, take: int, **params) -> _List[_Alliance]:
    params = {
        'skip': skip,
        'take': take,
        **params
    }
    content = None
    result = await _core.get_entities_from_path(_Alliance, 'Alliances', production_server, LIST_ALLIANCES_BY_RANKING_BASE_PATH, 'GET', request_content=content, **params)
    return result


async def list_users_2(production_server: str, access_token: str, alliance_id: int, skip: int, take: int, **params) -> _List[_Message]:
    params = {
        'accessToken': access_token,
        'allianceId': alliance_id,
        'skip': skip,
        'take': take,
        **params
    }
    content = None
    result = await _core.get_entities_from_path(_Message, 'Messages', production_server, LIST_USERS_2_BASE_PATH, 'GET', request_content=content, **params)
    return result


async def search_alliances(production_server: str, access_token: str, name: str, skip: int, take: int, **params) -> _List[_Alliance]:
    params = {
        'accessToken': access_token,
        'name': name,
        'skip': skip,
        'take': take,
        **params
    }
    content = None
    result = await _core.get_entities_from_path(_Alliance, 'Alliances', production_server, SEARCH_ALLIANCES_BASE_PATH, 'GET', request_content=content, **params)
    return result
