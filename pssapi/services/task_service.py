from typing import List as _List

from .raw import TaskServiceRaw as _TaskServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import TaskDesign as _TaskDesign


class TaskService(_ServiceBase, _TaskServiceRaw):
    async def list_all_task_designs_2(self, design_version: int = None, **params) -> _List[_TaskDesign]:
        return await self._list_all_task_designs_2(self.production_server, self.language_key, design_version, **params)

    def __repr__(self) -> str:
        return f'<TaskService: {self.name}>'

    def __str__(self) -> str:
        return f'<TaskService: {self.name}>'
