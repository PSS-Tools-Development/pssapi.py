"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class MissileDesignRaw(EntityBaseRaw, tag="MissileDesign"):
    XML_NODE_NAME: str = "MissileDesign"

    animation_id: Optional[int] = attr(name="AnimationId", default=None)
    breach_chance: Optional[int] = attr(name="BreachChance", default=None)
    character_damage: Optional[float] = attr(name="CharacterDamage", default=None)
    direct_system_damage: Optional[float] = attr(name="DirectSystemDamage", default=None)
    emp_length: Optional[int] = attr(name="EMPLength", default=None)
    explosion_radius: Optional[int] = attr(name="ExplosionRadius", default=None)
    explosion_type: Optional[str] = attr(name="ExplosionType", default=None)
    fire_length: Optional[int] = attr(name="FireLength", default=None)
    flight_argument_x: Optional[int] = attr(name="FlightArgumentX", default=None)
    flight_argument_y: Optional[int] = attr(name="FlightArgumentY", default=None)
    flight_type: Optional[str] = attr(name="FlightType", default=None)
    hit_animation_id: Optional[int] = attr(name="HitAnimationId", default=None)
    hit_sound_file_id: Optional[int] = attr(name="HitSoundFileId", default=None)
    hull_damage: Optional[float] = attr(name="HullDamage", default=None)
    hull_percentage_damage: Optional[int] = attr(name="HullPercentageDamage", default=None)
    launch_animation_id: Optional[int] = attr(name="LaunchAnimationId", default=None)
    launch_sound_file_id: Optional[int] = attr(name="LaunchSoundFileId", default=None)
    logo_sprite_id: Optional[int] = attr(name="LogoSpriteId", default=None)
    mask_animation_id: Optional[int] = attr(name="MaskAnimationId", default=None)
    mask_hit_animation_id: Optional[int] = attr(name="MaskHitAnimationId", default=None)
    mask_launch_animation_id: Optional[int] = attr(name="MaskLaunchAnimationId", default=None)
    metadata: Optional[str] = attr(name="Metadata", default=None)
    missile_design_id: Optional[int] = attr(name="MissileDesignId", default=None)
    missile_design_name: Optional[str] = attr(name="MissileDesignName", default=None)
    missile_type: Optional[str] = attr(name="MissileType", default=None)
    shield_damage: Optional[float] = attr(name="ShieldDamage", default=None)
    speed: Optional[int] = attr(name="Speed", default=None)
    sprite_id: Optional[int] = attr(name="SpriteId", default=None)
    stun_length: Optional[int] = attr(name="StunLength", default=None)
    system_damage: Optional[float] = attr(name="SystemDamage", default=None)
    volley: Optional[int] = attr(name="Volley", default=None)
    volley_delay: Optional[int] = attr(name="VolleyDelay", default=None)

    def _key(self):
        return (
            self.animation_id,
            self.breach_chance,
            self.character_damage,
            self.direct_system_damage,
            self.emp_length,
            self.explosion_radius,
            self.explosion_type,
            self.fire_length,
            self.flight_argument_x,
            self.flight_argument_y,
            self.flight_type,
            self.hit_animation_id,
            self.hit_sound_file_id,
            self.hull_damage,
            self.hull_percentage_damage,
            self.launch_animation_id,
            self.launch_sound_file_id,
            self.logo_sprite_id,
            self.mask_animation_id,
            self.mask_hit_animation_id,
            self.mask_launch_animation_id,
            self.metadata,
            self.missile_design_id,
            self.missile_design_name,
            self.missile_type,
            self.shield_damage,
            self.speed,
            self.sprite_id,
            self.stun_length,
            self.system_damage,
            self.volley,
            self.volley_delay,
        )


__all__ = [
    "MissileDesignRaw",
]
