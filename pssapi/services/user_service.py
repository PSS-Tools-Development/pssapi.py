from typing import List as _List

from .raw import UserServiceRaw as _UserServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import User as _User


class UserService(_ServiceBase, _UserServiceRaw):
    async def search_users(self, **params) -> _List[_User]:
        return self._search_users(self.production_server, self.search_string, **params)

    def __repr__(self) -> str:
        return f'<UserService: {self.name}>'

    def __str__(self) -> str:
        return f'<UserService: {self.name}>'
