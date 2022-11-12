"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import Ship as _Ship
from ...entities import StarSystem as _StarSystem
from ...entities import StarSystemLink as _StarSystemLink
from ...entities import StarSystemMarker as _StarSystemMarker
from ...entities import StarSystemMarkerGenerator as _StarSystemMarkerGenerator

# ---------- Constants ----------

LIST_MARKER_GENERATOR_DESIGNS_BASE_PATH: str = 'GalaxyService/ListMarkerGeneratorDesigns'
LIST_STAR_SYSTEM_LINKS_BASE_PATH: str = 'GalaxyService/ListStarSystemLinks'
LIST_STAR_SYSTEM_MARKERS_BASE_PATH: str = 'GalaxyService/ListStarSystemMarkers'
LIST_STAR_SYSTEMS_BASE_PATH: str = 'GalaxyService/ListStarSystems'


# ---------- Endpoints ----------

async def list_marker_generator_designs(production_server: str, design_version: int, language_key: str, **params) -> _List[_StarSystemMarkerGenerator]:
    params = {
        'designVersion': design_version,
        'languageKey': language_key,
        **params
    }
    content = None
    result = await _core.get_entities_from_path(_StarSystemMarkerGenerator, 'StarSystemMarkerGenerators', production_server, LIST_MARKER_GENERATOR_DESIGNS_BASE_PATH, 'GET', request_content=content, **params)
    return result


async def list_star_system_links(production_server: str, design_version: int, **params) -> _List[_StarSystemLink]:
    params = {
        'designVersion': design_version,
        **params
    }
    content = None
    result = await _core.get_entities_from_path(_StarSystemLink, 'StarSystemLinks', production_server, LIST_STAR_SYSTEM_LINKS_BASE_PATH, 'GET', request_content=content, **params)
    return result


async def list_star_system_markers(production_server: str, access_token: str, client_date_time: str, **params) -> _List[_StarSystemMarker]:
    params = {
        'accessToken': access_token,
        'clientDateTime': client_date_time,
        **params
    }
    content = None
    result = await _core.get_entities_from_path(_StarSystemMarker, 'StarSystemMarkers', production_server, LIST_STAR_SYSTEM_MARKERS_BASE_PATH, 'GET', request_content=content, **params)
    return result


async def list_star_systems(production_server: str, design_version: int, language_key: str, **params) -> _List[_StarSystem]:
    params = {
        'designVersion': design_version,
        'languageKey': language_key,
        **params
    }
    content = None
    result = await _core.get_entities_from_path(_StarSystem, 'StarSystems', production_server, LIST_STAR_SYSTEMS_BASE_PATH, 'GET', request_content=content, **params)
    return result
