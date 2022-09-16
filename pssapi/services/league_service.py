from typing import List as _List

from .raw import LeagueServiceRaw as _LeagueServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import League as _League


class LeagueService(_ServiceBase):
    async def list_leagues_2(self, language_key: str, access_token: str, design_version: int) -> _List[_League]:
        raise NotImplemented()
        result = await _LeagueServiceRaw.list_leagues_2(self.production_server, language_key: str, access_token: str, design_version: int)
        return result


