from .entity_base import EntityWithIdBase
from .raw import StarSystemMarkerRaw


class StarSystemMarker(StarSystemMarkerRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.star_system_marker_id


__all__ = [
    "StarSystemMarker",
]
