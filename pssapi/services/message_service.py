from typing import List as _List

from .raw import MessageServiceRaw as _MessageServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import Message as _Message


class MessageService(_ServiceBase, _MessageServiceRaw):
    async def list_active_marketplace_messages_5(self, item_design_id: int, item_sub_type: str, access_token: str, user_id: int, currency_type: str, rarity: str, **params) -> _List[_Message]:
        return await self._list_active_marketplace_messages_5(self.production_server, item_design_id, item_sub_type, access_token, user_id, currency_type, rarity, **params)

    async def list_messages_for_channel_key(self, channel_key: str, access_token: str, **params) -> _List[_Message]:
        return await self._list_messages_for_channel_key(self.production_server, channel_key, access_token, **params)

    def __repr__(self) -> str:
        return f'<MessageService: {self.name}>'

    def __str__(self) -> str:
        return f'<MessageService: {self.name}>'
