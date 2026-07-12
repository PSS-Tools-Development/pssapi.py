"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from typing import List as _List

from ... import core as _core
from ...entities import Character as _Character
from ...entities import Ship as _Ship


# ---------- Constants ----------

GET_SHIP_CHARACTERS_BY_USERNAME_BASE_PATH: str = "PublicService/GetShipCharactersByUsername"
GET_SHIP_DETAILS_BASE_PATH: str = "PublicService/GetShipDetails"
GET_SHIP_ROOM_DETAILS_BASE_PATH: str = "PublicService/GetShipRoomDetails"


# ---------- Endpoints ----------


async def get_ship_characters_by_username(production_server: str, access_token: str, username: str, **params) -> _List[_Character]:
    params = {"accessToken": access_token, "username": username, **params}
    result = await _core.get_entities_from_path(
        ((_Character, "Characters", True),), "Characters", production_server, GET_SHIP_CHARACTERS_BY_USERNAME_BASE_PATH, "GET", response_gzipped=False, **params
    )
    return result


async def get_ship_details(production_server: str, access_token: str, user_id: int, **params) -> _Ship:
    params = {"accessToken": access_token, "userId": user_id, **params}
    result = await _core.get_entities_from_path(((_Ship, "Ship", False),), "GetShipDetails", production_server, GET_SHIP_DETAILS_BASE_PATH, "GET", response_gzipped=False, **params)
    return result


async def get_ship_room_details(production_server: str, access_token: str, user_id: int, **params) -> _Ship:
    params = {"accessToken": access_token, "userId": user_id, **params}
    result = await _core.get_entities_from_path(((_Ship, "Ship", False),), "GetShipRoomDetails", production_server, GET_SHIP_ROOM_DETAILS_BASE_PATH, "GET", response_gzipped=False, **params)
    return result
