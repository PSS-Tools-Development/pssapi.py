####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ListFriendsRaw():
    XML_NODE_NAME: str = 'ListFriends'

    def __init__(self, list_friends_info: _EntityInfo) -> None:
        self.__user_id: int = _parse.pss_int(list_friends_info.get('UserId'))

    @property
    def user_id(self) -> int:
        return self.__user_id
