from typing import List as _List

import pssapi.services.service_base as _service_base

from ..entities import Sale as _Sale
from .raw import MarketServiceRaw as _MarketServiceRaw


class MarketService(_service_base.ServiceBase):
    async def list_sales_by_item_design_id(self, from_: int, item_design_id: int, sale_status: str, to: int) -> _List[_Sale]:
        production_server = await self.get_production_server()
        result = await _MarketServiceRaw.list_sales_by_item_design_id(production_server, from_, item_design_id, sale_status, to)
        return result
