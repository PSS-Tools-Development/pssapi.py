####################################################
##   This file has been generated automatically   ##
####################################################

from typing import List as _List

from ... import core as _core
from ...entities import PromotionDesign as _PromotionDesign



# ---------- Constants ----------

LIST_ALL_PROMOTION_DESIGNS_2_BASE_PATH: str = 'PromotionService/ListAllPromotionDesigns2'


# ---------- Endpoints ----------

async def list_all_promotion_designs_2(production_server: str, language_key: str, design_version: int, **params) -> _List[_PromotionDesign]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
    }
    result = await _core.get_entities_from_path(_PromotionDesign, 'PromotionDesigns', production_server, LIST_ALL_PROMOTION_DESIGNS_2_BASE_PATH, **params)
    return result

