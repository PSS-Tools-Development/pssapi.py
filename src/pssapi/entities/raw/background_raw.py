"""
This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class BackgroundRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "Background"

    def __init__(self, background_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._background_effect_type: str = _parse.pss_str(background_info.pop("BackgroundEffectType", None))
        self._background_id: int = _parse.pss_int(background_info.pop("BackgroundId", None))
        self._background_sprite_id: int = _parse.pss_int(background_info.pop("BackgroundSpriteId", None))
        self._background_type: str = _parse.pss_str(background_info.pop("BackgroundType", None))
        self._close_object_sprite_id: str = _parse.pss_str(background_info.pop("CloseObjectSpriteId", None))
        self._environment_float_argument: int = _parse.pss_int(background_info.pop("EnvironmentFloatArgument", None))
        self._environment_int_argument: int = _parse.pss_int(background_info.pop("EnvironmentIntArgument", None))
        self._environment_type: str = _parse.pss_str(background_info.pop("EnvironmentType", None))
        self._far_object_sprite_id: str = _parse.pss_str(background_info.pop("FarObjectSpriteId", None))
        self._hazard_argument: int = _parse.pss_int(background_info.pop("HazardArgument", None))
        self._hazard_category: str = _parse.pss_str(background_info.pop("HazardCategory", None))
        self._hazard_chance: int = _parse.pss_int(background_info.pop("HazardChance", None))
        self._hazard_effect_sprite_id: int = _parse.pss_int(background_info.pop("HazardEffectSpriteId", None))
        self._hazard_icon_sprite_id: int = _parse.pss_int(background_info.pop("HazardIconSpriteId", None))
        self._hazard_type: str = _parse.pss_str(background_info.pop("HazardType", None))
        self._is_active: bool = _parse.pss_bool(background_info.pop("IsActive", None))
        self._max_hazard_interval: int = _parse.pss_int(background_info.pop("MaxHazardInterval", None))
        self._medium_object_sprite_id: str = _parse.pss_str(background_info.pop("MediumObjectSpriteId", None))
        self._min_hazard_interval: int = _parse.pss_int(background_info.pop("MinHazardInterval", None))
        self._music_file_id: int = _parse.pss_int(background_info.pop("MusicFileId", None))
        self._orbit_anchor_alignment: str = _parse.pss_str(background_info.pop("OrbitAnchorAlignment", None))
        self._orbit_animation_id: int = _parse.pss_int(background_info.pop("OrbitAnimationId", None))
        super().__init__(background_info)

    @property
    def background_effect_type(self) -> str:
        return self._background_effect_type

    @property
    def background_id(self) -> int:
        return self._background_id

    @property
    def background_sprite_id(self) -> int:
        return self._background_sprite_id

    @property
    def background_type(self) -> str:
        return self._background_type

    @property
    def close_object_sprite_id(self) -> str:
        return self._close_object_sprite_id

    @property
    def environment_float_argument(self) -> int:
        return self._environment_float_argument

    @property
    def environment_int_argument(self) -> int:
        return self._environment_int_argument

    @property
    def environment_type(self) -> str:
        return self._environment_type

    @property
    def far_object_sprite_id(self) -> str:
        return self._far_object_sprite_id

    @property
    def hazard_argument(self) -> int:
        return self._hazard_argument

    @property
    def hazard_category(self) -> str:
        return self._hazard_category

    @property
    def hazard_chance(self) -> int:
        return self._hazard_chance

    @property
    def hazard_effect_sprite_id(self) -> int:
        return self._hazard_effect_sprite_id

    @property
    def hazard_icon_sprite_id(self) -> int:
        return self._hazard_icon_sprite_id

    @property
    def hazard_type(self) -> str:
        return self._hazard_type

    @property
    def is_active(self) -> bool:
        return self._is_active

    @property
    def max_hazard_interval(self) -> int:
        return self._max_hazard_interval

    @property
    def medium_object_sprite_id(self) -> str:
        return self._medium_object_sprite_id

    @property
    def min_hazard_interval(self) -> int:
        return self._min_hazard_interval

    @property
    def music_file_id(self) -> int:
        return self._music_file_id

    @property
    def orbit_anchor_alignment(self) -> str:
        return self._orbit_anchor_alignment

    @property
    def orbit_animation_id(self) -> int:
        return self._orbit_animation_id

    def _key(self):
        return (
            self.background_effect_type,
            self.background_id,
            self.background_sprite_id,
            self.background_type,
            self.close_object_sprite_id,
            self.environment_float_argument,
            self.environment_int_argument,
            self.environment_type,
            self.far_object_sprite_id,
            self.hazard_argument,
            self.hazard_category,
            self.hazard_chance,
            self.hazard_effect_sprite_id,
            self.hazard_icon_sprite_id,
            self.hazard_type,
            self.is_active,
            self.max_hazard_interval,
            self.medium_object_sprite_id,
            self.min_hazard_interval,
            self.music_file_id,
            self.orbit_anchor_alignment,
            self.orbit_animation_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "BackgroundEffectType": self.background_effect_type,
                "BackgroundId": self.background_id,
                "BackgroundSpriteId": self.background_sprite_id,
                "BackgroundType": self.background_type,
                "CloseObjectSpriteId": self.close_object_sprite_id,
                "EnvironmentFloatArgument": self.environment_float_argument,
                "EnvironmentIntArgument": self.environment_int_argument,
                "EnvironmentType": self.environment_type,
                "FarObjectSpriteId": self.far_object_sprite_id,
                "HazardArgument": self.hazard_argument,
                "HazardCategory": self.hazard_category,
                "HazardChance": self.hazard_chance,
                "HazardEffectSpriteId": self.hazard_effect_sprite_id,
                "HazardIconSpriteId": self.hazard_icon_sprite_id,
                "HazardType": self.hazard_type,
                "IsActive": self.is_active,
                "MaxHazardInterval": self.max_hazard_interval,
                "MediumObjectSpriteId": self.medium_object_sprite_id,
                "MinHazardInterval": self.min_hazard_interval,
                "MusicFileId": self.music_file_id,
                "OrbitAnchorAlignment": self.orbit_anchor_alignment,
                "OrbitAnimationId": self.orbit_animation_id,
            }
            self._dict.update(super().__dict__())

        return self._dict
