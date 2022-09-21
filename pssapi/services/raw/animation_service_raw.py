"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import Animation as _Animation


class AnimationServiceRaw:

    SERVICE_NAME = 'AnimationService'
    LIST_ANIMATIONS_BASE_PATH: str = 'AnimationService/ListAnimations'

    @staticmethod
    async def _list_animations(production_server: str, design_version: int = None, **params) -> _List[_Animation]:
        params = {
            'designVersion': design_version,
            **params
        }
        result = await _core.get_entities_from_path(_Animation, 'Animations', production_server, AnimationServiceRaw.LIST_ANIMATIONS_BASE_PATH, **params)
        return result
