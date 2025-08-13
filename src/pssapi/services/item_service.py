from typing import List

from pssapi.services import service_base

from ..entities import ItemDesign, ItemDesignAction
from .raw import ItemServiceRaw


class ItemService(service_base.CacheableServiceBase):
    @service_base.cache_endpoint("ItemDesignActionVersion")
    async def list_item_design_actions(self, client_date_time: str, design_version: int = None) -> List[ItemDesignAction]:
        production_server = await self.get_production_server()
        result = await ItemServiceRaw.list_item_design_actions(production_server, client_date_time, design_version)
        return result

    @service_base.cache_endpoint("ItemDesignVersion")
    async def list_item_designs(self, client_date_time: str, design_version: int = None) -> List[ItemDesign]:
        production_server = await self.get_production_server()
        result = await ItemServiceRaw.list_item_designs_2(production_server, client_date_time, design_version, self.language_key)
        return result
