"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from typing import List

from ... import core
from ...entities import Animation


# ---------- Constants ----------

LIST_ANIMATIONS_BASE_PATH: str = "AnimationService/ListAnimations"

# ---------- Endpoint structure ----------


# ---------- Endpoints ----------


async def list_animations(production_server: str, client_date_time: str, design_version: int, **params) -> List[Animation]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, **params}
    result = await core.get_entities_from_path(((Animation, "Animations", True),), "Animations", production_server, LIST_ANIMATIONS_BASE_PATH, "GET", response_gzipped=False, **params)
    return result
