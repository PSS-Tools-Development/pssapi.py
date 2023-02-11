from typing import List as _List
from typing import Tuple as _Tuple

from .raw import ItemServiceRaw as _ItemServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import ItemDesign as _ItemDesign
from ..entities import ItemDesignAction as _ItemDesignAction


class ItemService(_ServiceBase):
    async def list_item_design_actions(self, design_version: int = None) -> _List[_ItemDesignAction]:
        production_server = await self.get_production_server()
        result = await _ItemServiceRaw.list_item_design_actions(production_server, design_version)
        return result

    async def list_item_designs(self, design_version: int = None) -> _List[_ItemDesign]:
        production_server = await self.get_production_server()
        result = await _ItemServiceRaw.list_item_designs_2(production_server, design_version, self.language_key)
        return result

