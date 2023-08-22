"""
    This file has been generated automatically.
    Any changes to this file will be lost eventually.
"""

from typing import List as _List

from ... import core as _core
from ...entities import Message as _Message

# ---------- Constants ----------

LIST_ACTIVE_MARKETPLACE_MESSAGES_5_BASE_PATH: str = "MessageService/ListActiveMarketplaceMessages5"
LIST_MESSAGES_FOR_CHANNEL_KEY_BASE_PATH: str = "MessageService/ListMessagesForChannelKey"
LIST_PRIVATE_MESSAGES_BASE_PATH: str = "MessageService/ListPrivateMessages"
SEND_MESSAGE_3_BASE_PATH: str = "MessageService/SendMessage3"
SEND_PRIVATE_MESSAGE_3_BASE_PATH: str = "MessageService/SendPrivateMessage3"


# ---------- Endpoints ----------


async def list_active_marketplace_messages_5(
    production_server: str, access_token: str, currency_type: str, item_design_id: int, item_sub_type: str, rarity: str, skip: int, take: int, user_id: int, **params
) -> _List[_Message]:
    params = {
        "accessToken": access_token,
        "currencyType": currency_type,
        "itemDesignId": item_design_id,
        "itemSubType": item_sub_type,
        "rarity": rarity,
        "skip": skip,
        "take": take,
        "userId": user_id,
        **params,
    }
    result = await _core.get_entities_from_path(((_Message, "Messages", True),), "Messages", production_server, LIST_ACTIVE_MARKETPLACE_MESSAGES_5_BASE_PATH, "GET", **params)
    return result


async def list_messages_for_channel_key(production_server: str, access_token: str, channel_key: str, **params) -> _List[_Message]:
    params = {"accessToken": access_token, "channelKey": channel_key, **params}
    result = await _core.get_entities_from_path(((_Message, "Messages", True),), "Messages", production_server, LIST_MESSAGES_FOR_CHANNEL_KEY_BASE_PATH, "GET", **params)
    return result


async def list_private_messages(production_server: str, access_token: str, **params) -> _List[_Message]:
    params = {"accessToken": access_token, **params}
    result = await _core.get_entities_from_path(((_Message, "Messages", True),), "Messages", production_server, LIST_PRIVATE_MESSAGES_BASE_PATH, "GET", **params)
    return result


async def send_message_3(production_server: str, access_token: str, channel_key: str, message: str, **params) -> _Message:
    params = {"AccessToken": access_token, "ChannelKey": channel_key, "Message": message, **params}
    content = _core.create_request_content(__SEND_MESSAGE_3_REQUEST_CONTENT_STRUCTURE, params, "json")
    result = await _core.get_entities_from_path(((_Message, "Message", False),), "SendMessage", production_server, SEND_MESSAGE_3_BASE_PATH, "POST", request_content=content, **params)
    return result


__SEND_MESSAGE_3_REQUEST_CONTENT_STRUCTURE: str = '{"AccessToken":"str","ChannelKey":"str","Message":"str"}'


async def send_private_message_3(production_server: str, access_token: str, message: str, to_user_id: int, **params) -> _Message:
    params = {"AccessToken": access_token, "Message": message, "ToUserId": to_user_id, **params}
    content = _core.create_request_content(__SEND_PRIVATE_MESSAGE_3_REQUEST_CONTENT_STRUCTURE, params, "json")
    result = await _core.get_entities_from_path(((_Message, "Message", False),), "SendMessage", production_server, SEND_PRIVATE_MESSAGE_3_BASE_PATH, "POST", request_content=content, **params)
    return result


__SEND_PRIVATE_MESSAGE_3_REQUEST_CONTENT_STRUCTURE: str = '{"AccessToken":"str","Message":"str","ToUserId":"int"}'
