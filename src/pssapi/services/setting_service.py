from typing import List

from pssapi.services import service_base

from ..entities import NewsDesign, Setting
from .raw import SettingServiceRaw


class SettingService(service_base.CacheableServiceBase):
    async def get_latest_version(self, device_type: str) -> Setting:
        production_server = await self.get_production_server()
        result = await SettingServiceRaw.get_latest_version_4(production_server, device_type, self.language_key)
        return result

    @service_base.cache_endpoint("NewsDesignVersion")
    async def list_all_news_designs(self, client_date_time: str, design_version: int = None) -> List[NewsDesign]:
        production_server = await self.get_production_server()
        result = await SettingServiceRaw.list_all_news_designs(production_server, client_date_time, design_version, self.language_key)
        return result
