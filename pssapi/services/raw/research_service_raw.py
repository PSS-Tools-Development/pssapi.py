####################################################
##   This file has been generated automatically   ##
####################################################

from datetime import datetime as _datetime
from typing import List as _List

from ... import core as _core
from ...entities import ResearchDesign as _ResearchDesign
from ...entities import Research as _Research



# ---------- Constants ----------

LIST_ALL_RESEARCH_DESIGNS_2_BASE_PATH: str = 'ResearchService/ListAllResearchDesigns2'
LIST_ALL_RESEARCHES_BASE_PATH: str = 'ResearchService/ListAllResearches'


# ---------- Endpoints ----------

async def list_all_research_designs_2(production_server: str, language_key: str, design_version: int, **params) -> _List[_ResearchDesign]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
    }
    result = await _core.get_entities_from_path(_ResearchDesign, 'ResearchDesigns', production_server, LIST_ALL_RESEARCH_DESIGNS_2_BASE_PATH, **params)
    return result


async def list_all_researches(production_server: str, access_token: str, client_date_time: _datetime, **params) -> _List[_Research]:
    params = {
        'accessToken': access_token,
        'clientDateTime': client_date_time,
    }
    result = await _core.get_entities_from_path(_Research, 'Researches', production_server, LIST_ALL_RESEARCHES_BASE_PATH, **params)
    return result


