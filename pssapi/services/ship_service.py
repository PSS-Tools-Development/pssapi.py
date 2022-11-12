from typing import List as _List

from .raw import ShipServiceRaw as _ShipServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import Ship as _Ship
from ..entities import ShipDesign as _ShipDesign


class ShipService(_ServiceBase):
    async def inspect_ship(self, access_token: str, user_id: int) -> _List[_Ship]:
        result = await _ShipServiceRaw.inspect_ship_2(self.production_server, access_token, user_id)
        return result

    async def list_all_ship_designs(self, design_version: int = None) -> _List[_ShipDesign]:
        result = await _ShipServiceRaw.list_all_ship_designs_2(self.production_server, design_version, self.language_key)
        return result
