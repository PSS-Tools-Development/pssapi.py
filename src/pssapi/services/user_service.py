import datetime as _datetime
import hashlib as _hashlib
from typing import List as _List
from typing import Tuple as _Tuple
from uuid import uuid4

import pssapi.services.service_base as _service_base

from .. import entities as _entities
from .. import enums as _enums
from .. import utils as _utils
from .raw import UserServiceRaw as _UserServiceRaw


class _UserServiceUtils:
    @staticmethod
    def create_device_login_checksum(device_key: str, device_type: _enums.DeviceType, client_datetime: _datetime.datetime, checksum_key: str) -> str:
        """
        Generate a checksum for the `DeviceLogin` endpoints.

        :param device_type: Device type.
        :param client_datetime: Current UTC date and time.
        :param checksum_key: A secret key for creating the checksum. While easily found online, it won't be included in pssapi, complying with SavySoda.
        :param device_key: Optional UUID; will be generated if left empty.
        """
        if not checksum_key:
            raise _utils.exceptions.InvalidChecksumKey()

        timestamp = _utils.datetime.convert_to_pss_timestamp(client_datetime)
        result = _hashlib.md5(f"{device_key}{timestamp}{device_type}{checksum_key}".encode("utf-8")).hexdigest()
        return result

    @staticmethod
    def _create_device_key() -> str:
        return str(uuid4())


class UserService(_service_base.ServiceBase):
    utils = _UserServiceUtils()

    async def accept_friend_request(self, access_token: str, friend_user_id: int) -> _entities.Friend:
        """Accept a pending friend request and return the friend entry: id, friend user id, type, name, level, trophy and unread messages count."""
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.accept_friend_request(production_server, access_token, friend_user_id)
        return result

    async def add_friend(self, access_token: str, friend_user_id: int) -> _entities.Friend:
        """Send a friend request to a user and return the friend entry: id, friend user id, type, name, level, trophy and unread messages count."""
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.add_friend_2(production_server, access_token, friend_user_id)
        return result

    async def decline_friend_request(self, access_token: str, friend_user_id: int) -> _entities.Friend:
        """Decline a pending friend request and return the friend entry: id, friend user id, type, name, level, trophy and unread messages count."""
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.decline_friend_request(production_server, access_token, friend_user_id)
        return result

    async def device_login(
        self,
        checksum: str,
        client_date_time: _datetime.datetime,
        device_key: str,
        device_type: _enums.DeviceType,
        access_token: str = None,
        advertising_key: str = None,
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
        """
        This is a shortcut to `UserService.device_login_17`.
        """
        return await self.device_login_17(
            checksum,
            client_date_time,
            device_key,
            device_type,
            self.language_key,
            access_token,
            advertising_key,
            client_build,
            client_version,
            device_name,
            is_jail_broken,
            locale,
            os_build,
            os_version,
            refresh_token,
            signal,
        )

    async def device_login_17(
        self,
        checksum: str,
        client_date_time: _datetime.datetime,
        device_key: str,
        device_type: _enums.DeviceType,
        language_key: _enums.LanguageKey,
        access_token: str = None,
        advertising_key: str = None,
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
        """Log in with a device and return the user login: user id, credits, trophy, language, icon sprite, alliance membership, stats, and last login date."""
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.device_login_17(
            production_server,
            access_token or "00000000-0000-0000-0000-000000000000",
            advertising_key or "00000000-0000-0000-0000-000000000000",
            checksum,
            client_build or "",
            _utils.datetime.convert_to_pss_timestamp(client_date_time),
            client_version,
            device_key,
            device_name or "",
            str(device_type),
            _utils.convert.to_pss_bool(is_jail_broken or False),
            str(language_key) if language_key else None,
            locale or "",
            os_build or "",
            os_version or "",
            refresh_token,
            _utils.convert.to_pss_bool(signal or False),
        )
        return result

    async def list_all_user_data_first(
        self, access_token: str, user_id: int
    ) -> _Tuple[
        _List[_entities.Achievement],
        _List[_entities.AllianceTask],
        _List[_entities.Battle],
        _List[_entities.CharacterAction],
        _List[_entities.Character],
        _List[_entities.Item],
        _List[_entities.MissionEvent],
        _entities.Research,
        _List[_entities.RoomAction],
        _List[_entities.Room],
        _List[_entities.Situation],
        _List[_entities.StarSystemDetail],
        _List[_entities.StarSystemMarker],
        _List[_entities.Task],
        _List[_entities.UserMarker],
        _List[_entities.UserSkin],
        _List[_entities.UserStarSystem],
    ]:
        """Retrieve a user's full savegame data: research, items, characters, rooms, achievements, tasks, star systems, markers, situations, mission/room actions, and system details."""
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.list_all_user_data_first_2(production_server, access_token, user_id)
        return result

    async def list_friends(self, user_id: int, access_token: str) -> _entities.ListFriends:
        """Retrieve a user's friends list: each friend entry includes id, name, trophy, level, friend type, unread messages, and last interaction dates."""
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.list_friends(production_server, user_id, access_token)
        return result

    async def list_skin_sets(self, client_date_time: _datetime.datetime = None, design_version: int = None) -> _List[_entities.SkinSet]:
        """List all skin sets, the grouped collections of purchasable room skins (e.g. Hangar, Quarters, Cannon) with name, description, requirement and sprite."""
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.list_skin_sets_2(production_server, _utils.datetime.convert_to_pss_timestamp(client_date_time), design_version, self.language_key)
        return result

    async def list_skins(self, client_date_time: _datetime.datetime = None, design_version: int = None) -> _List[_entities.Skin]:
        """List all skins, the cosmetic room skins with interior/exterior/destroyed sprites, name, description and skin set."""
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.list_skins_2(production_server, _utils.datetime.convert_to_pss_timestamp(client_date_time), design_version, self.language_key)
        return result

    async def remove_friend(self, access_token: str, friend_user_id: int) -> None:
        """Remove a user from the friend list."""
        production_server = await self.get_production_server()
        await _UserServiceRaw.remove_friend(production_server, access_token, friend_user_id)

    async def search_users(self, search_string: str) -> _List[_entities.User]:
        """Search users by (partial) name and return matching user profiles: trophy, alliance membership, PvP stats, completed missions and ship design."""
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.search_users(production_server, search_string)
        return result

    async def steam_login(
        self,
        checksum: str,
        client_date_time: _datetime.datetime,
        device_key: str,
        device_type: _enums.DeviceType,
        language_key: _enums.LanguageKey,
        access_token: str = None,
        advertising_key: str = None,
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
        """Log in with a Steam account ticket and return the user login, including access token and user data."""
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.steam_login_8(
            production_server,
            access_token or "00000000-0000-0000-0000-00000000",
            advertising_key or "00000000-0000-0000-0000-00000000",
            checksum,
            client_build,
            _utils.datetime.convert_to_pss_timestamp(client_date_time),
            client_version,
            device_key,
            device_name,
            str(device_type),
            _utils.convert.to_pss_bool(is_jail_broken or False),
            str(language_key),
            str(locale),
            os_build,
            os_version,
            refresh_token,
            _utils.convert.to_pss_bool(signal or False),
            ticket,
        )
        return result

    async def user_email_password_authorize(
        self, access_token: str, checksum: str, client_date_time: _datetime.datetime, device_key: str, email: str, is_web: bool, language_key: str, password: str
    ) -> _entities.UserEmailPasswordAuthorize:
        """
        Authorize a user account (with email and password) on the device with the given device key: this ties the user to the device,
        and subsequent calls to `UserService.device_login` with this device key will return this user.

        Returns the authorized user and a refresh token, or an error message if authorization fails.
        """
        production_server = await self.get_production_server()
        result = await _UserServiceRaw.user_email_password_authorize_4(
            production_server, access_token, checksum, _utils.datetime.convert_to_pss_timestamp(client_date_time), device_key, email, is_web, language_key, password
        )
        return result
