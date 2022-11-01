from typing import List as _List

from .raw import ItemServiceRaw as _ItemServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import ItemDesign as _ItemDesign
from ..entities import ItemDesignAction as _ItemDesignAction


class ItemService(_ServiceBase):
    async def list_item_design_actions(self, design_version: int = None) -> _List[_ItemDesignAction]:
        result = await _ItemServiceRaw.list_item_design_actions(self.production_server, design_version)
        return result

    async def list_item_designs(self, design_version: int = None) -> _List[_ItemDesign]:
        result = await _ItemServiceRaw.list_item_designs_2(self.production_server, self.language_key, design_version)
        return result
