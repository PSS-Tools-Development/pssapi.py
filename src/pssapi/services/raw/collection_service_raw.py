"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import CollectionDesign as _CollectionDesign

# ---------- Constants ----------

LIST_ALL_COLLECTION_DESIGNS_BASE_PATH: str = "CollectionService/ListAllCollectionDesigns"


# ---------- Endpoints ----------


async def list_all_collection_designs(production_server: str, design_version: int, language_key: str, **params) -> _List[_CollectionDesign]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_CollectionDesign, "CollectionDesigns", True),), "CollectionDesigns", production_server, LIST_ALL_COLLECTION_DESIGNS_BASE_PATH, "GET", **params)
    return result
