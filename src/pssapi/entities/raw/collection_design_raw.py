"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class CollectionDesignRaw:
    XML_NODE_NAME: str = "CollectionDesign"

    def __init__(self, collection_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._ability_icon_sprite_id: int = _parse.pss_int(collection_design_info.get("AbilityIconSpriteId"))
        self._ability_name: str = _parse.pss_str(collection_design_info.get("AbilityName"))
        self._argument: int = _parse.pss_int(collection_design_info.get("Argument"))
        self._base_chance: int = _parse.pss_int(collection_design_info.get("BaseChance"))
        self._base_enhancement_value: int = _parse.pss_int(collection_design_info.get("BaseEnhancementValue"))
        self._collection_description: str = _parse.pss_str(collection_design_info.get("CollectionDescription"))
        self._collection_design_id: int = _parse.pss_int(collection_design_info.get("CollectionDesignId"))
        self._collection_name: str = _parse.pss_str(collection_design_info.get("CollectionName"))
        self._collection_type: str = _parse.pss_str(collection_design_info.get("CollectionType"))
        self._color_string: str = _parse.pss_str(collection_design_info.get("ColorString"))
        self._enhancement_type: str = _parse.pss_str(collection_design_info.get("EnhancementType"))
        self._flags: int = _parse.pss_int(collection_design_info.get("Flags"))
        self._halo_animation_id: int = _parse.pss_int(collection_design_info.get("HaloAnimationId"))
        self._icon_sprite_id: int = _parse.pss_int(collection_design_info.get("IconSpriteId"))
        self._max_combo: int = _parse.pss_int(collection_design_info.get("MaxCombo"))
        self._max_use: int = _parse.pss_int(collection_design_info.get("MaxUse"))
        self._min_combo: int = _parse.pss_int(collection_design_info.get("MinCombo"))
        self._sprite_id: int = _parse.pss_int(collection_design_info.get("SpriteId"))
        self._step_chance: int = _parse.pss_int(collection_design_info.get("StepChance"))
        self._step_enhancement_value: int = _parse.pss_int(collection_design_info.get("StepEnhancementValue"))
        self._trigger_type: str = _parse.pss_str(collection_design_info.get("TriggerType"))

    @property
    def ability_icon_sprite_id(self) -> int:
        return self._ability_icon_sprite_id

    @property
    def ability_name(self) -> str:
        return self._ability_name

    @property
    def argument(self) -> int:
        return self._argument

    @property
    def base_chance(self) -> int:
        return self._base_chance

    @property
    def base_enhancement_value(self) -> int:
        return self._base_enhancement_value

    @property
    def collection_description(self) -> str:
        return self._collection_description

    @property
    def collection_design_id(self) -> int:
        return self._collection_design_id

    @property
    def collection_name(self) -> str:
        return self._collection_name

    @property
    def collection_type(self) -> str:
        return self._collection_type

    @property
    def color_string(self) -> str:
        return self._color_string

    @property
    def enhancement_type(self) -> str:
        return self._enhancement_type

    @property
    def flags(self) -> int:
        return self._flags

    @property
    def halo_animation_id(self) -> int:
        return self._halo_animation_id

    @property
    def icon_sprite_id(self) -> int:
        return self._icon_sprite_id

    @property
    def max_combo(self) -> int:
        return self._max_combo

    @property
    def max_use(self) -> int:
        return self._max_use

    @property
    def min_combo(self) -> int:
        return self._min_combo

    @property
    def sprite_id(self) -> int:
        return self._sprite_id

    @property
    def step_chance(self) -> int:
        return self._step_chance

    @property
    def step_enhancement_value(self) -> int:
        return self._step_enhancement_value

    @property
    def trigger_type(self) -> str:
        return self._trigger_type

    def _key(self):
        return (
            self.ability_icon_sprite_id,
            self.ability_name,
            self.argument,
            self.base_chance,
            self.base_enhancement_value,
            self.collection_description,
            self.collection_design_id,
            self.collection_name,
            self.collection_type,
            self.color_string,
            self.enhancement_type,
            self.flags,
            self.halo_animation_id,
            self.icon_sprite_id,
            self.max_combo,
            self.max_use,
            self.min_combo,
            self.sprite_id,
            self.step_chance,
            self.step_enhancement_value,
            self.trigger_type,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "AbilityIconSpriteId": self.ability_icon_sprite_id,
                "AbilityName": self.ability_name,
                "Argument": self.argument,
                "BaseChance": self.base_chance,
                "BaseEnhancementValue": self.base_enhancement_value,
                "CollectionDescription": self.collection_description,
                "CollectionDesignId": self.collection_design_id,
                "CollectionName": self.collection_name,
                "CollectionType": self.collection_type,
                "ColorString": self.color_string,
                "EnhancementType": self.enhancement_type,
                "Flags": self.flags,
                "HaloAnimationId": self.halo_animation_id,
                "IconSpriteId": self.icon_sprite_id,
                "MaxCombo": self.max_combo,
                "MaxUse": self.max_use,
                "MinCombo": self.min_combo,
                "SpriteId": self.sprite_id,
                "StepChance": self.step_chance,
                "StepEnhancementValue": self.step_enhancement_value,
                "TriggerType": self.trigger_type,
            }

        return self._dict
