import hashlib as _hashlib
import random as _random
import string as _string
from datetime import datetime as _datetime
from typing import List as _List

import pssapi.services.service_base as _service_base

from .. import entities as _entities
from .. import enums as _enums
from .. import utils as _utils
from .raw import UserServiceRaw as _UserServiceRaw


class _UserServiceUtils:
    @staticmethod
    def create_device_login_checksum(device_key: str, device_type: _enums.DeviceType, client_datetime: _datetime, checksum_key: str) -> str:
        timestamp = _utils.datetime.convert_to_pss_timestamp(client_datetime)
        result = _hashlib.md5(f"{device_key}{timestamp}{device_type}{checksum_key}savysoda".encode("utf-8")).hexdigest()
        return result

    @staticmethod
    def _create_device_key() -> str:
        result = "".join(_random.choice(_string.hexdigits) + _random.choice("26ae") + _random.choices(_string.hexdigits, k=10))
        return result


class UserService(_service_base.ServiceBase):
    utils = _UserServiceUtils()

    async def accept_friend_request(self, access_token: str, friend_user_id: int) -> _entities.Friend:
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.accept_friend_request(production_server, access_token, friend_user_id)
        return result

    async def add_friend(self, access_token: str, friend_user_id: int) -> _entities.Friend:
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.add_friend_2(production_server, access_token, friend_user_id)
        return result

    async def decline_friend_request(self, access_token: str, friend_user_id: int) -> _entities.Friend:
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.decline_friend_request(production_server, access_token, friend_user_id)
        return result

    async def device_login(
        self,
        access_token: str,
        checksum: str,
        client_date_time: _datetime,
        device_key: str,
        device_type: _enums.DeviceType,
        language_key: _enums.LanguageKey,
        advertising_key: str = '""',
        client_build: int = None,
        client_version: str = None,
        device_name: str = None,
        is_jail_broken: bool = None,
        locale: str = None,
        os_build: int = None,
        os_version: str = None,
        refresh_token: str = None,
        signal: bool = None,
    ) -> _entities.UserLogin:
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.device_login_15(
            production_server,
            access_token,
            advertising_key or '""',
            checksum,
            client_build,
            _utils.datetime.convert_to_pss_timestamp(client_date_time),
            client_version,
            device_key,
            device_name,
            str(device_type),
            is_jail_broken,
            str(language_key),
            locale,
            os_build,
            os_version,
            refresh_token,
            signal,
        )
        return result

    async def list_friends(self, user_id: int, access_token: str) -> _entities.ListFriends:
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.list_friends(production_server, user_id, access_token)
        return result

    async def remove_friend(self, access_token: str, friend_user_id: int) -> None:
        production_server = await self.get_production_server()
        await _UserServiceRaw.remove_friend(production_server, access_token, friend_user_id)

    async def search_users(self, search_string: str) -> _List[_entities.User]:
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.search_users(production_server, search_string)
        return result

    async def steam_login(
        self,
        access_token: str,
        checksum: str,
        client_date_time: _datetime,
        device_key: str,
        device_type: _enums.DeviceType,
        language_key: _enums.LanguageKey,
        advertising_key: str = '""',
        client_build: int = None,
        client_version: str = None,
        device_name: str = None,
        is_jail_broken: bool = None,
        locale: str = None,
        os_build: int = None,
        os_version: str = None,
        refresh_token: str = None,
        signal: bool = None,
        ticket: str = None,
    ) -> _entities.UserLogin:
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.steam_login_6(
            production_server,
            access_token,
            advertising_key or '""',
            checksum,
            client_build,
            _utils.datetime.convert_to_pss_timestamp(client_date_time),
            client_version,
            device_key,
            device_name,
            str(device_type),
            is_jail_broken,
            str(language_key),
            locale,
            os_build,
            os_version,
            refresh_token,
            signal,
            ticket,
        )
        return result

    async def user_email_password_authorize(self, access_token: str, checksum: str, client_date_time: str, device_key: str, email: str, password: str) -> _entities.UserEmailPasswordAuthorize:
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.user_email_password_authorize_2(production_server, access_token, checksum, client_date_time, device_key, email, password)
        return result
