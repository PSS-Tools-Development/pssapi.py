"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import Message as _Message
from ...entities import Sale as _Sale

# ---------- Constants ----------

LIST_ACTIVE_MARKETPLACE_MESSAGES_5_BASE_PATH: str = "MessageService/ListActiveMarketplaceMessages5"
LIST_MESSAGES_FOR_CHANNEL_KEY_BASE_PATH: str = "MessageService/ListMessagesForChannelKey"
LIST_PRIVATE_MESSAGES_BASE_PATH: str = "MessageService/ListPrivateMessages"
LIST_SALES_BY_ITEM_DESIGN_ID_BASE_PATH: str = "MessageService/ListSalesByItemDesignId"
SEND_MESSAGE_3_BASE_PATH: str = "MessageService/SendMessage3"


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


async def list_sales_by_item_design_id(production_server: str, from_: int, item_design_id: int, sale_status: str, to: int, **params) -> _List[_Sale]:
    params = {"from": from_, "itemDesignId": item_design_id, "saleStatus": sale_status, "to": to, **params}
    result = await _core.get_entities_from_path(((_Sale, "Sales", True),), "Sales", production_server, LIST_SALES_BY_ITEM_DESIGN_ID_BASE_PATH, "GET", **params)
    return result


async def send_message_3(production_server: str, access_token: str, channel_key: str, message: str, **params) -> _Message:
    params = {"AccessToken": access_token, "ChannelKey": channel_key, "Message": message, **params}
    content = _core.create_request_content(__SEND_MESSAGE_3_REQUEST_CONTENT_STRUCTURE, params, "json")
    result = await _core.get_entities_from_path(((_Message, "Message", False),), "SendMessage", production_server, SEND_MESSAGE_3_BASE_PATH, "POST", request_content=content, **params)
    return result


__SEND_MESSAGE_3_REQUEST_CONTENT_STRUCTURE: str = '{"AccessToken":"str","ChannelKey":"str","Message":"str"}'
