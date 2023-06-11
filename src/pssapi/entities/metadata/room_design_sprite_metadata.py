from ...utils import parse as _parse
from .entity_metadata_base import EntityMetadata as _EntityMetadata
from .metadata_color import Color as _Color


class RoomDesignSpriteMetadata(_EntityMetadata):
    def __init__(self, metadata: str):
        super().__init__(metadata)
        self._custom_engine_trail_sprite_id: int = _parse.pss_int(self._metadata_dict.get("CustomEngineTrailSpriteId"))
        self._custom_missile_design_id: int = _parse.pss_int(self._metadata_dict.get("CustomMissileDesignId"))
        self._custom_shield_active_sprite_id: int = _parse.pss_int(self._metadata_dict.get("CustomShieldActiveSpriteId"))
        self._custom_shield_hit_sprite_id: int = _parse.pss_int(self._metadata_dict.get("CustomShieldHitSpriteId"))
        self._flight_tint_color: _Color = _parse.pss_color(self._metadata_dict.get("FlightTintColor"))
        self._hit_tint_color: _Color = _parse.pss_color(self._metadata_dict.get("HitTintColor"))
        self._launch_tint_color: _Color = _parse.pss_color(self._metadata_dict.get("LaunchTintColor"))
        self._lift_override_sprite_id: int = _parse.pss_int(self._metadata_dict.get("LiftOverrideSpriteId"))

    @property
    def custom_engine_trail_sprite_id(self) -> int:
        return self._custom_engine_trail_sprite_id

    @property
    def custom_missile_design_id(self) -> int:
        return self._custom_missile_design_id

    @property
    def custom_shield_active_sprite_id(self) -> int:
        return self._custom_shield_active_sprite_id

    @property
    def custom_shield_hit_sprite_id(self) -> int:
        return self._custom_shield_hit_sprite_id

    @property
    def flight_tint_color(self) -> _Color:
        return self._flight_tint_color

    @property
    def hit_tint_color(self) -> _Color:
        return self._hit_tint_color

    @property
    def launch_tint_color(self) -> _Color:
        return self._launch_tint_color

    @property
    def lift_override_sprite_id(self) -> int:
        return self._lift_override_sprite_id
