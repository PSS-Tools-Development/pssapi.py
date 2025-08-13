from .entity_base import EntityWithIdBase
from .raw import StarSystemLinkRaw


class StarSystemLink(StarSystemLinkRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.star_system_link_id


__all__ = [
    "StarSystemLink",
]
