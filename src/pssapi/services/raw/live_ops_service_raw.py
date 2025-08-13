"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from ... import core
from ...entities import GetCatalogQuantity, LiveOps


# ---------- Constants ----------

GET_CATALOG_QUANTITY_BASE_PATH: str = "LiveOpsService/GetCatalogQuantity"
GET_TODAY_LIVE_OPS_BASE_PATH: str = "LiveOpsService/GetTodayLiveOps"
GET_TODAY_LIVE_OPS_2_BASE_PATH: str = "LiveOpsService/GetTodayLiveOps2"

# ---------- Endpoint structure ----------


# ---------- Endpoints ----------


async def get_catalog_quantity(production_server: str, **params) -> GetCatalogQuantity:
    params = {**params}
    result = await core.get_entities_from_path(
        ((GetCatalogQuantity, "GetCatalogQuantity", False),), "LiveOpsService", production_server, GET_CATALOG_QUANTITY_BASE_PATH, "GET", response_gzipped=False, **params
    )
    return result


async def get_today_live_ops(production_server: str, device_type: str, language_key: str, **params) -> LiveOps:
    params = {"deviceType": device_type, "languageKey": language_key, **params}
    result = await core.get_entities_from_path(((LiveOps, "LiveOps", False),), "GetTodayLiveOps", production_server, GET_TODAY_LIVE_OPS_BASE_PATH, "GET", response_gzipped=False, **params)
    return result


async def get_today_live_ops_2(production_server: str, device_type: str, language_key: str, **params) -> LiveOps:
    params = {"deviceType": device_type, "languageKey": language_key, **params}
    result = await core.get_entities_from_path(((LiveOps, "LiveOps", False),), "GetTodayLiveOps", production_server, GET_TODAY_LIVE_OPS_2_BASE_PATH, "GET", response_gzipped=False, **params)
    return result
