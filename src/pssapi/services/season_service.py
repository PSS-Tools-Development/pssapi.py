from typing import List

from pssapi.services import service_base

from ..entities import SeasonDesign
from .raw import SeasonServiceRaw


class SeasonService(service_base.CacheableServiceBase):
    @service_base.cache_endpoint("SeasonDesignVersion")
    async def list_all_season_designs(self, client_date_time: str, design_version: int = None) -> List[SeasonDesign]:
        production_server = await self.get_production_server()
        result = await SeasonServiceRaw.list_all_season_designs(production_server, client_date_time, design_version, self.language_key)
        return result
