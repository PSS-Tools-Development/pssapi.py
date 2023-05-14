from datetime import datetime as _datetime
import hashlib as _hashlib
import random as _random
import string as _string
from typing import List as _List

import pssapi.services.service_base as _service_base

from ..entities import Friend as _Friend
from ..entities import ListFriends as _ListFriends
from ..entities import User as _User
from ..entities import UserEmailPasswordAuthorize as _UserEmailPasswordAuthorize
from ..entities import UserLogin as _UserLogin
from .raw import UserServiceRaw as _UserServiceRaw



class __UserServiceUtils():
    def create_device_checksum(device_key: str, device_type: str, client_datetime: str, checksum_key: str) -> str:
        result = _hashlib.md5(f'{device_key}{client_datetime}{device_type}{checksum_key}savysoda'.encode('utf-8')).hexdigest()
        return result

    def _create_device_key() -> str:
        result = ''.join(
            _random.choice(_string.hexdigits)
            + _random.choice('26ae')
            + _random.choices(_string.hexdigits, k=10)
        )
        return result



class UserService(_service_base.ServiceBase):
    utils = __UserServiceUtils()
    
    async def accept_friend_request(self, access_token: str, friend_user_id: int) -> _Friend:
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.accept_friend_request(production_server, access_token, friend_user_id)
        return result

    async def add_friend(self, access_token: str, friend_user_id: int) -> _Friend:
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.add_friend_2(production_server, access_token, friend_user_id)
        return result

    async def decline_friend_request(self, access_token: str, friend_user_id: int) -> _Friend:
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.decline_friend_request(production_server, access_token, friend_user_id)
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

    async def list_friends(self, user_id: int, access_token: str) -> _ListFriends:
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.list_friends(production_server, user_id, access_token)
        return result

    async def remove_friend(self, access_token: str, friend_user_id: int) -> None:
        production_server = await self.get_production_server()
        await _UserServiceRaw.remove_friend(production_server, access_token, friend_user_id)

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

    async def user_email_password_authorize(self, access_token: str, checksum: str, client_date_time: str, device_key: str, email: str, password: str) -> _UserEmailPasswordAuthorize:
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.user_email_password_authorize_2(production_server, access_token, checksum, client_date_time, device_key, email, password)
        return result