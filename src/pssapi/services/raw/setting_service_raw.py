"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from typing import List

from ... import core
from ...entities import NewsDesign, Setting


# ---------- Constants ----------

GET_LATEST_VERSION_3_BASE_PATH: str = "SettingService/GetLatestVersion3"
GET_LATEST_VERSION_4_BASE_PATH: str = "SettingService/GetLatestVersion4"
LIST_ALL_NEWS_DESIGNS_BASE_PATH: str = "SettingService/ListAllNewsDesigns"

# ---------- Endpoint structure ----------


# ---------- Endpoints ----------


async def get_latest_version_3(production_server: str, device_type: str, language_key: str, **params) -> Setting:
    params = {"deviceType": device_type, "languageKey": language_key, **params}
    result = await core.get_entities_from_path(((Setting, "Setting", False),), "GetLatestSetting", production_server, GET_LATEST_VERSION_3_BASE_PATH, "GET", response_gzipped=False, **params)
    return result


async def get_latest_version_4(production_server: str, device_type: str, language_key: str, **params) -> Setting:
    params = {"deviceType": device_type, "languageKey": language_key, **params}
    result = await core.get_entities_from_path(((Setting, "Setting", False),), "GetLatestSetting", production_server, GET_LATEST_VERSION_4_BASE_PATH, "GET", response_gzipped=False, **params)
    return result


async def list_all_news_designs(production_server: str, client_date_time: str, design_version: int, language_key: str, **params) -> List[NewsDesign]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, "languageKey": language_key, **params}
    result = await core.get_entities_from_path(((NewsDesign, "NewsDesigns", True),), "NewsDesigns", production_server, LIST_ALL_NEWS_DESIGNS_BASE_PATH, "GET", response_gzipped=False, **params)
    return result
