from typing import List as _List

from .raw import SettingServiceRaw as _SettingServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import NewsDesign as _NewsDesign


class SettingService(_ServiceBase):
    async def list_all_news_designs(self, design_version: int = None) -> _List[_NewsDesign]:
        result = await _SettingServiceRaw.list_all_news_designs(self.production_server, self.language_key, design_version)
        return result
