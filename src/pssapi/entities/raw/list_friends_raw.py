"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, List, Optional

from pydantic_xml import attr, element, wrapped


if TYPE_CHECKING:
    from pssapi import entities

from .entity_base_raw import EntityBaseRaw


class ListFriendsRaw(EntityBaseRaw, tag="ListFriends"):
    XML_NODE_NAME: str = "ListFriends"

    friends: List["entities.Friend"] = wrapped("Friends", element(tag="Friend", default_factory=list))
    user_id: Optional[int] = attr(name="UserId", default=None)

    def _key(self):
        return (
            tuple(child._key() for child in self.friends),
            self.user_id,
        )


__all__ = [
    "ListFriendsRaw",
]
