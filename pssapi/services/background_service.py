from typing import List as _List

from .raw import BackgroundServiceRaw as _BackgroundServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import Background as _Background


class BackgroundService(_ServiceBase):
    async def list_backgrounds(self, design_version: int) -> _List[_Background]:
        raise NotImplemented()
        result = await _BackgroundServiceRaw.list_backgrounds(self.production_server, design_version: int)
        return result


