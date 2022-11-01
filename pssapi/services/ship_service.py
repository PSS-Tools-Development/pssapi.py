from typing import List as _List

from .raw import ShipServiceRaw as _ShipServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import ShipDesign as _ShipDesign


class ShipService(_ServiceBase):
    async def list_all_ship_designs(self, design_version: int = None) -> _List[_ShipDesign]:
        result = await _ShipServiceRaw.list_all_ship_designs_2(self.production_server, self.language_key, design_version)
        return result
