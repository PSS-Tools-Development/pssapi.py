"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw


class MessageRaw(EntityBaseRaw):
    XML_NODE_NAME: str = "Message"

    def __init__(self, message_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._activity_argument: str = _parse.pss_str(message_info.pop("ActivityArgument", None))
        self._activity_type: str = _parse.pss_str(message_info.pop("ActivityType", None))
        self._alliance_id: int = _parse.pss_int(message_info.pop("AllianceId", None))
        self._alliance_name: str = _parse.pss_str(message_info.pop("AllianceName", None))
        self._alliance_sprite_id: int = _parse.pss_int(message_info.pop("AllianceSpriteId", None))
        self._argument: str = _parse.pss_str(message_info.pop("Argument", None))
        self._border_sprite_id: str = _parse.pss_str(message_info.pop("BorderSpriteId", None))
        self._channel_id: int = _parse.pss_int(message_info.pop("ChannelId", None))
        self._message: str = _parse.pss_str(message_info.pop("Message", None))
        self._message_date: _datetime = _parse.pss_datetime(message_info.pop("MessageDate", None))
        self._message_id: int = _parse.pss_int(message_info.pop("MessageId", None))
        self._message_type: str = _parse.pss_str(message_info.pop("MessageType", None))
        self._sale_id: str = _parse.pss_str(message_info.pop("SaleId", None))
        self._ship_design_id: int = _parse.pss_int(message_info.pop("ShipDesignId", None))
        self._to_user_id: str = _parse.pss_str(message_info.pop("ToUserId", None))
        self._trophy: int = _parse.pss_int(message_info.pop("Trophy", None))
        self._user_id: int = _parse.pss_int(message_info.pop("UserId", None))
        self._user_name: str = _parse.pss_str(message_info.pop("UserName", None))
        self._user_sprite_id: int = _parse.pss_int(message_info.pop("UserSpriteId", None))
        super().__init__(message_info)

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
            self._dict.update(super().__dict__())

        return self._dict
