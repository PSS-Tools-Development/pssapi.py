"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from typing import List

from ... import core
from ...entities import CharacterDesign, CharacterDesignAction, DrawDesign, Prestige


# ---------- Constants ----------

LIST_ALL_CHARACTER_DESIGN_ACTIONS_BASE_PATH: str = "CharacterService/ListAllCharacterDesignActions"
LIST_ALL_CHARACTER_DESIGNS_2_BASE_PATH: str = "CharacterService/ListAllCharacterDesigns2"
LIST_ALL_DRAW_DESIGNS_BASE_PATH: str = "CharacterService/ListAllDrawDesigns"
PRESTIGE_CHARACTER_FROM_BASE_PATH: str = "CharacterService/PrestigeCharacterFrom"
PRESTIGE_CHARACTER_TO_BASE_PATH: str = "CharacterService/PrestigeCharacterTo"

# ---------- Endpoint structure ----------


# ---------- Endpoints ----------


async def list_all_character_design_actions(production_server: str, client_date_time: str, design_version: int, **params) -> List[CharacterDesignAction]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, **params}
    result = await core.get_entities_from_path(
        ((CharacterDesignAction, "CharacterDesignActions", True),), "CharacterDesignActions", production_server, LIST_ALL_CHARACTER_DESIGN_ACTIONS_BASE_PATH, "GET", response_gzipped=False, **params
    )
    return result


async def list_all_character_designs_2(production_server: str, client_date_time: str, design_version: int, language_key: str, **params) -> List[CharacterDesign]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, "languageKey": language_key, **params}
    result = await core.get_entities_from_path(
        ((CharacterDesign, "CharacterDesigns", True),), "CharacterDesigns", production_server, LIST_ALL_CHARACTER_DESIGNS_2_BASE_PATH, "GET", response_gzipped=False, **params
    )
    return result


async def list_all_draw_designs(production_server: str, client_date_time: str, design_version: int, language_key: str, **params) -> List[DrawDesign]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, "languageKey": language_key, **params}
    result = await core.get_entities_from_path(((DrawDesign, "DrawDesigns", True),), "DrawDesigns", production_server, LIST_ALL_DRAW_DESIGNS_BASE_PATH, "GET", response_gzipped=False, **params)
    return result


async def prestige_character_from(production_server: str, character_design_id: int, **params) -> List[Prestige]:
    params = {"characterDesignId": character_design_id, **params}
    result = await core.get_entities_from_path(((Prestige, "Prestiges", True),), "Prestiges", production_server, PRESTIGE_CHARACTER_FROM_BASE_PATH, "GET", response_gzipped=False, **params)
    return result


async def prestige_character_to(production_server: str, character_design_id: int, **params) -> List[Prestige]:
    params = {"characterDesignId": character_design_id, **params}
    result = await core.get_entities_from_path(((Prestige, "Prestiges", True),), "Prestiges", production_server, PRESTIGE_CHARACTER_TO_BASE_PATH, "GET", response_gzipped=False, **params)
    return result
