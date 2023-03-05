"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import PromotionDesign as _PromotionDesign
from ...entities import User as _User

# ---------- Constants ----------

FIX_USER_PROMOTIONS_BASE_PATH: str = 'PromotionService/FixUserPromotions'
LIST_ALL_PROMOTION_DESIGNS_2_BASE_PATH: str = 'PromotionService/ListAllPromotionDesigns2'


# ---------- Endpoints ----------

async def fix_user_promotions(production_server: str, access_token: str, **params) -> _User:
    params = {
        'accessToken': access_token,
        **params
    }
    result = await _core.get_entities_from_path(((_User, 'FixUserPromotions', False),), 'FixUserPromotions', production_server, FIX_USER_PROMOTIONS_BASE_PATH, 'POST', **params)
    return result


async def list_all_promotion_designs_2(production_server: str, design_version: int, language_key: str, **params) -> _List[_PromotionDesign]:
    params = {
        'designVersion': design_version,
        'languageKey': language_key,
        **params
    }
    result = await _core.get_entities_from_path(((_PromotionDesign, 'PromotionDesigns', True),), 'PromotionDesigns', production_server, LIST_ALL_PROMOTION_DESIGNS_2_BASE_PATH, 'GET', **params)
    return result
