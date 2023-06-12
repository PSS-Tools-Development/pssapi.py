from ...utils import parse as _parse
from .entity_metadata_base import EntityMetadata as _EntityMetadata


class SeasonDesignMetadata(_EntityMetadata):
    def __init__(self, metadata: str):
        super().__init__(metadata)
        self._background_sprite_id: int = _parse.pss_int(self._metadata_dict.get("BackgroundSpriteId"))
        self._core_background_sprite_id: int = _parse.pss_int(self._metadata_dict.get("CoreBackgroundSpriteId"))
        self._large_floating_sprite_id: int = _parse.pss_int(self._metadata_dict.get("LargeFloatingSpriteId"))
        self._medium_floating_sprite_id: int = _parse.pss_int(self._metadata_dict.get("MediumFloatingSpriteId"))
        self._small_floating_sprite_id: int = _parse.pss_int(self._metadata_dict.get("SmallFloatingSpriteId"))

    @property
    def background_sprite_id(self) -> int:
        return self._background_sprite_id

    @property
    def core_background_sprite_id(self) -> int:
        return self._core_background_sprite_id

    @property
    def large_floating_sprite_id(self) -> int:
        return self._large_floating_sprite_id

    @property
    def medium_floating_sprite_id(self) -> int:
        return self._medium_floating_sprite_id

    @property
    def small_floating_sprite_id(self) -> int:
        return self._small_floating_sprite_id
