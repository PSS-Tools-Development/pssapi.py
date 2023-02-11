from typing import List as _List
from typing import Tuple as _Tuple

from .raw import RewardServiceRaw as _RewardServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import RewardDesign as _RewardDesign


class RewardService(_ServiceBase):
    async def list_all_reward_designs(self, design_version: int = None) -> _List[_RewardDesign]:
        production_server = await self.get_production_server()
        result = await _RewardServiceRaw.list_all_reward_designs_2(production_server, design_version, self.language_key)
        return result

