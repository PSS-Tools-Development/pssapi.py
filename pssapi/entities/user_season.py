
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import UserSeasonRaw as _UserSeasonRaw
from ..types import EntityInfo as _EntityInfo


class UserSeason(_UserSeasonRaw, _EntityWithIdBase):
    def __init__(self, user_season_info: _EntityInfo) -> None:
        super().__init__(user_season_info)

    @property
    def id(self) -> int:
        return self.user_season_id
