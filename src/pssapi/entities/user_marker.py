from .entity_base import EntityWithIdBase
from .raw import UserMarkerRaw


class UserMarker(UserMarkerRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.user_marker_id


__all__ = [
    "UserMarker",
]
