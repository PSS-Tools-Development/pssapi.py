from typing import List as _List

from .raw import CollectionServiceRaw as _CollectionServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import CollectionDesign as _CollectionDesign


class CollectionService(_ServiceBase, _CollectionServiceRaw):
    async def list_all_collection_designs(self, **params) -> _List[_CollectionDesign]:
        return self._list_all_collection_designs(self.production_server, self.language_key, self.design_version, **params)

    def __repr__(self) -> str:
        return f'<CollectionService: {self.name}>'

    def __str__(self) -> str:
        return f'<CollectionService: {self.name}>'
