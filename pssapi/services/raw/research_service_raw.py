"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import ResearchDesign as _ResearchDesign


# ---------- Constants ----------

LIST_ALL_RESEARCH_DESIGNS_2_BASE_PATH: str = 'ResearchService/ListAllResearchDesigns2'


# ---------- Endpoints ----------

async def list_all_research_designs_2(production_server: str, language_key: str, design_version: int, **params) -> _List[_ResearchDesign]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
        **params
    }
    result = await _core.get_entities_from_path(_ResearchDesign, 'ResearchDesigns', production_server, LIST_ALL_RESEARCH_DESIGNS_2_BASE_PATH, **params)
    return result
