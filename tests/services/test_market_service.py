import pytest

import pssapi

ITEM_DESIGN_ID: int = 778  # Void Particle


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_sales_by_item_design_id(client: pssapi.PssApiClient):
    sales = await client.market_service.list_sales_by_item_design_id(0, ITEM_DESIGN_ID, pssapi.enums.SaleStatus.LISTED, 100)
    assert isinstance(sales, list)
    assert len(sales) > 0
    assert isinstance(sales[0], pssapi.entities.Sale)
