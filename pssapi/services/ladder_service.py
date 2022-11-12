from typing import List as _List

from .raw import LadderServiceRaw as _LadderServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import User as _User


class LadderService(_ServiceBase):
    async def list_users_by_championship_score_ranking(self, access_token: str, from_: int, to: int) -> _List[_User]:
        result = await _LadderServiceRaw.list_users_by_championship_score_ranking(self.production_server, access_token, from_, to)
        return result

    async def list_users_by_ranking(self, access_token: str, from_: int, to: str) -> _List[_User]:
        result = await _LadderServiceRaw.list_users_by_ranking(self.production_server, access_token, from_, to)
        return result
