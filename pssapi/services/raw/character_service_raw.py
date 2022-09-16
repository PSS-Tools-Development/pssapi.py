####################################################
##   This file has been generated automatically   ##
####################################################

from datetime import datetime as _datetime
from typing import List as _List

from ... import core as _core
from ...entities import CharacterDesignAction as _CharacterDesignAction
from ...entities import DrawDesign as _DrawDesign
from ...entities import CharacterDesign as _CharacterDesign
from ...entities import Character as _Character
from ...entities import CharacterAction as _CharacterAction



# ---------- Constants ----------

LIST_ALL_CHARACTER_DESIGN_ACTIONS_BASE_PATH: str = 'CharacterService/ListAllCharacterDesignActions'
LIST_ALL_CHARACTER_DESIGNS_2_BASE_PATH: str = 'CharacterService/ListAllCharacterDesigns2'
LIST_ALL_CHARACTERS_OF_USER_BASE_PATH: str = 'CharacterService/ListAllCharactersOfUser'
LIST_ALL_DRAW_DESIGNS_BASE_PATH: str = 'CharacterService/ListAllDrawDesigns'
LIST_CHARACTER_ACTIONS_BY_SHIP_ID_BASE_PATH: str = 'CharacterService/ListCharacterActionsByShipId'


# ---------- Endpoints ----------

async def list_all_character_design_actions(production_server: str, design_version: int, **params) -> _List[_CharacterDesignAction]:
    params = {
        'designVersion': design_version,
    }
    result = await _core.get_entities_from_path(_CharacterDesignAction, 'CharacterDesignActions', production_server, LIST_ALL_CHARACTER_DESIGN_ACTIONS_BASE_PATH, **params)
    return result


async def list_all_character_designs_2(production_server: str, language_key: str, design_version: int, **params) -> _List[_CharacterDesign]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
    }
    result = await _core.get_entities_from_path(_CharacterDesign, 'CharacterDesigns', production_server, LIST_ALL_CHARACTER_DESIGNS_2_BASE_PATH, **params)
    return result


async def list_all_characters_of_user(production_server: str, access_token: str, client_date_time: _datetime, **params) -> _List[_Character]:
    params = {
        'accessToken': access_token,
        'clientDateTime': client_date_time,
    }
    result = await _core.get_entities_from_path(_Character, 'Characters', production_server, LIST_ALL_CHARACTERS_OF_USER_BASE_PATH, **params)
    return result


async def list_all_draw_designs(production_server: str, language_key: str, design_version: int, **params) -> _List[_DrawDesign]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
    }
    result = await _core.get_entities_from_path(_DrawDesign, 'DrawDesigns', production_server, LIST_ALL_DRAW_DESIGNS_BASE_PATH, **params)
    return result


async def list_character_actions_by_ship_id(production_server: str, ship_id: int, access_token: str, **params) -> _List[_CharacterAction]:
    params = {
        'shipId': ship_id,
        'accessToken': access_token,
    }
    result = await _core.get_entities_from_path(_CharacterAction, 'CharacterActions', production_server, LIST_CHARACTER_ACTIONS_BY_SHIP_ID_BASE_PATH, **params)
    return result


