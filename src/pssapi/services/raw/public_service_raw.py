"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from ... import core
from ...entities import Ship


# ---------- Constants ----------

GET_SHIP_DETAILS_BASE_PATH: str = "PublicService/GetShipDetails"
GET_SHIP_ROOM_DETAILS_BASE_PATH: str = "PublicService/GetShipRoomDetails"

# ---------- Endpoint structure ----------


# ---------- Endpoints ----------


async def get_ship_details(production_server: str, access_token: str, user_id: int, **params) -> Ship:
    params = {"accessToken": access_token, "userId": user_id, **params}
    result = await core.get_entities_from_path(((Ship, "Ship", False),), "GetShipDetails", production_server, GET_SHIP_DETAILS_BASE_PATH, "GET", response_gzipped=False, **params)
    return result


async def get_ship_room_details(production_server: str, access_token: str, user_id: int, **params) -> Ship:
    params = {"accessToken": access_token, "userId": user_id, **params}
    result = await core.get_entities_from_path(((Ship, "Ship", False),), "GetShipRoomDetails", production_server, GET_SHIP_ROOM_DETAILS_BASE_PATH, "GET", response_gzipped=False, **params)
    return result
