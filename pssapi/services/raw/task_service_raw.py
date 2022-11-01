"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import TaskDesign as _TaskDesign


# ---------- Constants ----------

LIST_ALL_TASK_DESIGNS_2_BASE_PATH: str = 'TaskService/ListAllTaskDesigns2'


# ---------- Endpoints ----------

async def list_all_task_designs_2(production_server: str, language_key: str, design_version: int, **params) -> _List[_TaskDesign]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
        **params
    }
    result = await _core.get_entities_from_path(_TaskDesign, 'TaskDesigns', production_server, LIST_ALL_TASK_DESIGNS_2_BASE_PATH, **params)
    return result
