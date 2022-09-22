from datetime import datetime as _datetime
from typing import List as _List

from .raw import GalaxyServiceRaw as _GalaxyServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import Ship as _Ship
from ..entities import StarSystem as _StarSystem
from ..entities import StarSystemLink as _StarSystemLink
from ..entities import StarSystemMarker as _StarSystemMarker
from ..entities import StarSystemMarkerGenerator as _StarSystemMarkerGenerator


class GalaxyService(_ServiceBase, _GalaxyServiceRaw):
    async def go_to(self, star_system_id: int, client_date_time: _datetime, checksum: str, access_token: str, **params) -> _List[_Ship]:
        return await self._go_to(self.production_server, star_system_id, client_date_time, checksum, access_token, **params)

    async def list_marker_generator_designs(self, design_version: int = None, **params) -> _List[_StarSystemMarkerGenerator]:
        return await self._list_marker_generator_designs(self.production_server, self.language_key, design_version, **params)

    async def list_star_system_links(self, design_version: int = None, **params) -> _List[_StarSystemLink]:
        return await self._list_star_system_links(self.production_server, design_version, **params)

    async def list_star_system_markers(self, access_token: str, client_date_time: _datetime, **params) -> _List[_StarSystemMarker]:
        return await self._list_star_system_markers(self.production_server, access_token, client_date_time, **params)

    async def list_star_systems(self, design_version: int = None, **params) -> _List[_StarSystem]:
        return await self._list_star_systems(self.production_server, self.language_key, design_version, **params)

    def __repr__(self) -> str:
        return f'<GalaxyService: {self.name}>'

    def __str__(self) -> str:
        return f'<GalaxyService: {self.name}>'
