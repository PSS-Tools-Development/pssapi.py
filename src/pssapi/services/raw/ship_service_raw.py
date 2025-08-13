"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from typing import List, Tuple

from ... import core
from ...entities import Ship, ShipDesign, User


# ---------- Constants ----------

GET_SHIP_BY_USER_ID_BASE_PATH: str = "ShipService/GetShipByUserId"
INSPECT_SHIP_2_BASE_PATH: str = "ShipService/InspectShip2"
LIST_ALL_SHIP_DESIGNS_2_BASE_PATH: str = "ShipService/ListAllShipDesigns2"

# ---------- Endpoint structure ----------


# ---------- Endpoints ----------


async def get_ship_by_user_id(production_server: str, access_token: str, client_date_time: str, user_id: int, **params) -> Ship:
    params = {"accessToken": access_token, "clientDateTime": client_date_time, "userId": user_id, **params}
    result = await core.get_entities_from_path(((Ship, "Ship", False),), "GetShipByUserId", production_server, GET_SHIP_BY_USER_ID_BASE_PATH, "GET", response_gzipped=False, **params)
    return result


async def inspect_ship_2(production_server: str, access_token: str, user_id: int, **params) -> Tuple[Ship, User]:
    params = {"accessToken": access_token, "userId": user_id, **params}
    result = await core.get_entities_from_path(((Ship, "Ship", False), (User, "User", False)), "InspectShip", production_server, INSPECT_SHIP_2_BASE_PATH, "GET", response_gzipped=False, **params)
    return result


async def list_all_ship_designs_2(production_server: str, client_date_time: str, design_version: int, language_key: str, **params) -> List[ShipDesign]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, "languageKey": language_key, **params}
    result = await core.get_entities_from_path(((ShipDesign, "ShipDesigns", True),), "ShipDesigns", production_server, LIST_ALL_SHIP_DESIGNS_2_BASE_PATH, "GET", response_gzipped=False, **params)
    return result
