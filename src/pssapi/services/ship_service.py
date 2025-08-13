from typing import List, Tuple

from pssapi.services import service_base

from ..entities import Ship, ShipDesign, User
from .raw import ShipServiceRaw


class ShipService(service_base.CacheableServiceBase):
    async def get_ship_by_user_id(self, access_token: str, client_date_time: str, user_id: int) -> Ship:
        production_server = await self.get_production_server()
        result = await ShipServiceRaw.get_ship_by_user_id(production_server, access_token, client_date_time, user_id)
        return result

    async def inspect_ship(self, access_token: str, user_id: int) -> Tuple[Ship, User]:
        production_server = await self.get_production_server()
        result = await ShipServiceRaw.inspect_ship_2(production_server, access_token, user_id)
        return result

    @service_base.cache_endpoint("ShipDesignVersion")
    async def list_all_ship_designs(self, client_date_time: str, design_version: int = None) -> List[ShipDesign]:
        production_server = await self.get_production_server()
        result = await ShipServiceRaw.list_all_ship_designs_2(production_server, client_date_time, design_version, self.language_key)
        return result
