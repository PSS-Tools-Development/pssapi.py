"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import Sale as _Sale

# ---------- Constants ----------

LIST_SALES_BY_ITEM_DESIGN_ID_BASE_PATH: str = "MarketService/ListSalesByItemDesignId"


# ---------- Endpoints ----------


async def list_sales_by_item_design_id(production_server: str, from_: int, item_design_id: int, sale_status: str, to: int, **params) -> _List[_Sale]:
    params = {"from": from_, "itemDesignId": item_design_id, "saleStatus": sale_status, "to": to, **params}
    result = await _core.get_entities_from_path(((_Sale, "Sales", True),), "Sales", production_server, LIST_SALES_BY_ITEM_DESIGN_ID_BASE_PATH, "GET", **params)
    return result
