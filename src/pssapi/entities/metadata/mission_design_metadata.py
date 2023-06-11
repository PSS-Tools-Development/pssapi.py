from ...utils import parse as _parse
from .entity_metadata_base import EntityMetadata as _EntityMetadata


class MissionDesignMetadata(_EntityMetadata):
    def __init__(self, metadata: str):
        super().__init__(metadata)
        self._surprise_background_sprite_id: int = _parse.pss_int(self._metadata_dict.get("SurpriseBackgroundSpriteId"))

    @property
    def surprise_background_sprite_id(self) -> int:
        return self._surprise_background_sprite_id
