"""
    This file has been generated automatically.
    Any changes to this file will be lost eventually.
"""

from typing import List as _List

from ... import core as _core
from ...entities import Background as _Background

# ---------- Constants ----------

LIST_BACKGROUNDS_BASE_PATH: str = "BackgroundService/ListBackgrounds"


# ---------- Endpoints ----------


async def list_backgrounds(production_server: str, design_version: int, **params) -> _List[_Background]:
    params = {"designVersion": design_version, **params}
    result = await _core.get_entities_from_path(((_Background, "Backgrounds", True),), "Backgrounds", production_server, LIST_BACKGROUNDS_BASE_PATH, "GET", **params)
    return result
