"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import GetCatalogQuantity as _GetCatalogQuantity

# ---------- Constants ----------

GET_CATALOG_QUANTITY_BASE_PATH: str = 'LiveOpsService/GetCatalogQuantity'


# ---------- Endpoints ----------

async def get_catalog_quantity(production_server: str, **params) -> _List[_GetCatalogQuantity]:
    params = {
        **params
    }
    result = await _core.get_entities_from_path(_GetCatalogQuantity, 'LiveOpsService', production_server, GET_CATALOG_QUANTITY_BASE_PATH, **params)
    return result
