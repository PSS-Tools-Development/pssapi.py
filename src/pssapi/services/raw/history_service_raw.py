"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from ... import core
from ...entities import History


# ---------- Constants ----------

PRICE_HISTORY_BASE_PATH: str = "HistoryService/PriceHistory"

# ---------- Endpoint structure ----------


# ---------- Endpoints ----------


async def price_history(production_server: str, item_design_id: int, **params) -> History:
    params = {"itemDesignId": item_design_id, **params}
    result = await core.get_entities_from_path(((History, "History", False),), "Histories", production_server, PRICE_HISTORY_BASE_PATH, "GET", response_gzipped=False, **params)
    return result
