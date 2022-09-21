from typing import List as _List

from .raw import ShipServiceRaw as _ShipServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import ShipDesign as _ShipDesign


class ShipService(_ServiceBase, _ShipServiceRaw):
    async def list_all_ship_designs_2(self, **params) -> _List[_ShipDesign]:
        return await self._list_all_ship_designs_2(self.production_server, self.language_key, **params)

    def __repr__(self) -> str:
        return f'<ShipService: {self.name}>'

    def __str__(self) -> str:
        return f'<ShipService: {self.name}>'
