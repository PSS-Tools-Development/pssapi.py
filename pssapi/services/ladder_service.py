from typing import List as _List

from .raw import LadderServiceRaw as _LadderServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import User as _User


class LadderService(_ServiceBase, _LadderServiceRaw):
    async def list_users_by_championship_score_ranking(self, from_: int, to: int, access_token: str, **params) -> _List[_User]:
        return await self._list_users_by_championship_score_ranking(self.production_server, from_, to, access_token, **params)

    async def list_users_by_ranking(self, from_: int, to: int, access_token: str, **params) -> _List[_User]:
        return await self._list_users_by_ranking(self.production_server, from_, to, access_token, **params)

    def __repr__(self) -> str:
        return f'<LadderService: {self.name}>'

    def __str__(self) -> str:
        return f'<LadderService: {self.name}>'
