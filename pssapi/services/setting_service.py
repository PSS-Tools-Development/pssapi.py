from typing import List as _List

from .raw import SettingServiceRaw as _SettingServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import NewsDesign as _NewsDesign


class SettingService(_ServiceBase, _SettingServiceRaw):
    async def list_all_news_designs(self, **params) -> _List[_NewsDesign]:
        return await self._list_all_news_designs(self.production_server, self.language_key, **params)

    def __repr__(self) -> str:
        return f'<SettingService: {self.name}>'

    def __str__(self) -> str:
        return f'<SettingService: {self.name}>'
