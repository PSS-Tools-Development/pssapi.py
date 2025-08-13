from typing import List

from pssapi.services import service_base

from ..entities import TaskDesign
from .raw import TaskServiceRaw


class TaskService(service_base.CacheableServiceBase):
    @service_base.cache_endpoint("TaskDesignVersion")
    async def list_all_task_designs(self, client_date_time: str, design_version: int = None) -> List[TaskDesign]:
        production_server = await self.get_production_server()
        result = await TaskServiceRaw.list_all_task_designs_2(production_server, client_date_time, design_version, self.language_key)
        return result
