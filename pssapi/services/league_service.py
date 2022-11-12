from typing import List as _List

from .raw import LeagueServiceRaw as _LeagueServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import League as _League


class LeagueService(_ServiceBase):
    async def list_leagues(self, access_token: str, design_version: int = None) -> _List[_League]:
        result = await _LeagueServiceRaw.list_leagues_2(self.production_server, access_token, design_version, self.language_key)
        return result
