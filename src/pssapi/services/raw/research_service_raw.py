"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from typing import List

from ... import core
from ...entities import ResearchDesign


# ---------- Constants ----------

LIST_ALL_RESEARCH_DESIGNS_2_BASE_PATH: str = "ResearchService/ListAllResearchDesigns2"

# ---------- Endpoint structure ----------


# ---------- Endpoints ----------


async def list_all_research_designs_2(production_server: str, client_date_time: str, design_version: int, language_key: str, **params) -> List[ResearchDesign]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, "languageKey": language_key, **params}
    result = await core.get_entities_from_path(
        ((ResearchDesign, "ResearchDesigns", True),), "ResearchDesigns", production_server, LIST_ALL_RESEARCH_DESIGNS_2_BASE_PATH, "GET", response_gzipped=False, **params
    )
    return result
