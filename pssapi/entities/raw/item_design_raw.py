"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ItemDesignRaw:
    XML_NODE_NAME: str = 'ItemDesign'

    def __init__(self, item_design_info: _EntityInfo) -> None:
        self.__content: str = _parse.pss_str(item_design_info.get('Content'))
        self.__race_id: int = _parse.pss_int(item_design_info.get('RaceId'))
        self.__logo_sprite_id: int = _parse.pss_int(
            item_design_info.get('LogoSpriteId'))
        self.__character_part_id: int = _parse.pss_int(
            item_design_info.get('CharacterPartId'))
        self.__required_research_design_id: int = _parse.pss_int(
            item_design_info.get('RequiredResearchDesignId'))
        self.__item_design_name_en: str = _parse.pss_str(
            item_design_info.get('ItemDesignNameEN'))
        self.__ingredients: str = _parse.pss_str(
            item_design_info.get('Ingredients'))
        self.__training_design_id: int = _parse.pss_int(
            item_design_info.get('TrainingDesignId'))
        self.__item_design_name: str = _parse.pss_str(
            item_design_info.get('ItemDesignName'))
        self.__parent_item_design_id: int = _parse.pss_int(
            item_design_info.get('ParentItemDesignId'))
        self.__module_argument: int = _parse.pss_int(
            item_design_info.get('ModuleArgument'))
        self.__active_animation_id: int = _parse.pss_int(
            item_design_info.get('ActiveAnimationId'))
        self.__item_design_id: int = _parse.pss_int(
            item_design_info.get('ItemDesignId'))
        self.__enhancement_value: float = _parse.pss_float(
            item_design_info.get('EnhancementValue'))
        self.__missile_design_id: int = _parse.pss_int(
            item_design_info.get('MissileDesignId'))
        self.__market_price: int = _parse.pss_int(
            item_design_info.get('MarketPrice'))
        self.__character_design_id: int = _parse.pss_int(
            item_design_info.get('CharacterDesignId'))
        self.__animation_id: int = _parse.pss_int(
            item_design_info.get('AnimationId'))
        self.__item_design_key: str = _parse.pss_str(
            item_design_info.get('ItemDesignKey'))
        self.__equip_sound_file_id: int = _parse.pss_int(
            item_design_info.get('EquipSoundFileId'))
        self.__room_design_id: int = _parse.pss_int(
            item_design_info.get('RoomDesignId'))
        self.__max_count: int = _parse.pss_int(
            item_design_info.get('MaxCount'))
        self.__item_type: str = _parse.pss_str(
            item_design_info.get('ItemType'))
        self.__tags: str = _parse.pss_str(item_design_info.get('Tags'))
        self.__priority: int = _parse.pss_int(item_design_info.get('Priority'))
        self.__flags: int = _parse.pss_int(item_design_info.get('Flags'))
        self.__drop_chance: int = _parse.pss_int(
            item_design_info.get('DropChance'))
        self.__rank: int = _parse.pss_int(item_design_info.get('Rank'))
        self.__rarity: str = _parse.pss_str(item_design_info.get('Rarity'))
        self.__situation_design_id: int = _parse.pss_int(
            item_design_info.get('SituationDesignId'))
        self.__min_room_level: int = _parse.pss_int(
            item_design_info.get('MinRoomLevel'))
        self.__fair_price: int = _parse.pss_int(
            item_design_info.get('FairPrice'))
        self.__build_time: int = _parse.pss_int(
            item_design_info.get('BuildTime'))
        self.__particle_sprite_id: int = _parse.pss_int(
            item_design_info.get('ParticleSpriteId'))
        self.__root_item_design_id: int = _parse.pss_int(
            item_design_info.get('RootItemDesignId'))
        self.__border_sprite_id: int = _parse.pss_int(
            item_design_info.get('BorderSpriteId'))
        self.__metadata: str = _parse.pss_str(item_design_info.get('Metadata'))
        self.__item_design_description: str = _parse.pss_str(
            item_design_info.get('ItemDesignDescription'))
        self.__gas_cost: int = _parse.pss_int(item_design_info.get('GasCost'))
        self.__our_price: str = _parse.pss_str(
            item_design_info.get('OurPrice'))
        self.__reload_time: str = _parse.pss_str(
            item_design_info.get('ReloadTime'))
        self.__module_type: str = _parse.pss_str(
            item_design_info.get('ModuleType'))
        self.__craft_design_id: int = _parse.pss_int(
            item_design_info.get('CraftDesignId'))
        self.__mineral_cost: int = _parse.pss_int(
            item_design_info.get('MineralCost'))
        self.__item_space: int = _parse.pss_int(
            item_design_info.get('ItemSpace'))
        self.__level: int = _parse.pss_int(item_design_info.get('Level'))
        self.__image_sprite_id: int = _parse.pss_int(
            item_design_info.get('ImageSpriteId'))
        self.__manufacture_cost: str = _parse.pss_str(
            item_design_info.get('ManufactureCost'))
        self.__enhancement_type: str = _parse.pss_str(
            item_design_info.get('EnhancementType'))
        self.__min_ship_level: int = _parse.pss_int(
            item_design_info.get('MinShipLevel'))
        self.__requirement_string: str = _parse.pss_str(
            item_design_info.get('RequirementString'))
        self.__sound_file_id: int = _parse.pss_int(
            item_design_info.get('SoundFileId'))
        self.__item_sub_type: str = _parse.pss_str(
            item_design_info.get('ItemSubType'))

    @property
    def content(self) -> str:
        return self.__content

    @property
    def race_id(self) -> int:
        return self.__race_id

    @property
    def logo_sprite_id(self) -> int:
        return self.__logo_sprite_id

    @property
    def character_part_id(self) -> int:
        return self.__character_part_id

    @property
    def required_research_design_id(self) -> int:
        return self.__required_research_design_id

    @property
    def item_design_name_en(self) -> str:
        return self.__item_design_name_en

    @property
    def ingredients(self) -> str:
        return self.__ingredients

    @property
    def training_design_id(self) -> int:
        return self.__training_design_id

    @property
    def item_design_name(self) -> str:
        return self.__item_design_name

    @property
    def parent_item_design_id(self) -> int:
        return self.__parent_item_design_id

    @property
    def module_argument(self) -> int:
        return self.__module_argument

    @property
    def active_animation_id(self) -> int:
        return self.__active_animation_id

    @property
    def item_design_id(self) -> int:
        return self.__item_design_id

    @property
    def enhancement_value(self) -> float:
        return self.__enhancement_value

    @property
    def missile_design_id(self) -> int:
        return self.__missile_design_id

    @property
    def market_price(self) -> int:
        return self.__market_price

    @property
    def character_design_id(self) -> int:
        return self.__character_design_id

    @property
    def animation_id(self) -> int:
        return self.__animation_id

    @property
    def item_design_key(self) -> str:
        return self.__item_design_key

    @property
    def equip_sound_file_id(self) -> int:
        return self.__equip_sound_file_id

    @property
    def room_design_id(self) -> int:
        return self.__room_design_id

    @property
    def max_count(self) -> int:
        return self.__max_count

    @property
    def item_type(self) -> str:
        return self.__item_type

    @property
    def tags(self) -> str:
        return self.__tags

    @property
    def priority(self) -> int:
        return self.__priority

    @property
    def flags(self) -> int:
        return self.__flags

    @property
    def drop_chance(self) -> int:
        return self.__drop_chance

    @property
    def rank(self) -> int:
        return self.__rank

    @property
    def rarity(self) -> str:
        return self.__rarity

    @property
    def situation_design_id(self) -> int:
        return self.__situation_design_id

    @property
    def min_room_level(self) -> int:
        return self.__min_room_level

    @property
    def fair_price(self) -> int:
        return self.__fair_price

    @property
    def build_time(self) -> int:
        return self.__build_time

    @property
    def particle_sprite_id(self) -> int:
        return self.__particle_sprite_id

    @property
    def root_item_design_id(self) -> int:
        return self.__root_item_design_id

    @property
    def border_sprite_id(self) -> int:
        return self.__border_sprite_id

    @property
    def metadata(self) -> str:
        return self.__metadata

    @property
    def item_design_description(self) -> str:
        return self.__item_design_description

    @property
    def gas_cost(self) -> int:
        return self.__gas_cost

    @property
    def our_price(self) -> str:
        return self.__our_price

    @property
    def reload_time(self) -> str:
        return self.__reload_time

    @property
    def module_type(self) -> str:
        return self.__module_type

    @property
    def craft_design_id(self) -> int:
        return self.__craft_design_id

    @property
    def mineral_cost(self) -> int:
        return self.__mineral_cost

    @property
    def item_space(self) -> int:
        return self.__item_space

    @property
    def level(self) -> int:
        return self.__level

    @property
    def image_sprite_id(self) -> int:
        return self.__image_sprite_id

    @property
    def manufacture_cost(self) -> str:
        return self.__manufacture_cost

    @property
    def enhancement_type(self) -> str:
        return self.__enhancement_type

    @property
    def min_ship_level(self) -> int:
        return self.__min_ship_level

    @property
    def requirement_string(self) -> str:
        return self.__requirement_string

    @property
    def sound_file_id(self) -> int:
        return self.__sound_file_id

    @property
    def item_sub_type(self) -> str:
        return self.__item_sub_type
