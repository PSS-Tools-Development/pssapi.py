"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import NewsDesign as _NewsDesign


class SettingServiceRaw:

    SERVICE_NAME = 'SettingService'
    LIST_ALL_NEWS_DESIGNS_BASE_PATH: str = 'SettingService/ListAllNewsDesigns'

    @staticmethod
    async def _list_all_news_designs(production_server: str, language_key: str, design_version: int = None, **params) -> _List[_NewsDesign]:
        params = {
            'languageKey': language_key,
            'designVersion': design_version,
            **params
        }
        result = await _core.get_entities_from_path(_NewsDesign, 'NewsDesigns', production_server, SettingServiceRaw.LIST_ALL_NEWS_DESIGNS_BASE_PATH, **params)
        return result
