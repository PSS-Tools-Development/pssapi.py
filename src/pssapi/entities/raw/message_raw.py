"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class MessageRaw(EntityBaseRaw, tag="Message"):
    XML_NODE_NAME: str = "Message"

    activity_argument: Optional[str] = attr(name="ActivityArgument", default=None)
    activity_type: Optional[str] = attr(name="ActivityType", default=None)
    alliance_id: Optional[int] = attr(name="AllianceId", default=None)
    alliance_name: Optional[str] = attr(name="AllianceName", default=None)
    alliance_sprite_id: Optional[int] = attr(name="AllianceSpriteId", default=None)
    argument: Optional[str] = attr(name="Argument", default=None)
    border_sprite_id: Optional[str] = attr(name="BorderSpriteId", default=None)
    channel_id: Optional[int] = attr(name="ChannelId", default=None)
    message: Optional[str] = attr(name="Message", default=None)
    message_date: Optional[datetime] = attr(name="MessageDate", default=None)
    message_id: Optional[int] = attr(name="MessageId", default=None)
    message_type: Optional[str] = attr(name="MessageType", default=None)
    sale_id: Optional[str] = attr(name="SaleId", default=None)
    ship_design_id: Optional[int] = attr(name="ShipDesignId", default=None)
    to_user_id: Optional[str] = attr(name="ToUserId", default=None)
    trophy: Optional[int] = attr(name="Trophy", default=None)
    user_id: Optional[int] = attr(name="UserId", default=None)
    user_name: Optional[str] = attr(name="UserName", default=None)
    user_sprite_id: Optional[int] = attr(name="UserSpriteId", default=None)

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


__all__ = [
    "MessageRaw",
]
