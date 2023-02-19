from typing import List as _List

from .raw import TaskServiceRaw as _TaskServiceRaw
import pssapi.services.service_base as _service_base
from ..entities import TaskDesign as _TaskDesign


class TaskService(_service_base.ServiceBase):
    async def list_all_task_designs(self, design_version: int = None) -> _List[_TaskDesign]:
        production_server = await self.get_production_server()
        result = await _TaskServiceRaw.list_all_task_designs_2(production_server, design_version, self.language_key)
        return result
