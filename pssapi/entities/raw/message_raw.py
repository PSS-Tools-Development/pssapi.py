"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import List as _List

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class MessageRaw:
    XML_NODE_NAME: str = 'Message'

    def __init__(self, message_info: _EntityInfo) -> None:
        self.activity_argument: str = _parse.pss_str(message_info.get('ActivityArgument'))
        self.activity_type: str = _parse.pss_str(message_info.get('ActivityType'))
        self.alliance_id: int = _parse.pss_int(message_info.get('AllianceId'))
        self.alliance_name: str = _parse.pss_str(message_info.get('AllianceName'))
        self.alliance_sprite_id: int = _parse.pss_int(message_info.get('AllianceSpriteId'))
        self.argument: str = _parse.pss_str(message_info.get('Argument'))
        self.border_sprite_id: str = _parse.pss_str(message_info.get('BorderSpriteId'))
        self.channel_id: int = _parse.pss_int(message_info.get('ChannelId'))
        self.message: str = _parse.pss_str(message_info.get('Message'))
        self.message_date: _datetime = _parse.pss__datetime(message_info.get('MessageDate'))
        self.message_id: int = _parse.pss_int(message_info.get('MessageId'))
        self.message_type: str = _parse.pss_str(message_info.get('MessageType'))
        self.sale_id: str = _parse.pss_str(message_info.get('SaleId'))
        self.ship_design_id: int = _parse.pss_int(message_info.get('ShipDesignId'))
        self.trophy: int = _parse.pss_int(message_info.get('Trophy'))
        self.user_id: int = _parse.pss_int(message_info.get('UserId'))
        self.user_name: str = _parse.pss_str(message_info.get('UserName'))
        self.user_sprite_id: int = _parse.pss_int(message_info.get('UserSpriteId'))
