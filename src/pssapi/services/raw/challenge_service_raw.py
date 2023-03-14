"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import ChallengeDesign as _ChallengeDesign

# ---------- Constants ----------

LIST_ALL_CHALLENGE_DESIGNS_2_BASE_PATH: str = "ChallengeService/ListAllChallengeDesigns2"


# ---------- Endpoints ----------


async def list_all_challenge_designs_2(production_server: str, design_version: int, language_key: str, **params) -> _List[_ChallengeDesign]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_ChallengeDesign, "ChallengeDesigns", True),), "ChallengeDesigns", production_server, LIST_ALL_CHALLENGE_DESIGNS_2_BASE_PATH, "GET", **params)
    return result
