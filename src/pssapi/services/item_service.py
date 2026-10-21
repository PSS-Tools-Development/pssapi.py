import datetime as _datetime
from typing import List as _List

import pssapi.services.service_base as _service_base

from .. import utils as _utils
from ..entities import ItemDesign as _ItemDesign
from ..entities import ItemDesignAction as _ItemDesignAction
from .raw import ItemServiceRaw as _ItemServiceRaw


class ItemService(_service_base.CacheableServiceBase):
    async def to_item(self, item_name: str, client_date_time: _datetime.datetime = None, design_version: int = None) -> _List[_ItemDesign]:
        """List item designs whose name contains the given item name, case-insensitive."""
        items = await self.list_item_designs(client_date_time, design_version)
        result = list(filter(lambda item: item_name.lower() in item.item_design_name.lower(), items))

        return result

    @_service_base.cache_endpoint("ItemDesignActionVersion")
    async def list_item_design_actions(self, client_date_time: _datetime.datetime = None, design_version: int = None) -> _List[_ItemDesignAction]:
        """List all item design actions, as a versioned design list.

        An item design action denotes the AI that can be copied from an AI chip item.
        """
        production_server = await self.get_production_server()
        result = await _ItemServiceRaw.list_item_design_actions(production_server, _utils.datetime.convert_to_pss_timestamp(client_date_time), design_version)
        return result

    @_service_base.cache_endpoint("ItemDesignVersion")
    async def list_item_designs(self, client_date_time: _datetime.datetime = None, design_version: int = None) -> _List[_ItemDesign]:
        """List all item designs, the equipment blueprints (e.g. Rocket, Penetrator, EMP) with name, stats and craftable materials."""
        production_server = await self.get_production_server()
        result = await _ItemServiceRaw.list_item_designs_2(production_server, _utils.datetime.convert_to_pss_timestamp(client_date_time), design_version, self.language_key)
        return result
