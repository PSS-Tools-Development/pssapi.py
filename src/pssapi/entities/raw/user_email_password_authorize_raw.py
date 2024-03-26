"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

import pssapi.entities as _entities

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw


class UserEmailPasswordAuthorizeRaw(EntityBaseRaw):
    XML_NODE_NAME: str = "UserEmailPasswordAuthorize"

    def __init__(self, user_email_password_authorize_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._require_reload: str = _parse.pss_str(user_email_password_authorize_info.pop("RequireReload", None))
        self._user: _entities.User = _entities.User(user_email_password_authorize_info.pop("User")[0]) if user_email_password_authorize_info.get("User", []) else None
        self._user_id: str = _parse.pss_str(user_email_password_authorize_info.pop("UserId", None))
        self._error_message: str = _parse.pss_str(user_email_password_authorize_info.pop("errorMessage", None))
        self._refresh_token: str = _parse.pss_str(user_email_password_authorize_info.pop("refreshToken", None))
        super().__init__(user_email_password_authorize_info)

    @property
    def require_reload(self) -> str:
        return self._require_reload

    @property
    def user(self) -> "_entities.User":
        return self._user

    @property
    def user_id(self) -> str:
        return self._user_id

    @property
    def error_message(self) -> str:
        return self._error_message

    @property
    def refresh_token(self) -> str:
        return self._refresh_token

    def _key(self):
        return (
            self.require_reload,
            self.user._key() if self.user else None,
            self.user_id,
            self.error_message,
            self.refresh_token,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "RequireReload": self.require_reload,
                "User": dict(self.user) if self.user else None,
                "UserId": self.user_id,
                "errorMessage": self.error_message,
                "refreshToken": self.refresh_token,
            }
            self._dict.update(super().__dict__())

        return self._dict
