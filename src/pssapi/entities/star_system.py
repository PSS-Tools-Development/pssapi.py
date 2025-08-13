from .entity_base import EntityWithIdBase
from .raw import StarSystemRaw


class StarSystem(StarSystemRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.star_system_id


__all__ = [
    "StarSystem",
]
