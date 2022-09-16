import asyncio as _asyncio
from typing import Optional as _Optional

from . import constants as _constants
from .services import ItemService as _ItemService
from .services import SettingService as _SettingService
from .enums import DeviceType as _DeviceType
from .enums import LanguageKey as _LanguageKey



class PssApiClient():
    def __init__(self, device_type: _DeviceType = None, language_key: _LanguageKey = None, production_server: str = None) -> None:
        self.__device_type: _DeviceType = device_type or _DeviceType.DeviceTypeAndroid
        self.__language_key: _LanguageKey = language_key or _LanguageKey.English
        self.__production_server: str = production_server
        if not self.production_server:
            loop = _asyncio.get_event_loop()
            self.__production_server = loop.run_until_complete(_get_production_server(self.device_type, self.language_key))
        self._update_services()


    @property
    def device_type(self) -> _DeviceType:
        return self.__device_type

    @property
    def item_service(self) -> _ItemService:
        return self.__item_service

    @property
    def language_key(self) -> _LanguageKey:
        return self.__language_key

    @property
    def production_server(self) -> str:
        return self.__production_server

    @property
    def setting_service(self) -> _SettingService:
        return self.__setting_service


    def _update_services(self) -> None:
        self.__item_service: _ItemService = _ItemService(self.production_server, self.device_type)
        self.__setting_service: _SettingService = _SettingService(self.production_server, self.device_type)


    async def get_production_server(self) -> str:
        return await self.setting_service.get_latest_version_3(self.__language_key)





async def _get_production_server(device_type: _DeviceType, language_key: _LanguageKey) -> _Optional[str]:
    setting_service = _SettingService(_constants.DEFAULT_PRODUCTION_SERVER)
    setting = await setting_service.get_latest_version_3(device_type, language_key)
    return setting.production_server