from typing import List

from pssapi.services import service_base

from ..entities import Sale
from .raw import MarketServiceRaw


class MarketService(service_base.ServiceBase):
    async def list_sales_by_item_design_id(self, from_: int, item_design_id: int, sale_status: str, to: int) -> List[Sale]:
        production_server = await self.get_production_server()
        result = await MarketServiceRaw.list_sales_by_item_design_id(production_server, from_, item_design_id, sale_status, to)
        return result
