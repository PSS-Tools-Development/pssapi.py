from typing import List as _List
from typing import Tuple as _Tuple

import pssapi.services.service_base as _service_base

from ..entities import Alliance as _Alliance
from ..entities import Character as _Character
from ..entities import Message as _Message
from ..entities import User as _User
from .raw import AllianceServiceRaw as _AllianceServiceRaw


class AllianceService(_service_base.ServiceBase):
    async def get_alliance(self, access_token: str, alliance_id: int) -> _Alliance:
        production_server = await self.get_production_server()
        result = await _AllianceServiceRaw.get_alliance(production_server, access_token, alliance_id)
        return result

    async def get_user(self, access_token: str, user_id: int) -> _User:
        production_server = await self.get_production_server()
        result = await _AllianceServiceRaw.get_user(production_server, access_token, user_id)
        return result

    async def list_alliances_by_championship_score_ranking(self, access_token: str, from_: int, to: int) -> _List[_Alliance]:
        production_server = await self.get_production_server()
        result = await _AllianceServiceRaw.list_alliances_by_championship_score_ranking(production_server, access_token, from_, to)
        return result

    async def list_alliances_by_ranking(self, skip: int, take: int) -> _List[_Alliance]:
        production_server = await self.get_production_server()
        result = await _AllianceServiceRaw.list_alliances_by_ranking(production_server, skip, take)
        return result

    async def list_alliances_with_division(self, division_design_id: int) -> _List[_Alliance]:
        production_server = await self.get_production_server()
        result = await _AllianceServiceRaw.list_alliances_with_division(production_server, division_design_id)
        return result

    async def list_characters_given_in_alliance(self, access_token: str, alliance_id: int, skip: int, take: int) -> _List[_Character]:
        production_server = await self.get_production_server()
        result = await _AllianceServiceRaw.list_characters_given_in_alliance(production_server, access_token, alliance_id, skip, take)
        return result

    async def list_users(self, access_token: str, alliance_id: int, skip: int, take: int) -> _Tuple[_List[_Message], _List[_User]]:
        production_server = await self.get_production_server()
        result = await _AllianceServiceRaw.list_users_2(production_server, access_token, alliance_id, skip, take)
        return result

    async def search_alliances(self, access_token: str, name: str, skip: int, take: int) -> _List[_Alliance]:
        production_server = await self.get_production_server()
        result = await _AllianceServiceRaw.search_alliances(production_server, access_token, name, skip, take)
        return result
