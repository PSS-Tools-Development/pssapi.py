"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr, element


if TYPE_CHECKING:
    from pssapi import entities

from .entity_base_raw import EntityBaseRaw


class UserLoginRaw(EntityBaseRaw, tag="UserLogin"):
    XML_NODE_NAME: str = "UserLogin"

    previous_last_login_date: Optional[datetime] = attr(name="PreviousLastLoginDate", default=None)
    user: Optional["entities.User"] = element(tag="User", default=None)
    user_id: Optional[int] = attr(name="UserId", default=None)
    access_token: Optional[str] = attr(name="accessToken", default=None)

    def _key(self):
        return (
            self.previous_last_login_date,
            self.user._key() if self.user else None,
            self.user_id,
            self.access_token,
        )


__all__ = [
    "UserLoginRaw",
]
