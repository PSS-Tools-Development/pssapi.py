from typing import List as _List

from .raw import LadderServiceRaw as _LadderServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import User as _User


class LadderService(_ServiceBase):
    async def list_users_by_championship_score_ranking(self, from_: int, to: int, access_token: str) -> _List[_User]:
        result = await _LadderServiceRaw.list_users_by_championship_score_ranking(production_server=self.production_server, from_=from_, to=to, access_token=access_token)
        return result

    async def list_users_by_ranking(self, to_100: str, from_: int, to: str, access_token: str) -> _List[_User]:
        result = await _LadderServiceRaw.list_users_by_ranking(production_server=self.production_server, to_100=to_100, from_=from_, to=to, access_token=access_token)
        return result
