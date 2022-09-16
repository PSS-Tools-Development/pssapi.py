####################################################
##   This file has been generated automatically   ##
####################################################

from datetime import datetime as _datetime
from typing import List as _List

from ... import core as _core
from ...entities import Task as _Task
from ...entities import TaskDesign as _TaskDesign



# ---------- Constants ----------

LIST_ALL_TASK_DESIGNS_2_BASE_PATH: str = 'TaskService/ListAllTaskDesigns2'
LIST_TASKS_OF_A_USER_BASE_PATH: str = 'TaskService/ListTasksOfAUser'


# ---------- Endpoints ----------

async def list_all_task_designs_2(production_server: str, language_key: str, design_version: int, **params) -> _List[_TaskDesign]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
    }
    result = await _core.get_entities_from_path(_TaskDesign, 'TaskDesigns', production_server, LIST_ALL_TASK_DESIGNS_2_BASE_PATH, **params)
    return result


async def list_tasks_of_a_user(production_server: str, access_token: str, client_date_time: _datetime, **params) -> _List[_Task]:
    params = {
        'accessToken': access_token,
        'clientDateTime': client_date_time,
    }
    result = await _core.get_entities_from_path(_Task, 'Tasks', production_server, LIST_TASKS_OF_A_USER_BASE_PATH, **params)
    return result


