from typing import List as _List

from .raw import LadderServiceRaw as _LadderServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import User as _User


class LadderService(_ServiceBase, _LadderServiceRaw):
    async def list_users_by_championship_score_ranking(self, **params) -> _List[_User]:
        return self._list_users_by_championship_score_ranking(self.production_server, self.from_, self.to, self.access_token, **params)

    async def list_users_by_ranking(self, **params) -> _List[_User]:
        return self._list_users_by_ranking(self.production_server, self.from_, self.access_token, **params)

    def __repr__(self) -> str:
        return f'<LadderService: {self.name}>'

    def __str__(self) -> str:
        return f'<LadderService: {self.name}>'
