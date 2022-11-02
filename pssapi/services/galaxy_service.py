from typing import List as _List

from .raw import GalaxyServiceRaw as _GalaxyServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import Ship as _Ship
from ..entities import StarSystem as _StarSystem
from ..entities import StarSystemLink as _StarSystemLink
from ..entities import StarSystemMarker as _StarSystemMarker
from ..entities import StarSystemMarkerGenerator as _StarSystemMarkerGenerator


class GalaxyService(_ServiceBase):
    async def go_to(self, star_system_id: int, client_date_time: str, checksum: str, access_token: str) -> _List[_Ship]:
        result = await _GalaxyServiceRaw.go_to(production_server=self.production_server, star_system_id=star_system_id, client_date_time=client_date_time, checksum=checksum, access_token=access_token)
        return result

    async def list_marker_generator_designs(self, design_version: int = None) -> _List[_StarSystemMarkerGenerator]:
        result = await _GalaxyServiceRaw.list_marker_generator_designs(production_server=self.production_server, design_version=design_version, language_key=self.language_key)
        return result

    async def list_star_system_links(self, design_version: int = None) -> _List[_StarSystemLink]:
        result = await _GalaxyServiceRaw.list_star_system_links(production_server=self.production_server, design_version=design_version)
        return result

    async def list_star_system_markers(self, client_date_time: str, access_token: str) -> _List[_StarSystemMarker]:
        result = await _GalaxyServiceRaw.list_star_system_markers(production_server=self.production_server, client_date_time=client_date_time, access_token=access_token)
        return result

    async def list_star_systems(self, design_version: int = None) -> _List[_StarSystem]:
        result = await _GalaxyServiceRaw.list_star_systems(production_server=self.production_server, design_version=design_version, language_key=self.language_key)
        return result

    async def update_marker_movement(self, star_system_marker_id: int, checksum: str, client_date_time: str, access_token: str) -> _List[_StarSystemMarker]:
        result = await _GalaxyServiceRaw.update_marker_movement(production_server=self.production_server, star_system_marker_id=star_system_marker_id, checksum=checksum, client_date_time=client_date_time, access_token=access_token)
        return result
