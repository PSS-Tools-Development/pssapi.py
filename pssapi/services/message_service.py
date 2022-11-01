from typing import List as _List

from .raw import MessageServiceRaw as _MessageServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import Message as _Message


class MessageService(_ServiceBase):
    async def list_active_marketplace_messages(self, user_id: int, access_token: str, item_sub_type: str, item_design_id: int, currency_type: str, rarity: str) -> _List[_Message]:
        result = await _MessageServiceRaw.list_active_marketplace_messages_5(self.production_server, user_id, access_token, item_sub_type, item_design_id, currency_type, rarity)
        return result

    async def list_messages_for_channel_key(self, access_token: str, channel_key: str) -> _List[_Message]:
        result = await _MessageServiceRaw.list_messages_for_channel_key(self.production_server, access_token, channel_key)
        return result
