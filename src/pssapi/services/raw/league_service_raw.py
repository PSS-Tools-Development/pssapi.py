"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from typing import List

from ... import core
from ...entities import League


# ---------- Constants ----------

LIST_LEAGUES_2_BASE_PATH: str = "LeagueService/ListLeagues2"

# ---------- Endpoint structure ----------


# ---------- Endpoints ----------


async def list_leagues_2(production_server: str, access_token: str, client_date_time: str, design_version: int, language_key: str, **params) -> List[League]:
    params = {"accessToken": access_token, "clientDateTime": client_date_time, "designVersion": design_version, "languageKey": language_key, **params}
    result = await core.get_entities_from_path(((League, "Leagues", True),), "Leagues", production_server, LIST_LEAGUES_2_BASE_PATH, "GET", response_gzipped=False, **params)
    return result
