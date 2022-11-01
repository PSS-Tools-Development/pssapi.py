
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import UserRaw as _UserRaw
from ..types import EntityInfo as _EntityInfo


class User(_EntityWithIdBase, _UserRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<User {self.id}>'

    def __str__(self) -> str:
        return f'<User {self.id}>'

    @property
    def id(self) -> int:
        return self.id
