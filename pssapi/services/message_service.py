from typing import List as _List

from .raw import MessageServiceRaw as _MessageServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import Message as _Message


class MessageService(_ServiceBase, _MessageServiceRaw):
    async def list_active_marketplace_messages_5(self, **params) -> _List[_Message]:
        return self._list_active_marketplace_messages_5(self.production_server, self.access_token, self.item_design_id, self.item_sub_type, self.currency_type, self.user_id, self.rarity, **params)

    async def list_messages_for_channel_key(self, **params) -> _List[_Message]:
        return self._list_messages_for_channel_key(self.production_server, self.channel_key, self.access_token, **params)

    def __repr__(self) -> str:
        return f'<MessageService: {self.name}>'

    def __str__(self) -> str:
        return f'<MessageService: {self.name}>'
