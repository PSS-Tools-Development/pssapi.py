"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr, element


if TYPE_CHECKING:
    from pssapi import entities

from .entity_base_raw import EntityBaseRaw


class UserEmailPasswordAuthorizeRaw(EntityBaseRaw, tag="UserEmailPasswordAuthorize"):
    XML_NODE_NAME: str = "UserEmailPasswordAuthorize"

    require_reload: Optional[str] = attr(name="RequireReload", default=None)
    user: Optional["entities.User"] = element(tag="User", default=None)
    user_id: Optional[str] = attr(name="UserId", default=None)
    error_message: Optional[str] = attr(name="errorMessage", default=None)
    refresh_token: Optional[str] = attr(name="refreshToken", default=None)

    def _key(self):
        return (
            self.require_reload,
            self.user._key() if self.user else None,
            self.user_id,
            self.error_message,
            self.refresh_token,
        )


__all__ = [
    "UserEmailPasswordAuthorizeRaw",
]
