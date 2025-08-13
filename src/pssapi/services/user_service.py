from datetime import datetime
from typing import List

from pssapi.services import service_base

from ..entities import Friend, ListFriends, Skin, SkinSet, User, UserEmailPasswordAuthorize, UserLogin
from .raw import UserServiceRaw


class UserService(service_base.ServiceBase):
    async def accept_friend_request(self, access_token: str, friend_user_id: int) -> Friend:
        production_server = await self.get_production_server()
        result = await UserServiceRaw.accept_friend_request(production_server, access_token, friend_user_id)
        return result

    async def add_friend(self, access_token: str, friend_user_id: int) -> Friend:
        production_server = await self.get_production_server()
        result = await UserServiceRaw.add_friend_2(production_server, access_token, friend_user_id)
        return result

    async def decline_friend_request(self, access_token: str, friend_user_id: int) -> Friend:
        production_server = await self.get_production_server()
        result = await UserServiceRaw.decline_friend_request(production_server, access_token, friend_user_id)
        return result

    async def device_login(
        self,
        access_token: str,
        advertising_key: str,
        checksum: str,
        client_build: int,
        client_date_time: datetime,
        client_version: str,
        device_key: str,
        device_name: str,
        device_type: str,
        is_jail_broken: bool,
        language_key: str,
        locale: str,
        os_build: int,
        os_version: str,
        refresh_token: str,
        signal: bool,
    ) -> UserLogin:
        production_server = await self.get_production_server()
        result = await UserServiceRaw.device_login_15(
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

    async def list_friends(self, user_id: int, access_token: str) -> ListFriends:
        production_server = await self.get_production_server()
        result = await UserServiceRaw.list_friends(production_server, user_id, access_token)
        return result

    async def list_skin_sets(self, client_date_time: str, design_version: int = None) -> List[SkinSet]:
        production_server = await self.get_production_server()
        result = await UserServiceRaw.list_skin_sets_2(production_server, client_date_time, design_version, self.language_key)
        return result

    async def list_skins(self, client_date_time: str, design_version: int = None) -> List[Skin]:
        production_server = await self.get_production_server()
        result = await UserServiceRaw.list_skins_2(production_server, client_date_time, design_version, self.language_key)
        return result

    async def remove_friend(self, access_token: str, friend_user_id: int) -> None:
        production_server = await self.get_production_server()
        await UserServiceRaw.remove_friend(production_server, access_token, friend_user_id)

    async def search_users(self, search_string: str) -> List[User]:
        production_server = await self.get_production_server()
        result = await UserServiceRaw.search_users(production_server, search_string)
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
        device_type: str,
        is_jail_broken: bool,
        language_key: str,
        locale: str,
        os_build: int,
        os_version: str,
        refresh_token: str,
        signal: bool,
        ticket: str,
    ) -> UserLogin:
        production_server = await self.get_production_server()
        result = await UserServiceRaw.steam_login_6(
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

    async def user_email_password_authorize(self, access_token: str, checksum: str, client_date_time: str, device_key: str, email: str, is_web: bool, password: str) -> UserEmailPasswordAuthorize:
        production_server = await self.get_production_server()
        result = await UserServiceRaw.user_email_password_authorize_4(production_server, access_token, checksum, client_date_time, device_key, email, is_web, self.language_key, password)
        return result
