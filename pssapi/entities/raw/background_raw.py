"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class BackgroundRaw:
    XML_NODE_NAME: str = 'Background'

    def __init__(self, background_info: _EntityInfo) -> None:
        self.background_effect_type: str = _parse.pss_str(
            background_info.get('BackgroundEffectType'))
        self.background_id: int = _parse.pss_int(
            background_info.get('BackgroundId'))
        self.background_sprite_id: int = _parse.pss_int(
            background_info.get('BackgroundSpriteId'))
        self.background_type: str = _parse.pss_str(
            background_info.get('BackgroundType'))
        self.close_object_sprite_id: str = _parse.pss_str(
            background_info.get('CloseObjectSpriteId'))
        self.environment_float_argument: int = _parse.pss_int(
            background_info.get('EnvironmentFloatArgument'))
        self.environment_int_argument: int = _parse.pss_int(
            background_info.get('EnvironmentIntArgument'))
        self.environment_type: str = _parse.pss_str(
            background_info.get('EnvironmentType'))
        self.far_object_sprite_id: str = _parse.pss_str(
            background_info.get('FarObjectSpriteId'))
        self.hazard_argument: int = _parse.pss_int(
            background_info.get('HazardArgument'))
        self.hazard_category: str = _parse.pss_str(
            background_info.get('HazardCategory'))
        self.hazard_chance: int = _parse.pss_int(
            background_info.get('HazardChance'))
        self.hazard_effect_sprite_id: int = _parse.pss_int(
            background_info.get('HazardEffectSpriteId'))
        self.hazard_icon_sprite_id: int = _parse.pss_int(
            background_info.get('HazardIconSpriteId'))
        self.hazard_type: str = _parse.pss_str(
            background_info.get('HazardType'))
        self.is_active: bool = _parse.pss_bool(background_info.get('IsActive'))
        self.max_hazard_interval: int = _parse.pss_int(
            background_info.get('MaxHazardInterval'))
        self.medium_object_sprite_id: str = _parse.pss_str(
            background_info.get('MediumObjectSpriteId'))
        self.min_hazard_interval: int = _parse.pss_int(
            background_info.get('MinHazardInterval'))
        self.music_file_id: int = _parse.pss_int(
            background_info.get('MusicFileId'))
        self.orbit_anchor_alignment: str = _parse.pss_str(
            background_info.get('OrbitAnchorAlignment'))
        self.orbit_animation_id: int = _parse.pss_int(
            background_info.get('OrbitAnimationId'))
