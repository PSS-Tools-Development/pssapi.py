"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import ChallengeDesign as _ChallengeDesign


# ---------- Constants ----------

LIST_ALL_CHALLENGE_DESIGNS_2_BASE_PATH: str = 'ChallengeService/ListAllChallengeDesigns2'


# ---------- Endpoints ----------

async def list_all_challenge_designs_2(production_server: str, language_key: str, design_version: int, **params) -> _List[_ChallengeDesign]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
        **params
    }
    result = await _core.get_entities_from_path(_ChallengeDesign, 'ChallengeDesigns', production_server, LIST_ALL_CHALLENGE_DESIGNS_2_BASE_PATH, **params)
    return result
