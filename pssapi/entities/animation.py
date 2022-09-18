
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import AnimationRaw as _AnimationRaw
from ..types import EntityInfo as _EntityInfo


class Animation(_EntityWithIdBase, _AnimationRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<Animation {self.id}: {self.name}>'

    def __str__(self) -> str:
        return f'<Animation {self.id}: {self.name}>'

    @property
    def id(self) -> int:
        return self.animation_id
