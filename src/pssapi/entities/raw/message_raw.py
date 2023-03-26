"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class MessageRaw:
    XML_NODE_NAME: str = "Message"

    def __init__(self, message_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._activity_argument: str = _parse.pss_str(message_info.get("ActivityArgument"))
        self._activity_type: str = _parse.pss_str(message_info.get("ActivityType"))
        self._alliance_id: int = _parse.pss_int(message_info.get("AllianceId"))
        self._alliance_name: str = _parse.pss_str(message_info.get("AllianceName"))
        self._alliance_sprite_id: int = _parse.pss_int(message_info.get("AllianceSpriteId"))
        self._argument: str = _parse.pss_str(message_info.get("Argument"))
        self._border_sprite_id: str = _parse.pss_str(message_info.get("BorderSpriteId"))
        self._channel_id: int = _parse.pss_int(message_info.get("ChannelId"))
        self._message: str = _parse.pss_str(message_info.get("Message"))
        self._message_date: _datetime = _parse.pss_datetime(message_info.get("MessageDate"))
        self._message_id: int = _parse.pss_int(message_info.get("MessageId"))
        self._message_type: str = _parse.pss_str(message_info.get("MessageType"))
        self._sale_id: str = _parse.pss_str(message_info.get("SaleId"))
        self._ship_design_id: int = _parse.pss_int(message_info.get("ShipDesignId"))
        self._to_user_id: str = _parse.pss_str(message_info.get("ToUserId"))
        self._trophy: int = _parse.pss_int(message_info.get("Trophy"))
        self._user_id: int = _parse.pss_int(message_info.get("UserId"))
        self._user_name: str = _parse.pss_str(message_info.get("UserName"))
        self._user_sprite_id: int = _parse.pss_int(message_info.get("UserSpriteId"))

    @property
    def activity_argument(self) -> str:
        return self._activity_argument

    @property
    def activity_type(self) -> str:
        return self._activity_type

    @property
    def alliance_id(self) -> int:
        return self._alliance_id

    @property
    def alliance_name(self) -> str:
        return self._alliance_name

    @property
    def alliance_sprite_id(self) -> int:
        return self._alliance_sprite_id

    @property
    def argument(self) -> str:
        return self._argument

    @property
    def border_sprite_id(self) -> str:
        return self._border_sprite_id

    @property
    def channel_id(self) -> int:
        return self._channel_id

    @property
    def message(self) -> str:
        return self._message

    @property
    def message_date(self) -> _datetime:
        return self._message_date

    @property
    def message_id(self) -> int:
        return self._message_id

    @property
    def message_type(self) -> str:
        return self._message_type

    @property
    def sale_id(self) -> str:
        return self._sale_id

    @property
    def ship_design_id(self) -> int:
        return self._ship_design_id

    @property
    def to_user_id(self) -> str:
        return self._to_user_id

    @property
    def trophy(self) -> int:
        return self._trophy

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def user_name(self) -> str:
        return self._user_name

    @property
    def user_sprite_id(self) -> int:
        return self._user_sprite_id

    def _key(self):
        return (
            self.activity_argument,
            self.activity_type,
            self.alliance_id,
            self.alliance_name,
            self.alliance_sprite_id,
            self.argument,
            self.border_sprite_id,
            self.channel_id,
            self.message,
            self.message_date,
            self.message_id,
            self.message_type,
            self.sale_id,
            self.ship_design_id,
            self.to_user_id,
            self.trophy,
            self.user_id,
            self.user_name,
            self.user_sprite_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "ActivityArgument": self.activity_argument,
                "ActivityType": self.activity_type,
                "AllianceId": self.alliance_id,
                "AllianceName": self.alliance_name,
                "AllianceSpriteId": self.alliance_sprite_id,
                "Argument": self.argument,
                "BorderSpriteId": self.border_sprite_id,
                "ChannelId": self.channel_id,
                "Message": self.message,
                "MessageDate": self.message_date,
                "MessageId": self.message_id,
                "MessageType": self.message_type,
                "SaleId": self.sale_id,
                "ShipDesignId": self.ship_design_id,
                "ToUserId": self.to_user_id,
                "Trophy": self.trophy,
                "UserId": self.user_id,
                "UserName": self.user_name,
                "UserSpriteId": self.user_sprite_id,
            }

        return self._dict
