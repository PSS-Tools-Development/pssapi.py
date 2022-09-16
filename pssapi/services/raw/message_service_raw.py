####################################################
##   This file has been generated automatically   ##
####################################################

from datetime import datetime as _datetime
from typing import List as _List

from ... import core as _core
from ...entities import Message as _Message



# ---------- Constants ----------

LIST_ACTIVE_MARKETPLACE_MESSAGES_5_BASE_PATH: str = 'MessageService/ListActiveMarketplaceMessages5'
LIST_IMPORTANT_MESSAGES_FOR_USER_BASE_PATH: str = 'MessageService/ListImportantMessagesForUser'
LIST_MESSAGES_FOR_CHANNEL_KEY_BASE_PATH: str = 'MessageService/ListMessagesForChannelKey'
LIST_PRIVATE_MESSAGES_BASE_PATH: str = 'MessageService/ListPrivateMessages'
LIST_SYSTEM_MESSAGES_FOR_USER_3_BASE_PATH: str = 'MessageService/ListSystemMessagesForUser3'


# ---------- Endpoints ----------

async def list_active_marketplace_messages_5(production_server: str, item_sub_type: str, rarity: str, currency_type: str, item_design_id: int, user_id: int, access_token: str, **params) -> _List[_Message]:
    params = {
        'itemSubType': item_sub_type,
        'rarity': rarity,
        'currencyType': currency_type,
        'itemDesignId': item_design_id,
        'userId': user_id,
        'accessToken': access_token,
    }
    result = await _core.get_entities_from_path(_Message, 'Messages', production_server, LIST_ACTIVE_MARKETPLACE_MESSAGES_5_BASE_PATH, **params)
    return result


async def list_important_messages_for_user(production_server: str, access_token: str, client_date_time: _datetime, **params) -> _List[_None]:
    params = {
        'accessToken': access_token,
        'clientDateTime': client_date_time,
    }
    result = await _core.get_entities_from_path(_None, 'None', production_server, LIST_IMPORTANT_MESSAGES_FOR_USER_BASE_PATH, **params)
    return result


async def list_messages_for_channel_key(production_server: str, channel_key: str, access_token: str, **params) -> _List[_Message]:
    params = {
        'channelKey': channel_key,
        'accessToken': access_token,
    }
    result = await _core.get_entities_from_path(_Message, 'Messages', production_server, LIST_MESSAGES_FOR_CHANNEL_KEY_BASE_PATH, **params)
    return result


async def list_private_messages(production_server: str, access_token: str, **params) -> _List[_Message]:
    params = {
        'accessToken': access_token,
    }
    result = await _core.get_entities_from_path(_Message, 'Messages', production_server, LIST_PRIVATE_MESSAGES_BASE_PATH, **params)
    return result


async def list_system_messages_for_user_3(production_server: str, access_token: str, from_message_id: int, take: int, **params) -> _List[_Message]:
    params = {
        'accessToken': access_token,
        'fromMessageId': from_message_id,
        'take': take,
    }
    result = await _core.get_entities_from_path(_Message, 'Messages', production_server, LIST_SYSTEM_MESSAGES_FOR_USER_3_BASE_PATH, **params)
    return result


