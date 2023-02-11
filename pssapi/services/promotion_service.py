from typing import List as _List
from typing import Tuple as _Tuple

from .raw import PromotionServiceRaw as _PromotionServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import PromotionDesign as _PromotionDesign
from ..entities import User as _User


class PromotionService(_ServiceBase):
    async def fix_user_promotions(self, access_token: str) -> _List[_User]:
        production_server = await self.get_production_server()
        result = await _PromotionServiceRaw.fix_user_promotions(production_server, access_token)
        return result

    async def list_all_promotion_designs(self, design_version: int = None) -> _List[_PromotionDesign]:
        production_server = await self.get_production_server()
        result = await _PromotionServiceRaw.list_all_promotion_designs_2(production_server, design_version, self.language_key)
        return result

