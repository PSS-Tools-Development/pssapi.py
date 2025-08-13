from .entity_base import EntityWithIdBase
from .raw import UserStarSystemRaw


class UserStarSystem(UserStarSystemRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.user_star_system_id


__all__ = [
    "UserStarSystem",
]
