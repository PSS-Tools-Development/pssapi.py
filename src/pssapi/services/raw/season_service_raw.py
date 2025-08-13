"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from typing import List

from ... import core
from ...entities import SeasonDesign


# ---------- Constants ----------

LIST_ALL_SEASON_DESIGNS_BASE_PATH: str = "SeasonService/ListAllSeasonDesigns"

# ---------- Endpoint structure ----------


# ---------- Endpoints ----------


async def list_all_season_designs(production_server: str, client_date_time: str, design_version: int, language_key: str, **params) -> List[SeasonDesign]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, "languageKey": language_key, **params}
    result = await core.get_entities_from_path(((SeasonDesign, "SeasonDesigns", True),), "SeasonDesigns", production_server, LIST_ALL_SEASON_DESIGNS_BASE_PATH, "GET", response_gzipped=False, **params)
    return result
