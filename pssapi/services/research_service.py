from datetime import datetime as _datetime
from typing import List as _List

from .raw import ResearchServiceRaw as _ResearchServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import ResearchDesign as _ResearchDesign
from ...entities import Research as _Research


class ResearchService(_ServiceBase):
    async def list_all_research_designs_2(self, language_key: str, design_version: int) -> _List[_ResearchDesign]:
        raise NotImplemented()
        result = await _ResearchServiceRaw.list_all_research_designs_2(self.production_server, language_key: str, design_version: int)
        return result


    async def list_all_researches(self, access_token: str, client_date_time: _datetime) -> _List[_Research]:
        raise NotImplemented()
        result = await _ResearchServiceRaw.list_all_researches(self.production_server, access_token: str, client_date_time: _datetime)
        return result


