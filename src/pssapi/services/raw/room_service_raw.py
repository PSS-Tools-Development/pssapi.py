"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import ActionType as _ActionType
from ...entities import ConditionType as _ConditionType
from ...entities import CraftDesign as _CraftDesign
from ...entities import Item as _Item
from ...entities import MissileDesign as _MissileDesign
from ...entities import Room as _Room
from ...entities import RoomDesign as _RoomDesign
from ...entities import RoomDesignPurchase as _RoomDesignPurchase

# ---------- Constants ----------

COLLECT_ALL_RESOURCES_BASE_PATH: str = "RoomService/CollectAllResources"
LIST_ACTION_TYPES_2_BASE_PATH: str = "RoomService/ListActionTypes2"
LIST_CONDITION_TYPES_2_BASE_PATH: str = "RoomService/ListConditionTypes2"
LIST_CRAFT_DESIGNS_BASE_PATH: str = "RoomService/ListCraftDesigns"
LIST_MISSILE_DESIGNS_BASE_PATH: str = "RoomService/ListMissileDesigns"
LIST_ROOM_DESIGN_PURCHASE_BASE_PATH: str = "RoomService/ListRoomDesignPurchase"
LIST_ROOM_DESIGNS_2_BASE_PATH: str = "RoomService/ListRoomDesigns2"
MOVE_ROOM_BASE_PATH: str = "RoomService/MoveRoom"
REBUILD_AMMO_2_BASE_PATH: str = "RoomService/RebuildAmmo2"


# ---------- Endpoints ----------


async def collect_all_resources(production_server: str, access_token: str, collect_date: str, item_type: str, **params) -> _List[_Item]:
    params = {"accessToken": access_token, "collectDate": collect_date, "itemType": item_type, **params}
    result = await _core.get_entities_from_path(((_Item, "Items", True),), "Items", production_server, COLLECT_ALL_RESOURCES_BASE_PATH, "POST", **params)
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


async def move_room(production_server: str, access_token: str, column: int, room_id: int, row: int, **params) -> _Room:
    params = {"accessToken": access_token, "column": column, "roomId": room_id, "row": row, **params}
    result = await _core.get_entities_from_path(((_Room, "Room", False),), "MoveRoom", production_server, MOVE_ROOM_BASE_PATH, "POST", **params)
    return result


async def rebuild_ammo_2(production_server: str, access_token: str, ammo_category: str, checksum: str, client_date_time: str, **params) -> _List[_Room]:
    params = {"accessToken": access_token, "ammoCategory": ammo_category, "checksum": checksum, "clientDateTime": client_date_time, **params}
    result = await _core.get_entities_from_path(((_Room, "Rooms", True),), "Rooms", production_server, REBUILD_AMMO_2_BASE_PATH, "POST", **params)
    return result
