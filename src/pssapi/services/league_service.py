from typing import List

from pssapi.services import service_base

from ..entities import League
from .raw import LeagueServiceRaw


class LeagueService(service_base.CacheableServiceBase):
    @service_base.cache_endpoint("LeagueVersion")
    async def list_leagues(self, access_token: str, client_date_time: str, design_version: int = None) -> List[League]:
        production_server = await self.get_production_server()
        result = await LeagueServiceRaw.list_leagues_2(production_server, access_token, client_date_time, design_version, self.language_key)
        return result
