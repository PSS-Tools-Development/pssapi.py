import pytest

import pssapi

ITEM_DESIGN_ID: int = 778  # Void Particle


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_price_history(client: pssapi.PssApiClient):
    history = await client.history_service.price_history(ITEM_DESIGN_ID)
    assert isinstance(history, pssapi.entities.History)
