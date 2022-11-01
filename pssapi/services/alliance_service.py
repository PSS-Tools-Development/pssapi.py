from typing import List as _List

from .raw import AllianceServiceRaw as _AllianceServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import Alliance as _Alliance
from ..entities import User as _User


class AllianceService(_ServiceBase):
    async def list_alliances_by_championship_score_ranking(self, from_: int, to: int, access_token: str) -> _List[_Alliance]:
        result = await _AllianceServiceRaw.list_alliances_by_championship_score_ranking(self.production_server, from_, to, access_token)
        return result

    async def list_alliances_by_ranking(self, skip: int, take: int) -> _List[_Alliance]:
        result = await _AllianceServiceRaw.list_alliances_by_ranking(self.production_server, skip, take)
        return result

    async def list_users(self, alliance_id: int, skip: int, take: int, access_token: str) -> _List[_User]:
        result = await _AllianceServiceRaw.list_users_2(self.production_server, alliance_id, skip, take, access_token)
        return result

    async def search_alliances(self, name: str, skip: int, take: int, access_token: str) -> _List[_Alliance]:
        result = await _AllianceServiceRaw.search_alliances(self.production_server, name, skip, take, access_token)
        return result
