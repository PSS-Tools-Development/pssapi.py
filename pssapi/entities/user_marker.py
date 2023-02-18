
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import UserMarkerRaw as _UserMarkerRaw
from ..types import EntityInfo as _EntityInfo


class UserMarker(_EntityWithIdBase, _UserMarkerRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<UserMarker {self.id}>'

    def __str__(self) -> str:
        return f'<UserMarker {self.id}>'

    @property
    def id(self) -> int:
        return self.user_marker_id
