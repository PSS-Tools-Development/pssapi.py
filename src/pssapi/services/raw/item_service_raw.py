"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import ItemDesign as _ItemDesign
from ...entities import ItemDesignAction as _ItemDesignAction

# ---------- Constants ----------

LIST_ITEM_DESIGN_ACTIONS_BASE_PATH: str = "ItemService/ListItemDesignActions"
LIST_ITEM_DESIGNS_2_BASE_PATH: str = "ItemService/ListItemDesigns2"


# ---------- Endpoints ----------


async def list_item_design_actions(production_server: str, design_version: int, **params) -> _List[_ItemDesignAction]:
    params = {"designVersion": design_version, **params}
    result = await _core.get_entities_from_path(((_ItemDesignAction, "ItemDesignActions", True),), "ItemDesignActions", production_server, LIST_ITEM_DESIGN_ACTIONS_BASE_PATH, "GET", **params)
    return result


async def list_item_designs_2(production_server: str, design_version: int, language_key: str, **params) -> _List[_ItemDesign]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_ItemDesign, "ItemDesigns", True),), "ItemDesigns", production_server, LIST_ITEM_DESIGNS_2_BASE_PATH, "GET", **params)
    return result
