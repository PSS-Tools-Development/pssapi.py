import pssapi.services.service_base as _service_base

from ..entities import GetCatalogQuantity as _GetCatalogQuantity
from ..entities import LiveOps as _LiveOps
from .raw import LiveOpsServiceRaw as _LiveOpsServiceRaw


class LiveOpsService(_service_base.ServiceBase):
    async def get_catalog_quantity(self) -> _GetCatalogQuantity:
        production_server = await self.get_production_server()
        result = await _LiveOpsServiceRaw.get_catalog_quantity(production_server)
        return result

    async def get_today_live_ops(self, device_type: str) -> _LiveOps:
        production_server = await self.get_production_server()
        result = await _LiveOpsServiceRaw.get_today_live_ops_2(production_server, device_type, self.language_key)
        return result
