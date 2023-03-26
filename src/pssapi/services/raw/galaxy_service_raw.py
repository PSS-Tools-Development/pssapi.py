"""
    This file has been generated automatically
"""

from typing import List as _List
from typing import Tuple as _Tuple

from ... import core as _core
from ...entities import Planet as _Planet
from ...entities import Ship as _Ship
from ...entities import StarSystem as _StarSystem
from ...entities import StarSystemLink as _StarSystemLink
from ...entities import StarSystemMarker as _StarSystemMarker
from ...entities import StarSystemMarkerGenerator as _StarSystemMarkerGenerator
from ...entities import UserMarker as _UserMarker

# ---------- Constants ----------

GO_TO_BASE_PATH: str = "GalaxyService/GoTo"
LIST_MARKER_GENERATOR_DESIGNS_BASE_PATH: str = "GalaxyService/ListMarkerGeneratorDesigns"
LIST_PLANETS_BASE_PATH: str = "GalaxyService/ListPlanets"
LIST_STAR_SYSTEM_LINKS_BASE_PATH: str = "GalaxyService/ListStarSystemLinks"
LIST_STAR_SYSTEM_MARKERS_BASE_PATH: str = "GalaxyService/ListStarSystemMarkers"
LIST_STAR_SYSTEM_MARKERS_AND_USER_MARKERS_BASE_PATH: str = "GalaxyService/ListStarSystemMarkersAndUserMarkers"
LIST_STAR_SYSTEMS_BASE_PATH: str = "GalaxyService/ListStarSystems"


# ---------- Endpoints ----------


async def go_to(production_server: str, access_token: str, checksum: str, client_date_time: str, star_system_id: int, **params) -> _Ship:
    params = {"accessToken": access_token, "checksum": checksum, "clientDateTime": client_date_time, "starSystemId": star_system_id, **params}
    result = await _core.get_entities_from_path(((_Ship, "Ship", False),), "GoTo", production_server, GO_TO_BASE_PATH, "POST", **params)
    return result


async def list_marker_generator_designs(production_server: str, design_version: int, language_key: str, **params) -> _List[_StarSystemMarkerGenerator]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(
        ((_StarSystemMarkerGenerator, "StarSystemMarkerGenerators", True),), "StarSystemMarkerGenerators", production_server, LIST_MARKER_GENERATOR_DESIGNS_BASE_PATH, "GET", **params
    )
    return result


async def list_planets(production_server: str, design_version: int, **params) -> _List[_Planet]:
    params = {"designVersion": design_version, **params}
    result = await _core.get_entities_from_path(((_Planet, "Planets", True),), "Planets", production_server, LIST_PLANETS_BASE_PATH, "GET", **params)
    return result


async def list_star_system_links(production_server: str, design_version: int, **params) -> _List[_StarSystemLink]:
    params = {"designVersion": design_version, **params}
    result = await _core.get_entities_from_path(((_StarSystemLink, "StarSystemLinks", True),), "StarSystemLinks", production_server, LIST_STAR_SYSTEM_LINKS_BASE_PATH, "GET", **params)
    return result


async def list_star_system_markers(production_server: str, access_token: str, client_date_time: str, **params) -> _List[_StarSystemMarker]:
    params = {"accessToken": access_token, "clientDateTime": client_date_time, **params}
    result = await _core.get_entities_from_path(((_StarSystemMarker, "StarSystemMarkers", True),), "StarSystemMarkers", production_server, LIST_STAR_SYSTEM_MARKERS_BASE_PATH, "GET", **params)
    return result


async def list_star_system_markers_and_user_markers(production_server: str, access_token: str, **params) -> _Tuple[_List[_StarSystemMarker], _List[_UserMarker]]:
    params = {"accessToken": access_token, **params}
    result = await _core.get_entities_from_path(
        ((_StarSystemMarker, "StarSystemMarkers", True), (_UserMarker, "UserMarkers", True)),
        "ListStarSystemMarkersAndUserMarkers",
        production_server,
        LIST_STAR_SYSTEM_MARKERS_AND_USER_MARKERS_BASE_PATH,
        "GET",
        **params,
    )
    return result


async def list_star_systems(production_server: str, design_version: int, language_key: str, **params) -> _List[_StarSystem]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_StarSystem, "StarSystems", True),), "StarSystems", production_server, LIST_STAR_SYSTEMS_BASE_PATH, "GET", **params)
    return result
