from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import StarSystemMarkerRaw as _StarSystemMarkerRaw


class StarSystemMarker(_StarSystemMarkerRaw, _EntityWithIdBase):
    def __init__(self, star_system_marker_info: _EntityInfo) -> None:
        super().__init__(star_system_marker_info)

    @property
    def id(self) -> int:
        return self.star_system_marker_id
