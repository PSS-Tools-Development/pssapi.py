"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from typing import List

from ... import core
from ...entities import TaskDesign


# ---------- Constants ----------

LIST_ALL_TASK_DESIGNS_2_BASE_PATH: str = "TaskService/ListAllTaskDesigns2"

# ---------- Endpoint structure ----------


# ---------- Endpoints ----------


async def list_all_task_designs_2(production_server: str, client_date_time: str, design_version: int, language_key: str, **params) -> List[TaskDesign]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, "languageKey": language_key, **params}
    result = await core.get_entities_from_path(((TaskDesign, "TaskDesigns", True),), "TaskDesigns", production_server, LIST_ALL_TASK_DESIGNS_2_BASE_PATH, "GET", response_gzipped=False, **params)
    return result
