
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import LeagueRaw as _LeagueRaw
from ..types import EntityInfo as _EntityInfo


class League(_EntityWithIdBase, _LeagueRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<League {self.id}: {self.name}>'

    def __str__(self) -> str:
        return f'<League {self.id}: {self.name}>'

    @property
    def id(self) -> int:
        return self.league_id
