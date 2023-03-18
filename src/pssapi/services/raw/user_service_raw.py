"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import List as _List
from typing import Tuple as _Tuple

from ... import core as _core
from ...entities import AddStarbux as _AddStarbux
from ...entities import Item as _Item
from ...entities import User as _User
from ...entities import UserLogin as _UserLogin

# ---------- Constants ----------

ADD_STARBUX_2_BASE_PATH: str = "UserService/AddStarbux2"
COLLECT_DAILY_REWARD_2_BASE_PATH: str = "UserService/CollectDailyReward2"
DEVICE_LOGIN_12_BASE_PATH: str = "UserService/DeviceLogin12"
DEVICE_LOGIN_15_BASE_PATH: str = "UserService/DeviceLogin15"
PURCHASE_CATALOG_2_BASE_PATH: str = "UserService/PurchaseCatalog2"
SEARCH_USERS_BASE_PATH: str = "UserService/SearchUsers"
STEAM_LOGIN_6_BASE_PATH: str = "UserService/SteamLogin6"


# ---------- Endpoints ----------


async def add_starbux_2(production_server: str, access_token: str, checksum: int, client_date_time: str, quantity: int, **params) -> _Tuple[_AddStarbux, _AddStarbux]:
    params = {"accessToken": access_token, "checksum": checksum, "clientDateTime": client_date_time, "quantity": quantity, **params}
    result = await _core.get_entities_from_path(((_AddStarbux, "AddStarbux", False), (_AddStarbux, "AddStarbux", False)), "None", production_server, ADD_STARBUX_2_BASE_PATH, "POST", **params)
    return result


async def collect_daily_reward_2(production_server: str, access_token: str, argument: int, daily_reward_status: str, **params) -> _List[_Item]:
    params = {"accessToken": access_token, "argument": argument, "dailyRewardStatus": daily_reward_status, **params}
    result = await _core.get_entities_from_path(((_Item, "Items", True),), "Items", production_server, COLLECT_DAILY_REWARD_2_BASE_PATH, "POST", **params)
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
    device_type: int,
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


__DEVICE_LOGIN_12_REQUEST_CONTENT_STRUCTURE: str = '{"AccessToken":"str","AdvertisingKey":"str","Checksum":"str","ClientDateTime":"datetime","DeviceKey":"str","DeviceType":"int","IsJailBroken":"bool","LanguageKey":"str","RefreshToken":"str","Signal":"bool","UserDeviceInfo":{"ClientBuild":"int","ClientVersion":"str","DeviceName":"str","Locale":"str","OSBuild":"int","OsVersion":"str"}}'


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
    device_type: int,
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


__DEVICE_LOGIN_15_REQUEST_CONTENT_STRUCTURE: str = '{"AccessToken":"str","AdvertisingKey":"str","Checksum":"str","ClientDateTime":"datetime","DeviceKey":"str","DeviceType":"int","IsJailBroken":"bool","LanguageKey":"str","RefreshToken":"str","Signal":"bool","UserDeviceInfo":{"ClientBuild":"int","ClientVersion":"str","DeviceName":"str","Locale":"str","OSBuild":"int","OsVersion":"str"}}'


async def purchase_catalog_2(production_server: str, access_token: str, argument: int, checksum: int, client_date_time: str, **params) -> _User:
    params = {"accessToken": access_token, "argument": argument, "checksum": checksum, "clientDateTime": client_date_time, **params}
    result = await _core.get_entities_from_path(((_User, "User", False),), "PurchaseCatalog", production_server, PURCHASE_CATALOG_2_BASE_PATH, "POST", **params)
    return result


async def search_users(production_server: str, search_string: str, **params) -> _List[_User]:
    params = {"searchString": search_string, **params}
    result = await _core.get_entities_from_path(((_User, "Users", True),), "Users", production_server, SEARCH_USERS_BASE_PATH, "GET", **params)
    return result


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
    device_type: int,
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


__STEAM_LOGIN_6_REQUEST_CONTENT_STRUCTURE: str = '{"AccessToken":"str","AdvertisingKey":"str","Checksum":"str","ClientDateTime":"str","DeviceKey":"str","DeviceType":"int","IsJailBroken":"bool","LanguageKey":"str","RefreshToken":"str","Signal":"bool","Ticket":"str","UserDeviceInfo":{"ClientBuild":"int","ClientVersion":"str","DeviceName":"str","Locale":"str","OSBuild":"int","OsVersion":"str"}}'
