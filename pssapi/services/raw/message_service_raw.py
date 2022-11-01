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

async def list_active_marketplace_messages_5(production_server: str, user_id: int, access_token: str, item_sub_type: str, item_design_id: int, currency_type: str, rarity: str, **params) -> _List[_Message]:
    params = {
        'userId': user_id,
        'accessToken': access_token,
        'itemSubType': item_sub_type,
        'itemDesignId': item_design_id,
        'currencyType': currency_type,
        'rarity': rarity,
        **params
    }
    result = await _core.get_entities_from_path(_Message, 'Messages', production_server, LIST_ACTIVE_MARKETPLACE_MESSAGES_5_BASE_PATH, **params)
    return result


async def list_messages_for_channel_key(production_server: str, access_token: str, channel_key: str, **params) -> _List[_Message]:
    params = {
        'accessToken': access_token,
        'channelKey': channel_key,
        **params
    }
    result = await _core.get_entities_from_path(_Message, 'Messages', production_server, LIST_MESSAGES_FOR_CHANNEL_KEY_BASE_PATH, **params)
    return result
