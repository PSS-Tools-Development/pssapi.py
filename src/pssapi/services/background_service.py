from typing import List as _List

import pssapi.services.service_base as _service_base

from ..entities import Background as _Background
from .raw import BackgroundServiceRaw as _BackgroundServiceRaw


class BackgroundService(_service_base.CacheableServiceBase):
    @_service_base.cache_endpoint("BackgroundVersion")
    async def list_backgrounds(self, design_version: int = None) -> _List[_Background]:
        production_server = await self.get_production_server()
        result = await _BackgroundServiceRaw.list_backgrounds(production_server, design_version)
        return result
