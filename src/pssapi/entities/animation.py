from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import AnimationRaw as _AnimationRaw


class Animation(_AnimationRaw, _EntityWithIdBase):
    def __init__(self, animation_info: _EntityInfo) -> None:
        super().__init__(animation_info)

    @property
    def id(self) -> int:
        return self.animation_id
