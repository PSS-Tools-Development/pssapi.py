from typing import List as _List
from typing import Tuple as _Tuple

import pssapi.services.service_base as _service_base

from ..entities import Research as _Research
from ..entities import ResearchDesign as _ResearchDesign
from ..entities import User as _User
from .raw import ResearchServiceRaw as _ResearchServiceRaw


class ResearchService(_service_base.CacheableServiceBase):
    @_service_base.cache_endpoint("ResearchDesignVersion")
    async def list_all_research_designs(self, design_version: int = None) -> _List[_ResearchDesign]:
        production_server = await self.get_production_server()
        result = await _ResearchServiceRaw.list_all_research_designs_2(production_server, design_version, self.language_key)
        return result

    async def speed_up_research_using_boost_gauge(self, access_token: str, client_date_time: str, research_id: int) -> _Tuple[_Research, _User]:
        production_server = await self.get_production_server()
        result = await _ResearchServiceRaw.speed_up_research_using_boost_gauge(production_server, access_token, client_date_time, research_id)
        return result
