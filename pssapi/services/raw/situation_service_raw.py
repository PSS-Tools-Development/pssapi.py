####################################################
##   This file has been generated automatically   ##
####################################################

from datetime import datetime as _datetime
from typing import List as _List

from ... import core as _core
from ...entities import Situation as _Situation
from ...entities import SituationDesign as _SituationDesign



# ---------- Constants ----------

LIST_SITUATION_DESIGNS_BASE_PATH: str = 'SituationService/ListSituationDesigns'
LIST_SITUATIONS_BASE_PATH: str = 'SituationService/ListSituations'


# ---------- Endpoints ----------

async def list_situation_designs(production_server: str, language_key: str, design_version: int, **params) -> _List[_SituationDesign]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
    }
    result = await _core.get_entities_from_path(_SituationDesign, 'SituationDesigns', production_server, LIST_SITUATION_DESIGNS_BASE_PATH, **params)
    return result


async def list_situations(production_server: str, access_token: str, client_date_time: _datetime, **params) -> _List[_Situation]:
    params = {
        'accessToken': access_token,
        'clientDateTime': client_date_time,
    }
    result = await _core.get_entities_from_path(_Situation, 'Situations', production_server, LIST_SITUATIONS_BASE_PATH, **params)
    return result


