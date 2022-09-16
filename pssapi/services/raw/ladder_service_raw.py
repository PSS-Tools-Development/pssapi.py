####################################################
##   This file has been generated automatically   ##
####################################################

from typing import List as _List

from ... import core as _core
from ...entities import FindUserRanking as _FindUserRanking



# ---------- Constants ----------

FIND_USER_RANKING_BASE_PATH: str = 'LadderService/FindUserRanking'


# ---------- Endpoints ----------

async def find_user_ranking(production_server: str, access_token: str, **params) -> _List[_FindUserRanking]:
    params = {
        'accessToken': access_token,
    }
    result = await _core.get_entities_from_path(_FindUserRanking, 'LadderService', production_server, FIND_USER_RANKING_BASE_PATH, **params)
    return result


