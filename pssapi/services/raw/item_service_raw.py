"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import ItemDesign as _ItemDesign
from ...entities import ItemDesignAction as _ItemDesignAction


class ItemServiceRaw:

    SERVICE_NAME = 'ItemService'
    LIST_ITEM_DESIGN_ACTIONS_BASE_PATH: str = 'ItemService/ListItemDesignActions'
    LIST_ITEM_DESIGNS_2_BASE_PATH: str = 'ItemService/ListItemDesigns2'

    @staticmethod
    async def _list_item_design_actions(production_server: str, design_version: int, **params) -> _List[_ItemDesignAction]:
        params = {
            'designVersion': design_version,
            **params
        }

        result = await _core.get_entities_from_path(_ItemDesignAction, 'ItemDesignActions', production_server, ItemServiceRaw.LIST_ITEM_DESIGN_ACTIONS_BASE_PATH, **params)
        return result

    @staticmethod
    async def _list_item_designs_2(production_server: str, language_key: str, design_version: int, **params) -> _List[_ItemDesign]:
        params = {
            'languageKey': language_key,
            'designVersion': design_version,
            **params
        }

        result = await _core.get_entities_from_path(_ItemDesign, 'ItemDesigns', production_server, ItemServiceRaw.LIST_ITEM_DESIGNS_2_BASE_PATH, **params)
        return result
