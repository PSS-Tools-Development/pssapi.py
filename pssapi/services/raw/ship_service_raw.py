"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import Ship as _Ship
from ...entities import ShipDesign as _ShipDesign

# ---------- Constants ----------

INSPECT_SHIP_2_BASE_PATH: str = 'ShipService/InspectShip2'
LIST_ALL_SHIP_DESIGNS_2_BASE_PATH: str = 'ShipService/ListAllShipDesigns2'


# ---------- Endpoints ----------

async def inspect_ship_2(production_server: str, access_token: str, user_id: int, **params) -> _List[_Ship]:
    params = {
        'accessToken': access_token,
        'userId': user_id,
        **params
    }
    content = None
    result = await _core.get_entities_from_path(_Ship, 'InspectShip', production_server, INSPECT_SHIP_2_BASE_PATH, 'GET', request_content=content, **params)
    return result


async def list_all_ship_designs_2(production_server: str, design_version: int, language_key: str, **params) -> _List[_ShipDesign]:
    params = {
        'designVersion': design_version,
        'languageKey': language_key,
        **params
    }
    content = None
    result = await _core.get_entities_from_path(_ShipDesign, 'ShipDesigns', production_server, LIST_ALL_SHIP_DESIGNS_2_BASE_PATH, 'GET', request_content=content, **params)
    return result
