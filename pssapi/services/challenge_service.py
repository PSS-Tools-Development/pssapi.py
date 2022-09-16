from typing import List as _List

from .raw import ChallengeServiceRaw as _ChallengeServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import ChallengeDesign as _ChallengeDesign


class ChallengeService(_ServiceBase):
    async def list_all_challenge_designs_2(self, language_key: str, design_version: int) -> _List[_ChallengeDesign]:
        raise NotImplemented()
        result = await _ChallengeServiceRaw.list_all_challenge_designs_2(self.production_server, language_key: str, design_version: int)
        return result


