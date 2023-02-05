from typing import List as _List

from .raw import PromotionServiceRaw as _PromotionServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import PromotionDesign as _PromotionDesign
from ..entities import User as _User


class PromotionService(_ServiceBase):
    async def fix_user_promotions(self, access_token: str) -> _List[_User]:
        result = await _PromotionServiceRaw.fix_user_promotions((await self.get_production_server()), access_token)
        return result

    async def list_all_promotion_designs(self, design_version: int = None) -> _List[_PromotionDesign]:
        result = await _PromotionServiceRaw.list_all_promotion_designs_2((await self.get_production_server()), design_version, self.language_key)
        return result
