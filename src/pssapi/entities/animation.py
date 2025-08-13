from .entity_base import EntityWithIdBase
from .raw import AnimationRaw


class Animation(AnimationRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.animation_id


__all__ = [
    "Animation",
]
