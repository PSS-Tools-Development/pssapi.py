from typing import List

from pssapi.services import service_base

from ..entities import Background
from .raw import BackgroundServiceRaw


class BackgroundService(service_base.CacheableServiceBase):
    @service_base.cache_endpoint("BackgroundVersion")
    async def list_backgrounds(self, client_date_time: str, design_version: int = None) -> List[Background]:
        production_server = await self.get_production_server()
        result = await BackgroundServiceRaw.list_backgrounds(production_server, client_date_time, design_version)
        return result
