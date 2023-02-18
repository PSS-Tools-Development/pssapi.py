from typing import List as _List

from .raw import MarketServiceRaw as _MarketServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import Sale as _Sale


class MarketService(_ServiceBase):
    async def list_sales_by_item_design_id(self, from_: int, item_design_id: int, sale_status: str, to: int) -> _List[_Sale]:
        production_server = await self.get_production_server()
        result = await _MarketServiceRaw.list_sales_by_item_design_id(production_server, from_, item_design_id, sale_status, to)
        return result
