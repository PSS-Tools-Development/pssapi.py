from typing import List as _List

from .raw import ChallengeServiceRaw as _ChallengeServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import ChallengeDesign as _ChallengeDesign


class ChallengeService(_ServiceBase):
    async def list_all_challenge_designs(self, design_version: int = None) -> _List[_ChallengeDesign]:
        result = await _ChallengeServiceRaw.list_all_challenge_designs_2(self.production_server, self.language_key, design_version)
        return result
