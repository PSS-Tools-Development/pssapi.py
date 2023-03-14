"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import TaskDesign as _TaskDesign

# ---------- Constants ----------

LIST_ALL_TASK_DESIGNS_2_BASE_PATH: str = "TaskService/ListAllTaskDesigns2"


# ---------- Endpoints ----------


async def list_all_task_designs_2(production_server: str, design_version: int, language_key: str, **params) -> _List[_TaskDesign]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_TaskDesign, "TaskDesigns", True),), "TaskDesigns", production_server, LIST_ALL_TASK_DESIGNS_2_BASE_PATH, "GET", **params)
    return result
