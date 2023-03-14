from typing import List as _List

import pssapi.services.service_base as _service_base

from ..entities import MissionDesign as _MissionDesign
from .raw import MissionServiceRaw as _MissionServiceRaw


class MissionService(_service_base.CacheableServiceBase):
    @_service_base.cache_endpoint("MissionDesignVersion")
    async def list_all_mission_designs(self, design_version: int = None) -> _List[_MissionDesign]:
        production_server = await self.get_production_server()
        result = await _MissionServiceRaw.list_all_mission_designs_4(production_server, design_version, self.language_key)
        return result
