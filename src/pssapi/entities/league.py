from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import LeagueRaw as _LeagueRaw


class League(_LeagueRaw, _EntityWithIdBase):
    def __init__(self, league_info: _EntityInfo) -> None:
        super().__init__(league_info)

    @property
    def id(self) -> int:
        return self.league_id
