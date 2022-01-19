"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import CharacterDesign as _CharacterDesign
from ...entities import CharacterDesignAction as _CharacterDesignAction
from ...entities import DrawDesign as _DrawDesign
from ...entities import Prestige as _Prestige

# ---------- Constants ----------

LIST_ALL_CHARACTER_DESIGN_ACTIONS_BASE_PATH: str = "CharacterService/ListAllCharacterDesignActions"
LIST_ALL_CHARACTER_DESIGNS_2_BASE_PATH: str = "CharacterService/ListAllCharacterDesigns2"
LIST_ALL_DRAW_DESIGNS_BASE_PATH: str = "CharacterService/ListAllDrawDesigns"
PRESTIGE_CHARACTER_FROM_BASE_PATH: str = "CharacterService/PrestigeCharacterFrom"
PRESTIGE_CHARACTER_TO_BASE_PATH: str = "CharacterService/PrestigeCharacterTo"


# ---------- Endpoints ----------


async def list_all_character_design_actions(production_server: str, design_version: int, **params) -> _List[_CharacterDesignAction]:
    params = {"designVersion": design_version, **params}
    result = await _core.get_entities_from_path(
        ((_CharacterDesignAction, "CharacterDesignActions", True),), "CharacterDesignActions", production_server, LIST_ALL_CHARACTER_DESIGN_ACTIONS_BASE_PATH, "GET", **params
    )
    return result


async def list_all_character_designs_2(production_server: str, design_version: int, language_key: str, **params) -> _List[_CharacterDesign]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_CharacterDesign, "CharacterDesigns", True),), "CharacterDesigns", production_server, LIST_ALL_CHARACTER_DESIGNS_2_BASE_PATH, "GET", **params)
    return result


async def list_all_draw_designs(production_server: str, design_version: int, language_key: str, **params) -> _List[_DrawDesign]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_DrawDesign, "DrawDesigns", True),), "DrawDesigns", production_server, LIST_ALL_DRAW_DESIGNS_BASE_PATH, "GET", **params)
    return result


async def prestige_character_from(production_server: str, character_design_id: int, **params) -> _List[_Prestige]:
    params = {"characterDesignId": character_design_id, **params}
    result = await _core.get_entities_from_path(((_Prestige, "Prestiges", True),), "Prestiges", production_server, PRESTIGE_CHARACTER_FROM_BASE_PATH, "GET", **params)
    return result


async def prestige_character_to(production_server: str, character_design_id: int, **params) -> _List[_Prestige]:
    params = {"characterDesignId": character_design_id, **params}
    result = await _core.get_entities_from_path(((_Prestige, "Prestiges", True),), "Prestiges", production_server, PRESTIGE_CHARACTER_TO_BASE_PATH, "GET", **params)
    return result
