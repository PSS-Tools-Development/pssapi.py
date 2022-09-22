from typing import List as _List

from .raw import ItemServiceRaw as _ItemServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import ItemDesign as _ItemDesign
from ..entities import ItemDesignAction as _ItemDesignAction


class ItemService(_ServiceBase, _ItemServiceRaw):
    async def list_item_design_actions(self, design_version: int = None, **params) -> _List[_ItemDesignAction]:
        return await self._list_item_design_actions(self.production_server, design_version, **params)

    async def list_item_designs_2(self, design_version: int = None, **params) -> _List[_ItemDesign]:
        return await self._list_item_designs_2(self.production_server, self.language_key, design_version, **params)

    def __repr__(self) -> str:
        return f'<ItemService: {self.name}>'

    def __str__(self) -> str:
        return f'<ItemService: {self.name}>'
