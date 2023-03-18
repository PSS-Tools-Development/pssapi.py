from typing import List as _List

import pssapi.services.service_base as _service_base

from ..entities import ActionType as _ActionType
from ..entities import ConditionType as _ConditionType
from ..entities import CraftDesign as _CraftDesign
from ..entities import Item as _Item
from ..entities import MissileDesign as _MissileDesign
from ..entities import Room as _Room
from ..entities import RoomDesign as _RoomDesign
from ..entities import RoomDesignPurchase as _RoomDesignPurchase
from .raw import RoomServiceRaw as _RoomServiceRaw


class RoomService(_service_base.CacheableServiceBase):
    async def collect_all_resources(self, access_token: str, collect_date: str, item_type: str) -> _List[_Item]:
        production_server = await self.get_production_server()
        result = await _RoomServiceRaw.collect_all_resources(production_server, access_token, collect_date, item_type)
        return result

    @_service_base.cache_endpoint("ActionTypeVersion")
    async def list_action_types(self, design_version: int = None) -> _List[_ActionType]:
        production_server = await self.get_production_server()
        result = await _RoomServiceRaw.list_action_types_2(production_server, design_version, self.language_key)
        return result

    @_service_base.cache_endpoint("ConditionTypeVersion")
    async def list_condition_types(self, design_version: int = None) -> _List[_ConditionType]:
        production_server = await self.get_production_server()
        result = await _RoomServiceRaw.list_condition_types_2(production_server, design_version, self.language_key)
        return result

    @_service_base.cache_endpoint("CraftDesignVersion")
    async def list_craft_designs(self, design_version: int = None) -> _List[_CraftDesign]:
        production_server = await self.get_production_server()
        result = await _RoomServiceRaw.list_craft_designs(production_server, design_version)
        return result

    @_service_base.cache_endpoint("MissileDesignVersion")
    async def list_missile_designs(self, design_version: int = None) -> _List[_MissileDesign]:
        production_server = await self.get_production_server()
        result = await _RoomServiceRaw.list_missile_designs(production_server, design_version)
        return result

    @_service_base.cache_endpoint("RoomDesignPurchaseVersion")
    async def list_room_design_purchase(self, design_version: int = None) -> _List[_RoomDesignPurchase]:
        production_server = await self.get_production_server()
        result = await _RoomServiceRaw.list_room_design_purchase(production_server, design_version)
        return result

    @_service_base.cache_endpoint("RoomDesignVersion")
    async def list_room_designs(self, design_version: int = None) -> _List[_RoomDesign]:
        production_server = await self.get_production_server()
        result = await _RoomServiceRaw.list_room_designs_2(production_server, design_version, self.language_key)
        return result

    async def move_room(self, access_token: str, column: int, room_id: int, row: int) -> _Room:
        production_server = await self.get_production_server()
        result = await _RoomServiceRaw.move_room(production_server, access_token, column, room_id, row)
        return result

    async def rebuild_ammo(self, access_token: str, ammo_category: str, checksum: str, client_date_time: str) -> _List[_Room]:
        production_server = await self.get_production_server()
        result = await _RoomServiceRaw.rebuild_ammo_2(production_server, access_token, ammo_category, checksum, client_date_time)
        return result
