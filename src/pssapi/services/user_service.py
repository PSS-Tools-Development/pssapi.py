from datetime import datetime as _datetime
from typing import List as _List

from .raw import UserServiceRaw as _UserServiceRaw
import pssapi.services.service_base as _service_base
from ..entities import User as _User
from ..entities import UserLogin as _UserLogin


class UserService(_service_base.ServiceBase):
    async def device_login(self, access_token: str, advertising_key: str, checksum: str, client_build: int, client_date_time: _datetime, client_version: str, device_key: str, device_name: str, device_type: int, is_jail_broken: bool, language_key: str, locale: str, os_build: int, os_version: str, refresh_token: str, signal: bool) -> _UserLogin:
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.device_login_12(production_server, access_token, advertising_key, checksum, client_build, client_date_time, client_version, device_key, device_name, device_type, is_jail_broken, language_key, locale, os_build, os_version, refresh_token, signal)
        return result

    async def search_users(self, search_string: str) -> _List[_User]:
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.search_users(production_server, search_string)
        return result

    async def steam_login(self, access_token: str, advertising_key: str, checksum: str, client_build: int, client_date_time: str, client_version: str, device_key: str, device_name: str, device_type: int, is_jail_broken: bool, language_key: str, locale: str, os_build: int, os_version: str, refresh_token: str, signal: bool, ticket: str) -> _UserLogin:
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.steam_login_6(production_server, access_token, advertising_key, checksum, client_build, client_date_time, client_version, device_key, device_name, device_type, is_jail_broken, language_key, locale, os_build, os_version, refresh_token, signal, ticket)
        return result
