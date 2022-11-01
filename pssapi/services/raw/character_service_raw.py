"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import CharacterDesign as _CharacterDesign
from ...entities import CharacterDesignAction as _CharacterDesignAction
from ...entities import DrawDesign as _DrawDesign

# ---------- Constants ----------

LIST_ALL_CHARACTER_DESIGN_ACTIONS_BASE_PATH: str = 'CharacterService/ListAllCharacterDesignActions'
LIST_ALL_CHARACTER_DESIGNS_2_BASE_PATH: str = 'CharacterService/ListAllCharacterDesigns2'
LIST_ALL_DRAW_DESIGNS_BASE_PATH: str = 'CharacterService/ListAllDrawDesigns'


# ---------- Endpoints ----------

async def list_all_character_design_actions(production_server: str, design_version: int, **params) -> _List[_CharacterDesignAction]:
    params = {
        'designVersion': design_version,
        **params
    }
    result = await _core.get_entities_from_path(_CharacterDesignAction, 'CharacterDesignActions', production_server, LIST_ALL_CHARACTER_DESIGN_ACTIONS_BASE_PATH, **params)
    return result


async def list_all_character_designs_2(production_server: str, language_key: str, design_version: int, **params) -> _List[_CharacterDesign]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
        **params
    }
    result = await _core.get_entities_from_path(_CharacterDesign, 'CharacterDesigns', production_server, LIST_ALL_CHARACTER_DESIGNS_2_BASE_PATH, **params)
    return result


async def list_all_draw_designs(production_server: str, language_key: str, design_version: int, **params) -> _List[_DrawDesign]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
        **params
    }
    result = await _core.get_entities_from_path(_DrawDesign, 'DrawDesigns', production_server, LIST_ALL_DRAW_DESIGNS_BASE_PATH, **params)
    return result
