"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import TrainingDesign as _TrainingDesign

# ---------- Constants ----------

LIST_ALL_TRAINING_DESIGNS_2_BASE_PATH: str = "TrainingService/ListAllTrainingDesigns2"


# ---------- Endpoints ----------


async def list_all_training_designs_2(production_server: str, design_version: int, language_key: str, **params) -> _List[_TrainingDesign]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_TrainingDesign, "TrainingDesigns", True),), "TrainingDesigns", production_server, LIST_ALL_TRAINING_DESIGNS_2_BASE_PATH, "GET", **params)
    return result
