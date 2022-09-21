"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import Background as _Background


class BackgroundServiceRaw:

    SERVICE_NAME = 'BackgroundService'
    LIST_BACKGROUNDS_BASE_PATH: str = 'BackgroundService/ListBackgrounds'

    @staticmethod
    async def _list_backgrounds(production_server: str, **params) -> _List[_Background]:
        params = {
            'designVersion': design_version,
            **params
        }
        result = await _core.get_entities_from_path(_Background, 'Backgrounds', production_server, BackgroundServiceRaw.LIST_BACKGROUNDS_BASE_PATH, **params)
        return result
