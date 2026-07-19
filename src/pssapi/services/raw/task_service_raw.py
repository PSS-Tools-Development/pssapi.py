"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from typing import List as _List
from typing import Tuple as _Tuple

from ... import core as _core
from ...entities import Item as _Item
from ...entities import Task as _Task
from ...entities import TaskDesign as _TaskDesign


# ---------- Constants ----------

COLLECT_TASK_COMPLETION_BASE_PATH: str = "TaskService/CollectTaskCompletion"
LIST_ALL_TASK_DESIGNS_2_BASE_PATH: str = "TaskService/ListAllTaskDesigns2"


# ---------- Endpoints ----------


async def collect_task_completion(production_server: str, access_token: str, task_design_id: int, **params) -> _Tuple[_Item, _List[_Task]]:
    params = {"accessToken": access_token, "taskDesignId": task_design_id, **params}
    result = await _core.get_entities_from_path(
        ((_Item, "Item", False), (_Task, "Tasks", True)), "CollectTaskCompletion", production_server, COLLECT_TASK_COMPLETION_BASE_PATH, "POST", response_gzipped=False, **params
    )
    return result


async def list_all_task_designs_2(production_server: str, client_date_time: str, design_version: int, language_key: str, **params) -> _List[_TaskDesign]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_TaskDesign, "TaskDesigns", True),), "TaskDesigns", production_server, LIST_ALL_TASK_DESIGNS_2_BASE_PATH, "GET", response_gzipped=False, **params)
    return result
