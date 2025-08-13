"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from typing import List

from ... import core
from ...entities import Background


# ---------- Constants ----------

LIST_BACKGROUNDS_BASE_PATH: str = "BackgroundService/ListBackgrounds"

# ---------- Endpoint structure ----------


# ---------- Endpoints ----------


async def list_backgrounds(production_server: str, client_date_time: str, design_version: int, **params) -> List[Background]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, **params}
    result = await core.get_entities_from_path(((Background, "Backgrounds", True),), "Backgrounds", production_server, LIST_BACKGROUNDS_BASE_PATH, "GET", response_gzipped=False, **params)
    return result
