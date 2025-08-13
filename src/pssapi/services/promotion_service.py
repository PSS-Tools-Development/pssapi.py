from typing import List

from pssapi.services import service_base

from ..entities import PromotionDesign
from .raw import PromotionServiceRaw


class PromotionService(service_base.CacheableServiceBase):
    @service_base.cache_endpoint("PromotionDesignVersion")
    async def list_all_promotion_designs(self, client_date_time: str, design_version: int = None) -> List[PromotionDesign]:
        production_server = await self.get_production_server()
        result = await PromotionServiceRaw.list_all_promotion_designs_2(production_server, client_date_time, design_version, self.language_key)
        return result
