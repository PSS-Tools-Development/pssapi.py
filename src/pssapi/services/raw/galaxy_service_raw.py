"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from typing import List, Tuple

from ... import core
from ...entities import Planet, Ship, StarSystem, StarSystemLink, StarSystemMarker, StarSystemMarkerGenerator, UserMarker


# ---------- Constants ----------

GO_TO_BASE_PATH: str = "GalaxyService/GoTo"
LIST_MARKER_GENERATOR_DESIGNS_BASE_PATH: str = "GalaxyService/ListMarkerGeneratorDesigns"
LIST_PLANETS_BASE_PATH: str = "GalaxyService/ListPlanets"
LIST_STAR_SYSTEM_LINKS_BASE_PATH: str = "GalaxyService/ListStarSystemLinks"
LIST_STAR_SYSTEM_MARKERS_BASE_PATH: str = "GalaxyService/ListStarSystemMarkers"
LIST_STAR_SYSTEM_MARKERS_AND_USER_MARKERS_BASE_PATH: str = "GalaxyService/ListStarSystemMarkersAndUserMarkers"
LIST_STAR_SYSTEMS_BASE_PATH: str = "GalaxyService/ListStarSystems"

# ---------- Endpoint structure ----------


# ---------- Endpoints ----------


async def go_to(production_server: str, access_token: str, checksum: str, client_date_time: str, star_system_id: int, **params) -> Ship:
    params = {"accessToken": access_token, "checksum": checksum, "clientDateTime": client_date_time, "starSystemId": star_system_id, **params}
    result = await core.get_entities_from_path(((Ship, "Ship", False),), "GoTo", production_server, GO_TO_BASE_PATH, "POST", response_gzipped=False, **params)
    return result


async def list_marker_generator_designs(production_server: str, client_date_time: str, design_version: int, language_key: str, **params) -> List[StarSystemMarkerGenerator]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, "languageKey": language_key, **params}
    result = await core.get_entities_from_path(
        ((StarSystemMarkerGenerator, "StarSystemMarkerGenerators", True),),
        "StarSystemMarkerGenerators",
        production_server,
        LIST_MARKER_GENERATOR_DESIGNS_BASE_PATH,
        "GET",
        response_gzipped=False,
        **params,
    )
    return result


async def list_planets(production_server: str, design_version: int, **params) -> List[Planet]:
    params = {"designVersion": design_version, **params}
    result = await core.get_entities_from_path(((Planet, "Planets", True),), "Planets", production_server, LIST_PLANETS_BASE_PATH, "GET", response_gzipped=False, **params)
    return result


async def list_star_system_links(production_server: str, client_date_time: str, design_version: int, **params) -> List[StarSystemLink]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, **params}
    result = await core.get_entities_from_path(
        ((StarSystemLink, "StarSystemLinks", True),), "StarSystemLinks", production_server, LIST_STAR_SYSTEM_LINKS_BASE_PATH, "GET", response_gzipped=False, **params
    )
    return result


async def list_star_system_markers(production_server: str, access_token: str, client_date_time: str, **params) -> List[StarSystemMarker]:
    params = {"accessToken": access_token, "clientDateTime": client_date_time, **params}
    result = await core.get_entities_from_path(
        ((StarSystemMarker, "StarSystemMarkers", True),), "StarSystemMarkers", production_server, LIST_STAR_SYSTEM_MARKERS_BASE_PATH, "GET", response_gzipped=False, **params
    )
    return result


async def list_star_system_markers_and_user_markers(production_server: str, access_token: str, **params) -> Tuple[List[StarSystemMarker], List[UserMarker]]:
    params = {"accessToken": access_token, **params}
    result = await core.get_entities_from_path(
        ((StarSystemMarker, "StarSystemMarkers", True), (UserMarker, "UserMarkers", True)),
        "ListStarSystemMarkersAndUserMarkers",
        production_server,
        LIST_STAR_SYSTEM_MARKERS_AND_USER_MARKERS_BASE_PATH,
        "GET",
        response_gzipped=False,
        **params,
    )
    return result


async def list_star_systems(production_server: str, client_date_time: str, design_version: int, language_key: str, **params) -> List[StarSystem]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, "languageKey": language_key, **params}
    result = await core.get_entities_from_path(((StarSystem, "StarSystems", True),), "StarSystems", production_server, LIST_STAR_SYSTEMS_BASE_PATH, "GET", response_gzipped=False, **params)
    return result
