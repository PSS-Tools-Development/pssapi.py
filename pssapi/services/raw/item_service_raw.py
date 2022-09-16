####################################################
##   This file has been generated automatically   ##
####################################################

from datetime import datetime as _datetime
from typing import List as _List

from ... import core as _core
from ...entities import ItemDesignAction as _ItemDesignAction
from ...entities import ItemDesign as _ItemDesign
from ...entities import Item as _Item



# ---------- Constants ----------

LIST_ITEM_DESIGN_ACTIONS_BASE_PATH: str = 'ItemService/ListItemDesignActions'
LIST_ITEM_DESIGNS_2_BASE_PATH: str = 'ItemService/ListItemDesigns2'
LIST_ITEMS_OF_A_SHIP_BASE_PATH: str = 'ItemService/ListItemsOfAShip'


# ---------- Endpoints ----------

async def list_item_design_actions(production_server: str, design_version: int, **params) -> _List[_ItemDesignAction]:
    params = {
        'designVersion': design_version,
    }
    result = await _core.get_entities_from_path(_ItemDesignAction, 'ItemDesignActions', production_server, LIST_ITEM_DESIGN_ACTIONS_BASE_PATH, **params)
    return result


async def list_item_designs_2(production_server: str, language_key: str, design_version: int, **params) -> _List[_ItemDesign]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
    }
    result = await _core.get_entities_from_path(_ItemDesign, 'ItemDesigns', production_server, LIST_ITEM_DESIGNS_2_BASE_PATH, **params)
    return result


async def list_items_of_a_ship(production_server: str, access_token: str, client_date_time: _datetime, **params) -> _List[_Item]:
    params = {
        'accessToken': access_token,
        'clientDateTime': client_date_time,
    }
    result = await _core.get_entities_from_path(_Item, 'Items', production_server, LIST_ITEMS_OF_A_SHIP_BASE_PATH, **params)
    return result


