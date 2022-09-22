from typing import List as _List

from .raw import AllianceServiceRaw as _AllianceServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import Alliance as _Alliance
from ..entities import User as _User


class AllianceService(_ServiceBase, _AllianceServiceRaw):
    async def list_alliances_by_championship_score_ranking(self, from_: int, to: int, access_token: str, **params) -> _List[_Alliance]:
        return await self._list_alliances_by_championship_score_ranking(self.production_server, from_, to, access_token, **params)

    async def list_alliances_by_ranking(self, skip: int, take: int, **params) -> _List[_Alliance]:
        return await self._list_alliances_by_ranking(self.production_server, skip, take, **params)

    async def list_users_2(self, alliance_id: int, skip: int, take: int, access_token: str, **params) -> _List[_User]:
        return await self._list_users_2(self.production_server, alliance_id, skip, take, access_token, **params)

    async def search_alliances(self, name: str, skip: int, take: int, access_token: str, **params) -> _List[_Alliance]:
        return await self._search_alliances(self.production_server, name, skip, take, access_token, **params)

    def __repr__(self) -> str:
        return f'<AllianceService: {self.name}>'

    def __str__(self) -> str:
        return f'<AllianceService: {self.name}>'
