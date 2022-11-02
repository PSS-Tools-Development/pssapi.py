from typing import List as _List

from .raw import SettingServiceRaw as _SettingServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import NewsDesign as _NewsDesign
from ..entities import Setting as _Setting


class SettingService(_ServiceBase):
    async def get_latest_version(self, device_type: str) -> _List[_Setting]:
        result = await _SettingServiceRaw.get_latest_version_3(production_server=self.production_server, device_type=device_type, language_key=self.language_key)
        return result

    async def list_all_news_designs(self, design_version: int = None) -> _List[_NewsDesign]:
        result = await _SettingServiceRaw.list_all_news_designs(production_server=self.production_server, design_version=design_version, language_key=self.language_key)
        return result
