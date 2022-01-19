from typing import List as _List
from typing import Tuple as _Tuple

import pssapi.services.service_base as _service_base

from ..entities import Ship as _Ship
from ..entities import ShipDesign as _ShipDesign
from ..entities import User as _User
from .raw import ShipServiceRaw as _ShipServiceRaw


class ShipService(_service_base.CacheableServiceBase):
    async def get_ship_by_user_id(self, access_token: str, client_date_time: str, user_id: int) -> _Ship:
        production_server = await self.get_production_server()
        result = await _ShipServiceRaw.get_ship_by_user_id(production_server, access_token, client_date_time, user_id)
        return result

    async def inspect_ship(self, access_token: str, user_id: int) -> _Tuple[_Ship, _User]:
        production_server = await self.get_production_server()
        result = await _ShipServiceRaw.inspect_ship_2(production_server, access_token, user_id)
        return result

    @_service_base.cache_endpoint("ShipDesignVersion")
    async def list_all_ship_designs(self, design_version: int = None) -> _List[_ShipDesign]:
        production_server = await self.get_production_server()
        result = await _ShipServiceRaw.list_all_ship_designs_2(production_server, design_version, self.language_key)
        return result
