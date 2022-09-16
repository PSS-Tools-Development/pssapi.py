from datetime import datetime as _datetime
from typing import List as _List

from .raw import TaskServiceRaw as _TaskServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import TaskDesign as _TaskDesign
from ...entities import Task as _Task


class TaskService(_ServiceBase):
    async def list_all_task_designs_2(self, language_key: str, design_version: int) -> _List[_TaskDesign]:
        raise NotImplemented()
        result = await _TaskServiceRaw.list_all_task_designs_2(self.production_server, language_key: str, design_version: int)
        return result


    async def list_tasks_of_a_user(self, access_token: str, client_date_time: _datetime) -> _List[_Task]:
        raise NotImplemented()
        result = await _TaskServiceRaw.list_tasks_of_a_user(self.production_server, access_token: str, client_date_time: _datetime)
        return result


