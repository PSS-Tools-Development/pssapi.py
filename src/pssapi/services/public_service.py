import pssapi.services.service_base as _service_base

from ..entities import Ship as _Ship
from .raw import PublicServiceRaw as _PublicServiceRaw


class PublicService(_service_base.ServiceBase):
    async def get_ship_details(self, access_token: str, user_id: int) -> _Ship:
        """
        Parameter 'access_token' needs to be a permanent token. A generated token doesn't work.
        """
        production_server = await self.get_production_server()
        result = await _PublicServiceRaw.get_ship_details(production_server, access_token, user_id)
        return result

    async def get_ship_room_details(self, access_token: str, user_id: int) -> _Ship:
        """
        Parameter 'access_token' needs to be a permanent token. A generated token doesn't work.
        """
        production_server = await self.get_production_server()
        result = await _PublicServiceRaw.get_ship_room_details(production_server, access_token, user_id)
        return result
