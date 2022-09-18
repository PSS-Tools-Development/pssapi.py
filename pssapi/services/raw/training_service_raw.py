"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import TrainingDesign as _TrainingDesign


class TrainingServiceRaw:

    SERVICE_NAME = 'TrainingService'
    LIST_ALL_TRAINING_DESIGNS_2_BASE_PATH: str = 'TrainingService/ListAllTrainingDesigns2'

    @staticmethod
    async def _list_all_training_designs_2(production_server: str, language_key: str, design_version: int, **params) -> _List[_TrainingDesign]:
        params = {
            'languageKey': language_key,
            'designVersion': design_version,
            **params
        }
        result = await _core.get_entities_from_path(_TrainingDesign, 'TrainingDesigns', production_server, TrainingServiceRaw.LIST_ALL_TRAINING_DESIGNS_2_BASE_PATH, **params)
        return result
