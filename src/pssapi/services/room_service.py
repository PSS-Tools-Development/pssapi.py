import datetime as _datetime
from typing import List as _List

import pssapi.services.service_base as _service_base

from .. import utils as _utils
from ..entities import ActionType as _ActionType
from ..entities import ConditionType as _ConditionType
from ..entities import CraftDesign as _CraftDesign
from ..entities import MissileDesign as _MissileDesign
from ..entities import RoomDesign as _RoomDesign
from ..entities import RoomDesignPurchase as _RoomDesignPurchase
from .raw import RoomServiceRaw as _RoomServiceRaw


class RoomService(_service_base.CacheableServiceBase):
    async def get_missile_design(self, missile_design_id: int) -> _MissileDesign:
        """Retrieve a single missile design (e.g. Rocket, Mining Beam), by missile design ID: damage values, missile type, speed, volley, flight type."""
        production_server = await self.get_production_server()
        result = await _RoomServiceRaw.get_missile_design(production_server, self.language_key, missile_design_id)
        return result

    async def get_room_design(self, room_design_id: int) -> _RoomDesign:
        """Retrieve a single room design (starship room blueprint), by room design ID: name, category, capacity, construction time, level, description."""
        production_server = await self.get_production_server()
        result = await _RoomServiceRaw.get_room_design(production_server, self.language_key, room_design_id)
        return result

    @_service_base.cache_endpoint("ActionTypeVersion")
    async def list_action_types(self, design_version: int = None) -> _List[_ActionType]:
        """List all action types (room actions such as Set Maximum Power, attack, repair), with category, parameter value and description, as a versioned design list."""
        production_server = await self.get_production_server()
        result = await _RoomServiceRaw.list_action_types_2(production_server, design_version, self.language_key)
        return result

    @_service_base.cache_endpoint("ConditionTypeVersion")
    async def list_condition_types(self, design_version: int = None) -> _List[_ConditionType]:
        """List all condition types (conditions that room actions can check, e.g. always true, shield checks), with category and comparison, as a versioned design list."""
        production_server = await self.get_production_server()
        result = await _RoomServiceRaw.list_condition_types_2(production_server, design_version, self.language_key)
        return result

    @_service_base.cache_endpoint("CraftDesignVersion")
    async def list_craft_designs(self, client_date_time: _datetime.datetime = None, design_version: int = None) -> _List[_CraftDesign]:
        """List all craft designs (starfighter crafts such as Interceptor, with flight speed, reload, missile design, HP and attack type), as a versioned design list."""
        production_server = await self.get_production_server()
        result = await _RoomServiceRaw.list_craft_designs(production_server, _utils.datetime.convert_to_pss_timestamp(client_date_time), design_version)
        return result

    @_service_base.cache_endpoint("MissileDesignVersion")
    async def list_missile_designs(self, client_date_time: _datetime.datetime = None, design_version: int = None) -> _List[_MissileDesign]:
        """List all missile designs (missile blueprints), as a versioned design list."""
        production_server = await self.get_production_server()
        result = await _RoomServiceRaw.list_missile_designs(production_server, _utils.datetime.convert_to_pss_timestamp(client_date_time), design_version)
        return result

    @_service_base.cache_endpoint("RoomDesignPurchaseVersion")
    async def list_room_design_purchase(self, client_date_time: _datetime.datetime = None, design_version: int = None) -> _List[_RoomDesignPurchase]:
        """List all room design purchases, as a versioned design list.

        Each entry describes how many instances of a room are available at which hull level, and sometimes additional requirements (e.g. original faction).
        """
        production_server = await self.get_production_server()
        result = await _RoomServiceRaw.list_room_design_purchase(production_server, _utils.datetime.convert_to_pss_timestamp(client_date_time), design_version)
        return result

    @_service_base.cache_endpoint("RoomDesignVersion")
    async def list_room_designs(self, client_date_time: _datetime.datetime = None, design_version: int = None) -> _List[_RoomDesign]:
        """List all room designs (starship room blueprints), as a versioned design list."""
        production_server = await self.get_production_server()
        result = await _RoomServiceRaw.list_room_designs_2(production_server, _utils.datetime.convert_to_pss_timestamp(client_date_time), design_version, self.language_key)
        return result
