####################################################
##   This file has been generated automatically   ##
####################################################

from datetime import datetime as _datetime
from typing import List as _List

from ... import core as _core
from ...entities import UserStarSystem as _UserStarSystem
from ...entities import StarSystemLink as _StarSystemLink
from ...entities import StarSystemMarker as _StarSystemMarker
from ...entities import StarSystem as _StarSystem



# ---------- Constants ----------

LIST_STAR_SYSTEM_LINKS_BASE_PATH: str = 'GalaxyService/ListStarSystemLinks'
LIST_STAR_SYSTEMS_BASE_PATH: str = 'GalaxyService/ListStarSystems'
LIST_USER_MARKERS_BASE_PATH: str = 'GalaxyService/ListUserMarkers'
LIST_USER_STAR_SYSTEMS_BASE_PATH: str = 'GalaxyService/ListUserStarSystems'


# ---------- Endpoints ----------

async def list_star_system_links(production_server: str, design_version: int, **params) -> _List[_StarSystemLink]:
    params = {
        'designVersion': design_version,
    }
    result = await _core.get_entities_from_path(_StarSystemLink, 'StarSystemLinks', production_server, LIST_STAR_SYSTEM_LINKS_BASE_PATH, **params)
    return result


async def list_star_systems(production_server: str, language_key: str, design_version: int, **params) -> _List[_StarSystem]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
    }
    result = await _core.get_entities_from_path(_StarSystem, 'StarSystems', production_server, LIST_STAR_SYSTEMS_BASE_PATH, **params)
    return result


async def list_user_markers(production_server: str, access_token: str, client_date_time: _datetime, **params) -> _List[_StarSystemMarker]:
    params = {
        'accessToken': access_token,
        'clientDateTime': client_date_time,
    }
    result = await _core.get_entities_from_path(_StarSystemMarker, 'StarSystemMarkers', production_server, LIST_USER_MARKERS_BASE_PATH, **params)
    return result


async def list_user_star_systems(production_server: str, access_token: str, client_date_time: _datetime, **params) -> _List[_UserStarSystem]:
    params = {
        'accessToken': access_token,
        'clientDateTime': client_date_time,
    }
    result = await _core.get_entities_from_path(_UserStarSystem, 'UserStarSystems', production_server, LIST_USER_STAR_SYSTEMS_BASE_PATH, **params)
    return result


