
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import UserStarSystemRaw as _UserStarSystemRaw
from ..types import EntityInfo as _EntityInfo


class UserStarSystem(_EntityWithIdBase, _UserStarSystemRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<UserStarSystem {self.id}: {self.name}>'

    def __str__(self) -> str:
        return f'<UserStarSystem {self.id}: {self.name}>'

    @property
    def id(self) -> int:
        return self.user_star_system_id
