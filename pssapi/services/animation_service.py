from typing import List as _List

from .raw import AnimationServiceRaw as _AnimationServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import Animation as _Animation


class AnimationService(_ServiceBase, _AnimationServiceRaw):
    async def list_animations(self, **params) -> _List[_Animation]:
        return self._list_animations(self.production_server, self.design_version, **params)

    def __repr__(self) -> str:
        return f'<AnimationService: {self.name}>'

    def __str__(self) -> str:
        return f'<AnimationService: {self.name}>'
