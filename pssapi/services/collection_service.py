from typing import List as _List

from .raw import CollectionServiceRaw as _CollectionServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import CollectionDesign as _CollectionDesign


class CollectionService(_ServiceBase):
    async def list_all_collection_designs(self, design_version: int = None) -> _List[_CollectionDesign]:
        production_server = await self.get_production_server()
        result = await _CollectionServiceRaw.list_all_collection_designs(production_server, design_version, self.language_key)
        return result
