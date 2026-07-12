"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from ... import core as _core
from ...entities import Engagement as _Engagement


# ---------- Constants ----------

GET_ENGAGEMENT_BASE_PATH: str = "BattleService/GetEngagement"


# ---------- Endpoints ----------


async def get_engagement(production_server: str, access_token: str, checksum: str, client_date_time: str, engagement_id: int, **params) -> _Engagement:
    params = {"accessToken": access_token, "checksum": checksum, "clientDateTime": client_date_time, "engagementId": engagement_id, **params}
    result = await _core.get_entities_from_path(((_Engagement, "Engagement", False),), "GetEngagement", production_server, GET_ENGAGEMENT_BASE_PATH, "GET", response_gzipped=False, **params)
    return result
