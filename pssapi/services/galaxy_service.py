from typing import List as _List

from .raw import GalaxyServiceRaw as _GalaxyServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import Ship as _Ship
from ..entities import StarSystem as _StarSystem
from ..entities import StarSystemLink as _StarSystemLink
from ..entities import StarSystemMarker as _StarSystemMarker
from ..entities import StarSystemMarkerGenerator as _StarSystemMarkerGenerator


class GalaxyService(_ServiceBase):
    async def go_to(self, access_token: str, checksum: str, client_date_time: str, star_system_id: int) -> _List[_Ship]:
        result = await _GalaxyServiceRaw.go_to(self.production_server, access_token, checksum, client_date_time, star_system_id)
        return result

    async def list_marker_generator_designs(self, design_version: int = None) -> _List[_StarSystemMarkerGenerator]:
        result = await _GalaxyServiceRaw.list_marker_generator_designs(self.production_server, design_version, self.language_key)
        return result

    async def list_star_system_links(self, design_version: int = None) -> _List[_StarSystemLink]:
        result = await _GalaxyServiceRaw.list_star_system_links(self.production_server, design_version)
        return result

    async def list_star_system_markers(self, access_token: str, client_date_time: str) -> _List[_StarSystemMarker]:
        result = await _GalaxyServiceRaw.list_star_system_markers(self.production_server, access_token, client_date_time)
        return result

    async def list_star_systems(self, design_version: int = None) -> _List[_StarSystem]:
        result = await _GalaxyServiceRaw.list_star_systems(self.production_server, design_version, self.language_key)
        return result

    async def update_marker_movement(self, access_token: str, checksum: str, client_date_time: str, star_system_marker_id: int) -> _List[_StarSystemMarker]:
        result = await _GalaxyServiceRaw.update_marker_movement(self.production_server, access_token, checksum, client_date_time, star_system_marker_id)
        return result
