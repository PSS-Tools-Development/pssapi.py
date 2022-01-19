from typing import List as _List

import pssapi.services.service_base as _service_base

from ..entities import DivisionDesign as _DivisionDesign
from .raw import DivisionServiceRaw as _DivisionServiceRaw


class DivisionService(_service_base.CacheableServiceBase):
    @_service_base.cache_endpoint("DivisionDesignVersion")
    async def list_all_division_designs(self, design_version: int = None) -> _List[_DivisionDesign]:
        production_server = await self.get_production_server()
        result = await _DivisionServiceRaw.list_all_division_designs_2(production_server, design_version, self.language_key)
        return result
