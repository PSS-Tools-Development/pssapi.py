import datetime

import pytest

import pssapi


ENGAGEMENT_ID = 21


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "checksum_key", "client", "client_date_time")
@pytest.mark.vcr(recode_mode="once")
async def test_get_engagement(access_token: str, checksum_key: str, client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    checksum = client.battle_service.utils.create_get_engagement_checksum(client_date_time, checksum_key)
    engagement = await client.battle_service.get_engagement(access_token, checksum, client_date_time, ENGAGEMENT_ID)
    assert isinstance(engagement, pssapi.entities.Engagement)
