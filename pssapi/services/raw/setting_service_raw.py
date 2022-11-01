"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import NewsDesign as _NewsDesign


# ---------- Constants ----------

LIST_ALL_NEWS_DESIGNS_BASE_PATH: str = 'SettingService/ListAllNewsDesigns'


# ---------- Endpoints ----------

async def list_all_news_designs(production_server: str, language_key: str, design_version: int, **params) -> _List[_NewsDesign]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
        **params
    }
    result = await _core.get_entities_from_path(_NewsDesign, 'NewsDesigns', production_server, LIST_ALL_NEWS_DESIGNS_BASE_PATH, **params)
    return result
