from .entity_base import EntityWithIdBase
from .raw import BackgroundRaw


class Background(BackgroundRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.background_id


__all__ = [
    "Background",
]
