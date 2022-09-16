####################################################
##   This file has been generated automatically   ##
####################################################

from typing import List as _List

from ... import core as _core
from ...entities import Animation as _Animation



# ---------- Constants ----------

LIST_ANIMATIONS_BASE_PATH: str = 'AnimationService/ListAnimations'


# ---------- Endpoints ----------

async def list_animations(production_server: str, design_version: int, **params) -> _List[_Animation]:
    params = {
        'designVersion': design_version,
    }
    result = await _core.get_entities_from_path(_Animation, 'Animations', production_server, LIST_ANIMATIONS_BASE_PATH, **params)
    return result


