from typing import List as _List

import pssapi.services.service_base as _service_base

from ..entities import ItemDesign as _ItemDesign
from ..entities import ItemDesignAction as _ItemDesignAction
from .raw import ItemServiceRaw as _ItemServiceRaw


class ItemService(_service_base.CacheableServiceBase):
    @_service_base.cache_endpoint("ItemDesignActionVersion")
    async def list_item_design_actions(self, design_version: int = None) -> _List[_ItemDesignAction]:
        production_server = await self.get_production_server()
        result = await _ItemServiceRaw.list_item_design_actions(production_server, design_version)
        return result

    @_service_base.cache_endpoint("ItemDesignVersion")
    async def list_item_designs(self, design_version: int = None) -> _List[_ItemDesign]:
        production_server = await self.get_production_server()
        result = await _ItemServiceRaw.list_item_designs_2(production_server, design_version, self.language_key)
        return result
