"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import RewardDesign as _RewardDesign


class RewardServiceRaw:

    SERVICE_NAME = 'RewardService'
    LIST_ALL_REWARD_DESIGNS_2_BASE_PATH: str = 'RewardService/ListAllRewardDesigns2'

    @staticmethod
    async def _list_all_reward_designs_2(production_server: str, language_key: str, design_version: int = None, **params) -> _List[_RewardDesign]:
        params = {
            'languageKey': language_key,
            'designVersion': design_version,
            **params
        }
        result = await _core.get_entities_from_path(_RewardDesign, 'RewardDesigns', production_server, RewardServiceRaw.LIST_ALL_REWARD_DESIGNS_2_BASE_PATH, **params)
        return result
