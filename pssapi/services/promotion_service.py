from typing import List as _List

from .raw import PromotionServiceRaw as _PromotionServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import PromotionDesign as _PromotionDesign


class PromotionService(_ServiceBase):
    async def list_all_promotion_designs(self, design_version: int = None) -> _List[_PromotionDesign]:
        result = await _PromotionServiceRaw.list_all_promotion_designs_2(self.production_server, design_version, self.language_key)
        return result
