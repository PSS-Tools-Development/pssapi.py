"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class FriendRaw(EntityBaseRaw, tag="Friend"):
    XML_NODE_NAME: str = "Friend"

    date_updated: Optional[datetime] = attr(name="DateUpdated", default=None)
    friend_icon_sprite_id: Optional[int] = attr(name="FriendIconSpriteId", default=None)
    friend_trophy: Optional[int] = attr(name="FriendTrophy", default=None)
    friend_type: Optional[str] = attr(name="FriendType", default=None)
    friend_user_id: Optional[int] = attr(name="FriendUserId", default=None)
    id_: Optional[int] = attr(name="Id", default=None)
    last_interaction_date: Optional[datetime] = attr(name="LastInteractionDate", default=None)
    last_login_date: Optional[datetime] = attr(name="LastLoginDate", default=None)
    level: Optional[int] = attr(name="Level", default=None)
    name: Optional[str] = attr(name="Name", default=None)
    unread_messages: Optional[int] = attr(name="UnreadMessages", default=None)

    def _key(self):
        return (
            self.date_updated,
            self.friend_icon_sprite_id,
            self.friend_trophy,
            self.friend_type,
            self.friend_user_id,
            self.id_,
            self.last_interaction_date,
            self.last_login_date,
            self.level,
            self.name,
            self.unread_messages,
        )


__all__ = [
    "FriendRaw",
]
