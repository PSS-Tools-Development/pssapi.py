from typing import List as _List
from typing import Tuple as _Tuple

from .raw import LeagueServiceRaw as _LeagueServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import League as _League


class LeagueService(_ServiceBase):
    async def list_leagues(self, access_token: str, design_version: int = None) -> _List[_League]:
        production_server = await self.get_production_server()
        result = await _LeagueServiceRaw.list_leagues_2(production_server, access_token, design_version, self.language_key)
        return result

