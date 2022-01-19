"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import User as _User

# ---------- Constants ----------

LIST_USERS_BY_CHAMPIONSHIP_SCORE_RANKING_BASE_PATH: str = "LadderService/ListUsersByChampionshipScoreRanking"
LIST_USERS_BY_RANKING_BASE_PATH: str = "LadderService/ListUsersByRanking"


# ---------- Endpoints ----------


async def list_users_by_championship_score_ranking(production_server: str, access_token: str, from_: int, to: int, **params) -> _List[_User]:
    params = {"accessToken": access_token, "from": from_, "to": to, **params}
    result = await _core.get_entities_from_path(((_User, "Users", True),), "Users", production_server, LIST_USERS_BY_CHAMPIONSHIP_SCORE_RANKING_BASE_PATH, "GET", **params)
    return result


async def list_users_by_ranking(production_server: str, access_token: str, from_: int, to: int, to_100: str, **params) -> _List[_User]:
    params = {"accessToken": access_token, "from": from_, "to": to, "to100": to_100, **params}
    result = await _core.get_entities_from_path(((_User, "Users", True),), "Users", production_server, LIST_USERS_BY_RANKING_BASE_PATH, "GET", **params)
    return result
