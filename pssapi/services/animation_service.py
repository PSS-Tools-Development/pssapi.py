from typing import List as _List

from .raw import AnimationServiceRaw as _AnimationServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import Animation as _Animation


class AnimationService(_ServiceBase):
    async def list_animations(self, design_version: int) -> _List[_Animation]:
        raise NotImplemented()
        result = await _AnimationServiceRaw.list_animations(self.production_server, design_version: int)
        return result

