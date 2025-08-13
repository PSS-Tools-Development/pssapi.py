from typing import List

from pssapi.services import service_base

from ..entities import TrainingDesign
from .raw import TrainingServiceRaw


class TrainingService(service_base.CacheableServiceBase):
    @service_base.cache_endpoint("TrainingDesignVersion")
    async def list_all_training_designs(self, client_date_time: str, design_version: int = None) -> List[TrainingDesign]:
        production_server = await self.get_production_server()
        result = await TrainingServiceRaw.list_all_training_designs_2(production_server, client_date_time, design_version, self.language_key)
        return result
