from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityBase as _EntityBase
from .raw import UserEmailPasswordAuthorizeRaw as _UserEmailPasswordAuthorizeRaw


class UserEmailPasswordAuthorize(_UserEmailPasswordAuthorizeRaw, _EntityBase):
    def __init__(self, user_email_password_authorize_info: _EntityInfo) -> None:
        super().__init__(user_email_password_authorize_info)
