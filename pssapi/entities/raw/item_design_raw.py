"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import List as _List

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ItemDesignRaw:
    XML_NODE_NAME: str = 'ItemDesign'

    def __init__(self, item_design_info: _EntityInfo) -> None:
        self.active_animation_id: int = _parse.pss_int(item_design_info.get('ActiveAnimationId'))
        self.animation_id: int = _parse.pss_int(item_design_info.get('AnimationId'))
        self.border_sprite_id: int = _parse.pss_int(item_design_info.get('BorderSpriteId'))
        self.build_time: int = _parse.pss_int(item_design_info.get('BuildTime'))
        self.character_design_id: int = _parse.pss_int(item_design_info.get('CharacterDesignId'))
        self.character_part_id: int = _parse.pss_int(item_design_info.get('CharacterPartId'))
        self.content: str = _parse.pss_str(item_design_info.get('Content'))
        self.craft_design_id: int = _parse.pss_int(item_design_info.get('CraftDesignId'))
        self.drop_chance: int = _parse.pss_int(item_design_info.get('DropChance'))
        self.enhancement_type: str = _parse.pss_str(item_design_info.get('EnhancementType'))
        self.enhancement_value: float = _parse.pss_float(item_design_info.get('EnhancementValue'))
        self.equip_sound_file_id: int = _parse.pss_int(item_design_info.get('EquipSoundFileId'))
        self.fair_price: int = _parse.pss_int(item_design_info.get('FairPrice'))
        self.flags: int = _parse.pss_int(item_design_info.get('Flags'))
        self.gas_cost: int = _parse.pss_int(item_design_info.get('GasCost'))
        self.image_sprite_id: int = _parse.pss_int(item_design_info.get('ImageSpriteId'))
        self.ingredients: str = _parse.pss_str(item_design_info.get('Ingredients'))
        self.item_design_description: str = _parse.pss_str(item_design_info.get('ItemDesignDescription'))
        self.item_design_id: int = _parse.pss_int(item_design_info.get('ItemDesignId'))
        self.item_design_key: str = _parse.pss_str(item_design_info.get('ItemDesignKey'))
        self.item_design_name: str = _parse.pss_str(item_design_info.get('ItemDesignName'))
        self.item_design_name_en: str = _parse.pss_str(item_design_info.get('ItemDesignNameEN'))
        self.item_space: int = _parse.pss_int(item_design_info.get('ItemSpace'))
        self.item_sub_type: str = _parse.pss_str(item_design_info.get('ItemSubType'))
        self.item_type: str = _parse.pss_str(item_design_info.get('ItemType'))
        self.level: int = _parse.pss_int(item_design_info.get('Level'))
        self.logo_sprite_id: int = _parse.pss_int(item_design_info.get('LogoSpriteId'))
        self.manufacture_cost: str = _parse.pss_str(item_design_info.get('ManufactureCost'))
        self.market_price: int = _parse.pss_int(item_design_info.get('MarketPrice'))
        self.max_count: int = _parse.pss_int(item_design_info.get('MaxCount'))
        self.metadata: str = _parse.pss_str(item_design_info.get('Metadata'))
        self.min_room_level: int = _parse.pss_int(item_design_info.get('MinRoomLevel'))
        self.min_ship_level: int = _parse.pss_int(item_design_info.get('MinShipLevel'))
        self.mineral_cost: int = _parse.pss_int(item_design_info.get('MineralCost'))
        self.missile_design_id: int = _parse.pss_int(item_design_info.get('MissileDesignId'))
        self.module_argument: int = _parse.pss_int(item_design_info.get('ModuleArgument'))
        self.module_type: str = _parse.pss_str(item_design_info.get('ModuleType'))
        self.our_price: str = _parse.pss_str(item_design_info.get('OurPrice'))
        self.parent_item_design_id: int = _parse.pss_int(item_design_info.get('ParentItemDesignId'))
        self.particle_sprite_id: int = _parse.pss_int(item_design_info.get('ParticleSpriteId'))
        self.priority: int = _parse.pss_int(item_design_info.get('Priority'))
        self.race_id: int = _parse.pss_int(item_design_info.get('RaceId'))
        self.rank: int = _parse.pss_int(item_design_info.get('Rank'))
        self.rarity: str = _parse.pss_str(item_design_info.get('Rarity'))
        self.reload_time: str = _parse.pss_str(item_design_info.get('ReloadTime'))
        self.required_research_design_id: int = _parse.pss_int(item_design_info.get('RequiredResearchDesignId'))
        self.requirement_string: str = _parse.pss_str(item_design_info.get('RequirementString'))
        self.room_design_id: int = _parse.pss_int(item_design_info.get('RoomDesignId'))
        self.root_item_design_id: int = _parse.pss_int(item_design_info.get('RootItemDesignId'))
        self.situation_design_id: int = _parse.pss_int(item_design_info.get('SituationDesignId'))
        self.sound_file_id: int = _parse.pss_int(item_design_info.get('SoundFileId'))
        self.tags: str = _parse.pss_str(item_design_info.get('Tags'))
        self.training_design_id: int = _parse.pss_int(item_design_info.get('TrainingDesignId'))
