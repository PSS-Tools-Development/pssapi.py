from typing import List as _List

from .raw import LiveOpsServiceRaw as _LiveOpsServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import GetCatalogQuantity as _GetCatalogQuantity
from ..entities import LiveOps as _LiveOps


class LiveOpsService(_ServiceBase, _LiveOpsServiceRaw):
    async def get_catalog_quantity(self, **params) -> _List[_GetCatalogQuantity]:
        return await self._get_catalog_quantity(self.production_server, **params)

    async def get_today_live_ops_2(self, **params) -> _List[_LiveOps]:
        return await self._get_today_live_ops_2(self.production_server, self.language_key, self.device_type, **params)

    def __repr__(self) -> str:
        return f'<LiveOpsService: {self.name}>'

    def __str__(self) -> str:
        return f'<LiveOpsService: {self.name}>'
