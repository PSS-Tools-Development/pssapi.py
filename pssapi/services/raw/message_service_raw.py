"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import Message as _Message

# ---------- Constants ----------

LIST_ACTIVE_MARKETPLACE_MESSAGES_5_BASE_PATH: str = 'MessageService/ListActiveMarketplaceMessages5'
LIST_MESSAGES_FOR_CHANNEL_KEY_BASE_PATH: str = 'MessageService/ListMessagesForChannelKey'


# ---------- Endpoints ----------

async def list_active_marketplace_messages_5(production_server: str, item_design_id: int, item_sub_type: str, currency_type: str, rarity: str, access_token: str, user_id: int, **params) -> _List[_Message]:
    params = {
        'itemDesignId': item_design_id,
        'itemSubType': item_sub_type,
        'currencyType': currency_type,
        'rarity': rarity,
        'accessToken': access_token,
        'userId': user_id,
        **params
    }
    result = await _core.get_entities_from_path(_Message, 'Messages', production_server, LIST_ACTIVE_MARKETPLACE_MESSAGES_5_BASE_PATH, **params)
    return result


async def list_messages_for_channel_key(production_server: str, channel_key: str, access_token: str, **params) -> _List[_Message]:
    params = {
        'channelKey': channel_key,
        'accessToken': access_token,
        **params
    }
    result = await _core.get_entities_from_path(_Message, 'Messages', production_server, LIST_MESSAGES_FOR_CHANNEL_KEY_BASE_PATH, **params)
    return result
