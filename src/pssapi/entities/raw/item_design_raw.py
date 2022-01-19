"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ItemDesignRaw:
    XML_NODE_NAME: str = "ItemDesign"

    def __init__(self, item_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._active_animation_id: int = _parse.pss_int(item_design_info.get("ActiveAnimationId"))
        self._animation_id: int = _parse.pss_int(item_design_info.get("AnimationId"))
        self._border_sprite_id: int = _parse.pss_int(item_design_info.get("BorderSpriteId"))
        self._build_time: int = _parse.pss_int(item_design_info.get("BuildTime"))
        self._character_design_id: int = _parse.pss_int(item_design_info.get("CharacterDesignId"))
        self._character_part_id: int = _parse.pss_int(item_design_info.get("CharacterPartId"))
        self._content: str = _parse.pss_str(item_design_info.get("Content"))
        self._craft_design_id: int = _parse.pss_int(item_design_info.get("CraftDesignId"))
        self._drop_chance: int = _parse.pss_int(item_design_info.get("DropChance"))
        self._enhancement_type: str = _parse.pss_str(item_design_info.get("EnhancementType"))
        self._enhancement_value: float = _parse.pss_float(item_design_info.get("EnhancementValue"))
        self._equip_sound_file_id: int = _parse.pss_int(item_design_info.get("EquipSoundFileId"))
        self._fair_price: int = _parse.pss_int(item_design_info.get("FairPrice"))
        self._flags: int = _parse.pss_int(item_design_info.get("Flags"))
        self._gas_cost: int = _parse.pss_int(item_design_info.get("GasCost"))
        self._image_sprite_id: int = _parse.pss_int(item_design_info.get("ImageSpriteId"))
        self._ingredients: str = _parse.pss_str(item_design_info.get("Ingredients"))
        self._item_design_description: str = _parse.pss_str(item_design_info.get("ItemDesignDescription"))
        self._item_design_id: int = _parse.pss_int(item_design_info.get("ItemDesignId"))
        self._item_design_key: str = _parse.pss_str(item_design_info.get("ItemDesignKey"))
        self._item_design_name: str = _parse.pss_str(item_design_info.get("ItemDesignName"))
        self._item_design_name_en: str = _parse.pss_str(item_design_info.get("ItemDesignNameEN"))
        self._item_space: int = _parse.pss_int(item_design_info.get("ItemSpace"))
        self._item_sub_type: str = _parse.pss_str(item_design_info.get("ItemSubType"))
        self._item_type: str = _parse.pss_str(item_design_info.get("ItemType"))
        self._level: int = _parse.pss_int(item_design_info.get("Level"))
        self._logo_sprite_id: int = _parse.pss_int(item_design_info.get("LogoSpriteId"))
        self._manufacture_cost: str = _parse.pss_str(item_design_info.get("ManufactureCost"))
        self._market_price: int = _parse.pss_int(item_design_info.get("MarketPrice"))
        self._max_count: int = _parse.pss_int(item_design_info.get("MaxCount"))
        self._metadata: str = _parse.pss_str(item_design_info.get("Metadata"))
        self._min_room_level: int = _parse.pss_int(item_design_info.get("MinRoomLevel"))
        self._min_ship_level: int = _parse.pss_int(item_design_info.get("MinShipLevel"))
        self._mineral_cost: int = _parse.pss_int(item_design_info.get("MineralCost"))
        self._missile_design_id: int = _parse.pss_int(item_design_info.get("MissileDesignId"))
        self._module_argument: int = _parse.pss_int(item_design_info.get("ModuleArgument"))
        self._module_type: str = _parse.pss_str(item_design_info.get("ModuleType"))
        self._our_price: int = _parse.pss_int(item_design_info.get("OurPrice"))
        self._parent_item_design_id: int = _parse.pss_int(item_design_info.get("ParentItemDesignId"))
        self._particle_sprite_id: int = _parse.pss_int(item_design_info.get("ParticleSpriteId"))
        self._priority: int = _parse.pss_int(item_design_info.get("Priority"))
        self._race_id: int = _parse.pss_int(item_design_info.get("RaceId"))
        self._rank: int = _parse.pss_int(item_design_info.get("Rank"))
        self._rarity: str = _parse.pss_str(item_design_info.get("Rarity"))
        self._reload_modifier: int = _parse.pss_int(item_design_info.get("ReloadModifier"))
        self._reload_time: int = _parse.pss_int(item_design_info.get("ReloadTime"))
        self._required_research_design_id: int = _parse.pss_int(item_design_info.get("RequiredResearchDesignId"))
        self._requirement_string: str = _parse.pss_str(item_design_info.get("RequirementString"))
        self._room_design_id: int = _parse.pss_int(item_design_info.get("RoomDesignId"))
        self._root_item_design_id: int = _parse.pss_int(item_design_info.get("RootItemDesignId"))
        self._situation_design_id: int = _parse.pss_int(item_design_info.get("SituationDesignId"))
        self._sound_file_id: int = _parse.pss_int(item_design_info.get("SoundFileId"))
        self._tags: str = _parse.pss_str(item_design_info.get("Tags"))
        self._training_design_id: int = _parse.pss_int(item_design_info.get("TrainingDesignId"))

    @property
    def active_animation_id(self) -> int:
        return self._active_animation_id

    @property
    def animation_id(self) -> int:
        return self._animation_id

    @property
    def border_sprite_id(self) -> int:
        return self._border_sprite_id

    @property
    def build_time(self) -> int:
        return self._build_time

    @property
    def character_design_id(self) -> int:
        return self._character_design_id

    @property
    def character_part_id(self) -> int:
        return self._character_part_id

    @property
    def content(self) -> str:
        return self._content

    @property
    def craft_design_id(self) -> int:
        return self._craft_design_id

    @property
    def drop_chance(self) -> int:
        return self._drop_chance

    @property
    def enhancement_type(self) -> str:
        return self._enhancement_type

    @property
    def enhancement_value(self) -> float:
        return self._enhancement_value

    @property
    def equip_sound_file_id(self) -> int:
        return self._equip_sound_file_id

    @property
    def fair_price(self) -> int:
        return self._fair_price

    @property
    def flags(self) -> int:
        return self._flags

    @property
    def gas_cost(self) -> int:
        return self._gas_cost

    @property
    def image_sprite_id(self) -> int:
        return self._image_sprite_id

    @property
    def ingredients(self) -> str:
        return self._ingredients

    @property
    def item_design_description(self) -> str:
        return self._item_design_description

    @property
    def item_design_id(self) -> int:
        return self._item_design_id

    @property
    def item_design_key(self) -> str:
        return self._item_design_key

    @property
    def item_design_name(self) -> str:
        return self._item_design_name

    @property
    def item_design_name_en(self) -> str:
        return self._item_design_name_en

    @property
    def item_space(self) -> int:
        return self._item_space

    @property
    def item_sub_type(self) -> str:
        return self._item_sub_type

    @property
    def item_type(self) -> str:
        return self._item_type

    @property
    def level(self) -> int:
        return self._level

    @property
    def logo_sprite_id(self) -> int:
        return self._logo_sprite_id

    @property
    def manufacture_cost(self) -> str:
        return self._manufacture_cost

    @property
    def market_price(self) -> int:
        return self._market_price

    @property
    def max_count(self) -> int:
        return self._max_count

    @property
    def metadata(self) -> str:
        return self._metadata

    @property
    def min_room_level(self) -> int:
        return self._min_room_level

    @property
    def min_ship_level(self) -> int:
        return self._min_ship_level

    @property
    def mineral_cost(self) -> int:
        return self._mineral_cost

    @property
    def missile_design_id(self) -> int:
        return self._missile_design_id

    @property
    def module_argument(self) -> int:
        return self._module_argument

    @property
    def module_type(self) -> str:
        return self._module_type

    @property
    def our_price(self) -> int:
        return self._our_price

    @property
    def parent_item_design_id(self) -> int:
        return self._parent_item_design_id

    @property
    def particle_sprite_id(self) -> int:
        return self._particle_sprite_id

    @property
    def priority(self) -> int:
        return self._priority

    @property
    def race_id(self) -> int:
        return self._race_id

    @property
    def rank(self) -> int:
        return self._rank

    @property
    def rarity(self) -> str:
        return self._rarity

    @property
    def reload_modifier(self) -> int:
        return self._reload_modifier

    @property
    def reload_time(self) -> int:
        return self._reload_time

    @property
    def required_research_design_id(self) -> int:
        return self._required_research_design_id

    @property
    def requirement_string(self) -> str:
        return self._requirement_string

    @property
    def room_design_id(self) -> int:
        return self._room_design_id

    @property
    def root_item_design_id(self) -> int:
        return self._root_item_design_id

    @property
    def situation_design_id(self) -> int:
        return self._situation_design_id

    @property
    def sound_file_id(self) -> int:
        return self._sound_file_id

    @property
    def tags(self) -> str:
        return self._tags

    @property
    def training_design_id(self) -> int:
        return self._training_design_id

    def _key(self):
        return (
            self.active_animation_id,
            self.animation_id,
            self.border_sprite_id,
            self.build_time,
            self.character_design_id,
            self.character_part_id,
            self.content,
            self.craft_design_id,
            self.drop_chance,
            self.enhancement_type,
            self.enhancement_value,
            self.equip_sound_file_id,
            self.fair_price,
            self.flags,
            self.gas_cost,
            self.image_sprite_id,
            self.ingredients,
            self.item_design_description,
            self.item_design_id,
            self.item_design_key,
            self.item_design_name,
            self.item_design_name_en,
            self.item_space,
            self.item_sub_type,
            self.item_type,
            self.level,
            self.logo_sprite_id,
            self.manufacture_cost,
            self.market_price,
            self.max_count,
            self.metadata,
            self.min_room_level,
            self.min_ship_level,
            self.mineral_cost,
            self.missile_design_id,
            self.module_argument,
            self.module_type,
            self.our_price,
            self.parent_item_design_id,
            self.particle_sprite_id,
            self.priority,
            self.race_id,
            self.rank,
            self.rarity,
            self.reload_modifier,
            self.reload_time,
            self.required_research_design_id,
            self.requirement_string,
            self.room_design_id,
            self.root_item_design_id,
            self.situation_design_id,
            self.sound_file_id,
            self.tags,
            self.training_design_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "ActiveAnimationId": self.active_animation_id,
                "AnimationId": self.animation_id,
                "BorderSpriteId": self.border_sprite_id,
                "BuildTime": self.build_time,
                "CharacterDesignId": self.character_design_id,
                "CharacterPartId": self.character_part_id,
                "Content": self.content,
                "CraftDesignId": self.craft_design_id,
                "DropChance": self.drop_chance,
                "EnhancementType": self.enhancement_type,
                "EnhancementValue": self.enhancement_value,
                "EquipSoundFileId": self.equip_sound_file_id,
                "FairPrice": self.fair_price,
                "Flags": self.flags,
                "GasCost": self.gas_cost,
                "ImageSpriteId": self.image_sprite_id,
                "Ingredients": self.ingredients,
                "ItemDesignDescription": self.item_design_description,
                "ItemDesignId": self.item_design_id,
                "ItemDesignKey": self.item_design_key,
                "ItemDesignName": self.item_design_name,
                "ItemDesignNameEN": self.item_design_name_en,
                "ItemSpace": self.item_space,
                "ItemSubType": self.item_sub_type,
                "ItemType": self.item_type,
                "Level": self.level,
                "LogoSpriteId": self.logo_sprite_id,
                "ManufactureCost": self.manufacture_cost,
                "MarketPrice": self.market_price,
                "MaxCount": self.max_count,
                "Metadata": self.metadata,
                "MinRoomLevel": self.min_room_level,
                "MinShipLevel": self.min_ship_level,
                "MineralCost": self.mineral_cost,
                "MissileDesignId": self.missile_design_id,
                "ModuleArgument": self.module_argument,
                "ModuleType": self.module_type,
                "OurPrice": self.our_price,
                "ParentItemDesignId": self.parent_item_design_id,
                "ParticleSpriteId": self.particle_sprite_id,
                "Priority": self.priority,
                "RaceId": self.race_id,
                "Rank": self.rank,
                "Rarity": self.rarity,
                "ReloadModifier": self.reload_modifier,
                "ReloadTime": self.reload_time,
                "RequiredResearchDesignId": self.required_research_design_id,
                "RequirementString": self.requirement_string,
                "RoomDesignId": self.room_design_id,
                "RootItemDesignId": self.root_item_design_id,
                "SituationDesignId": self.situation_design_id,
                "SoundFileId": self.sound_file_id,
                "Tags": self.tags,
                "TrainingDesignId": self.training_design_id,
            }

        return self._dict
