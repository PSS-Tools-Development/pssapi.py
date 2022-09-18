from typing import List as _List

from .raw import BackgroundServiceRaw as _BackgroundServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import Background as _Background


class BackgroundService(_ServiceBase, _BackgroundServiceRaw):
    async def list_backgrounds(self, **params) -> _List[_Background]:
        return self._list_backgrounds(self.production_server, self.design_version, **params)

    def __repr__(self) -> str:
        return f'<BackgroundService: {self.name}>'

    def __str__(self) -> str:
        return f'<BackgroundService: {self.name}>'
