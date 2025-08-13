from typing import List

from pssapi.services import service_base

from ..entities import ActionType, ConditionType, CraftDesign, MissileDesign, RoomDesign, RoomDesignPurchase
from .raw import RoomServiceRaw


class RoomService(service_base.CacheableServiceBase):
    async def get_missile_design(self, missile_design_id: int) -> MissileDesign:
        production_server = await self.get_production_server()
        result = await RoomServiceRaw.get_missile_design(production_server, self.language_key, missile_design_id)
        return result

    async def get_room_design(self, room_design_id: int) -> RoomDesign:
        production_server = await self.get_production_server()
        result = await RoomServiceRaw.get_room_design(production_server, self.language_key, room_design_id)
        return result

    @service_base.cache_endpoint("ActionTypeVersion")
    async def list_action_types(self, design_version: int = None) -> List[ActionType]:
        production_server = await self.get_production_server()
        result = await RoomServiceRaw.list_action_types_2(production_server, design_version, self.language_key)
        return result

    @service_base.cache_endpoint("ConditionTypeVersion")
    async def list_condition_types(self, design_version: int = None) -> List[ConditionType]:
        production_server = await self.get_production_server()
        result = await RoomServiceRaw.list_condition_types_2(production_server, design_version, self.language_key)
        return result

    @service_base.cache_endpoint("CraftDesignVersion")
    async def list_craft_designs(self, client_date_time: str, design_version: int = None) -> List[CraftDesign]:
        production_server = await self.get_production_server()
        result = await RoomServiceRaw.list_craft_designs(production_server, client_date_time, design_version)
        return result

    @service_base.cache_endpoint("MissileDesignVersion")
    async def list_missile_designs(self, client_date_time: str, design_version: int = None) -> List[MissileDesign]:
        production_server = await self.get_production_server()
        result = await RoomServiceRaw.list_missile_designs(production_server, client_date_time, design_version)
        return result

    @service_base.cache_endpoint("RoomDesignPurchaseVersion")
    async def list_room_design_purchase(self, client_date_time: str, design_version: int = None) -> List[RoomDesignPurchase]:
        production_server = await self.get_production_server()
        result = await RoomServiceRaw.list_room_design_purchase(production_server, client_date_time, design_version)
        return result

    @service_base.cache_endpoint("RoomDesignVersion")
    async def list_room_designs(self, client_date_time: str, design_version: int = None) -> List[RoomDesign]:
        production_server = await self.get_production_server()
        result = await RoomServiceRaw.list_room_designs_2(production_server, client_date_time, design_version, self.language_key)
        return result
