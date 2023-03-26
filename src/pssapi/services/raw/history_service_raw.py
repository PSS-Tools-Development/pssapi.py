"""
    This file has been generated automatically
"""


from ... import core as _core
from ...entities import History as _History

# ---------- Constants ----------

PRICE_HISTORY_BASE_PATH: str = "HistoryService/PriceHistory"


# ---------- Endpoints ----------


async def price_history(production_server: str, item_design_id: int, **params) -> _History:
    params = {"itemDesignId": item_design_id, **params}
    result = await _core.get_entities_from_path(((_History, "History", False),), "Histories", production_server, PRICE_HISTORY_BASE_PATH, "GET", **params)
    return result
