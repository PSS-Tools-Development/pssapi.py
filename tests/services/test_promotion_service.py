import datetime

import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_all_promotion_designs(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    promotion_designs = await client.promotion_service.list_all_promotion_designs(client_date_time)
    assert isinstance(promotion_designs, list)
    assert len(promotion_designs) > 0
    assert isinstance(promotion_designs[0], pssapi.entities.PromotionDesign)
