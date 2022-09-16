from datetime import datetime as _datetime
from typing import List as _List

from .raw import MessageServiceRaw as _MessageServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import Message as _Message


class MessageService(_ServiceBase):
    async def list_active_marketplace_messages_5(self, item_sub_type: str, rarity: str, currency_type: str, item_design_id: int, user_id: int, access_token: str) -> _List[_Message]:
        raise NotImplemented()
        result = await _MessageServiceRaw.list_active_marketplace_messages_5(self.production_server, item_sub_type: str, rarity: str, currency_type: str, item_design_id: int, user_id: int, access_token: str)
        return result


    async def list_important_messages_for_user(self, access_token: str, client_date_time: _datetime) -> _List[_None]:
        raise NotImplemented()
        result = await _MessageServiceRaw.list_important_messages_for_user(self.production_server, access_token: str, client_date_time: _datetime)
        return result


    async def list_messages_for_channel_key(self, channel_key: str, access_token: str) -> _List[_Message]:
        raise NotImplemented()
        result = await _MessageServiceRaw.list_messages_for_channel_key(self.production_server, channel_key: str, access_token: str)
        return result


    async def list_private_messages(self, access_token: str) -> _List[_Message]:
        raise NotImplemented()
        result = await _MessageServiceRaw.list_private_messages(self.production_server, access_token: str)
        return result


    async def list_system_messages_for_user_3(self, access_token: str, from_message_id: int, take: int) -> _List[_Message]:
        raise NotImplemented()
        result = await _MessageServiceRaw.list_system_messages_for_user_3(self.production_server, access_token: str, from_message_id: int, take: int)
        return result


