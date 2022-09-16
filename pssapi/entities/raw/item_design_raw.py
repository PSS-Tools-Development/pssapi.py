####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ItemDesignRaw():
    XML_NODE_NAME: str = 'ItemDesign'

    def __init__(self, item_design_info: _EntityInfo) -> None:
        self.__item_design_id: int = _parse.pss_int(item_design_info.get('ItemDesignId'))
        self.__item_design_name: str = _parse.pss_str(item_design_info.get('ItemDesignName'))
        self.__item_design_key: str = _parse.pss_str(item_design_info.get('ItemDesignKey'))
        self.__item_design_description: str = _parse.pss_str(item_design_info.get('ItemDesignDescription'))
        self.__image_sprite_id: int = _parse.pss_int(item_design_info.get('ImageSpriteId'))
        self.__logo_sprite_id: int = _parse.pss_int(item_design_info.get('LogoSpriteId'))
        self.__item_space: int = _parse.pss_int(item_design_info.get('ItemSpace'))
        self.__item_type: str = _parse.pss_str(item_design_info.get('ItemType'))
        self.__gas_cost: int = _parse.pss_int(item_design_info.get('GasCost'))
        self.__mineral_cost: int = _parse.pss_int(item_design_info.get('MineralCost'))
        self.__rank: int = _parse.pss_int(item_design_info.get('Rank'))
        self.__min_room_level: int = _parse.pss_int(item_design_info.get('MinRoomLevel'))
        self.__build_time: int = _parse.pss_int(item_design_info.get('BuildTime'))
        self.__root_item_design_id: int = _parse.pss_int(item_design_info.get('RootItemDesignId'))
        self.__item_sub_type: str = _parse.pss_str(item_design_info.get('ItemSubType'))
        self.__enhancement_type: str = _parse.pss_str(item_design_info.get('EnhancementType'))
        self.__enhancement_value: int = _parse.pss_int(item_design_info.get('EnhancementValue'))
        self.__market_price: int = _parse.pss_int(item_design_info.get('MarketPrice'))
        self.__drop_chance: int = _parse.pss_int(item_design_info.get('DropChance'))
        self.__ingredients: str = _parse.pss_str(item_design_info.get('Ingredients'))
        self.__rarity: str = _parse.pss_str(item_design_info.get('Rarity'))
        self.__module_type: str = _parse.pss_str(item_design_info.get('ModuleType'))
        self.__module_argument: int = _parse.pss_int(item_design_info.get('ModuleArgument'))
        self.__flags: int = _parse.pss_int(item_design_info.get('Flags'))
        self.__fair_price: int = _parse.pss_int(item_design_info.get('FairPrice'))
        self.__min_ship_level: int = _parse.pss_int(item_design_info.get('MinShipLevel'))
        self.__manufacture_cost: str = _parse.pss_str(item_design_info.get('ManufactureCost'))
        self.__item_design_name_en: str = _parse.pss_str(item_design_info.get('ItemDesignNameEN'))
        self.__content: str = _parse.pss_str(item_design_info.get('Content'))
        self.__metadata: str = _parse.pss_str(item_design_info.get('Metadata'))
        self.__priority: int = _parse.pss_int(item_design_info.get('Priority'))
        self.__requirement_string: str = _parse.pss_str(item_design_info.get('RequirementString'))
        self.__max_count: int = _parse.pss_int(item_design_info.get('MaxCount'))
        self.__level: int = _parse.pss_int(item_design_info.get('Level'))
        self.__race_id: int = _parse.pss_int(item_design_info.get('RaceId'))
        self.__required_research_design_id: int = _parse.pss_int(item_design_info.get('RequiredResearchDesignId'))
        self.__parent_item_design_id: int = _parse.pss_int(item_design_info.get('ParentItemDesignId'))
        self.__craft_design_id: int = _parse.pss_int(item_design_info.get('CraftDesignId'))
        self.__missile_design_id: int = _parse.pss_int(item_design_info.get('MissileDesignId'))
        self.__character_part_id: int = _parse.pss_int(item_design_info.get('CharacterPartId'))
        self.__active_animation_id: int = _parse.pss_int(item_design_info.get('ActiveAnimationId'))
        self.__animation_id: int = _parse.pss_int(item_design_info.get('AnimationId'))
        self.__border_sprite_id: int = _parse.pss_int(item_design_info.get('BorderSpriteId'))
        self.__sound_file_id: int = _parse.pss_int(item_design_info.get('SoundFileId'))
        self.__character_design_id: int = _parse.pss_int(item_design_info.get('CharacterDesignId'))
        self.__training_design_id: int = _parse.pss_int(item_design_info.get('TrainingDesignId'))
        self.__room_design_id: int = _parse.pss_int(item_design_info.get('RoomDesignId'))
        self.__particle_sprite_id: int = _parse.pss_int(item_design_info.get('ParticleSpriteId'))
        self.__equip_sound_file_id: int = _parse.pss_int(item_design_info.get('EquipSoundFileId'))
        self.__situation_design_id: int = _parse.pss_int(item_design_info.get('SituationDesignId'))

    @property
    def item_design_id(self) -> int:
        return self.__item_design_id

    @property
    def item_design_name(self) -> str:
        return self.__item_design_name

    @property
    def item_design_key(self) -> str:
        return self.__item_design_key

    @property
    def item_design_description(self) -> str:
        return self.__item_design_description

    @property
    def image_sprite_id(self) -> int:
        return self.__image_sprite_id

    @property
    def logo_sprite_id(self) -> int:
        return self.__logo_sprite_id

    @property
    def item_space(self) -> int:
        return self.__item_space

    @property
    def item_type(self) -> str:
        return self.__item_type

    @property
    def gas_cost(self) -> int:
        return self.__gas_cost

    @property
    def mineral_cost(self) -> int:
        return self.__mineral_cost

    @property
    def rank(self) -> int:
        return self.__rank

    @property
    def min_room_level(self) -> int:
        return self.__min_room_level

    @property
    def build_time(self) -> int:
        return self.__build_time

    @property
    def root_item_design_id(self) -> int:
        return self.__root_item_design_id

    @property
    def item_sub_type(self) -> str:
        return self.__item_sub_type

    @property
    def enhancement_type(self) -> str:
        return self.__enhancement_type

    @property
    def enhancement_value(self) -> int:
        return self.__enhancement_value

    @property
    def market_price(self) -> int:
        return self.__market_price

    @property
    def drop_chance(self) -> int:
        return self.__drop_chance

    @property
    def ingredients(self) -> str:
        return self.__ingredients

    @property
    def rarity(self) -> str:
        return self.__rarity

    @property
    def module_type(self) -> str:
        return self.__module_type

    @property
    def module_argument(self) -> int:
        return self.__module_argument

    @property
    def flags(self) -> int:
        return self.__flags

    @property
    def fair_price(self) -> int:
        return self.__fair_price

    @property
    def min_ship_level(self) -> int:
        return self.__min_ship_level

    @property
    def manufacture_cost(self) -> str:
        return self.__manufacture_cost

    @property
    def item_design_name_en(self) -> str:
        return self.__item_design_name_en

    @property
    def content(self) -> str:
        return self.__content

    @property
    def metadata(self) -> str:
        return self.__metadata

    @property
    def priority(self) -> int:
        return self.__priority

    @property
    def requirement_string(self) -> str:
        return self.__requirement_string

    @property
    def max_count(self) -> int:
        return self.__max_count

    @property
    def level(self) -> int:
        return self.__level

    @property
    def race_id(self) -> int:
        return self.__race_id

    @property
    def required_research_design_id(self) -> int:
        return self.__required_research_design_id

    @property
    def parent_item_design_id(self) -> int:
        return self.__parent_item_design_id

    @property
    def craft_design_id(self) -> int:
        return self.__craft_design_id

    @property
    def missile_design_id(self) -> int:
        return self.__missile_design_id

    @property
    def character_part_id(self) -> int:
        return self.__character_part_id

    @property
    def active_animation_id(self) -> int:
        return self.__active_animation_id

    @property
    def animation_id(self) -> int:
        return self.__animation_id

    @property
    def border_sprite_id(self) -> int:
        return self.__border_sprite_id

    @property
    def sound_file_id(self) -> int:
        return self.__sound_file_id

    @property
    def character_design_id(self) -> int:
        return self.__character_design_id

    @property
    def training_design_id(self) -> int:
        return self.__training_design_id

    @property
    def room_design_id(self) -> int:
        return self.__room_design_id

    @property
    def particle_sprite_id(self) -> int:
        return self.__particle_sprite_id

    @property
    def equip_sound_file_id(self) -> int:
        return self.__equip_sound_file_id

    @property
    def situation_design_id(self) -> int:
        return self.__situation_design_id
