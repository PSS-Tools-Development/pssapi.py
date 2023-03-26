"""
    This file has been generated automatically
"""

from typing import List as _List
from typing import Tuple as _Tuple

from ... import core as _core
from ...entities import Ship as _Ship
from ...entities import ShipDesign as _ShipDesign
from ...entities import User as _User

# ---------- Constants ----------

GET_SHIP_BY_USER_ID_BASE_PATH: str = "ShipService/GetShipByUserId"
INSPECT_SHIP_2_BASE_PATH: str = "ShipService/InspectShip2"
LIST_ALL_SHIP_DESIGNS_2_BASE_PATH: str = "ShipService/ListAllShipDesigns2"


# ---------- Endpoints ----------


async def get_ship_by_user_id(production_server: str, access_token: str, client_date_time: str, user_id: int, **params) -> _Ship:
    params = {"accessToken": access_token, "clientDateTime": client_date_time, "userId": user_id, **params}
    result = await _core.get_entities_from_path(((_Ship, "Ship", False),), "GetShipByUserId", production_server, GET_SHIP_BY_USER_ID_BASE_PATH, "GET", **params)
    return result


async def inspect_ship_2(production_server: str, access_token: str, user_id: int, **params) -> _Tuple[_Ship, _User]:
    params = {"accessToken": access_token, "userId": user_id, **params}
    result = await _core.get_entities_from_path(((_Ship, "Ship", False), (_User, "User", False)), "InspectShip", production_server, INSPECT_SHIP_2_BASE_PATH, "GET", **params)
    return result


async def list_all_ship_designs_2(production_server: str, design_version: int, language_key: str, **params) -> _List[_ShipDesign]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_ShipDesign, "ShipDesigns", True),), "ShipDesigns", production_server, LIST_ALL_SHIP_DESIGNS_2_BASE_PATH, "GET", **params)
    return result
