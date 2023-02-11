from typing import List as _List
from typing import Tuple as _Tuple

from .raw import LiveOpsServiceRaw as _LiveOpsServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import GetCatalogQuantity as _GetCatalogQuantity
from ..entities import LiveOps as _LiveOps


class LiveOpsService(_ServiceBase):
    async def get_catalog_quantity(self) -> _List[_GetCatalogQuantity]:
        production_server = await self.get_production_server()
        result = await _LiveOpsServiceRaw.get_catalog_quantity(production_server)
        return result

    async def get_today_live_ops(self, device_type: str) -> _List[_LiveOps]:
        production_server = await self.get_production_server()
        result = await _LiveOpsServiceRaw.get_today_live_ops_2(production_server, device_type, self.language_key)
        return result

