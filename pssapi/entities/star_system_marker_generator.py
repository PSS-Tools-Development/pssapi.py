
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import StarSystemMarkerGeneratorRaw as _StarSystemMarkerGeneratorRaw
from ..types import EntityInfo as _EntityInfo


class StarSystemMarkerGenerator(_EntityWithIdBase, _StarSystemMarkerGeneratorRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<StarSystemMarkerGenerator {self.id}: {self.name}>'

    def __str__(self) -> str:
        return f'<StarSystemMarkerGenerator {self.id}: {self.name}>'

    @property
    def id(self) -> int:
        return self.star_system_marker_generator_id
