from typing import List, Tuple

from pssapi.services import service_base

from ..entities import Planet, Ship, StarSystem, StarSystemLink, StarSystemMarker, StarSystemMarkerGenerator, UserMarker
from .raw import GalaxyServiceRaw


class GalaxyService(service_base.CacheableServiceBase):
    async def go_to(self, access_token: str, checksum: str, client_date_time: str, star_system_id: int) -> Ship:
        production_server = await self.get_production_server()
        result = await GalaxyServiceRaw.go_to(production_server, access_token, checksum, client_date_time, star_system_id)
        return result

    @service_base.cache_endpoint("MarkerGeneratorDesignVersion")
    async def list_marker_generator_designs(self, client_date_time: str, design_version: int = None) -> List[StarSystemMarkerGenerator]:
        production_server = await self.get_production_server()
        result = await GalaxyServiceRaw.list_marker_generator_designs(production_server, client_date_time, design_version, self.language_key)
        return result

    @service_base.cache_endpoint("PlanetVersion")
    async def list_planets(self, design_version: int = None) -> List[Planet]:
        production_server = await self.get_production_server()
        result = await GalaxyServiceRaw.list_planets(production_server, design_version)
        return result

    @service_base.cache_endpoint("StarSystemLinkVersion")
    async def list_star_system_links(self, client_date_time: str, design_version: int = None) -> List[StarSystemLink]:
        production_server = await self.get_production_server()
        result = await GalaxyServiceRaw.list_star_system_links(production_server, client_date_time, design_version)
        return result

    async def list_star_system_markers(self, access_token: str, client_date_time: str) -> List[StarSystemMarker]:
        production_server = await self.get_production_server()
        result = await GalaxyServiceRaw.list_star_system_markers(production_server, access_token, client_date_time)
        return result

    async def list_star_system_markers_and_user_markers(self, access_token: str) -> Tuple[List[StarSystemMarker], List[UserMarker]]:
        production_server = await self.get_production_server()
        result = await GalaxyServiceRaw.list_star_system_markers_and_user_markers(production_server, access_token)
        return result

    @service_base.cache_endpoint("StarSystemVersion")
    async def list_star_systems(self, client_date_time: str, design_version: int = None) -> List[StarSystem]:
        production_server = await self.get_production_server()
        result = await GalaxyServiceRaw.list_star_systems(production_server, client_date_time, design_version, self.language_key)
        return result
