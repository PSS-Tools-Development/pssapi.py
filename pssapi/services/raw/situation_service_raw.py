"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import SituationDesign as _SituationDesign

# ---------- Constants ----------

LIST_SITUATION_DESIGNS_BASE_PATH: str = 'SituationService/ListSituationDesigns'


# ---------- Endpoints ----------

async def list_situation_designs(production_server: str, language_key: str, design_version: int, **params) -> _List[_SituationDesign]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
        **params
    }
    result = await _core.get_entities_from_path(_SituationDesign, 'SituationDesigns', production_server, LIST_SITUATION_DESIGNS_BASE_PATH, **params)
    return result
