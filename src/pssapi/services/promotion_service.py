from typing import List as _List

import pssapi.services.service_base as _service_base

from ..entities import PromotionDesign as _PromotionDesign
from .raw import PromotionServiceRaw as _PromotionServiceRaw


class PromotionService(_service_base.CacheableServiceBase):
    @_service_base.cache_endpoint("PromotionDesignVersion")
    async def list_all_promotion_designs(self, design_version: int = None) -> _List[_PromotionDesign]:
        production_server = await self.get_production_server()
        result = await _PromotionServiceRaw.list_all_promotion_designs_2(production_server, design_version, self.language_key)
        return result
