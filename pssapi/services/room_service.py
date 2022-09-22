from typing import List as _List

from .raw import RoomServiceRaw as _RoomServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import ActionType as _ActionType
from ..entities import ConditionType as _ConditionType
from ..entities import CraftDesign as _CraftDesign
from ..entities import MissileDesign as _MissileDesign
from ..entities import RoomDesign as _RoomDesign
from ..entities import RoomDesignPurchase as _RoomDesignPurchase


class RoomService(_ServiceBase, _RoomServiceRaw):
    async def list_action_types_2(self, design_version: int = None, **params) -> _List[_ActionType]:
        return await self._list_action_types_2(self.production_server, self.language_key, design_version, **params)

    async def list_condition_types_2(self, design_version: int = None, **params) -> _List[_ConditionType]:
        return await self._list_condition_types_2(self.production_server, self.language_key, design_version, **params)

    async def list_craft_designs(self, design_version: int = None, **params) -> _List[_CraftDesign]:
        return await self._list_craft_designs(self.production_server, design_version, **params)

    async def list_missile_designs(self, design_version: int = None, **params) -> _List[_MissileDesign]:
        return await self._list_missile_designs(self.production_server, design_version, **params)

    async def list_room_design_purchase(self, design_version: int = None, **params) -> _List[_RoomDesignPurchase]:
        return await self._list_room_design_purchase(self.production_server, design_version, **params)

    async def list_room_designs_2(self, design_version: int = None, **params) -> _List[_RoomDesign]:
        return await self._list_room_designs_2(self.production_server, self.language_key, design_version, **params)

    def __repr__(self) -> str:
        return f'<RoomService: {self.name}>'

    def __str__(self) -> str:
        return f'<RoomService: {self.name}>'
