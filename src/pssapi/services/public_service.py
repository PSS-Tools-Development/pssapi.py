from pssapi.services import service_base

from ..entities import Ship
from .raw import PublicServiceRaw


class PublicService(service_base.ServiceBase):
    async def get_ship_details(self, access_token: str, user_id: int) -> Ship:
        production_server = await self.get_production_server()
        result = await PublicServiceRaw.get_ship_details(production_server, access_token, user_id)
        return result

    async def get_ship_room_details(self, access_token: str, user_id: int) -> Ship:
        production_server = await self.get_production_server()
        result = await PublicServiceRaw.get_ship_room_details(production_server, access_token, user_id)
        return result
