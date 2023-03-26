from typing import List as _List

import pssapi.services.service_base as _service_base

from ..entities import ResearchDesign as _ResearchDesign
from .raw import ResearchServiceRaw as _ResearchServiceRaw


class ResearchService(_service_base.CacheableServiceBase):
    @_service_base.cache_endpoint("ResearchDesignVersion")
    async def list_all_research_designs(self, design_version: int = None) -> _List[_ResearchDesign]:
        production_server = await self.get_production_server()
        result = await _ResearchServiceRaw.list_all_research_designs_2(production_server, design_version, self.language_key)
        return result
