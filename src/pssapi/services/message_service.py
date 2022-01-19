from typing import List as _List

import pssapi.services.service_base as _service_base

from ..entities import Message as _Message
from ..entities import Sale as _Sale
from .raw import MessageServiceRaw as _MessageServiceRaw


class MessageService(_service_base.ServiceBase):
    async def list_active_marketplace_messages(
        self, access_token: str, currency_type: str, item_design_id: int, item_sub_type: str, rarity: str, skip: int, take: int, user_id: int
    ) -> _List[_Message]:
        production_server = await self.get_production_server()
        result = await _MessageServiceRaw.list_active_marketplace_messages_5(production_server, access_token, currency_type, item_design_id, item_sub_type, rarity, skip, take, user_id)
        return result

    async def list_messages_for_channel_key(self, access_token: str, channel_key: str) -> _List[_Message]:
        production_server = await self.get_production_server()
        result = await _MessageServiceRaw.list_messages_for_channel_key(production_server, access_token, channel_key)
        return result

    async def list_private_messages(self, access_token: str) -> _List[_Message]:
        production_server = await self.get_production_server()
        result = await _MessageServiceRaw.list_private_messages(production_server, access_token)
        return result

    async def list_sales_by_item_design_id(self, from_: int, item_design_id: int, sale_status: str, to: int) -> _List[_Sale]:
        production_server = await self.get_production_server()
        result = await _MessageServiceRaw.list_sales_by_item_design_id(production_server, from_, item_design_id, sale_status, to)
        return result

    async def send_message(self, access_token: str, channel_key: str, message: str) -> _Message:
        production_server = await self.get_production_server()
        result = await _MessageServiceRaw.send_message_3(production_server, access_token, channel_key, message)
        return result
