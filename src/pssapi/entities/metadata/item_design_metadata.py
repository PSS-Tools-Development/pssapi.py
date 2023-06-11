from ...utils import parse as _parse
from .entity_metadata_base import EntityMetadata as _EntityMetadata
from .metadata_color import Color as _Color


class ItemDesignMetadata(_EntityMetadata):
    def __init__(self, metadata: str):
        super().__init__(metadata)
        self._background_sprite_id: int = _parse.pss_int(self._metadata_dict.get("BackgroundSpriteId"))
        self._destroyed_sprite_id: int = _parse.pss_int(self._metadata_dict.get("DestroyedSpriteId"))
        self._force_reward_scene: bool = _parse.pss_bool(self._metadata_dict.get("ForceRewardScene"))
        self._idle_animation_id: int = _parse.pss_int(self._metadata_dict.get("IdleAnimationId"))
        self._meta_liquid_falling_color: _Color = _parse.pss_color(self._metadata_dict.get("MetaLiquidFallingColor"))
        self._meta_liquid_falling_count: int = _parse.pss_int(self._metadata_dict.get("MetaLiquidFallingCount"))
        self._meta_liquid_falling_sprite_id: int = _parse.pss_int(self._metadata_dict.get("MetaLiquidFallingSpriteId"))
        self._meta_liquid_floating_color: _Color = _parse.pss_color(self._metadata_dict.get("MetaLiquidFloatingColor"))
        self._meta_liquid_floating_count: int = _parse.pss_int(self._metadata_dict.get("MetaLiquidFloatingCount"))
        self._meta_liquid_floating_sprite_id: int = _parse.pss_int(self._metadata_dict.get("MetaLiquidFloatingSpriteId"))
        self._meta_skin_type: int = _parse.pss_int(self._metadata_dict.get("MetaSkinType"))
        self._show_popup_only: bool = _parse.pss_bool(self._metadata_dict.get("ShowPopupOnly"))
        self._sticker_shine: bool = _parse.pss_bool(self._metadata_dict.get("StickerShine"))

    @property
    def background_sprite_id(self) -> int:
        return self._background_sprite_id

    @property
    def destroyed_sprite_id(self) -> int:
        return self._destroyed_sprite_id

    @property
    def force_reward_scene(self) -> bool:
        return self._force_reward_scene

    @property
    def idle_animation_id(self) -> int:
        return self._idle_animation_id

    @property
    def meta_liquid_falling_color(self) -> str:
        return self._meta_liquid_falling_color

    @property
    def meta_liquid_falling_count(self) -> int:
        return self._meta_liquid_falling_count

    @property
    def meta_liquid_falling_sprite_id(self) -> int:
        return self._meta_liquid_falling_sprite_id

    @property
    def meta_liquid_floating_color(self) -> str:
        return self._meta_liquid_floating_color

    @property
    def meta_liquid_floating_count(self) -> int:
        return self._meta_liquid_floating_count

    @property
    def meta_liquid_floating_sprite_id(self) -> int:
        return self._meta_liquid_floating_sprite_id

    @property
    def meta_skin_type(self) -> int:
        return self._meta_skin_type

    @property
    def show_popup_only(self) -> bool:
        return self._show_popup_only

    @property
    def sticker_shine(self) -> bool:
        return self._sticker_shine
