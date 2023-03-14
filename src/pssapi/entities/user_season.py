from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import UserSeasonRaw as _UserSeasonRaw


class UserSeason(_UserSeasonRaw, _EntityWithIdBase):
    def __init__(self, user_season_info: _EntityInfo) -> None:
        super().__init__(user_season_info)

    @property
    def id(self) -> int:
        return self.user_season_id
