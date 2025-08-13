from typing import List, Tuple

from pssapi.services import service_base

from ..entities import Alliance, Character, Message, User
from .raw import AllianceServiceRaw


class AllianceService(service_base.ServiceBase):
    async def get_alliance(self, access_token: str, alliance_id: int) -> Alliance:
        production_server = await self.get_production_server()
        result = await AllianceServiceRaw.get_alliance(production_server, access_token, alliance_id)
        return result

    async def get_user(self, access_token: str, user_id: int) -> User:
        production_server = await self.get_production_server()
        result = await AllianceServiceRaw.get_user(production_server, access_token, user_id)
        return result

    async def list_alliances_by_championship_score_ranking(self, access_token: str, from_: int, to: int) -> List[Alliance]:
        production_server = await self.get_production_server()
        result = await AllianceServiceRaw.list_alliances_by_championship_score_ranking(production_server, access_token, from_, to)
        return result

    async def list_alliances_by_ranking(self, skip: int, take: int) -> List[Alliance]:
        production_server = await self.get_production_server()
        result = await AllianceServiceRaw.list_alliances_by_ranking(production_server, skip, take)
        return result

    async def list_alliances_with_division(self, division_design_id: int) -> List[Alliance]:
        production_server = await self.get_production_server()
        result = await AllianceServiceRaw.list_alliances_with_division(production_server, division_design_id)
        return result

    async def list_characters_given_in_alliance(self, access_token: str, alliance_id: int, skip: int, take: int) -> List[Character]:
        production_server = await self.get_production_server()
        result = await AllianceServiceRaw.list_characters_given_in_alliance(production_server, access_token, alliance_id, skip, take)
        return result

    async def list_users(self, access_token: str, alliance_id: int, skip: int, take: int) -> Tuple[List[Message], List[User]]:
        production_server = await self.get_production_server()
        result = await AllianceServiceRaw.list_users_2(production_server, access_token, alliance_id, skip, take)
        return result

    async def search_alliances(self, access_token: str, name: str, skip: int, take: int) -> List[Alliance]:
        production_server = await self.get_production_server()
        result = await AllianceServiceRaw.search_alliances(production_server, access_token, name, skip, take)
        return result
