"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from typing import List

from ... import core
from ...entities import CollectionDesign


# ---------- Constants ----------

LIST_ALL_COLLECTION_DESIGNS_BASE_PATH: str = "CollectionService/ListAllCollectionDesigns"

# ---------- Endpoint structure ----------


# ---------- Endpoints ----------


async def list_all_collection_designs(production_server: str, client_date_time: str, design_version: int, language_key: str, **params) -> List[CollectionDesign]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, "languageKey": language_key, **params}
    result = await core.get_entities_from_path(
        ((CollectionDesign, "CollectionDesigns", True),), "CollectionDesigns", production_server, LIST_ALL_COLLECTION_DESIGNS_BASE_PATH, "GET", response_gzipped=False, **params
    )
    return result
