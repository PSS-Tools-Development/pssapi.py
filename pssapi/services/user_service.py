from typing import List as _List

from .raw import UserServiceRaw as _UserServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import User as _User
from ..entities import UserLogin as _UserLogin


class UserService(_ServiceBase):
    async def device_login(self) -> _List[_UserLogin]:
        result = await _UserServiceRaw.device_login_12(production_server=self.production_server)
        return result

    async def search_users(self, search_string: str) -> _List[_User]:
        result = await _UserServiceRaw.search_users(production_server=self.production_server, search_string=search_string)
        return result

    async def steam_login(self) -> _List[_UserLogin]:
        result = await _UserServiceRaw.steam_login_6(production_server=self.production_server)
        return result
