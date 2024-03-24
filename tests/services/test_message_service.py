import pytest

import pssapi

ITEM_DESIGN_ID: int = 778  # Void Particle
USER_ID: int = 4510693  # The worst.


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr(record_mode="once")
async def test_list_active_marketplace_messages(client: pssapi.PssApiClient, access_token: str):
    messages = await client.message_service.list_active_marketplace_messages(access_token, "Unknown", 0, "None", "None", 0, 20, 0)
    assert isinstance(messages, list)
    assert len(messages) > 0
    assert isinstance(messages[0], pssapi.entities.Message)


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr(record_mode="once")
async def test_list_messages_for_channel_key(client: pssapi.PssApiClient, access_token: str):
    messages = await client.message_service.list_messages_for_channel_key(access_token, "public-en")
    assert isinstance(messages, list)
    assert len(messages) > 0
    assert isinstance(messages[0], pssapi.entities.Message)


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr(record_mode="once")
async def test_list_private_messages(client: pssapi.PssApiClient, access_token: str):  # TODO: Test with access token from real account
    messages = await client.message_service.list_private_messages(access_token)
    assert isinstance(messages, list)
    assert len(messages) > 0
    assert isinstance(messages[0], pssapi.entities.Message)


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr(record_mode="once")
async def test_send_private_message(client: pssapi.PssApiClient, access_token: str):
    message = await client.message_service.send_private_message(access_token, "This is an automated message. Please do not reply.", USER_ID)
    assert isinstance(message, pssapi.entities.Message)


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr(record_mode="once")
async def test_send_message(client: pssapi.PssApiClient, access_token: str):  # TODO: Test with access token from real account
    messages = await client.message_service.send_message(access_token, "public-en", "This is a test message. Please ignore. Thank you for your attention.")
    assert isinstance(messages, pssapi.entities.Message)
