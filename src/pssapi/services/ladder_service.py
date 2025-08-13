from typing import List

from pssapi.services import service_base

from ..entities import User
from .raw import LadderServiceRaw


class LadderService(service_base.ServiceBase):
    async def list_users_by_championship_score_ranking(self, access_token: str, from_: int, to: int) -> List[User]:
        production_server = await self.get_production_server()
        result = await LadderServiceRaw.list_users_by_championship_score_ranking(production_server, access_token, from_, to)
        return result

    async def list_users_by_ranking(self, access_token: str, from_: int, to: int) -> List[User]:
        production_server = await self.get_production_server()
        result = await LadderServiceRaw.list_users_by_ranking(production_server, access_token, from_, to)
        return result
