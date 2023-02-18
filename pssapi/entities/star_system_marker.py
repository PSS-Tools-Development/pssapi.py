
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import StarSystemMarkerRaw as _StarSystemMarkerRaw
from ..types import EntityInfo as _EntityInfo


class StarSystemMarker(_EntityWithIdBase, _StarSystemMarkerRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<StarSystemMarker {self.id}>'

    def __str__(self) -> str:
        return f'<StarSystemMarker {self.id}>'

    @property
    def id(self) -> int:
        return self.star_system_marker_id
