from pssapi.services import service_base

from ..entities import GetCatalogQuantity, LiveOps
from .raw import LiveOpsServiceRaw


class LiveOpsService(service_base.ServiceBase):
    async def get_catalog_quantity(self) -> GetCatalogQuantity:
        production_server = await self.get_production_server()
        result = await LiveOpsServiceRaw.get_catalog_quantity(production_server)
        return result

    async def get_today_live_ops(self, device_type: str) -> LiveOps:
        production_server = await self.get_production_server()
        result = await LiveOpsServiceRaw.get_today_live_ops_2(production_server, device_type, self.language_key)
        return result
