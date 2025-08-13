"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from typing import List

from ... import core
from ...entities import Sale


# ---------- Constants ----------

LIST_SALES_BY_ITEM_DESIGN_ID_BASE_PATH: str = "MarketService/ListSalesByItemDesignId"

# ---------- Endpoint structure ----------


# ---------- Endpoints ----------


async def list_sales_by_item_design_id(production_server: str, from_: int, item_design_id: int, sale_status: str, to: int, **params) -> List[Sale]:
    params = {"from": from_, "itemDesignId": item_design_id, "saleStatus": sale_status, "to": to, **params}
    result = await core.get_entities_from_path(((Sale, "Sales", True),), "Sales", production_server, LIST_SALES_BY_ITEM_DESIGN_ID_BASE_PATH, "GET", response_gzipped=False, **params)
    return result
