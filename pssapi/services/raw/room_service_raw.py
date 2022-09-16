####################################################
##   This file has been generated automatically   ##
####################################################

from datetime import datetime as _datetime
from typing import List as _List

from ... import core as _core
from ...entities import ConditionType as _ConditionType
from ...entities import RoomAction as _RoomAction
from ...entities import CraftDesign as _CraftDesign
from ...entities import ActionType as _ActionType
from ...entities import MissileDesign as _MissileDesign
from ...entities import Room as _Room
from ...entities import RoomDesignPurchase as _RoomDesignPurchase
from ...entities import RoomDesign as _RoomDesign



# ---------- Constants ----------

LIST_ACTION_TYPES_2_BASE_PATH: str = 'RoomService/ListActionTypes2'
LIST_ALL_ROOM_ACTIONS_OF_SHIP_BASE_PATH: str = 'RoomService/ListAllRoomActionsOfShip'
LIST_CONDITION_TYPES_2_BASE_PATH: str = 'RoomService/ListConditionTypes2'
LIST_CRAFT_DESIGNS_BASE_PATH: str = 'RoomService/ListCraftDesigns'
LIST_MISSILE_DESIGNS_BASE_PATH: str = 'RoomService/ListMissileDesigns'
LIST_ROOM_DESIGN_PURCHASE_BASE_PATH: str = 'RoomService/ListRoomDesignPurchase'
LIST_ROOM_DESIGNS_2_BASE_PATH: str = 'RoomService/ListRoomDesigns2'
LIST_ROOMS_VIA_ACCESS_TOKEN_BASE_PATH: str = 'RoomService/ListRoomsViaAccessToken'


# ---------- Endpoints ----------

async def list_action_types_2(production_server: str, language_key: str, design_version: int, **params) -> _List[_ActionType]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
    }
    result = await _core.get_entities_from_path(_ActionType, 'ActionTypes', production_server, LIST_ACTION_TYPES_2_BASE_PATH, **params)
    return result


async def list_all_room_actions_of_ship(production_server: str, ship_id: int, access_token: str, **params) -> _List[_RoomAction]:
    params = {
        'shipId': ship_id,
        'accessToken': access_token,
    }
    result = await _core.get_entities_from_path(_RoomAction, 'RoomActions', production_server, LIST_ALL_ROOM_ACTIONS_OF_SHIP_BASE_PATH, **params)
    return result


async def list_condition_types_2(production_server: str, language_key: str, design_version: int, **params) -> _List[_ConditionType]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
    }
    result = await _core.get_entities_from_path(_ConditionType, 'ConditionTypes', production_server, LIST_CONDITION_TYPES_2_BASE_PATH, **params)
    return result


async def list_craft_designs(production_server: str, design_version: int, **params) -> _List[_CraftDesign]:
    params = {
        'designVersion': design_version,
    }
    result = await _core.get_entities_from_path(_CraftDesign, 'CraftDesigns', production_server, LIST_CRAFT_DESIGNS_BASE_PATH, **params)
    return result


async def list_missile_designs(production_server: str, design_version: int, **params) -> _List[_MissileDesign]:
    params = {
        'designVersion': design_version,
    }
    result = await _core.get_entities_from_path(_MissileDesign, 'MissileDesigns', production_server, LIST_MISSILE_DESIGNS_BASE_PATH, **params)
    return result


async def list_room_design_purchase(production_server: str, design_version: int, **params) -> _List[_RoomDesignPurchase]:
    params = {
        'designVersion': design_version,
    }
    result = await _core.get_entities_from_path(_RoomDesignPurchase, 'RoomDesignPurchases', production_server, LIST_ROOM_DESIGN_PURCHASE_BASE_PATH, **params)
    return result


async def list_room_designs_2(production_server: str, language_key: str, design_version: int, **params) -> _List[_RoomDesign]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
    }
    result = await _core.get_entities_from_path(_RoomDesign, 'RoomDesigns', production_server, LIST_ROOM_DESIGNS_2_BASE_PATH, **params)
    return result


async def list_rooms_via_access_token(production_server: str, access_token: str, client_date_time: _datetime, **params) -> _List[_Room]:
    params = {
        'accessToken': access_token,
        'clientDateTime': client_date_time,
    }
    result = await _core.get_entities_from_path(_Room, 'Rooms', production_server, LIST_ROOMS_VIA_ACCESS_TOKEN_BASE_PATH, **params)
    return result


