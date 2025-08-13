from typing import List

from pssapi.services import service_base

from ..entities import CollectionDesign
from .raw import CollectionServiceRaw


class CollectionService(service_base.CacheableServiceBase):
    @service_base.cache_endpoint("CollectionDesignVersion")
    async def list_all_collection_designs(self, client_date_time: str, design_version: int = None) -> List[CollectionDesign]:
        production_server = await self.get_production_server()
        result = await CollectionServiceRaw.list_all_collection_designs(production_server, client_date_time, design_version, self.language_key)
        return result
