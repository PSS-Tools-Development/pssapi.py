"""
    This file has been generated automatically
"""

from typing import List as _List
from typing import List as _Tuple

from ... import core as _core
from ...entities import ActionType as _ActionType
from ...entities import ConditionType as _ConditionType
from ...entities import CraftDesign as _CraftDesign
from ...entities import MissileDesign as _MissileDesign
from ...entities import RoomDesign as _RoomDesign
from ...entities import RoomDesignPurchase as _RoomDesignPurchase

# ---------- Constants ----------

LIST_ACTION_TYPES_2_BASE_PATH: str = 'RoomService/ListActionTypes2'
LIST_CONDITION_TYPES_2_BASE_PATH: str = 'RoomService/ListConditionTypes2'
LIST_CRAFT_DESIGNS_BASE_PATH: str = 'RoomService/ListCraftDesigns'
LIST_MISSILE_DESIGNS_BASE_PATH: str = 'RoomService/ListMissileDesigns'
LIST_ROOM_DESIGN_PURCHASE_BASE_PATH: str = 'RoomService/ListRoomDesignPurchase'
LIST_ROOM_DESIGNS_2_BASE_PATH: str = 'RoomService/ListRoomDesigns2'


# ---------- Endpoints ----------

async def list_action_types_2(production_server: str, design_version: int, language_key: str, **params) -> _List[_ActionType]:
    params = {
        'designVersion': design_version,
        'languageKey': language_key,
        **params
    }
    result = await _core.get_entities_from_path((_ActionType), 'ActionTypes', production_server, LIST_ACTION_TYPES_2_BASE_PATH, 'GET', **params)
    return result


async def list_condition_types_2(production_server: str, design_version: int, language_key: str, **params) -> _List[_ConditionType]:
    params = {
        'designVersion': design_version,
        'languageKey': language_key,
        **params
    }
    result = await _core.get_entities_from_path((_ConditionType), 'ConditionTypes', production_server, LIST_CONDITION_TYPES_2_BASE_PATH, 'GET', **params)
    return result


async def list_craft_designs(production_server: str, design_version: int, **params) -> _List[_CraftDesign]:
    params = {
        'designVersion': design_version,
        **params
    }
    result = await _core.get_entities_from_path((_CraftDesign), 'CraftDesigns', production_server, LIST_CRAFT_DESIGNS_BASE_PATH, 'GET', **params)
    return result


async def list_missile_designs(production_server: str, design_version: int, **params) -> _List[_MissileDesign]:
    params = {
        'designVersion': design_version,
        **params
    }
    result = await _core.get_entities_from_path((_MissileDesign), 'MissileDesigns', production_server, LIST_MISSILE_DESIGNS_BASE_PATH, 'GET', **params)
    return result


async def list_room_design_purchase(production_server: str, design_version: int, **params) -> _List[_RoomDesignPurchase]:
    params = {
        'designVersion': design_version,
        **params
    }
    result = await _core.get_entities_from_path((_RoomDesignPurchase), 'RoomDesignPurchases', production_server, LIST_ROOM_DESIGN_PURCHASE_BASE_PATH, 'GET', **params)
    return result


async def list_room_designs_2(production_server: str, design_version: int, language_key: str, **params) -> _List[_RoomDesign]:
    params = {
        'designVersion': design_version,
        'languageKey': language_key,
        **params
    }
    result = await _core.get_entities_from_path((_RoomDesign), 'RoomDesigns', production_server, LIST_ROOM_DESIGNS_2_BASE_PATH, 'GET', **params)
    return result


