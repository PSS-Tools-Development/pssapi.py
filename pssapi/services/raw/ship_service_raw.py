####################################################
##   This file has been generated automatically   ##
####################################################

from datetime import datetime as _datetime
from typing import List as _List

from ... import core as _core
from ...entities import Ship as _Ship
from ...entities import ShipDesign as _ShipDesign



# ---------- Constants ----------

GET_SHIP_BY_USER_ID_BASE_PATH: str = 'ShipService/GetShipByUserId'
LIST_ALL_SHIP_DESIGNS_2_BASE_PATH: str = 'ShipService/ListAllShipDesigns2'


# ---------- Endpoints ----------

async def get_ship_by_user_id(production_server: str, user_id: int, access_token: str, client_date_time: _datetime, **params) -> _List[_Ship]:
    params = {
        'userId': user_id,
        'accessToken': access_token,
        'clientDateTime': client_date_time,
    }
    result = await _core.get_entities_from_path(_Ship, 'GetShipByUserId', production_server, GET_SHIP_BY_USER_ID_BASE_PATH, **params)
    return result


async def list_all_ship_designs_2(production_server: str, language_key: str, design_version: int, **params) -> _List[_ShipDesign]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
    }
    result = await _core.get_entities_from_path(_ShipDesign, 'ShipDesigns', production_server, LIST_ALL_SHIP_DESIGNS_2_BASE_PATH, **params)
    return result


