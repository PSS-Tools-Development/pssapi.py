from datetime import datetime as _datetime
from typing import List as _List

from .raw import ShipServiceRaw as _ShipServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import Ship as _Ship
from ...entities import ShipDesign as _ShipDesign


class ShipService(_ServiceBase):
    async def get_ship_by_user_id(self, user_id: int, access_token: str, client_date_time: _datetime) -> _List[_Ship]:
        raise NotImplemented()
        result = await _ShipServiceRaw.get_ship_by_user_id(self.production_server, user_id: int, access_token: str, client_date_time: _datetime)
        return result


    async def list_all_ship_designs_2(self, language_key: str, design_version: int) -> _List[_ShipDesign]:
        raise NotImplemented()
        result = await _ShipServiceRaw.list_all_ship_designs_2(self.production_server, language_key: str, design_version: int)
        return result


