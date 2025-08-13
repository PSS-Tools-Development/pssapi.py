from typing import List

from pssapi.services import service_base

from ..entities import Message
from .raw import MessageServiceRaw


class MessageService(service_base.ServiceBase):
    async def list_active_marketplace_messages(self, access_token: str, currency_type: str, item_design_id: int, item_sub_type: str, rarity: str, skip: int, take: int, user_id: int) -> List[Message]:
        production_server = await self.get_production_server()
        result = await MessageServiceRaw.list_active_marketplace_messages_5(production_server, access_token, currency_type, item_design_id, item_sub_type, rarity, skip, take, user_id)
        return result

    async def list_messages_for_channel_key(self, access_token: str, channel_key: str) -> List[Message]:
        production_server = await self.get_production_server()
        result = await MessageServiceRaw.list_messages_for_channel_key(production_server, access_token, channel_key)
        return result

    async def list_private_messages(self, access_token: str) -> List[Message]:
        production_server = await self.get_production_server()
        result = await MessageServiceRaw.list_private_messages(production_server, access_token)
        return result

    async def send_message(self, access_token: str, channel_key: str, message: str) -> Message:
        production_server = await self.get_production_server()
        result = await MessageServiceRaw.send_message_3(production_server, access_token, channel_key, message)
        return result

    async def send_private_message(self, access_token: str, message: str, to_user_id: int) -> Message:
        production_server = await self.get_production_server()
        result = await MessageServiceRaw.send_private_message_3(production_server, access_token, message, to_user_id)
        return result
