from typing import List as _List

from .raw import ResearchServiceRaw as _ResearchServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import ResearchDesign as _ResearchDesign


class ResearchService(_ServiceBase, _ResearchServiceRaw):
    async def list_all_research_designs_2(self, design_version: int = None, **params) -> _List[_ResearchDesign]:
        return await self._list_all_research_designs_2(self.production_server, self.language_key, design_version, **params)

    def __repr__(self) -> str:
        return f'<ResearchService: {self.name}>'

    def __str__(self) -> str:
        return f'<ResearchService: {self.name}>'
