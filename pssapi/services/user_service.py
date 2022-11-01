from typing import List as _List

from .raw import UserServiceRaw as _UserServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import User as _User


class UserService(_ServiceBase):
    async def search_users(self, search_string: str) -> _List[_User]:
        result = await _UserServiceRaw.search_users(self.production_server, search_string)
        return result
