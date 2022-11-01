"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import RewardDesign as _RewardDesign

# ---------- Constants ----------

LIST_ALL_REWARD_DESIGNS_2_BASE_PATH: str = 'RewardService/ListAllRewardDesigns2'


# ---------- Endpoints ----------

async def list_all_reward_designs_2(production_server: str, language_key: str, design_version: int, **params) -> _List[_RewardDesign]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
        **params
    }
    result = await _core.get_entities_from_path(_RewardDesign, 'RewardDesigns', production_server, LIST_ALL_REWARD_DESIGNS_2_BASE_PATH, **params)
    return result
