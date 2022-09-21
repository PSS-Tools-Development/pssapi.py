from typing import List as _List

from .raw import ItemServiceRaw as _ItemServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import ItemDesign as _ItemDesign
from ..entities import ItemDesignAction as _ItemDesignAction


class ItemService(_ServiceBase, _ItemServiceRaw):
    async def list_item_design_actions(self, **params) -> _List[_ItemDesignAction]:
        return self._list_item_design_actions(self.production_server, **params)

    async def list_item_designs_2(self, **params) -> _List[_ItemDesign]:
        return self._list_item_designs_2(self.production_server, self.language_key, **params)

    def __repr__(self) -> str:
        return f'<ItemService: {self.name}>'

    def __str__(self) -> str:
        return f'<ItemService: {self.name}>'
