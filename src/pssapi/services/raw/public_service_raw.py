"""
    This file has been generated automatically.
    Any changes to this file will be lost eventually.
"""

from ... import core as _core
from ...entities import Ship as _Ship

# ---------- Constants ----------

GET_SHIP_DETAILS_BASE_PATH: str = "PublicService/GetShipDetails"
GET_SHIP_ROOM_DETAILS_BASE_PATH: str = "PublicService/GetShipRoomDetails"


# ---------- Endpoints ----------


async def get_ship_details(production_server: str, access_token: str, user_id: int, **params) -> _Ship:
    params = {"accessToken": access_token, "userId": user_id, **params}
    result = await _core.get_entities_from_path(((_Ship, "Ship", False),), "GetShipDetails", production_server, GET_SHIP_DETAILS_BASE_PATH, "GET", response_gzipped=False, **params)
    return result


async def get_ship_room_details(production_server: str, access_token: str, user_id: int, **params) -> _Ship:
    params = {"accessToken": access_token, "userId": user_id, **params}
    result = await _core.get_entities_from_path(((_Ship, "Ship", False),), "GetShipRoomDetails", production_server, GET_SHIP_ROOM_DETAILS_BASE_PATH, "GET", response_gzipped=False, **params)
    return result
