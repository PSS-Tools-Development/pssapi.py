"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import User as _User
from ...entities import UserLogin as _UserLogin

# ---------- Constants ----------

DEVICE_LOGIN_12_BASE_PATH: str = 'UserService/DeviceLogin12'
SEARCH_USERS_BASE_PATH: str = 'UserService/SearchUsers'
STEAM_LOGIN_6_BASE_PATH: str = 'UserService/SteamLogin6'


# ---------- Endpoints ----------

async def device_login_12(production_server: str, **params) -> _List[_UserLogin]:
    params = {
        **params
    }
    result = await _core.get_entities_from_path(_UserLogin, 'UserService', production_server, DEVICE_LOGIN_12_BASE_PATH, **params)
    return result


async def search_users(production_server: str, search_string: str, **params) -> _List[_User]:
    params = {
        'searchString': search_string,
        **params
    }
    result = await _core.get_entities_from_path(_User, 'Users', production_server, SEARCH_USERS_BASE_PATH, **params)
    return result


async def steam_login_6(production_server: str, **params) -> _List[_UserLogin]:
    params = {
        **params
    }
    result = await _core.get_entities_from_path(_UserLogin, 'UserService', production_server, STEAM_LOGIN_6_BASE_PATH, **params)
    return result
