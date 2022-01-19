"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import ActionType as _ActionType
from ...entities import ConditionType as _ConditionType
from ...entities import CraftDesign as _CraftDesign
from ...entities import MissileDesign as _MissileDesign
from ...entities import RoomDesign as _RoomDesign
from ...entities import RoomDesignPurchase as _RoomDesignPurchase

# ---------- Constants ----------

GET_MISSILE_DESIGN_BASE_PATH: str = "RoomService/GetMissileDesign"
GET_ROOM_DESIGN_BASE_PATH: str = "RoomService/GetRoomDesign"
LIST_ACTION_TYPES_2_BASE_PATH: str = "RoomService/ListActionTypes2"
LIST_CONDITION_TYPES_2_BASE_PATH: str = "RoomService/ListConditionTypes2"
LIST_CRAFT_DESIGNS_BASE_PATH: str = "RoomService/ListCraftDesigns"
LIST_MISSILE_DESIGNS_BASE_PATH: str = "RoomService/ListMissileDesigns"
LIST_ROOM_DESIGN_PURCHASE_BASE_PATH: str = "RoomService/ListRoomDesignPurchase"
LIST_ROOM_DESIGNS_2_BASE_PATH: str = "RoomService/ListRoomDesigns2"


# ---------- Endpoints ----------


async def get_missile_design(production_server: str, language_key: str, missile_design_id: int, **params) -> _MissileDesign:
    params = {"languageKey": language_key, "missileDesignId": missile_design_id, **params}
    result = await _core.get_entities_from_path(((_MissileDesign, "MissileDesign", False),), "GetMissileDesign", production_server, GET_MISSILE_DESIGN_BASE_PATH, "GET", **params)
    return result


async def get_room_design(production_server: str, language_key: str, room_design_id: int, **params) -> _RoomDesign:
    params = {"languageKey": language_key, "roomDesignId": room_design_id, **params}
    result = await _core.get_entities_from_path(((_RoomDesign, "RoomDesign", False),), "GetRoomDesign", production_server, GET_ROOM_DESIGN_BASE_PATH, "GET", **params)
    return result


async def list_action_types_2(production_server: str, design_version: int, language_key: str, **params) -> _List[_ActionType]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_ActionType, "ActionTypes", True),), "ActionTypes", production_server, LIST_ACTION_TYPES_2_BASE_PATH, "GET", **params)
    return result


async def list_condition_types_2(production_server: str, design_version: int, language_key: str, **params) -> _List[_ConditionType]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_ConditionType, "ConditionTypes", True),), "ConditionTypes", production_server, LIST_CONDITION_TYPES_2_BASE_PATH, "GET", **params)
    return result


async def list_craft_designs(production_server: str, design_version: int, **params) -> _List[_CraftDesign]:
    params = {"designVersion": design_version, **params}
    result = await _core.get_entities_from_path(((_CraftDesign, "CraftDesigns", True),), "CraftDesigns", production_server, LIST_CRAFT_DESIGNS_BASE_PATH, "GET", **params)
    return result


async def list_missile_designs(production_server: str, design_version: int, **params) -> _List[_MissileDesign]:
    params = {"designVersion": design_version, **params}
    result = await _core.get_entities_from_path(((_MissileDesign, "MissileDesigns", True),), "MissileDesigns", production_server, LIST_MISSILE_DESIGNS_BASE_PATH, "GET", **params)
    return result


async def list_room_design_purchase(production_server: str, design_version: int, **params) -> _List[_RoomDesignPurchase]:
    params = {"designVersion": design_version, **params}
    result = await _core.get_entities_from_path(((_RoomDesignPurchase, "RoomDesignPurchases", True),), "RoomDesignPurchases", production_server, LIST_ROOM_DESIGN_PURCHASE_BASE_PATH, "GET", **params)
    return result


async def list_room_designs_2(production_server: str, design_version: int, language_key: str, **params) -> _List[_RoomDesign]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_RoomDesign, "RoomDesigns", True),), "RoomDesigns", production_server, LIST_ROOM_DESIGNS_2_BASE_PATH, "GET", **params)
    return result
