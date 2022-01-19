from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import UserStarSystemRaw as _UserStarSystemRaw


class UserStarSystem(_UserStarSystemRaw, _EntityWithIdBase):
    def __init__(self, user_star_system_info: _EntityInfo) -> None:
        super().__init__(user_star_system_info)

    @property
    def id(self) -> int:
        return self.user_star_system_id
