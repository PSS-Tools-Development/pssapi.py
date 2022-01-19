import asyncio as _asyncio

from . import constants as _constants
from . import core as _core
from .services import ItemService as _ItemService
from .services import SettingService as _SettingService
from .enums import LanguageKey as _LanguageKey



class PssApiClient():
    def __init__(self, production_server: str, language_key: _LanguageKey = _LanguageKey.English) -> None:
        self.__language_key: _LanguageKey = language_key or _LanguageKey.English
        self.__production_server: str = production_server
        if not self.production_server:
            self.__production_server = _asyncio.run(self.get_production_server)
        self._update_services(self.production_server)


    @property
    def production_server(self) -> str:
        return self.__production_server


    def _update_services(self, production_server: str) -> None:
        self.item_service: _ItemService = _ItemService(production_server)
        self.setting_service: _SettingService = _SettingService(production_server)


    async def get_production_server(self) -> str:
        setting_service = _SettingService(_constants.DEFAULT_PRODUCTION_SERVER)
        return await setting_service.get_latest_version(self.__language_key)