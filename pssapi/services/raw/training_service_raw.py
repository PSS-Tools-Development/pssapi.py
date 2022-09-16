####################################################
##   This file has been generated automatically   ##
####################################################

from typing import List as _List

from ... import core as _core
from ...entities import TrainingDesign as _TrainingDesign



# ---------- Constants ----------

LIST_ALL_TRAINING_DESIGNS_2_BASE_PATH: str = 'TrainingService/ListAllTrainingDesigns2'


# ---------- Endpoints ----------

async def list_all_training_designs_2(production_server: str, language_key: str, design_version: int, **params) -> _List[_TrainingDesign]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
    }
    result = await _core.get_entities_from_path(_TrainingDesign, 'TrainingDesigns', production_server, LIST_ALL_TRAINING_DESIGNS_2_BASE_PATH, **params)
    return result


