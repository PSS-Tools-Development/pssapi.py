from .entity_base import EntityWithIdBase
from .raw import LeagueRaw


class League(LeagueRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.league_id


__all__ = [
    "League",
]
