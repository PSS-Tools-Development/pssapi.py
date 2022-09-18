
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import UserSeasonRaw as _UserSeasonRaw
from ..types import EntityInfo as _EntityInfo


class UserSeason(_EntityWithIdBase, _UserSeasonRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<UserSeason {self.id}: {self.name}>'

    def __str__(self) -> str:
        return f'<UserSeason {self.id}: {self.name}>'

    @property
    def id(self) -> int:
        return self.user_season_id
