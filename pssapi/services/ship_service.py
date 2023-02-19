from typing import List as _List
from typing import Tuple as _Tuple

from .raw import ShipServiceRaw as _ShipServiceRaw
import pssapi.services.service_base as _service_base
from ..entities import Ship as _Ship
from ..entities import ShipDesign as _ShipDesign
from ..entities import User as _User


class ShipService(_service_base.ServiceBase):
    async def inspect_ship(self, access_token: str, user_id: int) -> _Tuple[_Ship, _User]:
        production_server = await self.get_production_server()
        result = await _ShipServiceRaw.inspect_ship_2(production_server, access_token, user_id)
        return result

    async def list_all_ship_designs(self, design_version: int = None) -> _List[_ShipDesign]:
        production_server = await self.get_production_server()
        result = await _ShipServiceRaw.list_all_ship_designs_2(production_server, design_version, self.language_key)
        return result
