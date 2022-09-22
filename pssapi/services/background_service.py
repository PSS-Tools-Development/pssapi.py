from typing import List as _List

from .raw import BackgroundServiceRaw as _BackgroundServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import Background as _Background


class BackgroundService(_ServiceBase, _BackgroundServiceRaw):
    async def list_backgrounds(self, design_version: int = None, **params) -> _List[_Background]:
        return await self._list_backgrounds(self.production_server, design_version, **params)

    def __repr__(self) -> str:
        return f'<BackgroundService: {self.name}>'

    def __str__(self) -> str:
        return f'<BackgroundService: {self.name}>'
