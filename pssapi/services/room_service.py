from datetime import datetime as _datetime
from typing import List as _List

from .raw import RoomServiceRaw as _RoomServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import MissileDesign as _MissileDesign
from ...entities import CraftDesign as _CraftDesign
from ...entities import ActionType as _ActionType
from ...entities import ConditionType as _ConditionType
from ...entities import RoomDesignPurchase as _RoomDesignPurchase
from ...entities import RoomAction as _RoomAction
from ...entities import RoomDesign as _RoomDesign
from ...entities import Room as _Room


class RoomService(_ServiceBase):
    async def list_action_types_2(self, language_key: str, design_version: int) -> _List[_ActionType]:
        raise NotImplemented()
        result = await _RoomServiceRaw.list_action_types_2(self.production_server, language_key: str, design_version: int)
        return result


    async def list_all_room_actions_of_ship(self, ship_id: int, access_token: str) -> _List[_RoomAction]:
        raise NotImplemented()
        result = await _RoomServiceRaw.list_all_room_actions_of_ship(self.production_server, ship_id: int, access_token: str)
        return result


    async def list_condition_types_2(self, language_key: str, design_version: int) -> _List[_ConditionType]:
        raise NotImplemented()
        result = await _RoomServiceRaw.list_condition_types_2(self.production_server, language_key: str, design_version: int)
        return result


    async def list_craft_designs(self, design_version: int) -> _List[_CraftDesign]:
        raise NotImplemented()
        result = await _RoomServiceRaw.list_craft_designs(self.production_server, design_version: int)
        return result


    async def list_missile_designs(self, design_version: int) -> _List[_MissileDesign]:
        raise NotImplemented()
        result = await _RoomServiceRaw.list_missile_designs(self.production_server, design_version: int)
        return result


    async def list_room_design_purchase(self, design_version: int) -> _List[_RoomDesignPurchase]:
        raise NotImplemented()
        result = await _RoomServiceRaw.list_room_design_purchase(self.production_server, design_version: int)
        return result


    async def list_room_designs_2(self, language_key: str, design_version: int) -> _List[_RoomDesign]:
        raise NotImplemented()
        result = await _RoomServiceRaw.list_room_designs_2(self.production_server, language_key: str, design_version: int)
        return result


    async def list_rooms_via_access_token(self, access_token: str, client_date_time: _datetime) -> _List[_Room]:
        raise NotImplemented()
        result = await _RoomServiceRaw.list_rooms_via_access_token(self.production_server, access_token: str, client_date_time: _datetime)
        return result


