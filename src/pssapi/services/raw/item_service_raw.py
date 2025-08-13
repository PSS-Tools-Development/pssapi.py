"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from typing import List

from ... import core
from ...entities import ItemDesign, ItemDesignAction


# ---------- Constants ----------

LIST_ITEM_DESIGN_ACTIONS_BASE_PATH: str = "ItemService/ListItemDesignActions"
LIST_ITEM_DESIGNS_2_BASE_PATH: str = "ItemService/ListItemDesigns2"

# ---------- Endpoint structure ----------


# ---------- Endpoints ----------


async def list_item_design_actions(production_server: str, client_date_time: str, design_version: int, **params) -> List[ItemDesignAction]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, **params}
    result = await core.get_entities_from_path(
        ((ItemDesignAction, "ItemDesignActions", True),), "ItemDesignActions", production_server, LIST_ITEM_DESIGN_ACTIONS_BASE_PATH, "GET", response_gzipped=False, **params
    )
    return result


async def list_item_designs_2(production_server: str, client_date_time: str, design_version: int, language_key: str, **params) -> List[ItemDesign]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, "languageKey": language_key, **params}
    result = await core.get_entities_from_path(((ItemDesign, "ItemDesigns", True),), "ItemDesigns", production_server, LIST_ITEM_DESIGNS_2_BASE_PATH, "GET", response_gzipped=False, **params)
    return result
