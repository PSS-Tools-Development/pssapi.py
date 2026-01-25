"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from datetime import datetime as _datetime
from typing import List as _List
from typing import Tuple as _Tuple

from ... import core as _core
from ...entities import Achievement as _Achievement
from ...entities import AllianceTask as _AllianceTask
from ...entities import Battle as _Battle
from ...entities import Character as _Character
from ...entities import CharacterAction as _CharacterAction
from ...entities import Friend as _Friend
from ...entities import Item as _Item
from ...entities import ListFriends as _ListFriends
from ...entities import MissionEvent as _MissionEvent
from ...entities import Research as _Research
from ...entities import Room as _Room
from ...entities import RoomAction as _RoomAction
from ...entities import Situation as _Situation
from ...entities import Skin as _Skin
from ...entities import SkinSet as _SkinSet
from ...entities import StarSystemDetail as _StarSystemDetail
from ...entities import StarSystemMarker as _StarSystemMarker
from ...entities import Task as _Task
from ...entities import User as _User
from ...entities import UserEmailPasswordAuthorize as _UserEmailPasswordAuthorize
from ...entities import UserLogin as _UserLogin
from ...entities import UserMarker as _UserMarker
from ...entities import UserSkin as _UserSkin
from ...entities import UserStarSystem as _UserStarSystem


# ---------- Constants ----------

ACCEPT_FRIEND_REQUEST_BASE_PATH: str = "UserService/AcceptFriendRequest"
ADD_FRIEND_2_BASE_PATH: str = "UserService/AddFriend2"
DECLINE_FRIEND_REQUEST_BASE_PATH: str = "UserService/DeclineFriendRequest"
DEVICE_LOGIN_11_BASE_PATH: str = "UserService/DeviceLogin11"
DEVICE_LOGIN_12_BASE_PATH: str = "UserService/DeviceLogin12"
DEVICE_LOGIN_15_BASE_PATH: str = "UserService/DeviceLogin15"
LIST_ALL_USER_DATA_FIRST_2_BASE_PATH: str = "UserService/ListAllUserDataFirst2"
LIST_FRIENDS_BASE_PATH: str = "UserService/ListFriends"
LIST_SKIN_SETS_2_BASE_PATH: str = "UserService/ListSkinSets2"
LIST_SKINS_BASE_PATH: str = "UserService/ListSkins"
LIST_SKINS_2_BASE_PATH: str = "UserService/ListSkins2"
REDEEM_CODE_BASE_PATH: str = "UserService/RedeemCode"
REMOVE_FRIEND_BASE_PATH: str = "UserService/RemoveFriend"
SEARCH_USERS_BASE_PATH: str = "UserService/SearchUsers"
SET_TIP_STATUS_BASE_PATH: str = "UserService/SetTipStatus"
SET_TUTORIAL_STATUS_BASE_PATH: str = "UserService/SetTutorialStatus"
STEAM_LOGIN_3_BASE_PATH: str = "UserService/SteamLogin3"
STEAM_LOGIN_6_BASE_PATH: str = "UserService/SteamLogin6"
STEAM_LOGIN_8_BASE_PATH: str = "UserService/SteamLogin8"
USER_EMAIL_PASSWORD_AUTHORIZE_2_BASE_PATH: str = "UserService/UserEmailPasswordAuthorize2"
USER_EMAIL_PASSWORD_AUTHORIZE_4_BASE_PATH: str = "UserService/UserEmailPasswordAuthorize4"


# ---------- Endpoints ----------


async def accept_friend_request(production_server: str, access_token: str, friend_user_id: int, **params) -> _Friend:
    params = {"accessToken": access_token, "friendUserId": friend_user_id, **params}
    result = await _core.get_entities_from_path(((_Friend, "Friend", False),), "AcceptFriendRequest", production_server, ACCEPT_FRIEND_REQUEST_BASE_PATH, "POST", response_gzipped=False, **params)
    return result


async def add_friend_2(production_server: str, access_token: str, friend_user_id: int, **params) -> _Friend:
    params = {"accessToken": access_token, "friendUserId": friend_user_id, **params}
    result = await _core.get_entities_from_path(((_Friend, "Friend", False),), "AddFriend", production_server, ADD_FRIEND_2_BASE_PATH, "POST", response_gzipped=False, **params)
    return result


async def decline_friend_request(production_server: str, access_token: str, friend_user_id: int, **params) -> _Friend:
    params = {"accessToken": access_token, "friendUserId": friend_user_id, **params}
    result = await _core.get_entities_from_path(((_Friend, "Friend", False),), "DeclineFriendRequest", production_server, DECLINE_FRIEND_REQUEST_BASE_PATH, "POST", response_gzipped=False, **params)
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
        "advertisingKey": advertising_key,
        "checksum": checksum,
        "clientDateTime": client_date_time,
        "device_key": device_key,
        "device_type": device_type,
        "is_jail_broken": is_jail_broken,
        "language_key": language_key,
        "refresh_token": refresh_token,
        "signal": signal,
        **params,
    }
    result = await _core.get_entities_from_path(((_UserLogin, "UserLogin", False),), "UserService", production_server, DEVICE_LOGIN_11_BASE_PATH, "POST", response_gzipped=False, **params)
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
    result = await _core.get_entities_from_path(
        ((_UserLogin, "UserLogin", False),), "UserService", production_server, DEVICE_LOGIN_12_BASE_PATH, "POST", request_content=content, response_gzipped=False, **params
    )
    return result


__DEVICE_LOGIN_12_REQUEST_CONTENT_STRUCTURE: str = (
    '{"AccessToken":"str","AdvertisingKey":"str","Checksum":"str","ClientDateTime":"datetime","DeviceKey":"str","DeviceType":"str","IsJailBroken":"bool","LanguageKey":"str","RefreshToken":"str","Signal":"bool","UserDeviceInfo":{"ClientBuild":"int","ClientVersion":"str","DeviceName":"str","Locale":"str","OSBuild":"int","OsVersion":"str"}}'
)


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
    result = await _core.get_entities_from_path(
        ((_UserLogin, "UserLogin", False),), "UserService", production_server, DEVICE_LOGIN_15_BASE_PATH, "POST", request_content=content, response_gzipped=False, **params
    )
    return result


__DEVICE_LOGIN_15_REQUEST_CONTENT_STRUCTURE: str = (
    '{"AccessToken":"str","AdvertisingKey":"str","Checksum":"str","ClientDateTime":"datetime","DeviceKey":"str","DeviceType":"str","IsJailBroken":"bool","LanguageKey":"str","RefreshToken":"str","Signal":"bool","UserDeviceInfo":{"ClientBuild":"int","ClientVersion":"str","DeviceName":"str","Locale":"str","OSBuild":"int","OsVersion":"str"}}'
)


async def list_all_user_data_first_2(production_server: str, access_token: str, user_id: int, **params) -> _Tuple[
    _List[_Achievement],
    _List[_AllianceTask],
    _List[_Battle],
    _List[_CharacterAction],
    _List[_Character],
    _List[_Item],
    _List[_MissionEvent],
    _Research,
    _List[_RoomAction],
    _List[_Room],
    _List[_Situation],
    _List[_StarSystemDetail],
    _List[_StarSystemMarker],
    _List[_Task],
    _List[_UserMarker],
    _List[_UserSkin],
    _List[_UserStarSystem],
]:
    params = {"accessToken": access_token, "userId": user_id, **params}
    result = await _core.get_entities_from_path(
        (
            (_Achievement, "Achievements", True),
            (_AllianceTask, "AllianceTasks", True),
            (_Battle, "Battles", True),
            (_CharacterAction, "CharacterActions", True),
            (_Character, "Characters", True),
            (_Item, "Items", True),
            (_MissionEvent, "MissionEvents", True),
            (_Research, "Research", False),
            (_RoomAction, "RoomActions", True),
            (_Room, "Rooms", True),
            (_Situation, "Situations", True),
            (_StarSystemDetail, "StarSystemDetails", True),
            (_StarSystemMarker, "StarSystemMarkers", True),
            (_Task, "Tasks", True),
            (_UserMarker, "UserMarkers", True),
            (_UserSkin, "UserSkins", True),
            (_UserStarSystem, "UserStarSystems", True),
        ),
        "ListAllUserDataFirst",
        production_server,
        LIST_ALL_USER_DATA_FIRST_2_BASE_PATH,
        "GET",
        response_gzipped=False,
        **params,
    )
    return result


async def list_friends(production_server: str, user_id: int, access_token: str, **params) -> _ListFriends:
    params = {"UserId": user_id, "accessToken": access_token, **params}
    result = await _core.get_entities_from_path(((_ListFriends, "ListFriends", False),), "UserService", production_server, LIST_FRIENDS_BASE_PATH, "GET", response_gzipped=False, **params)
    return result


async def list_skin_sets_2(production_server: str, client_date_time: str, design_version: int, language_key: str, **params) -> _List[_SkinSet]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_SkinSet, "SkinSets", True),), "SkinSets", production_server, LIST_SKIN_SETS_2_BASE_PATH, "GET", response_gzipped=False, **params)
    return result


async def list_skins(production_server: str, client_date_time: str, design_version: int, language_key: str, **params) -> _Tuple[_List[_SkinSet], _List[_Skin]]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_SkinSet, "SkinSets", True), (_Skin, "Skins", True)), "ListSkins", production_server, LIST_SKINS_BASE_PATH, "GET", response_gzipped=False, **params)
    return result


async def list_skins_2(production_server: str, client_date_time: str, design_version: int, language_key: str, **params) -> _List[_Skin]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_Skin, "Skins", True),), "Skins", production_server, LIST_SKINS_2_BASE_PATH, "GET", response_gzipped=False, **params)
    return result


async def redeem_code(production_server: str, access_token: str, checksum: str, client_date_time: str, code: str, **params) -> None:
    params = {"accessToken": access_token, "checksum": checksum, "clientDateTime": client_date_time, "code": code, **params}
    await _core.get_entities_from_path((), None, production_server, REDEEM_CODE_BASE_PATH, "POST", response_gzipped=False, **params)


async def remove_friend(production_server: str, access_token: str, friend_user_id: int, **params) -> None:
    params = {"accessToken": access_token, "friendUserId": friend_user_id, **params}
    await _core.get_entities_from_path((), None, production_server, REMOVE_FRIEND_BASE_PATH, "POST", response_gzipped=False, **params)


async def search_users(production_server: str, search_string: str, **params) -> _List[_User]:
    params = {"searchString": search_string, **params}
    result = await _core.get_entities_from_path(((_User, "Users", True),), "Users", production_server, SEARCH_USERS_BASE_PATH, "GET", response_gzipped=False, **params)
    return result


async def set_tip_status(production_server: str, access_token: str, tip_status: int, **params) -> _User:
    params = {"accessToken": access_token, "tipStatus": tip_status, **params}
    result = await _core.get_entities_from_path(((_User, "User", False),), "SetTipStatus", production_server, SET_TIP_STATUS_BASE_PATH, "POST", response_gzipped=False, **params)
    return result


async def set_tutorial_status(production_server: str, access_token: str, tutorial_status: int, **params) -> _User:
    params = {"accessToken": access_token, "tutorialStatus": tutorial_status, **params}
    result = await _core.get_entities_from_path(((_User, "User", False),), "SetTutorialStatus", production_server, SET_TUTORIAL_STATUS_BASE_PATH, "POST", response_gzipped=False, **params)
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
    result = await _core.get_entities_from_path(
        ((_UserLogin, "UserLogin", False),), "UserService", production_server, STEAM_LOGIN_3_BASE_PATH, "POST", request_content=content, response_gzipped=False, **params
    )
    return result


__STEAM_LOGIN_3_REQUEST_CONTENT_STRUCTURE: str = (
    '{"AccessToken":"str","AdvertisingKey":null,"Checksum":"str","ClientDateTime":"str","DeviceKey":"str","DeviceType":"str","IsJailBroken":"bool","LanguageKey":"str","RefreshToken":"str","Signal":"bool","Ticket":"str","UserDeviceInfo":{"ClientBuild":"int","ClientVersion":"str","DeviceName":"str","Locale":"str","OSBuild":"int","OsVersion":"str"}}'
)


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
    result = await _core.get_entities_from_path(
        ((_UserLogin, "UserLogin", False),), "UserService", production_server, STEAM_LOGIN_6_BASE_PATH, "POST", request_content=content, response_gzipped=False, **params
    )
    return result


__STEAM_LOGIN_6_REQUEST_CONTENT_STRUCTURE: str = (
    '{"AccessToken":"str","AdvertisingKey":null,"Checksum":"str","ClientDateTime":"str","DeviceKey":"str","DeviceType":"str","IsJailBroken":"bool","LanguageKey":"str","RefreshToken":"str","Signal":"bool","Ticket":"str","UserDeviceInfo":{"ClientBuild":"int","ClientVersion":"str","DeviceName":"str","Locale":"str","OSBuild":"int","OsVersion":"str"}}'
)


async def steam_login_8(
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
    content = _core.create_request_content(__STEAM_LOGIN_8_REQUEST_CONTENT_STRUCTURE, params, "json")
    result = await _core.get_entities_from_path(
        ((_UserLogin, "UserLogin", False),), "UserService", production_server, STEAM_LOGIN_8_BASE_PATH, "POST", request_content=content, response_gzipped=False, **params
    )
    return result


__STEAM_LOGIN_8_REQUEST_CONTENT_STRUCTURE: str = (
    '{"AccessToken":"str","AdvertisingKey":null,"Checksum":"str","ClientDateTime":"str","DeviceKey":"str","DeviceType":"int","IsJailBroken":"bool","LanguageKey":"str","RefreshToken":"str","Signal":"bool","Ticket":"str","UserDeviceInfo":{"ClientBuild":"int","ClientVersion":"str","DeviceName":"str","Locale":"str","OSBuild":"int","OsVersion":"str"}}'
)


async def user_email_password_authorize_2(
    production_server: str, access_token: str, checksum: str, client_date_time: str, device_key: str, email: str, password: str, **params
) -> _UserEmailPasswordAuthorize:
    params = {"accessToken": access_token, "checksum": checksum, "clientDateTime": client_date_time, "deviceKey": device_key, "email": email, "password": password, **params}
    result = await _core.get_entities_from_path(
        ((_UserEmailPasswordAuthorize, "UserEmailPasswordAuthorize", False),), "UserService", production_server, USER_EMAIL_PASSWORD_AUTHORIZE_2_BASE_PATH, "POST", response_gzipped=False, **params
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
        ((_UserEmailPasswordAuthorize, "UserEmailPasswordAuthorize", False),), "UserService", production_server, USER_EMAIL_PASSWORD_AUTHORIZE_4_BASE_PATH, "POST", response_gzipped=False, **params
    )
    return result
