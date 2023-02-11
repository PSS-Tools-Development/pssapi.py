from typing import List as _List
from typing import Tuple as _Tuple

from .raw import TaskServiceRaw as _TaskServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import TaskDesign as _TaskDesign


class TaskService(_ServiceBase):
    async def list_all_task_designs(self, design_version: int = None) -> _List[_TaskDesign]:
        production_server = await self.get_production_server()
        result = await _TaskServiceRaw.list_all_task_designs_2(production_server, design_version, self.language_key)
        return result

