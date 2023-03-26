from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityBase as _EntityBase
from .raw import ListFriendsRaw as _ListFriendsRaw


class ListFriends(_ListFriendsRaw, _EntityBase):
    def __init__(self, list_friends_info: _EntityInfo) -> None:
        super().__init__(list_friends_info)
