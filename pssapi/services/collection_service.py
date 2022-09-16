from typing import List as _List

from .raw import CollectionServiceRaw as _CollectionServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import CollectionDesign as _CollectionDesign


class CollectionService(_ServiceBase):
    async def list_all_collection_designs(self, language_key: str, design_version: int) -> _List[_CollectionDesign]:
        raise NotImplemented()
        result = await _CollectionServiceRaw.list_all_collection_designs(self.production_server, language_key: str, design_version: int)
        return result


