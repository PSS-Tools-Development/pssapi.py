from typing import List as _List

from .raw import LiveOpsServiceRaw as _LiveOpsServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import GetCatalogQuantity as _GetCatalogQuantity


class LiveOpsService(_ServiceBase):
    async def get_catalog_quantity(self, ) -> _List[_GetCatalogQuantity]:
        result = await _LiveOpsServiceRaw.get_catalog_quantity(self.production_server)
        return result
