from typing import List as _List

from .raw import PromotionServiceRaw as _PromotionServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import PromotionDesign as _PromotionDesign


class PromotionService(_ServiceBase, _PromotionServiceRaw):
    async def list_all_promotion_designs_2(self, **params) -> _List[_PromotionDesign]:
        return self._list_all_promotion_designs_2(self.production_server, self.language_key, **params)

    def __repr__(self) -> str:
        return f'<PromotionService: {self.name}>'

    def __str__(self) -> str:
        return f'<PromotionService: {self.name}>'
