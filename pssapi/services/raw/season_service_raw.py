####################################################
##   This file has been generated automatically   ##
####################################################

from typing import List as _List

from ... import core as _core
from ...entities import SeasonDesign as _SeasonDesign



# ---------- Constants ----------

LIST_ALL_SEASON_DESIGNS_BASE_PATH: str = 'SeasonService/ListAllSeasonDesigns'


# ---------- Endpoints ----------

async def list_all_season_designs(production_server: str, : None, language_key: str, design_version: int, **params) -> _List[_SeasonDesign]:
    params = {
        '': ,
        'languageKey': language_key,
        'designVersion': design_version,
    }
    result = await _core.get_entities_from_path(_SeasonDesign, 'SeasonDesigns', production_server, LIST_ALL_SEASON_DESIGNS_BASE_PATH, **params)
    return result

