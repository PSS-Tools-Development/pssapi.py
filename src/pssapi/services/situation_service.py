from typing import List

from pssapi.services import service_base

from ..entities import SituationDesign
from .raw import SituationServiceRaw


class SituationService(service_base.CacheableServiceBase):
    @service_base.cache_endpoint("SituationDesignVersion")
    async def list_situation_designs(self, client_date_time: str, design_version: int = None) -> List[SituationDesign]:
        production_server = await self.get_production_server()
        result = await SituationServiceRaw.list_situation_designs(production_server, client_date_time, design_version, self.language_key)
        return result
