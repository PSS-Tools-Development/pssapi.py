from typing import List as _List

from .raw import AllianceServiceRaw as _AllianceServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import Alliance as _Alliance
from ..entities import Message as _Message


class AllianceService(_ServiceBase):
    async def list_alliances_by_championship_score_ranking(self, from_: int, to: int, access_token: str) -> _List[_Alliance]:
        result = await _AllianceServiceRaw.list_alliances_by_championship_score_ranking(production_server=self.production_server, from_=from_, to=to, access_token=access_token)
        return result

    async def list_alliances_by_ranking(self, take: int, skip: int) -> _List[_Alliance]:
        result = await _AllianceServiceRaw.list_alliances_by_ranking(production_server=self.production_server, take=take, skip=skip)
        return result

    async def list_users(self, take: int, skip: int, access_token: str, alliance_id: int) -> _List[_Message]:
        result = await _AllianceServiceRaw.list_users_2(production_server=self.production_server, take=take, skip=skip, access_token=access_token, alliance_id=alliance_id)
        return result

    async def search_alliances(self, take: int, skip: int, access_token: str, name: str) -> _List[_Alliance]:
        result = await _AllianceServiceRaw.search_alliances(production_server=self.production_server, take=take, skip=skip, access_token=access_token, name=name)
        return result
