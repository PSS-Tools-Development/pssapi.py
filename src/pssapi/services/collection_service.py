from typing import List as _List

import pssapi.services.service_base as _service_base

from ..entities import CollectionDesign as _CollectionDesign
from .raw import CollectionServiceRaw as _CollectionServiceRaw


class CollectionService(_service_base.CacheableServiceBase):
    @_service_base.cache_endpoint("CollectionDesignVersion")
    async def list_all_collection_designs(self, design_version: int = None) -> _List[_CollectionDesign]:
        production_server = await self.get_production_server()
        result = await _CollectionServiceRaw.list_all_collection_designs(production_server, design_version, self.language_key)
        return result
