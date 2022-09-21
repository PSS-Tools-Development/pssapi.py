from typing import List as _List

from .raw import LeagueServiceRaw as _LeagueServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import League as _League


class LeagueService(_ServiceBase, _LeagueServiceRaw):
    async def list_leagues_2(self, **params) -> _List[_League]:
        return await self._list_leagues_2(self.production_server, self.language_key, self.access_token, **params)

    def __repr__(self) -> str:
        return f'<LeagueService: {self.name}>'

    def __str__(self) -> str:
        return f'<LeagueService: {self.name}>'
