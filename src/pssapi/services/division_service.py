from typing import List

from pssapi.services import service_base

from ..entities import DivisionDesign
from .raw import DivisionServiceRaw


class DivisionService(service_base.CacheableServiceBase):
    @service_base.cache_endpoint("DivisionDesignVersion")
    async def list_all_division_designs(self, client_date_time: str, design_version: int = None) -> List[DivisionDesign]:
        production_server = await self.get_production_server()
        result = await DivisionServiceRaw.list_all_division_designs_2(production_server, client_date_time, design_version, self.language_key)
        return result
