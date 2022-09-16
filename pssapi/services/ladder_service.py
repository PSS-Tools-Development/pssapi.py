from typing import List as _List

from .raw import LadderServiceRaw as _LadderServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import FindUserRanking as _FindUserRanking


class LadderService(_ServiceBase):
    async def find_user_ranking(self, access_token: str) -> _List[_FindUserRanking]:
        raise NotImplemented()
        result = await _LadderServiceRaw.find_user_ranking(self.production_server, access_token: str)
        return result


