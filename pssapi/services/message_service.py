from typing import List as _List

from .raw import MessageServiceRaw as _MessageServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import Message as _Message


class MessageService(_ServiceBase):
    async def list_active_marketplace_messages(self, access_token: str, currency_type: str, item_design_id: int, item_sub_type: str, rarity: str, user_id: int) -> _List[_Message]:
        result = await _MessageServiceRaw.list_active_marketplace_messages_5((await self.get_production_server()), access_token, currency_type, item_design_id, item_sub_type, rarity, user_id)
        return result

    async def list_messages_for_channel_key(self, access_token: str, channel_key: str) -> _List[_Message]:
        result = await _MessageServiceRaw.list_messages_for_channel_key((await self.get_production_server()), access_token, channel_key)
        return result
