from typing import List as _List

import pssapi.services.service_base as _service_base

from ..entities import SituationDesign as _SituationDesign
from .raw import SituationServiceRaw as _SituationServiceRaw


class SituationService(_service_base.CacheableServiceBase):
    @_service_base.cache_endpoint("SituationDesignVersion")
    async def list_situation_designs(self, design_version: int = None) -> _List[_SituationDesign]:
        production_server = await self.get_production_server()
        result = await _SituationServiceRaw.list_situation_designs(production_server, design_version, self.language_key)
        return result
