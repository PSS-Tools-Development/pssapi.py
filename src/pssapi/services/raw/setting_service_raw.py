"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import NewsDesign as _NewsDesign
from ...entities import Setting as _Setting

# ---------- Constants ----------

GET_LATEST_VERSION_3_BASE_PATH: str = "SettingService/GetLatestVersion3"
LIST_ALL_NEWS_DESIGNS_BASE_PATH: str = "SettingService/ListAllNewsDesigns"


# ---------- Endpoints ----------


async def get_latest_version_3(production_server: str, device_type: str, language_key: str, **params) -> _Setting:
    params = {"deviceType": device_type, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_Setting, "Setting", False),), "GetLatestSetting", production_server, GET_LATEST_VERSION_3_BASE_PATH, "GET", **params)
    return result


async def list_all_news_designs(production_server: str, design_version: int, language_key: str, **params) -> _List[_NewsDesign]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_NewsDesign, "NewsDesigns", True),), "NewsDesigns", production_server, LIST_ALL_NEWS_DESIGNS_BASE_PATH, "GET", **params)
    return result
