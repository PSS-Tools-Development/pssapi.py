from typing import List as _List
from typing import Tuple as _Tuple

from .raw import ChallengeServiceRaw as _ChallengeServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import ChallengeDesign as _ChallengeDesign


class ChallengeService(_ServiceBase):
    async def list_all_challenge_designs(self, design_version: int = None) -> _List[_ChallengeDesign]:
        production_server = await self.get_production_server()
        result = await _ChallengeServiceRaw.list_all_challenge_designs_2(production_server, design_version, self.language_key)
        return result

