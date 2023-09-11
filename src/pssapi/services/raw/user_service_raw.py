"""
    This file has been generated automatically.
    Any changes to this file will be lost eventually.
"""

from datetime import datetime as _datetime
from typing import List as _List
from typing import Tuple as _Tuple

from ... import core as _core
from ...entities import Friend as _Friend
from ...entities import ListFriends as _ListFriends
from ...entities import Skin as _Skin
from ...entities import SkinSet as _SkinSet
from ...entities import User as _User
from ...entities import UserEmailPasswordAuthorize as _UserEmailPasswordAuthorize
from ...entities import UserLogin as _UserLogin

# ---------- Constants ----------

ACCEPT_FRIEND_REQUEST_BASE_PATH: str = "UserService/AcceptFriendRequest"
ADD_FRIEND_2_BASE_PATH: str = "UserService/AddFriend2"
DECLINE_FRIEND_REQUEST_BASE_PATH: str = "UserService/DeclineFriendRequest"
DEVICE_LOGIN_11_BASE_PATH: str = "UserService/DeviceLogin11"
DEVICE_LOGIN_12_BASE_PATH: str = "UserService/DeviceLogin12"
DEVICE_LOGIN_15_BASE_PATH: str = "UserService/DeviceLogin15"
LIST_FRIENDS_BASE_PATH: str = "UserService/ListFriends"
LIST_SKINS_BASE_PATH: str = "UserService/ListSkins"
REMOVE_FRIEND_BASE_PATH: str = "UserService/RemoveFriend"
SEARCH_USERS_BASE_PATH: str = "UserService/SearchUsers"
STEAM_LOGIN_3_BASE_PATH: str = "UserService/SteamLogin3"
STEAM_LOGIN_6_BASE_PATH: str = "UserService/SteamLogin6"
USER_EMAIL_PASSWORD_AUTHORIZE_2_BASE_PATH: str = "UserService/UserEmailPasswordAuthorize2"
USER_EMAIL_PASSWORD_AUTHORIZE_4_BASE_PATH: str = "UserService/UserEmailPasswordAuthorize4"


# ---------- Endpoints ----------


async def accept_friend_request(production_server: str, access_token: str, friend_user_id: int, **params) -> _Friend:
    params = {"accessToken": access_token, "friendUserId": friend_user_id, **params}
    result = await _core.get_entities_from_path(((_Friend, "Friend", False),), "AcceptFriendRequest", production_server, ACCEPT_FRIEND_REQUEST_BASE_PATH, "POST", **params)
    return result


async def add_friend_2(production_server: str, access_token: str, friend_user_id: int, **params) -> _Friend:
    params = {"accessToken": access_token, "friendUserId": friend_user_id, **params}
    result = await _core.get_entities_from_path(((_Friend, "Friend", False),), "AddFriend", production_server, ADD_FRIEND_2_BASE_PATH, "POST", **params)
    return result


async def decline_friend_request(production_server: str, access_token: str, friend_user_id: int, **params) -> _Friend:
    params = {"accessToken": access_token, "friendUserId": friend_user_id, **params}
    result = await _core.get_entities_from_path(((_Friend, "Friend", False),), "DeclineFriendRequest", production_server, DECLINE_FRIEND_REQUEST_BASE_PATH, "POST", **params)
    return result


async def device_login_11(
    production_server: str,
    advertising_key: str,
    checksum: str,
    client_date_time: _datetime,
    device_key: str,
    device_type: str,
    is_jail_broken: bool,
    language_key: str,
    refresh_token: str,
    signal: bool,
    **params,
) -> _UserLogin:
    params = {
        "AdvertisingKey": advertising_key,
        "Checksum": checksum,
        "ClientDateTime": client_date_time,
        "DeviceKey": device_key,
        "DeviceType": device_type,
        "IsJailBroken": is_jail_broken,
        "LanguageKey": language_key,
        "RefreshToken": refresh_token,
        "Signal": signal,
        **params,
    }
    result = await _core.get_entities_from_path(((_UserLogin, "UserLogin", False),), "UserService", production_server, DEVICE_LOGIN_11_BASE_PATH, "POST", **params)
    return result


async def device_login_12(
    production_server: str,
    access_token: str,
    advertising_key: str,
    checksum: str,
    client_build: int,
    client_date_time: _datetime,
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
    **params,
) -> _UserLogin:
    params = {
        "AccessToken": access_token,
        "AdvertisingKey": advertising_key,
        "Checksum": checksum,
        "ClientBuild": client_build,
        "ClientDateTime": client_date_time,
        "ClientVersion": client_version,
        "DeviceKey": device_key,
        "DeviceName": device_name,
        "DeviceType": device_type,
        "IsJailBroken": is_jail_broken,
        "LanguageKey": language_key,
        "Locale": locale,
        "OSBuild": os_build,
        "OsVersion": os_version,
        "RefreshToken": refresh_token,
        "Signal": signal,
        **params,
    }
    content = _core.create_request_content(__DEVICE_LOGIN_12_REQUEST_CONTENT_STRUCTURE, params, "json")
    result = await _core.get_entities_from_path(((_UserLogin, "UserLogin", False),), "UserService", production_server, DEVICE_LOGIN_12_BASE_PATH, "POST", request_content=content, **params)
    return result


__DEVICE_LOGIN_12_REQUEST_CONTENT_STRUCTURE: str = '{"AccessToken":"str","AdvertisingKey":"str","Checksum":"str","ClientDateTime":"datetime","DeviceKey":"str","DeviceType":"str","IsJailBroken":"bool","LanguageKey":"str","RefreshToken":"str","Signal":"bool","UserDeviceInfo":{"ClientBuild":"int","ClientVersion":"str","DeviceName":"str","Locale":"str","OSBuild":"int","OsVersion":"str"}}'


async def device_login_15(
    production_server: str,
    access_token: str,
    advertising_key: str,
    checksum: str,
    client_build: int,
    client_date_time: _datetime,
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
    **params,
) -> _UserLogin:
    params = {
        "AccessToken": access_token,
        "AdvertisingKey": advertising_key,
        "Checksum": checksum,
        "ClientBuild": client_build,
        "ClientDateTime": client_date_time,
        "ClientVersion": client_version,
        "DeviceKey": device_key,
        "DeviceName": device_name,
        "DeviceType": device_type,
        "IsJailBroken": is_jail_broken,
        "LanguageKey": language_key,
        "Locale": locale,
        "OSBuild": os_build,
        "OsVersion": os_version,
        "RefreshToken": refresh_token,
        "Signal": signal,
        **params,
    }
    content = _core.create_request_content(__DEVICE_LOGIN_15_REQUEST_CONTENT_STRUCTURE, params, "json")
    result = await _core.get_entities_from_path(((_UserLogin, "UserLogin", False),), "UserService", production_server, DEVICE_LOGIN_15_BASE_PATH, "POST", request_content=content, **params)
    return result


__DEVICE_LOGIN_15_REQUEST_CONTENT_STRUCTURE: str = '{"AccessToken":"str","AdvertisingKey":"str","Checksum":"str","ClientDateTime":"datetime","DeviceKey":"str","DeviceType":"str","IsJailBroken":"bool","LanguageKey":"str","RefreshToken":"str","Signal":"bool","UserDeviceInfo":{"ClientBuild":"int","ClientVersion":"str","DeviceName":"str","Locale":"str","OSBuild":"int","OsVersion":"str"}}'


async def list_friends(production_server: str, user_id: int, access_token: str, **params) -> _ListFriends:
    params = {"UserId": user_id, "accessToken": access_token, **params}
    result = await _core.get_entities_from_path(((_ListFriends, "ListFriends", False),), "UserService", production_server, LIST_FRIENDS_BASE_PATH, "GET", **params)
    return result


async def list_skins(production_server: str, design_version: int, language_key: str, **params) -> _Tuple[_List[_SkinSet], _List[_Skin]]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_SkinSet, "SkinSets", True), (_Skin, "Skins", True)), "ListSkins", production_server, LIST_SKINS_BASE_PATH, "GET", **params)
    return result


async def remove_friend(production_server: str, access_token: str, friend_user_id: int, **params) -> None:
    params = {"accessToken": access_token, "friendUserId": friend_user_id, **params}
    await _core.get_entities_from_path((), None, production_server, REMOVE_FRIEND_BASE_PATH, "POST", **params)


async def search_users(production_server: str, search_string: str, **params) -> _List[_User]:
    params = {"searchString": search_string, **params}
    result = await _core.get_entities_from_path(((_User, "Users", True),), "Users", production_server, SEARCH_USERS_BASE_PATH, "GET", **params)
    return result


async def steam_login_3(
    production_server: str,
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
    **params,
) -> _UserLogin:
    params = {
        "AccessToken": access_token,
        "AdvertisingKey": advertising_key,
        "Checksum": checksum,
        "ClientBuild": client_build,
        "ClientDateTime": client_date_time,
        "ClientVersion": client_version,
        "DeviceKey": device_key,
        "DeviceName": device_name,
        "DeviceType": device_type,
        "IsJailBroken": is_jail_broken,
        "LanguageKey": language_key,
        "Locale": locale,
        "OSBuild": os_build,
        "OsVersion": os_version,
        "RefreshToken": refresh_token,
        "Signal": signal,
        "Ticket": ticket,
        **params,
    }
    content = _core.create_request_content(__STEAM_LOGIN_3_REQUEST_CONTENT_STRUCTURE, params, "json")
    result = await _core.get_entities_from_path(((_UserLogin, "UserLogin", False),), "UserService", production_server, STEAM_LOGIN_3_BASE_PATH, "POST", request_content=content, **params)
    return result


__STEAM_LOGIN_3_REQUEST_CONTENT_STRUCTURE: str = '{"AccessToken":"str","AdvertisingKey":null,"Checksum":"str","ClientDateTime":"str","DeviceKey":"str","DeviceType":"str","IsJailBroken":"bool","LanguageKey":"str","RefreshToken":"str","Signal":"bool","Ticket":"str","UserDeviceInfo":{"ClientBuild":"int","ClientVersion":"str","DeviceName":"str","Locale":"str","OSBuild":"int","OsVersion":"str"}}'


async def steam_login_6(
    production_server: str,
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
    **params,
) -> _UserLogin:
    params = {
        "AccessToken": access_token,
        "AdvertisingKey": advertising_key,
        "Checksum": checksum,
        "ClientBuild": client_build,
        "ClientDateTime": client_date_time,
        "ClientVersion": client_version,
        "DeviceKey": device_key,
        "DeviceName": device_name,
        "DeviceType": device_type,
        "IsJailBroken": is_jail_broken,
        "LanguageKey": language_key,
        "Locale": locale,
        "OSBuild": os_build,
        "OsVersion": os_version,
        "RefreshToken": refresh_token,
        "Signal": signal,
        "Ticket": ticket,
        **params,
    }
    content = _core.create_request_content(__STEAM_LOGIN_6_REQUEST_CONTENT_STRUCTURE, params, "json")
    result = await _core.get_entities_from_path(((_UserLogin, "UserLogin", False),), "UserService", production_server, STEAM_LOGIN_6_BASE_PATH, "POST", request_content=content, **params)
    return result


__STEAM_LOGIN_6_REQUEST_CONTENT_STRUCTURE: str = '{"AccessToken":"str","AdvertisingKey":null,"Checksum":"str","ClientDateTime":"str","DeviceKey":"str","DeviceType":"str","IsJailBroken":"bool","LanguageKey":"str","RefreshToken":"str","Signal":"bool","Ticket":"str","UserDeviceInfo":{"ClientBuild":"int","ClientVersion":"str","DeviceName":"str","Locale":"str","OSBuild":"int","OsVersion":"str"}}'


async def user_email_password_authorize_2(
    production_server: str, access_token: str, checksum: str, client_date_time: str, device_key: str, email: str, password: str, **params
) -> _UserEmailPasswordAuthorize:
    params = {"accessToken": access_token, "checksum": checksum, "clientDateTime": client_date_time, "deviceKey": device_key, "email": email, "password": password, **params}
    result = await _core.get_entities_from_path(
        ((_UserEmailPasswordAuthorize, "UserEmailPasswordAuthorize", False),), "UserService", production_server, USER_EMAIL_PASSWORD_AUTHORIZE_2_BASE_PATH, "POST", **params
    )
    return result


async def user_email_password_authorize_4(
    production_server: str, access_token: str, checksum: str, client_date_time: str, device_key: str, email: str, is_web: bool, language_key: str, password: str, **params
) -> _UserEmailPasswordAuthorize:
    params = {
        "accessToken": access_token,
        "checksum": checksum,
        "clientDateTime": client_date_time,
        "deviceKey": device_key,
        "email": email,
        "isWeb": is_web,
        "languageKey": language_key,
        "password": password,
        **params,
    }
    result = await _core.get_entities_from_path(
        ((_UserEmailPasswordAuthorize, "UserEmailPasswordAuthorize", False),), "UserService", production_server, USER_EMAIL_PASSWORD_AUTHORIZE_4_BASE_PATH, "POST", **params
    )
    return result
