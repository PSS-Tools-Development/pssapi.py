from typing import List as _List
from typing import Tuple as _Tuple

import pssapi.services.service_base as _service_base

from ..entities import Planet as _Planet
from ..entities import Ship as _Ship
from ..entities import StarSystem as _StarSystem
from ..entities import StarSystemLink as _StarSystemLink
from ..entities import StarSystemMarker as _StarSystemMarker
from ..entities import StarSystemMarkerGenerator as _StarSystemMarkerGenerator
from ..entities import UserMarker as _UserMarker
from .raw import GalaxyServiceRaw as _GalaxyServiceRaw


class GalaxyService(_service_base.CacheableServiceBase):
    async def go_to(self, access_token: str, checksum: str, client_date_time: str, star_system_id: int) -> _Ship:
        production_server = await self.get_production_server()
        result = await _GalaxyServiceRaw.go_to(production_server, access_token, checksum, client_date_time, star_system_id)
        return result

    @_service_base.cache_endpoint("MarkerGeneratorDesignVersion")
    async def list_marker_generator_designs(self, design_version: int = None) -> _List[_StarSystemMarkerGenerator]:
        production_server = await self.get_production_server()
        result = await _GalaxyServiceRaw.list_marker_generator_designs(production_server, design_version, self.language_key)
        return result

    @_service_base.cache_endpoint("PlanetVersion")
    async def list_planets(self, design_version: int = None) -> _List[_Planet]:
        production_server = await self.get_production_server()
        result = await _GalaxyServiceRaw.list_planets(production_server, design_version)
        return result

    @_service_base.cache_endpoint("StarSystemLinkVersion")
    async def list_star_system_links(self, design_version: int = None) -> _List[_StarSystemLink]:
        production_server = await self.get_production_server()
        result = await _GalaxyServiceRaw.list_star_system_links(production_server, design_version)
        return result

    async def list_star_system_markers(self, access_token: str, client_date_time: str) -> _List[_StarSystemMarker]:
        production_server = await self.get_production_server()
        result = await _GalaxyServiceRaw.list_star_system_markers(production_server, access_token, client_date_time)
        return result

    async def list_star_system_markers_and_user_markers(self, access_token: str) -> _Tuple[_List[_StarSystemMarker], _List[_UserMarker]]:
        production_server = await self.get_production_server()
        result = await _GalaxyServiceRaw.list_star_system_markers_and_user_markers(production_server, access_token)
        return result

    @_service_base.cache_endpoint("StarSystemVersion")
    async def list_star_systems(self, design_version: int = None) -> _List[_StarSystem]:
        production_server = await self.get_production_server()
        result = await _GalaxyServiceRaw.list_star_systems(production_server, design_version, self.language_key)
        return result
