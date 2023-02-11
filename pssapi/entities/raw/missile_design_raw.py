"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import List as _List

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class MissileDesignRaw:
    XML_NODE_NAME: str = 'MissileDesign'

    def __init__(self, missile_design_info: _EntityInfo) -> None:
        self.animation_id: int = _parse.pss_int(missile_design_info.get('AnimationId'))
        self.breach_chance: int = _parse.pss_int(missile_design_info.get('BreachChance'))
        self.character_damage: float = _parse.pss_float(missile_design_info.get('CharacterDamage'))
        self.direct_system_damage: float = _parse.pss_float(missile_design_info.get('DirectSystemDamage'))
        self.emp_length: int = _parse.pss_int(missile_design_info.get('EMPLength'))
        self.explosion_radius: int = _parse.pss_int(missile_design_info.get('ExplosionRadius'))
        self.explosion_type: str = _parse.pss_str(missile_design_info.get('ExplosionType'))
        self.fire_length: int = _parse.pss_int(missile_design_info.get('FireLength'))
        self.flight_argument_x: int = _parse.pss_int(missile_design_info.get('FlightArgumentX'))
        self.flight_argument_y: int = _parse.pss_int(missile_design_info.get('FlightArgumentY'))
        self.flight_type: str = _parse.pss_str(missile_design_info.get('FlightType'))
        self.hit_animation_id: int = _parse.pss_int(missile_design_info.get('HitAnimationId'))
        self.hit_sound_file_id: int = _parse.pss_int(missile_design_info.get('HitSoundFileId'))
        self.hull_damage: float = _parse.pss_float(missile_design_info.get('HullDamage'))
        self.hull_percentage_damage: int = _parse.pss_int(missile_design_info.get('HullPercentageDamage'))
        self.launch_animation_id: int = _parse.pss_int(missile_design_info.get('LaunchAnimationId'))
        self.launch_sound_file_id: int = _parse.pss_int(missile_design_info.get('LaunchSoundFileId'))
        self.logo_sprite_id: int = _parse.pss_int(missile_design_info.get('LogoSpriteId'))
        self.mask_animation_id: int = _parse.pss_int(missile_design_info.get('MaskAnimationId'))
        self.mask_hit_animation_id: int = _parse.pss_int(missile_design_info.get('MaskHitAnimationId'))
        self.mask_launch_animation_id: int = _parse.pss_int(missile_design_info.get('MaskLaunchAnimationId'))
        self.metadata: str = _parse.pss_str(missile_design_info.get('Metadata'))
        self.missile_design_id: int = _parse.pss_int(missile_design_info.get('MissileDesignId'))
        self.missile_design_name: str = _parse.pss_str(missile_design_info.get('MissileDesignName'))
        self.missile_type: str = _parse.pss_str(missile_design_info.get('MissileType'))
        self.shield_damage: float = _parse.pss_float(missile_design_info.get('ShieldDamage'))
        self.speed: int = _parse.pss_int(missile_design_info.get('Speed'))
        self.sprite_id: int = _parse.pss_int(missile_design_info.get('SpriteId'))
        self.stun_length: int = _parse.pss_int(missile_design_info.get('StunLength'))
        self.system_damage: float = _parse.pss_float(missile_design_info.get('SystemDamage'))
        self.volley: int = _parse.pss_int(missile_design_info.get('Volley'))
        self.volley_delay: int = _parse.pss_int(missile_design_info.get('VolleyDelay'))
