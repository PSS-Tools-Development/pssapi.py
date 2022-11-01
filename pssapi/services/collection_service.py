from typing import List as _List

from .raw import CollectionServiceRaw as _CollectionServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import CollectionDesign as _CollectionDesign


class CollectionService(_ServiceBase):
    async def list_all_collection_designs(self, design_version: int = None) -> _List[_CollectionDesign]:
        result = await _CollectionServiceRaw.list_all_collection_designs(self.production_server, self.language_key, design_version)
        return result
