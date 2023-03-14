from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityBase as _EntityBase
from .raw import UserLoginRaw as _UserLoginRaw


class UserLogin(_UserLoginRaw, _EntityBase):
    def __init__(self, user_login_info: _EntityInfo) -> None:
        super().__init__(user_login_info)
