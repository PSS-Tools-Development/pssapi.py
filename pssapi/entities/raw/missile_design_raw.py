"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class MissileDesignRaw:
    XML_NODE_NAME: str = 'MissileDesign'

    def __init__(self, missile_design_info: _EntityInfo) -> None:
        self.__fire_length: int = _parse.pss_int(
            missile_design_info.get('FireLength'))
        self.__stun_length: int = _parse.pss_int(
            missile_design_info.get('StunLength'))
        self.__system_damage: float = _parse.pss_float(
            missile_design_info.get('SystemDamage'))
        self.__logo_sprite_id: int = _parse.pss_int(
            missile_design_info.get('LogoSpriteId'))
        self.__flight_type: str = _parse.pss_str(
            missile_design_info.get('FlightType'))
        self.__hit_sound_file_id: int = _parse.pss_int(
            missile_design_info.get('HitSoundFileId'))
        self.__direct_system_damage: float = _parse.pss_float(
            missile_design_info.get('DirectSystemDamage'))
        self.__hit_animation_id: int = _parse.pss_int(
            missile_design_info.get('HitAnimationId'))
        self.__missile_design_name: str = _parse.pss_str(
            missile_design_info.get('MissileDesignName'))
        self.__mask_hit_animation_id: int = _parse.pss_int(
            missile_design_info.get('MaskHitAnimationId'))
        self.__character_damage: float = _parse.pss_float(
            missile_design_info.get('CharacterDamage'))
        self.__hull_percentage_damage: int = _parse.pss_int(
            missile_design_info.get('HullPercentageDamage'))
        self.__sprite_id: int = _parse.pss_int(
            missile_design_info.get('SpriteId'))
        self.__explosion_type: str = _parse.pss_str(
            missile_design_info.get('ExplosionType'))
        self.__launch_animation_id: int = _parse.pss_int(
            missile_design_info.get('LaunchAnimationId'))
        self.__metadata: str = _parse.pss_str(
            missile_design_info.get('Metadata'))
        self.__missile_design_id: int = _parse.pss_int(
            missile_design_info.get('MissileDesignId'))
        self.__breach_chance: int = _parse.pss_int(
            missile_design_info.get('BreachChance'))
        self.__volley: int = _parse.pss_int(missile_design_info.get('Volley'))
        self.__speed: int = _parse.pss_int(missile_design_info.get('Speed'))
        self.__flight_argument_y: int = _parse.pss_int(
            missile_design_info.get('FlightArgumentY'))
        self.__shield_damage: float = _parse.pss_float(
            missile_design_info.get('ShieldDamage'))
        self.__hull_damage: float = _parse.pss_float(
            missile_design_info.get('HullDamage'))
        self.__explosion_radius: int = _parse.pss_int(
            missile_design_info.get('ExplosionRadius'))
        self.__animation_id: int = _parse.pss_int(
            missile_design_info.get('AnimationId'))
        self.__mask_animation_id: int = _parse.pss_int(
            missile_design_info.get('MaskAnimationId'))
        self.__launch_sound_file_id: int = _parse.pss_int(
            missile_design_info.get('LaunchSoundFileId'))
        self.__flight_argument_x: int = _parse.pss_int(
            missile_design_info.get('FlightArgumentX'))
        self.__missile_type: str = _parse.pss_str(
            missile_design_info.get('MissileType'))
        self.__mask_launch_animation_id: int = _parse.pss_int(
            missile_design_info.get('MaskLaunchAnimationId'))
        self.__emp_length: int = _parse.pss_int(
            missile_design_info.get('EMPLength'))
        self.__volley_delay: int = _parse.pss_int(
            missile_design_info.get('VolleyDelay'))

    @property
    def fire_length(self) -> int:
        return self.__fire_length

    @property
    def stun_length(self) -> int:
        return self.__stun_length

    @property
    def system_damage(self) -> float:
        return self.__system_damage

    @property
    def logo_sprite_id(self) -> int:
        return self.__logo_sprite_id

    @property
    def flight_type(self) -> str:
        return self.__flight_type

    @property
    def hit_sound_file_id(self) -> int:
        return self.__hit_sound_file_id

    @property
    def direct_system_damage(self) -> float:
        return self.__direct_system_damage

    @property
    def hit_animation_id(self) -> int:
        return self.__hit_animation_id

    @property
    def missile_design_name(self) -> str:
        return self.__missile_design_name

    @property
    def mask_hit_animation_id(self) -> int:
        return self.__mask_hit_animation_id

    @property
    def character_damage(self) -> float:
        return self.__character_damage

    @property
    def hull_percentage_damage(self) -> int:
        return self.__hull_percentage_damage

    @property
    def sprite_id(self) -> int:
        return self.__sprite_id

    @property
    def explosion_type(self) -> str:
        return self.__explosion_type

    @property
    def launch_animation_id(self) -> int:
        return self.__launch_animation_id

    @property
    def metadata(self) -> str:
        return self.__metadata

    @property
    def missile_design_id(self) -> int:
        return self.__missile_design_id

    @property
    def breach_chance(self) -> int:
        return self.__breach_chance

    @property
    def volley(self) -> int:
        return self.__volley

    @property
    def speed(self) -> int:
        return self.__speed

    @property
    def flight_argument_y(self) -> int:
        return self.__flight_argument_y

    @property
    def shield_damage(self) -> float:
        return self.__shield_damage

    @property
    def hull_damage(self) -> float:
        return self.__hull_damage

    @property
    def explosion_radius(self) -> int:
        return self.__explosion_radius

    @property
    def animation_id(self) -> int:
        return self.__animation_id

    @property
    def mask_animation_id(self) -> int:
        return self.__mask_animation_id

    @property
    def launch_sound_file_id(self) -> int:
        return self.__launch_sound_file_id

    @property
    def flight_argument_x(self) -> int:
        return self.__flight_argument_x

    @property
    def missile_type(self) -> str:
        return self.__missile_type

    @property
    def mask_launch_animation_id(self) -> int:
        return self.__mask_launch_animation_id

    @property
    def emp_length(self) -> int:
        return self.__emp_length

    @property
    def volley_delay(self) -> int:
        return self.__volley_delay
