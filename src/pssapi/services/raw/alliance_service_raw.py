"""
    This file has been generated automatically
"""

from typing import List as _List
from typing import Tuple as _Tuple

from ... import core as _core
from ...entities import Alliance as _Alliance
from ...entities import Message as _Message
from ...entities import User as _User

# ---------- Constants ----------

GET_ALLIANCE_BASE_PATH: str = "AllianceService/GetAlliance"
INTERACT_WITH_STARBASE_ROOM_BASE_PATH: str = "AllianceService/InteractWithStarbaseRoom"
LIST_ALLIANCES_BY_CHAMPIONSHIP_SCORE_RANKING_BASE_PATH: str = "AllianceService/ListAlliancesByChampionshipScoreRanking"
LIST_ALLIANCES_BY_RANKING_BASE_PATH: str = "AllianceService/ListAlliancesByRanking"
LIST_USERS_2_BASE_PATH: str = "AllianceService/ListUsers2"
SEARCH_ALLIANCES_BASE_PATH: str = "AllianceService/SearchAlliances"


# ---------- Endpoints ----------


async def get_alliance(production_server: str, access_token: str, alliance_id: int, **params) -> _Alliance:
    params = {"accessToken": access_token, "allianceId": alliance_id, **params}
    result = await _core.get_entities_from_path(((_Alliance, "Alliance", False),), "GetAlliance", production_server, GET_ALLIANCE_BASE_PATH, "GET", **params)
    return result


async def interact_with_starbase_room(production_server: str, access_token: str, checksum: str, client_date_time: str, room_id: int, **params) -> _User:
    params = {"accessToken": access_token, "checksum": checksum, "clientDateTime": client_date_time, "roomId": room_id, **params}
    result = await _core.get_entities_from_path(((_User, "User", False),), "InteractWithStarbaseRoom", production_server, INTERACT_WITH_STARBASE_ROOM_BASE_PATH, "POST", **params)
    return result


async def list_alliances_by_championship_score_ranking(production_server: str, access_token: str, from_: int, to: int, **params) -> _List[_Alliance]:
    params = {"accessToken": access_token, "from": from_, "to": to, **params}
    result = await _core.get_entities_from_path(((_Alliance, "Alliances", True),), "Alliances", production_server, LIST_ALLIANCES_BY_CHAMPIONSHIP_SCORE_RANKING_BASE_PATH, "GET", **params)
    return result


async def list_alliances_by_ranking(production_server: str, skip: int, take: int, **params) -> _List[_Alliance]:
    params = {"skip": skip, "take": take, **params}
    result = await _core.get_entities_from_path(((_Alliance, "Alliances", True),), "Alliances", production_server, LIST_ALLIANCES_BY_RANKING_BASE_PATH, "GET", **params)
    return result


async def list_users_2(production_server: str, access_token: str, alliance_id: int, skip: int, take: int, **params) -> _Tuple[_List[_Message], _List[_User]]:
    params = {"accessToken": access_token, "allianceId": alliance_id, "skip": skip, "take": take, **params}
    result = await _core.get_entities_from_path(((_Message, "Messages", True), (_User, "Users", True)), "ListUsers", production_server, LIST_USERS_2_BASE_PATH, "GET", **params)
    return result


async def search_alliances(production_server: str, access_token: str, name: str, skip: int, take: int, **params) -> _List[_Alliance]:
    params = {"accessToken": access_token, "name": name, "skip": skip, "take": take, **params}
    result = await _core.get_entities_from_path(((_Alliance, "Alliances", True),), "Alliances", production_server, SEARCH_ALLIANCES_BASE_PATH, "GET", **params)
    return result
