####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class FriendRaw():
    XML_NODE_NAME: str = 'Friend'

    def __init__(self, friend_info: _EntityInfo) -> None:
        self.__id: int = _parse.pss_int(friend_info.get('Id'))
        self.__friend_user_id: int = _parse.pss_int(friend_info.get('FriendUserId'))
        self.__friend_type: str = _parse.pss_str(friend_info.get('FriendType'))
        self.__unread_messages: int = _parse.pss_int(friend_info.get('UnreadMessages'))
        self.__last_login_date: datetime = _parse.pss_datetime(friend_info.get('LastLoginDate'))
        self.__date_updated: datetime = _parse.pss_datetime(friend_info.get('DateUpdated'))
        self.__last_interaction_date: datetime = _parse.pss_datetime(friend_info.get('LastInteractionDate'))
        self.__name: str = _parse.pss_str(friend_info.get('Name'))
        self.__level: int = _parse.pss_int(friend_info.get('Level'))
        self.__friend_trophy: int = _parse.pss_int(friend_info.get('FriendTrophy'))
        self.__friend_icon_sprite_id: int = _parse.pss_int(friend_info.get('FriendIconSpriteId'))

    @property
    def id(self) -> int:
        return self.__id

    @property
    def friend_user_id(self) -> int:
        return self.__friend_user_id

    @property
    def friend_type(self) -> str:
        return self.__friend_type

    @property
    def unread_messages(self) -> int:
        return self.__unread_messages

    @property
    def last_login_date(self) -> datetime:
        return self.__last_login_date

    @property
    def date_updated(self) -> datetime:
        return self.__date_updated

    @property
    def last_interaction_date(self) -> datetime:
        return self.__last_interaction_date

    @property
    def name(self) -> str:
        return self.__name

    @property
    def level(self) -> int:
        return self.__level

    @property
    def friend_trophy(self) -> int:
        return self.__friend_trophy

    @property
    def friend_icon_sprite_id(self) -> int:
        return self.__friend_icon_sprite_id
