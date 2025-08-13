from .entity_base import EntityWithIdBase
from .raw import UserSeasonRaw


class UserSeason(UserSeasonRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.user_season_id


__all__ = [
    "UserSeason",
]
