from typing import List as _List

from .raw import AllianceServiceRaw as _AllianceServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import Alliance as _Alliance
from ..entities import User as _User


class AllianceService(_ServiceBase, _AllianceServiceRaw):
    async def list_alliances_by_championship_score_ranking(self, **params) -> _List[_Alliance]:
        return self._list_alliances_by_championship_score_ranking(self.production_server, self.from_, self.to, self.access_token, **params)

    async def list_alliances_by_ranking(self, **params) -> _List[_Alliance]:
        return self._list_alliances_by_ranking(self.production_server, self.skip, self.take, **params)

    async def list_users_2(self, **params) -> _List[_User]:
        return self._list_users_2(self.production_server, self.alliance_id, self.skip, self.take, self.access_token, **params)

    async def search_alliances(self, **params) -> _List[_Alliance]:
        return self._search_alliances(self.production_server, self.name, self.skip, self.take, self.access_token, **params)

    def __repr__(self) -> str:
        return f'<AllianceService: {self.name}>'

    def __str__(self) -> str:
        return f'<AllianceService: {self.name}>'
