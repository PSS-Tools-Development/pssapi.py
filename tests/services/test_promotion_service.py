import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_all_promotion_designs(client: pssapi.PssApiClient):
    promotion_designs = await client.promotion_service.list_all_promotion_designs()
    assert isinstance(promotion_designs, list)
    assert len(promotion_designs) > 0
    assert isinstance(promotion_designs[0], pssapi.entities.PromotionDesign)
