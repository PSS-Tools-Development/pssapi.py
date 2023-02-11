from typing import List as _List
from typing import Tuple as _Tuple

from .raw import RoomServiceRaw as _RoomServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import ActionType as _ActionType
from ..entities import ConditionType as _ConditionType
from ..entities import CraftDesign as _CraftDesign
from ..entities import MissileDesign as _MissileDesign
from ..entities import RoomDesign as _RoomDesign
from ..entities import RoomDesignPurchase as _RoomDesignPurchase


class RoomService(_ServiceBase):
    async def list_action_types(self, design_version: int = None) -> _List[_ActionType]:
        production_server = await self.get_production_server()
        result = await _RoomServiceRaw.list_action_types_2(production_server, design_version, self.language_key)
        return result

    async def list_condition_types(self, design_version: int = None) -> _List[_ConditionType]:
        production_server = await self.get_production_server()
        result = await _RoomServiceRaw.list_condition_types_2(production_server, design_version, self.language_key)
        return result

    async def list_craft_designs(self, design_version: int = None) -> _List[_CraftDesign]:
        production_server = await self.get_production_server()
        result = await _RoomServiceRaw.list_craft_designs(production_server, design_version)
        return result

    async def list_missile_designs(self, design_version: int = None) -> _List[_MissileDesign]:
        production_server = await self.get_production_server()
        result = await _RoomServiceRaw.list_missile_designs(production_server, design_version)
        return result

    async def list_room_design_purchase(self, design_version: int = None) -> _List[_RoomDesignPurchase]:
        production_server = await self.get_production_server()
        result = await _RoomServiceRaw.list_room_design_purchase(production_server, design_version)
        return result

    async def list_room_designs(self, design_version: int = None) -> _List[_RoomDesign]:
        production_server = await self.get_production_server()
        result = await _RoomServiceRaw.list_room_designs_2(production_server, design_version, self.language_key)
        return result

