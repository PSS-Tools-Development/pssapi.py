from typing import List as _List

from .raw import MessageServiceRaw as _MessageServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import Message as _Message


class MessageService(_ServiceBase):
    async def list_active_marketplace_messages(self, item_design_id: int, item_sub_type: str, currency_type: str, rarity: str, access_token: str, user_id: int) -> _List[_Message]:
        result = await _MessageServiceRaw.list_active_marketplace_messages_5(production_server=self.production_server, item_design_id=item_design_id, item_sub_type=item_sub_type, currency_type=currency_type, rarity=rarity, access_token=access_token, user_id=user_id)
        return result

    async def list_messages_for_channel_key(self, channel_key: str, access_token: str) -> _List[_Message]:
        result = await _MessageServiceRaw.list_messages_for_channel_key(production_server=self.production_server, channel_key=channel_key, access_token=access_token)
        return result
