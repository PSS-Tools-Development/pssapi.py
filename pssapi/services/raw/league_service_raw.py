"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import League as _League

# ---------- Constants ----------

LIST_LEAGUES_2_BASE_PATH: str = 'LeagueService/ListLeagues2'


# ---------- Endpoints ----------

async def list_leagues_2(production_server: str, design_version: int, language_key: str, access_token: str, **params) -> _List[_League]:
    params = {
        'designVersion': design_version,
        'languageKey': language_key,
        'accessToken': access_token,
        **params
    }
    result = await _core.get_entities_from_path(_League, 'Leagues', production_server, LIST_LEAGUES_2_BASE_PATH, **params)
    return result
