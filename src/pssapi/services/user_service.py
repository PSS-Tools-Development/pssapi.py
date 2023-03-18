from datetime import datetime as _datetime
from typing import List as _List
from typing import Tuple as _Tuple

import pssapi.services.service_base as _service_base

from ..entities import AddStarbux as _AddStarbux
from ..entities import Item as _Item
from ..entities import User as _User
from ..entities import UserLogin as _UserLogin
from .raw import UserServiceRaw as _UserServiceRaw


class UserService(_service_base.ServiceBase):
    async def add_starbux(self, access_token: str, checksum: int, client_date_time: str, quantity: int) -> _Tuple[_AddStarbux, _AddStarbux]:
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.add_starbux_2(production_server, access_token, checksum, client_date_time, quantity)
        return result

    async def collect_daily_reward(self, access_token: str, argument: int, daily_reward_status: str) -> _List[_Item]:
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.collect_daily_reward_2(production_server, access_token, argument, daily_reward_status)
        return result

    async def device_login(
        self,
        access_token: str,
        advertising_key: str,
        checksum: str,
        client_build: int,
        client_date_time: _datetime,
        client_version: str,
        device_key: str,
        device_name: str,
        device_type: int,
        is_jail_broken: bool,
        language_key: str,
        locale: str,
        os_build: int,
        os_version: str,
        refresh_token: str,
        signal: bool,
    ) -> _UserLogin:
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.device_login_15(
            production_server,
            access_token,
            advertising_key,
            checksum,
            client_build,
            client_date_time,
            client_version,
            device_key,
            device_name,
            device_type,
            is_jail_broken,
            language_key,
            locale,
            os_build,
            os_version,
            refresh_token,
            signal,
        )
        return result

    async def purchase_catalog(self, access_token: str, argument: int, checksum: int, client_date_time: str) -> _User:
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.purchase_catalog_2(production_server, access_token, argument, checksum, client_date_time)
        return result

    async def search_users(self, search_string: str) -> _List[_User]:
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.search_users(production_server, search_string)
        return result

    async def steam_login(
        self,
        access_token: str,
        advertising_key: str,
        checksum: str,
        client_build: int,
        client_date_time: str,
        client_version: str,
        device_key: str,
        device_name: str,
        device_type: int,
        is_jail_broken: bool,
        language_key: str,
        locale: str,
        os_build: int,
        os_version: str,
        refresh_token: str,
        signal: bool,
        ticket: str,
    ) -> _UserLogin:
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.steam_login_6(
            production_server,
            access_token,
            advertising_key,
            checksum,
            client_build,
            client_date_time,
            client_version,
            device_key,
            device_name,
            device_type,
            is_jail_broken,
            language_key,
            locale,
            os_build,
            os_version,
            refresh_token,
            signal,
            ticket,
        )
        return result
