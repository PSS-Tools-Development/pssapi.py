from typing import List as _List

from .raw import GalaxyServiceRaw as _GalaxyServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import Ship as _Ship
from ..entities import StarSystem as _StarSystem
from ..entities import StarSystemLink as _StarSystemLink
from ..entities import StarSystemMarker as _StarSystemMarker
from ..entities import StarSystemMarkerGenerator as _StarSystemMarkerGenerator


class GalaxyService(_ServiceBase, _GalaxyServiceRaw):
    async def go_to(self, **params) -> _List[_Ship]:
        return await self._go_to(self.production_server, self.star_system_id, self.client_date_time, self.checksum, self.access_token, **params)

    async def list_marker_generator_designs(self, **params) -> _List[_StarSystemMarkerGenerator]:
        return await self._list_marker_generator_designs(self.production_server, self.language_key, **params)

    async def list_star_system_links(self, **params) -> _List[_StarSystemLink]:
        return await self._list_star_system_links(self.production_server, **params)

    async def list_star_system_markers(self, **params) -> _List[_StarSystemMarker]:
        return await self._list_star_system_markers(self.production_server, self.access_token, self.client_date_time, **params)

    async def list_star_systems(self, **params) -> _List[_StarSystem]:
        return await self._list_star_systems(self.production_server, self.language_key, **params)

    def __repr__(self) -> str:
        return f'<GalaxyService: {self.name}>'

    def __str__(self) -> str:
        return f'<GalaxyService: {self.name}>'
