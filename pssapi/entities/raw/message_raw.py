####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class MessageRaw():
    XML_NODE_NAME: str = 'Message'

    def __init__(self, message_info: _EntityInfo) -> None:
        self.__user_name: str = _parse.pss_str(message_info.get('UserName'))
        self.__alliance_name: str = _parse.pss_str(message_info.get('AllianceName'))
        self.__activity_type: str = _parse.pss_str(message_info.get('ActivityType'))
        self.__argument: str = _parse.pss_str(message_info.get('Argument'))
        self.__sale_id: int = _parse.pss_int(message_info.get('SaleId'))
        self.__message_id: int = _parse.pss_int(message_info.get('MessageId'))
        self.__message_date: datetime = _parse.pss_datetime(message_info.get('MessageDate'))
        self.__ship_design_id: int = _parse.pss_int(message_info.get('ShipDesignId'))
        self.__message: str = _parse.pss_str(message_info.get('Message'))
        self.__activity_argument: int = _parse.pss_int(message_info.get('ActivityArgument'))
        self.__user_id: int = _parse.pss_int(message_info.get('UserId'))
        self.__border_sprite_id: int = _parse.pss_int(message_info.get('BorderSpriteId'))
        self.__user_sprite_id: int = _parse.pss_int(message_info.get('UserSpriteId'))
        self.__trophy: int = _parse.pss_int(message_info.get('Trophy'))
        self.__alliance_sprite_id: int = _parse.pss_int(message_info.get('AllianceSpriteId'))
        self.__to_user_id: int = _parse.pss_int(message_info.get('ToUserId'))
        self.__alliance_id: int = _parse.pss_int(message_info.get('AllianceId'))
        self.__message_type: str = _parse.pss_str(message_info.get('MessageType'))
        self.__channel_id: int = _parse.pss_int(message_info.get('ChannelId'))

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def alliance_name(self) -> str:
        return self.__alliance_name

    @property
    def activity_type(self) -> str:
        return self.__activity_type

    @property
    def argument(self) -> str:
        return self.__argument

    @property
    def sale_id(self) -> int:
        return self.__sale_id

    @property
    def message_id(self) -> int:
        return self.__message_id

    @property
    def message_date(self) -> datetime:
        return self.__message_date

    @property
    def ship_design_id(self) -> int:
        return self.__ship_design_id

    @property
    def message(self) -> str:
        return self.__message

    @property
    def activity_argument(self) -> int:
        return self.__activity_argument

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def border_sprite_id(self) -> int:
        return self.__border_sprite_id

    @property
    def user_sprite_id(self) -> int:
        return self.__user_sprite_id

    @property
    def trophy(self) -> int:
        return self.__trophy

    @property
    def alliance_sprite_id(self) -> int:
        return self.__alliance_sprite_id

    @property
    def to_user_id(self) -> int:
        return self.__to_user_id

    @property
    def alliance_id(self) -> int:
        return self.__alliance_id

    @property
    def message_type(self) -> str:
        return self.__message_type

    @property
    def channel_id(self) -> int:
        return self.__channel_id
