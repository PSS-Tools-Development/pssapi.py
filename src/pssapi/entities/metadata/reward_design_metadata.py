from ...utils import parse as _parse
from .entity_metadata_base import EntityMetadata as _EntityMetadata


class RewardDesignMetadata(_EntityMetadata):
    def __init__(self, metadata: str):
        super().__init__(metadata)
        self._custom_quantity_sprite_id: int = _parse.pss_int(self._metadata_dict.get("CustomQuantitySpriteId"))
        self._image_padding_percent: int = _parse.pss_int(self._metadata_dict.get("ImagePaddingPercent"))

    @property
    def custom_quantity_sprite_id(self) -> int:
        return self._custom_quantity_sprite_id

    @property
    def image_padding_percent(self) -> int:
        return self._image_padding_percent
