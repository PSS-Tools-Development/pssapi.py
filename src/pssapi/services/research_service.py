from typing import List

from pssapi.services import service_base

from ..entities import ResearchDesign
from .raw import ResearchServiceRaw


class ResearchService(service_base.CacheableServiceBase):
    @service_base.cache_endpoint("ResearchDesignVersion")
    async def list_all_research_designs(self, client_date_time: str, design_version: int = None) -> List[ResearchDesign]:
        production_server = await self.get_production_server()
        result = await ResearchServiceRaw.list_all_research_designs_2(production_server, client_date_time, design_version, self.language_key)
        return result
