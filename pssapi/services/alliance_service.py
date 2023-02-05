from typing import List as _List

from .raw import AllianceServiceRaw as _AllianceServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import Alliance as _Alliance
from ..entities import Message as _Message


class AllianceService(_ServiceBase):
    async def list_alliances_by_championship_score_ranking(self, access_token: str, from_: int, to: int) -> _List[_Alliance]:
        result = await _AllianceServiceRaw.list_alliances_by_championship_score_ranking((await self.get_production_server()), access_token, from_, to)
        return result

    async def list_alliances_by_ranking(self, skip: int, take: int) -> _List[_Alliance]:
        result = await _AllianceServiceRaw.list_alliances_by_ranking((await self.get_production_server()), skip, take)
        return result

    async def list_users(self, access_token: str, alliance_id: int, skip: int, take: int) -> _List[_Message]:
        result = await _AllianceServiceRaw.list_users_2((await self.get_production_server()), access_token, alliance_id, skip, take)
        return result

    async def search_alliances(self, access_token: str, name: str, skip: int, take: int) -> _List[_Alliance]:
        result = await _AllianceServiceRaw.search_alliances((await self.get_production_server()), access_token, name, skip, take)
        return result
