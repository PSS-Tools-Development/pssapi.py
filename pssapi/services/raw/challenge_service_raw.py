"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import ChallengeDesign as _ChallengeDesign


class ChallengeServiceRaw:

    SERVICE_NAME = 'ChallengeService'
    LIST_ALL_CHALLENGE_DESIGNS_2_BASE_PATH: str = 'ChallengeService/ListAllChallengeDesigns2'

    @staticmethod
    async def _list_all_challenge_designs_2(production_server: str, language_key: str, design_version: int = None, **params) -> _List[_ChallengeDesign]:
        params = {
            'languageKey': language_key,
            'designVersion': design_version,
            **params
        }
        result = await _core.get_entities_from_path(_ChallengeDesign, 'ChallengeDesigns', production_server, ChallengeServiceRaw.LIST_ALL_CHALLENGE_DESIGNS_2_BASE_PATH, **params)
        return result
