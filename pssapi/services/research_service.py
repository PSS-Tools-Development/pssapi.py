from typing import List as _List

from .raw import ResearchServiceRaw as _ResearchServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import ResearchDesign as _ResearchDesign


class ResearchService(_ServiceBase):
    async def list_all_research_designs(self, design_version: int = None) -> _List[_ResearchDesign]:
        result = await _ResearchServiceRaw.list_all_research_designs_2(self.production_server, design_version, self.language_key)
        return result
