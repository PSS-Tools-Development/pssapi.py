from typing import List as _List

from .raw import PromotionServiceRaw as _PromotionServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import PromotionDesign as _PromotionDesign


class PromotionService(_ServiceBase):
    async def list_all_promotion_designs_2(self, language_key: str, design_version: int) -> _List[_PromotionDesign]:
        raise NotImplemented()
        result = await _PromotionServiceRaw.list_all_promotion_designs_2(self.production_server, language_key: str, design_version: int)
        return result


