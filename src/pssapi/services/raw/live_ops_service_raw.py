"""
    This file has been generated automatically
"""


from ... import core as _core
from ...entities import GetCatalogQuantity as _GetCatalogQuantity
from ...entities import LiveOps as _LiveOps

# ---------- Constants ----------

GET_CATALOG_QUANTITY_BASE_PATH: str = "LiveOpsService/GetCatalogQuantity"
GET_TODAY_LIVE_OPS_BASE_PATH: str = "LiveOpsService/GetTodayLiveOps"
GET_TODAY_LIVE_OPS_2_BASE_PATH: str = "LiveOpsService/GetTodayLiveOps2"


# ---------- Endpoints ----------


async def get_catalog_quantity(production_server: str, **params) -> _GetCatalogQuantity:
    params = {**params}
    result = await _core.get_entities_from_path(((_GetCatalogQuantity, "GetCatalogQuantity", False),), "LiveOpsService", production_server, GET_CATALOG_QUANTITY_BASE_PATH, "GET", **params)
    return result


async def get_today_live_ops(production_server: str, device_type: str, language_key: str, **params) -> _LiveOps:
    params = {"deviceType": device_type, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_LiveOps, "LiveOps", False),), "GetTodayLiveOps", production_server, GET_TODAY_LIVE_OPS_BASE_PATH, "GET", **params)
    return result


async def get_today_live_ops_2(production_server: str, device_type: str, language_key: str, **params) -> _LiveOps:
    params = {"deviceType": device_type, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_LiveOps, "LiveOps", False),), "GetTodayLiveOps", production_server, GET_TODAY_LIVE_OPS_2_BASE_PATH, "GET", **params)
    return result
