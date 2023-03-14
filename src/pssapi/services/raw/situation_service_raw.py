"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import SituationDesign as _SituationDesign

# ---------- Constants ----------

LIST_SITUATION_DESIGNS_BASE_PATH: str = "SituationService/ListSituationDesigns"


# ---------- Endpoints ----------


async def list_situation_designs(production_server: str, design_version: int, language_key: str, **params) -> _List[_SituationDesign]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_SituationDesign, "SituationDesigns", True),), "SituationDesigns", production_server, LIST_SITUATION_DESIGNS_BASE_PATH, "GET", **params)
    return result
