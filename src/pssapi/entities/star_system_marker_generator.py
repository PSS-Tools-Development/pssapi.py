from .entity_base import EntityWithIdBase
from .raw import StarSystemMarkerGeneratorRaw


class StarSystemMarkerGenerator(StarSystemMarkerGeneratorRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.star_system_marker_generator_id


__all__ = [
    "StarSystemMarkerGenerator",
]
