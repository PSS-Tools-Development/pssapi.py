"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import DivisionDesign as _DivisionDesign

# ---------- Constants ----------

LIST_ALL_DIVISION_DESIGNS_2_BASE_PATH: str = "DivisionService/ListAllDivisionDesigns2"


# ---------- Endpoints ----------


async def list_all_division_designs_2(production_server: str, design_version: int, language_key: str, **params) -> _List[_DivisionDesign]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_DivisionDesign, "DivisionDesigns", True),), "DivisionDesigns", production_server, LIST_ALL_DIVISION_DESIGNS_2_BASE_PATH, "GET", **params)
    return result
