from typing import List as _List

from .service_base import ServiceBase as _ServiceBase
from ..entities import Sale as _Sale
from .. import core as _core


class MarketService(_ServiceBase):
    async def list_sales_by_item_design_id(self, item_design_id: int, sale_status: str, from_: int, to_: int) -> _List[_Sale]:
        params = {
            'itemDesignId': item_design_id,
            'saleStatus': sale_status,
            'from': from_,
            'to': to_,
        }

        result = await _core.get_entities_from_path(_Sale, 'Sales', self.production_server, 'MarketService/ListSalesByItemDesignId', **params)
        return result
