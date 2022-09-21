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
    async def list_action_types_2(self, **params) -> _List[_ActionType]:
        return self._list_action_types_2(self.production_server, self.language_key, **params)

    async def list_condition_types_2(self, **params) -> _List[_ConditionType]:
        return self._list_condition_types_2(self.production_server, self.language_key, **params)

    async def list_craft_designs(self, **params) -> _List[_CraftDesign]:
        return self._list_craft_designs(self.production_server, **params)

    async def list_missile_designs(self, **params) -> _List[_MissileDesign]:
        return self._list_missile_designs(self.production_server, **params)

    async def list_room_design_purchase(self, **params) -> _List[_RoomDesignPurchase]:
        return self._list_room_design_purchase(self.production_server, **params)

    async def list_room_designs_2(self, **params) -> _List[_RoomDesign]:
        return self._list_room_designs_2(self.production_server, self.language_key, **params)

    def __repr__(self) -> str:
        return f'<RoomService: {self.name}>'

    def __str__(self) -> str:
        return f'<RoomService: {self.name}>'
