import pytest

import pssapi


test_cases_get_today_live_ops = [
    pytest.param(pssapi.raw.services.LiveOpsServiceRaw.get_today_live_ops, id="get_today_live_ops"),
    pytest.param(pssapi.raw.services.LiveOpsServiceRaw.get_today_live_ops_2, id="get_today_live_ops_2"),
]


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
@pytest.mark.parametrize(["get_today_live_ops_method"], test_cases_get_today_live_ops)
async def test_get_today_live_ops(get_today_live_ops_method):
    live_ops = await get_today_live_ops_method(pssapi.enums.ProductionServer.DEFAULT, pssapi.enums.DeviceType.ANDROID, pssapi.enums.LanguageKey.ENGLISH)
    assert isinstance(live_ops, pssapi.entities.LiveOps)
