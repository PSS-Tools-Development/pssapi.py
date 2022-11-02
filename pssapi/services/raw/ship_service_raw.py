"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import ShipDesign as _ShipDesign
from ...entities import User as _User

# ---------- Constants ----------

INSPECT_SHIP_2_BASE_PATH: str = 'ShipService/InspectShip2'
LIST_ALL_SHIP_DESIGNS_2_BASE_PATH: str = 'ShipService/ListAllShipDesigns2'


# ---------- Endpoints ----------

async def inspect_ship_2(production_server: str, user_id: int, access_token: str, **params) -> _List[_User]:
    params = {
        'userId': user_id,
        'accessToken': access_token,
        **params
    }
    result = await _core.get_entities_from_path(_User, 'InspectShip', production_server, INSPECT_SHIP_2_BASE_PATH, **params)
    return result


async def list_all_ship_designs_2(production_server: str, design_version: int, language_key: str, **params) -> _List[_ShipDesign]:
    params = {
        'designVersion': design_version,
        'languageKey': language_key,
        **params
    }
    result = await _core.get_entities_from_path(_ShipDesign, 'ShipDesigns', production_server, LIST_ALL_SHIP_DESIGNS_2_BASE_PATH, **params)
    return result
