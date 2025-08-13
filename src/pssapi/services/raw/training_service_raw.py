"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from typing import List

from ... import core
from ...entities import TrainingDesign


# ---------- Constants ----------

LIST_ALL_TRAINING_DESIGNS_2_BASE_PATH: str = "TrainingService/ListAllTrainingDesigns2"

# ---------- Endpoint structure ----------


# ---------- Endpoints ----------


async def list_all_training_designs_2(production_server: str, client_date_time: str, design_version: int, language_key: str, **params) -> List[TrainingDesign]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, "languageKey": language_key, **params}
    result = await core.get_entities_from_path(
        ((TrainingDesign, "TrainingDesigns", True),), "TrainingDesigns", production_server, LIST_ALL_TRAINING_DESIGNS_2_BASE_PATH, "GET", response_gzipped=False, **params
    )
    return result
