"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class MissileDesignRaw:
    XML_NODE_NAME: str = "MissileDesign"

    def __init__(self, missile_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._animation_id: int = _parse.pss_int(missile_design_info.get("AnimationId"))
        self._breach_chance: int = _parse.pss_int(missile_design_info.get("BreachChance"))
        self._character_damage: float = _parse.pss_float(missile_design_info.get("CharacterDamage"))
        self._direct_system_damage: float = _parse.pss_float(missile_design_info.get("DirectSystemDamage"))
        self._emp_length: int = _parse.pss_int(missile_design_info.get("EMPLength"))
        self._explosion_radius: int = _parse.pss_int(missile_design_info.get("ExplosionRadius"))
        self._explosion_type: str = _parse.pss_str(missile_design_info.get("ExplosionType"))
        self._fire_length: int = _parse.pss_int(missile_design_info.get("FireLength"))
        self._flight_argument_x: int = _parse.pss_int(missile_design_info.get("FlightArgumentX"))
        self._flight_argument_y: int = _parse.pss_int(missile_design_info.get("FlightArgumentY"))
        self._flight_type: str = _parse.pss_str(missile_design_info.get("FlightType"))
        self._hit_animation_id: int = _parse.pss_int(missile_design_info.get("HitAnimationId"))
        self._hit_sound_file_id: int = _parse.pss_int(missile_design_info.get("HitSoundFileId"))
        self._hull_damage: float = _parse.pss_float(missile_design_info.get("HullDamage"))
        self._hull_percentage_damage: int = _parse.pss_int(missile_design_info.get("HullPercentageDamage"))
        self._launch_animation_id: int = _parse.pss_int(missile_design_info.get("LaunchAnimationId"))
        self._launch_sound_file_id: int = _parse.pss_int(missile_design_info.get("LaunchSoundFileId"))
        self._logo_sprite_id: int = _parse.pss_int(missile_design_info.get("LogoSpriteId"))
        self._mask_animation_id: int = _parse.pss_int(missile_design_info.get("MaskAnimationId"))
        self._mask_hit_animation_id: int = _parse.pss_int(missile_design_info.get("MaskHitAnimationId"))
        self._mask_launch_animation_id: int = _parse.pss_int(missile_design_info.get("MaskLaunchAnimationId"))
        self._metadata: str = _parse.pss_str(missile_design_info.get("Metadata"))
        self._missile_design_id: int = _parse.pss_int(missile_design_info.get("MissileDesignId"))
        self._missile_design_name: str = _parse.pss_str(missile_design_info.get("MissileDesignName"))
        self._missile_type: str = _parse.pss_str(missile_design_info.get("MissileType"))
        self._shield_damage: float = _parse.pss_float(missile_design_info.get("ShieldDamage"))
        self._speed: int = _parse.pss_int(missile_design_info.get("Speed"))
        self._sprite_id: int = _parse.pss_int(missile_design_info.get("SpriteId"))
        self._stun_length: int = _parse.pss_int(missile_design_info.get("StunLength"))
        self._system_damage: float = _parse.pss_float(missile_design_info.get("SystemDamage"))
        self._volley: int = _parse.pss_int(missile_design_info.get("Volley"))
        self._volley_delay: int = _parse.pss_int(missile_design_info.get("VolleyDelay"))

    @property
    def animation_id(self) -> int:
        return self._animation_id

    @property
    def breach_chance(self) -> int:
        return self._breach_chance

    @property
    def character_damage(self) -> float:
        return self._character_damage

    @property
    def direct_system_damage(self) -> float:
        return self._direct_system_damage

    @property
    def emp_length(self) -> int:
        return self._emp_length

    @property
    def explosion_radius(self) -> int:
        return self._explosion_radius

    @property
    def explosion_type(self) -> str:
        return self._explosion_type

    @property
    def fire_length(self) -> int:
        return self._fire_length

    @property
    def flight_argument_x(self) -> int:
        return self._flight_argument_x

    @property
    def flight_argument_y(self) -> int:
        return self._flight_argument_y

    @property
    def flight_type(self) -> str:
        return self._flight_type

    @property
    def hit_animation_id(self) -> int:
        return self._hit_animation_id

    @property
    def hit_sound_file_id(self) -> int:
        return self._hit_sound_file_id

    @property
    def hull_damage(self) -> float:
        return self._hull_damage

    @property
    def hull_percentage_damage(self) -> int:
        return self._hull_percentage_damage

    @property
    def launch_animation_id(self) -> int:
        return self._launch_animation_id

    @property
    def launch_sound_file_id(self) -> int:
        return self._launch_sound_file_id

    @property
    def logo_sprite_id(self) -> int:
        return self._logo_sprite_id

    @property
    def mask_animation_id(self) -> int:
        return self._mask_animation_id

    @property
    def mask_hit_animation_id(self) -> int:
        return self._mask_hit_animation_id

    @property
    def mask_launch_animation_id(self) -> int:
        return self._mask_launch_animation_id

    @property
    def metadata(self) -> str:
        return self._metadata

    @property
    def missile_design_id(self) -> int:
        return self._missile_design_id

    @property
    def missile_design_name(self) -> str:
        return self._missile_design_name

    @property
    def missile_type(self) -> str:
        return self._missile_type

    @property
    def shield_damage(self) -> float:
        return self._shield_damage

    @property
    def speed(self) -> int:
        return self._speed

    @property
    def sprite_id(self) -> int:
        return self._sprite_id

    @property
    def stun_length(self) -> int:
        return self._stun_length

    @property
    def system_damage(self) -> float:
        return self._system_damage

    @property
    def volley(self) -> int:
        return self._volley

    @property
    def volley_delay(self) -> int:
        return self._volley_delay

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

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "AnimationId": self.animation_id,
                "BreachChance": self.breach_chance,
                "CharacterDamage": self.character_damage,
                "DirectSystemDamage": self.direct_system_damage,
                "EMPLength": self.emp_length,
                "ExplosionRadius": self.explosion_radius,
                "ExplosionType": self.explosion_type,
                "FireLength": self.fire_length,
                "FlightArgumentX": self.flight_argument_x,
                "FlightArgumentY": self.flight_argument_y,
                "FlightType": self.flight_type,
                "HitAnimationId": self.hit_animation_id,
                "HitSoundFileId": self.hit_sound_file_id,
                "HullDamage": self.hull_damage,
                "HullPercentageDamage": self.hull_percentage_damage,
                "LaunchAnimationId": self.launch_animation_id,
                "LaunchSoundFileId": self.launch_sound_file_id,
                "LogoSpriteId": self.logo_sprite_id,
                "MaskAnimationId": self.mask_animation_id,
                "MaskHitAnimationId": self.mask_hit_animation_id,
                "MaskLaunchAnimationId": self.mask_launch_animation_id,
                "Metadata": self.metadata,
                "MissileDesignId": self.missile_design_id,
                "MissileDesignName": self.missile_design_name,
                "MissileType": self.missile_type,
                "ShieldDamage": self.shield_damage,
                "Speed": self.speed,
                "SpriteId": self.sprite_id,
                "StunLength": self.stun_length,
                "SystemDamage": self.system_damage,
                "Volley": self.volley,
                "VolleyDelay": self.volley_delay,
            }

        return self._dict
