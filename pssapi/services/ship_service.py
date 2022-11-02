from typing import List as _List

from .raw import ShipServiceRaw as _ShipServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import ShipDesign as _ShipDesign
from ..entities import User as _User


class ShipService(_ServiceBase):
    async def inspect_ship(self, user_id: int, access_token: str) -> _List[_User]:
        result = await _ShipServiceRaw.inspect_ship_2(production_server=self.production_server, user_id=user_id, access_token=access_token)
        return result

    async def list_all_ship_designs(self, design_version: int = None) -> _List[_ShipDesign]:
        result = await _ShipServiceRaw.list_all_ship_designs_2(production_server=self.production_server, design_version=design_version, language_key=self.language_key)
        return result
