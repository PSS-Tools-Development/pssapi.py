from typing import List as _List

from .raw import RewardServiceRaw as _RewardServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import RewardDesign as _RewardDesign


class RewardService(_ServiceBase):
    async def list_all_reward_designs_2(self, language_key: str, design_version: int) -> _List[_RewardDesign]:
        raise NotImplemented()
        result = await _RewardServiceRaw.list_all_reward_designs_2(self.production_server, language_key: str, design_version: int)
        return result


