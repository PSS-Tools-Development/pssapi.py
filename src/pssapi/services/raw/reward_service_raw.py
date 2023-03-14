"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import RewardDesign as _RewardDesign

# ---------- Constants ----------

LIST_ALL_REWARD_DESIGNS_2_BASE_PATH: str = "RewardService/ListAllRewardDesigns2"


# ---------- Endpoints ----------


async def list_all_reward_designs_2(production_server: str, design_version: int, language_key: str, **params) -> _List[_RewardDesign]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_RewardDesign, "RewardDesigns", True),), "RewardDesigns", production_server, LIST_ALL_REWARD_DESIGNS_2_BASE_PATH, "GET", **params)
    return result
