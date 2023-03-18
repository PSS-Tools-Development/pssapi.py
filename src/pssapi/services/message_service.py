from typing import List as _List
from typing import Tuple as _Tuple

import pssapi.services.service_base as _service_base

from ..entities import Item as _Item
from ..entities import Message as _Message
from .raw import MessageServiceRaw as _MessageServiceRaw


class MessageService(_service_base.ServiceBase):
    async def collect_reward(self, access_token: str, checksum: int, client_date_time: str, message_id: int) -> _Tuple[_Item, _Message]:
        production_server = await self.get_production_server()
        result = await _MessageServiceRaw.collect_reward_2(production_server, access_token, checksum, client_date_time, message_id)
        return result

    async def list_active_marketplace_messages(self, access_token: str, currency_type: str, item_design_id: int, item_sub_type: str, rarity: str, user_id: int) -> _List[_Message]:
        production_server = await self.get_production_server()
        result = await _MessageServiceRaw.list_active_marketplace_messages_5(production_server, access_token, currency_type, item_design_id, item_sub_type, rarity, user_id)
        return result

    async def list_messages_for_channel_key(self, access_token: str, channel_key: str) -> _List[_Message]:
        production_server = await self.get_production_server()
        result = await _MessageServiceRaw.list_messages_for_channel_key(production_server, access_token, channel_key)
        return result
