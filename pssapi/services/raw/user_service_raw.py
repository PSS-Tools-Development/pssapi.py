####################################################
##   This file has been generated automatically   ##
####################################################

from datetime import datetime as _datetime
from typing import List as _List

from ... import core as _core
from ...entities import ListFriends as _ListFriends
from ...entities import UserLogin as _UserLogin
from ...entities import UserGameCenterAuthorize as _UserGameCenterAuthorize
from ...entities import HeartBeat as _HeartBeat
from ...entities import User as _User



# ---------- Constants ----------

ADD_GAMECENTER_FRIENDS_BASE_PATH: str = 'UserService/AddGamecenterFriends'
AUTHORIZE_FIREBASE_TOKEN_BASE_PATH: str = 'UserService/AuthorizeFirebaseToken'
DEVICE_LOGIN_12_BASE_PATH: str = 'UserService/DeviceLogin12'
HEART_BEAT_4_BASE_PATH: str = 'UserService/HeartBeat4'
LIST_FRIENDS_BASE_PATH: str = 'UserService/ListFriends'
USER_GAME_CENTER_AUTHORIZE_BASE_PATH: str = 'UserService/UserGameCenterAuthorize'


# ---------- Endpoints ----------

async def add_gamecenter_friends(production_server: str, gamecenter_friend_ids: int, access_token: str, **params) -> _List[_User]:
    params = {
        'gamecenterFriendIds': gamecenter_friend_ids,
        'accessToken': access_token,
    }
    result = await _core.get_entities_from_path(_User, 'AddGamecenterFriends', production_server, ADD_GAMECENTER_FRIENDS_BASE_PATH, **params)
    return result


async def authorize_firebase_token(production_server: str, device_key: str, firebase_token: str, access_token: str, **params) -> _List[_User]:
    params = {
        'deviceKey': device_key,
        'firebaseToken': firebase_token,
        'accessToken': access_token,
    }
    result = await _core.get_entities_from_path(_User, 'AuthorizeFirebaseToken', production_server, AUTHORIZE_FIREBASE_TOKEN_BASE_PATH, **params)
    return result


async def device_login_12(production_server: str, , **params) -> _List[_UserLogin]:
    params = {
    }
    result = await _core.get_entities_from_path(_UserLogin, 'UserService', production_server, DEVICE_LOGIN_12_BASE_PATH, **params)
    return result


async def heart_beat_4(production_server: str, checksum: int, access_token: str, client_date_time: _datetime, **params) -> _List[_HeartBeat]:
    params = {
        'checksum': checksum,
        'accessToken': access_token,
        'clientDateTime': client_date_time,
    }
    result = await _core.get_entities_from_path(_HeartBeat, 'UserService', production_server, HEART_BEAT_4_BASE_PATH, **params)
    return result


async def list_friends(production_server: str, user_id: int, access_token: str, **params) -> _List[_ListFriends]:
    params = {
        'UserId': user_id,
        'accessToken': access_token,
    }
    result = await _core.get_entities_from_path(_ListFriends, 'UserService', production_server, LIST_FRIENDS_BASE_PATH, **params)
    return result


async def user_game_center_authorize(production_server: str, game_center_id: str, game_center_name: str, device_key: str, access_token: str, **params) -> _List[_UserGameCenterAuthorize]:
    params = {
        'gameCenterId': game_center_id,
        'gameCenterName': game_center_name,
        'deviceKey': device_key,
        'accessToken': access_token,
    }
    result = await _core.get_entities_from_path(_UserGameCenterAuthorize, 'None', production_server, USER_GAME_CENTER_AUTHORIZE_BASE_PATH, **params)
    return result


