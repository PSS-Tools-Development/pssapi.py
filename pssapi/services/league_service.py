from typing import List as _List

from .raw import LeagueServiceRaw as _LeagueServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import League as _League


class LeagueService(_ServiceBase):
    async def list_leagues(self, access_token: str, design_version: int = None) -> _List[_League]:
        result = await _LeagueServiceRaw.list_leagues_2(production_server=self.production_server, design_version=design_version, language_key=self.language_key, access_token=access_token)
        return result
