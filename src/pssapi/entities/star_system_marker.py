from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .metadata import StarSystemMarkerGeneratorMetadata as _StarSystemMarkerGeneratorMetadata
from .raw import StarSystemMarkerRaw as _StarSystemMarkerRaw


class StarSystemMarker(_StarSystemMarkerRaw, _EntityWithIdBase):
    def __init__(self, star_system_marker_info: _EntityInfo) -> None:
        super().__init__(star_system_marker_info)
        self._star_system_marker_metadata: _StarSystemMarkerGeneratorMetadata = _StarSystemMarkerGeneratorMetadata(self.metadata)

    @property
    def id(self) -> int:
        return self.star_system_marker_id

    @property
    def star_system_marker_metadata(self) -> _StarSystemMarkerGeneratorMetadata:
        return self._star_system_marker_metadata
