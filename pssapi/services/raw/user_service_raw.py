"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import User as _User


class UserServiceRaw:

    SERVICE_NAME = 'UserService'
    SEARCH_USERS_BASE_PATH: str = 'UserService/SearchUsers'

    @staticmethod
    async def _search_users(production_server: str, search_string: str, **params) -> _List[_User]:
        params = {
            'searchString': search_string,
            **params
        }

        result = await _core.get_entities_from_path(_User, 'Users', production_server, UserServiceRaw.SEARCH_USERS_BASE_PATH, **params)
        return result
