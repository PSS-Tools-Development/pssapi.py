from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


#######################################################################
##   This file will be generated automatically from API inspection   ##
#######################################################################


class ItemDesignRaw():
    def __init__(self, info: _EntityInfo) -> None:
        self.__action_border_file_id: int = _parse.int(info.get('ActionBorderFileId'))
        self.__action_file_id: int = _parse.int(info.get('ActionFileId'))
        self.__action_sprite_id: int = _parse.int(info.get('ActionSpriteId'))
        self.__active_animation_id: int = _parse.int(info.get('ActiveAnimationId'))
        self.__animation_id: int = _parse.int(info.get('AnimationId'))
        self.__border_sprite_id: int = _parse.int(info.get('AnimationId'))
        self.__build_time: int = _parse.int(info.get('AnimationId'))
        self.__character_design_id: int = _parse.int(info.get('AnimationId'))
        self.__character_part_id: int = _parse.int(info.get('AnimationId'))
        self.__character_part_name: str = info.get('CharacterPartName')
        self.__character_part_type: str = info.get('CharacterPartType')
        self.__content: str = info.get('Content')
        self.__craft_design_id: int = _parse.int(info.get('CraftDesignId'))
        self.__drop_chance: int = _parse.int(info.get('DropChance'))
        self.__enhancement_type: str = info.get('EnhancementType')
        self.__enhancement_value: float = _parse.float(info.get('EnhancementValue'))
        self.__fair_price: int = _parse.int(info.get('FairPrice'))
        self.__flags: int = _parse.int(info.get('Flags'))
        self.__gas_cost: int = _parse.int(info.get('GasCost'))
        self.__image_sprite_id: int = _parse.int(info.get('ImageSpriteId'))
        self.__ingredients: str = info.get('Ingredients')
        self.__item_design_id: int = _parse.int(info.get('ItemDesignId'))
        self.__item_design_key: str = info.get('ItemDesignKey')
        self.__item_design_name: str = info.get('ItemDesignName')
        self.__item_design_name_en: str = info.get('ItemDesignNameEN')
        self.__item_space: int = _parse.int(info.get('ItemSpace'))
        self.__item_sub_type: str = info.get('ItemSubType')
        self.__item_type: str = info.get('ItemType')
        self.__logo_sprite_id: int = _parse.int(info.get('LogoSpriteId'))
        self.__manufacture_cost: str = info.get('ManufactureCost')
        self.__market_price: int = _parse.int(info.get('MarketPrice'))
        self.__metadata: str = info.get('Metadata')
        self.__mineral_cost: int = _parse.int(info.get('MineralCost'))
        self.__min_room_level: int = _parse.int(info.get('MinRoomLevel'))
        self.__min_ship_level: int = _parse.int(info.get('MinShipLevel'))
        self.__missile_design_id: int = _parse.int(info.get('MissileDesignId'))
        self.__module_argument: int = _parse.int(info.get('ModuleArgument'))
        self.__module_type: str = info.get('ModuleType')
        self.__parent_item_design_id: int = _parse.int(info.get('ParentItemDesignId'))
        self.__particle_sprite_id: int = _parse.int(info.get('ParticleSpriteId'))
        self.__race_id: int = _parse.int(info.get('RaceId'))
        self.__rank: int = _parse.int(info.get('Rank'))
        self.__rarity: str = info.get('Rarity')
        self.__required_research_design_id: int = _parse.int(info.get('RequiredResearchDesignId'))
        self.__room_design_id: int = _parse.int(info.get('RoomDesignId'))
        self.__root_item_design_id: int = _parse.int(info.get('RootItemDesignId'))
        self.__sound_file_id: int = _parse.int(info.get('SoundFileId'))
        self.__standard_border_file_id: int = _parse.int(info.get('StandardBorderFileId'))
        self.__standard_file_id: int = _parse.int(info.get('StandardFileId'))
        self.__standard_sprite_id: int = _parse.int(info.get('StandardSpriteId'))
        self.__training_design_id: int = _parse.int(info.get('TrainingDesignId'))


    @property
    def action_border_file_id(self) -> int:
        return self.__action_border_file_id

    @property
    def action_file_id(self) -> int:
        return self.__action_file_id

    @property
    def action_sprite_id(self) -> int:
        return self.__action_sprite_id

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
    def build_time(self) -> int:
        return self.__build_time

    @property
    def character_design_id(self) -> int:
        return self.__character_design_id

    @property
    def character_part_id(self) -> int:
        return self.__character_part_id

    @property
    def character_part_name(self) -> str:
        return self.__character_part_name

    @property
    def character_part_type(self) -> str:
        return self.__character_part_type

    @property
    def content(self) -> str:
        return self.__content

    @property
    def craft_design_id(self) -> int:
        return self.__craft_design_id

    @property
    def drop_chance(self) -> int:
        return self.__drop_chance

    @property
    def enhancement_type(self) -> str:
        return self.__enhancement_type

    @property
    def enhancement_value(self) -> float:
        return self.__enhancement_value

    @property
    def fair_price(self) -> int:
        return self.__fair_price

    @property
    def flags(self) -> int:
        return self.__flags

    @property
    def gas_cost(self) -> int:
        return self.__gas_cost

    @property
    def image_sprite_id(self) -> int:
        return self.__image_sprite_id

    @property
    def ingredients(self) -> str:
        return self.__ingredients

    @property
    def item_design_id(self) -> int:
        return self.__item_design_id

    @property
    def item_design_key(self) -> str:
        return self.__item_design_key

    @property
    def item_design_name(self) -> str:
        return self.__item_design_name

    @property
    def item_design_name_en(self) -> str:
        return self.__item_design_name_en

    @property
    def item_space(self) -> int:
        return self.__item_space

    @property
    def item_sub_type(self) -> str:
        return self.__item_sub_type

    @property
    def item_type(self) -> str:
        return self.__item_type

    @property
    def logo_sprite_id(self) -> int:
        return self.__logo_sprite_id

    @property
    def manufacture_cost(self) -> str:
        return self.__manufacture_cost

    @property
    def market_price(self) -> int:
        return self.__market_price

    @property
    def metadata(self) -> str:
        return self.__metadata

    @property
    def mineral_cost(self) -> int:
        return self.__mineral_cost

    @property
    def min_room_level(self) -> int:
        return self.__min_room_level

    @property
    def min_ship_level(self) -> int:
        return self.__min_ship_level

    @property
    def missile_design_id(self) -> int:
        return self.__missile_design_id

    @property
    def module_argument(self) -> int:
        return self.__module_argument

    @property
    def module_type(self) -> str:
        return self.__module_type

    @property
    def parent_item_design_id(self) -> int:
        return self.__parent_item_design_id

    @property
    def particle_sprite_id(self) -> int:
        return self.__particle_sprite_id

    @property
    def race_id(self) -> int:
        return self.__race_id

    @property
    def rank(self) -> int:
        return self.__rank

    @property
    def rarity(self) -> str:
        return self.__rarity

    @property
    def required_research_design_id(self) -> int:
        return self.__required_research_design_id

    @property
    def room_design_id(self) -> int:
        return self.__room_design_id

    @property
    def root_item_design_id(self) -> int:
        return self.__root_item_design_id

    @property
    def sound_file_id(self) -> int:
        return self.__sound_file_id

    @property
    def standard_border_file_id(self) -> int:
        return self.__standard_border_file_id

    @property
    def standard_file_id(self) -> int:
        return self.__standard_file_id

    @property
    def standard_sprite_id(self) -> int:
        return self.__standard_sprite_id

    @property
    def training_design_id(self) -> int:
        return self.__training_design_id





