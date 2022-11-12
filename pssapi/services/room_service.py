from typing import List as _List

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
        result = await _RoomServiceRaw.list_action_types_2(self.production_server, design_version, self.language_key)
        return result

    async def list_condition_types(self, design_version: int = None) -> _List[_ConditionType]:
        result = await _RoomServiceRaw.list_condition_types_2(self.production_server, design_version, self.language_key)
        return result

    async def list_craft_designs(self, design_version: int = None) -> _List[_CraftDesign]:
        result = await _RoomServiceRaw.list_craft_designs(self.production_server, design_version)
        return result

    async def list_missile_designs(self, design_version: int = None) -> _List[_MissileDesign]:
        result = await _RoomServiceRaw.list_missile_designs(self.production_server, design_version)
        return result

    async def list_room_design_purchase(self, design_version: int = None) -> _List[_RoomDesignPurchase]:
        result = await _RoomServiceRaw.list_room_design_purchase(self.production_server, design_version)
        return result

    async def list_room_designs(self, design_version: int = None) -> _List[_RoomDesign]:
        result = await _RoomServiceRaw.list_room_designs_2(self.production_server, design_version, self.language_key)
        return result
