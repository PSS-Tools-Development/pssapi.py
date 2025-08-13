from .entity_base import EntityBase
from .raw import ListFriendsRaw


class ListFriends(ListFriendsRaw, EntityBase):
    pass


__all__ = [
    "ListFriends",
]
