from ...utils import parse as _parse
from .entity_metadata_base import EntityMetadata as _EntityMetadata


class StarSystemMarkerGeneratorMetadata(_EntityMetadata):
    def __init__(self, metadata: str):
        super().__init__(metadata)
        self._background_sprite_id: int = _parse.pss_int(self._metadata_dict.get("BackgroundSpriteId"))
        self._npc_sprite_id: int = _parse.pss_int(self._metadata_dict.get("NPCSpriteId"))
        self._title_image_sprite_id: int = _parse.pss_int(self._metadata_dict.get("TitleImageSpriteId"))

    @property
    def background_sprite_id(self) -> int:
        return self._background_sprite_id

    @property
    def npc_sprite_id(self) -> int:
        return self._npc_sprite_id

    @property
    def title_image_sprite_id(self) -> int:
        return self._title_image_sprite_id
