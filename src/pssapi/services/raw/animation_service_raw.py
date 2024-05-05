"""
    This file has been generated automatically.
    Any changes to this file will be lost eventually.
"""

from typing import List as _List

from ... import core as _core
from ...entities import Animation as _Animation

# ---------- Constants ----------

LIST_ANIMATIONS_BASE_PATH: str = "AnimationService/ListAnimations"


# ---------- Endpoints ----------


async def list_animations(production_server: str, client_date_time: str, design_version: int, **params) -> _List[_Animation]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, **params}
    result = await _core.get_entities_from_path(((_Animation, "Animations", True),), "Animations", production_server, LIST_ANIMATIONS_BASE_PATH, "GET", response_gzipped=False, **params)
    return result
