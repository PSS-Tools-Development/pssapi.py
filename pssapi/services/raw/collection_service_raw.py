"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import CollectionDesign as _CollectionDesign


class CollectionServiceRaw:

    SERVICE_NAME = 'CollectionService'
    LIST_ALL_COLLECTION_DESIGNS_BASE_PATH: str = 'CollectionService/ListAllCollectionDesigns'

    @staticmethod
    async def _list_all_collection_designs(production_server: str, language_key: str, design_version: int, **params) -> _List[_CollectionDesign]:
        params = {
            'languageKey': language_key,
            'designVersion': design_version,
            **params
        }

        result = await _core.get_entities_from_path(_CollectionDesign, 'CollectionDesigns', production_server, CollectionServiceRaw.LIST_ALL_COLLECTION_DESIGNS_BASE_PATH, **params)
        return result
