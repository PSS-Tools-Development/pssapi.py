from typing import List as _List

import pssapi.services.service_base as _service_base

from ..entities import TrainingDesign as _TrainingDesign
from .raw import TrainingServiceRaw as _TrainingServiceRaw


class TrainingService(_service_base.CacheableServiceBase):
    @_service_base.cache_endpoint("TrainingDesignVersion")
    async def list_all_training_designs(self, design_version: int = None) -> _List[_TrainingDesign]:
        production_server = await self.get_production_server()
        result = await _TrainingServiceRaw.list_all_training_designs_2(production_server, design_version, self.language_key)
        return result
