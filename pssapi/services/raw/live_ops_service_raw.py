####################################################
##   This file has been generated automatically   ##
####################################################

from typing import List as _List

from ... import core as _core
from ...entities import LiveOps as _LiveOps



# ---------- Constants ----------

GET_TODAY_LIVE_OPS_BASE_PATH: str = 'LiveOpsService/GetTodayLiveOps'


# ---------- Endpoints ----------

async def get_today_live_ops(production_server: str, language_key: str, device_type: str, **params) -> _List[_LiveOps]:
    params = {
        'languageKey': language_key,
        'deviceType': device_type,
    }
    result = await _core.get_entities_from_path(_LiveOps, 'GetTodayLiveOps', production_server, GET_TODAY_LIVE_OPS_BASE_PATH, **params)
    return result


