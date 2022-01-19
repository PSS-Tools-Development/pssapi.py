from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import UserMarkerRaw as _UserMarkerRaw


class UserMarker(_UserMarkerRaw, _EntityWithIdBase):
    def __init__(self, user_marker_info: _EntityInfo) -> None:
        super().__init__(user_marker_info)

    @property
    def id(self) -> int:
        return self.user_marker_id
