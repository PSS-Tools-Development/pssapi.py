import pytest

import pssapi

FRIEND_USER_ID: int = 8729280  # Dolores 2.0
SEARCH_USER_NAME: str = "Dolores 2.0"
USER_ID: int = 4510693  # The worst.


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr()
async def test_accept_friend_request(client: pssapi.PssApiClient, access_token: str):
    friend = await client.user_service.accept_friend_request(access_token, FRIEND_USER_ID)
    assert isinstance(friend, pssapi.entities.Friend)


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr()
async def test_add_friend(client: pssapi.PssApiClient, access_token: str):
    friend = await client.user_service.add_friend(access_token, FRIEND_USER_ID)
    assert isinstance(friend, pssapi.entities.Friend)


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr()
async def test_decline_friend_request(client: pssapi.PssApiClient, access_token: str):
    friend = await client.user_service.decline_friend_request(access_token, FRIEND_USER_ID)
    assert isinstance(friend, pssapi.entities.Friend)


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr()
async def test_list_friends(client: pssapi.PssApiClient, access_token: str):
    list_friends = await client.user_service.list_friends(access_token, FRIEND_USER_ID)
    assert isinstance(list_friends, pssapi.entities.ListFriends)


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr()
async def test_remove_friend(client: pssapi.PssApiClient, access_token: str):
    await client.user_service.remove_friend(access_token, FRIEND_USER_ID)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_search_users(client: pssapi.PssApiClient):
    users = await client.user_service.search_users(SEARCH_USER_NAME)
    assert isinstance(users, list)
    assert len(users) > 0
    assert isinstance(users[0], pssapi.entities.User)
