from typing import List as _List

from .raw import BackgroundServiceRaw as _BackgroundServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import Background as _Background


class BackgroundService(_ServiceBase):
    async def list_backgrounds(self, design_version: int = None) -> _List[_Background]:
        result = await _BackgroundServiceRaw.list_backgrounds((await self.get_production_server()), design_version)
        return result
