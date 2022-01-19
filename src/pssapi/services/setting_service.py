from typing import List as _List

import pssapi.services.service_base as _service_base

from ..entities import NewsDesign as _NewsDesign
from ..entities import Setting as _Setting
from .raw import SettingServiceRaw as _SettingServiceRaw


class SettingService(_service_base.CacheableServiceBase):
    async def get_latest_version(self, device_type: str) -> _Setting:
        production_server = await self.get_production_server()
        result = await _SettingServiceRaw.get_latest_version_3(production_server, device_type, self.language_key)
        return result

    @_service_base.cache_endpoint("NewsDesignVersion")
    async def list_all_news_designs(self, design_version: int = None) -> _List[_NewsDesign]:
        production_server = await self.get_production_server()
        result = await _SettingServiceRaw.list_all_news_designs(production_server, design_version, self.language_key)
        return result
