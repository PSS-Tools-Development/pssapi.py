####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class RoomDesignRaw():
    XML_NODE_NAME: str = 'RoomDesign'

    def __init__(self, room_design_info: _EntityInfo) -> None:
        self.__room_design_id: int = _parse.pss_int(room_design_info.get('RoomDesignId'))
        self.__room_name: str = _parse.pss_str(room_design_info.get('RoomName'))
        self.__room_short_name: str = _parse.pss_str(room_design_info.get('RoomShortName'))
        self.__room_type: str = _parse.pss_str(room_design_info.get('RoomType'))
        self.__max_system_power: int = _parse.pss_int(room_design_info.get('MaxSystemPower'))
        self.__construction_time: int = _parse.pss_int(room_design_info.get('ConstructionTime'))
        self.__capacity: int = _parse.pss_int(room_design_info.get('Capacity'))
        self.__reload_time: int = _parse.pss_int(room_design_info.get('ReloadTime'))
        self.__image_sprite_id: int = _parse.pss_int(room_design_info.get('ImageSpriteId'))
        self.__logo_sprite_id: int = _parse.pss_int(room_design_info.get('LogoSpriteId'))
        self.__max_power_generated: int = _parse.pss_int(room_design_info.get('MaxPowerGenerated'))
        self.__random_improvements: int = _parse.pss_int(room_design_info.get('RandomImprovements'))
        self.__improvement_amounts: int = _parse.pss_int(room_design_info.get('ImprovementAmounts'))
        self.__manufacture_capacity: int = _parse.pss_int(room_design_info.get('ManufactureCapacity'))
        self.__manufacture_rate: int = _parse.pss_int(room_design_info.get('ManufactureRate'))
        self.__manufacture_type: str = _parse.pss_str(room_design_info.get('ManufactureType'))
        self.__level: int = _parse.pss_int(room_design_info.get('Level'))
        self.__category_type: str = _parse.pss_str(room_design_info.get('CategoryType'))
        self.__construction_sprite_id: int = _parse.pss_int(room_design_info.get('ConstructionSpriteId'))
        self.__min_ship_level: int = _parse.pss_int(room_design_info.get('MinShipLevel'))
        self.__item_rank: int = _parse.pss_int(room_design_info.get('ItemRank'))
        self.__rotate: bool = _parse.pss_bool(room_design_info.get('Rotate'))
        self.__rows: int = _parse.pss_int(room_design_info.get('Rows'))
        self.__columns: int = _parse.pss_int(room_design_info.get('Columns'))
        self.__room_description: str = _parse.pss_str(room_design_info.get('RoomDescription'))
        self.__flip_on_enemy_ship: bool = _parse.pss_bool(room_design_info.get('FlipOnEnemyShip'))
        self.__root_room_design_id: int = _parse.pss_int(room_design_info.get('RootRoomDesignId'))
        self.__refill_unit_cost: int = _parse.pss_int(room_design_info.get('RefillUnitCost'))
        self.__default_defence_bonus: int = _parse.pss_int(room_design_info.get('DefaultDefenceBonus'))
        self.__price_string: str = _parse.pss_str(room_design_info.get('PriceString'))
        self.__sort_index: int = _parse.pss_int(room_design_info.get('SortIndex'))
        self.__flags: int = _parse.pss_int(room_design_info.get('Flags'))
        self.__target_type: str = _parse.pss_str(room_design_info.get('TargetType'))
        self.__supported_grid_types: int = _parse.pss_int(room_design_info.get('SupportedGridTypes'))
        self.__enhancement_type: str = _parse.pss_str(room_design_info.get('EnhancementType'))
        self.__cooldown_time: int = _parse.pss_int(room_design_info.get('CooldownTime'))
        self.__requirement_string: str = _parse.pss_str(room_design_info.get('RequirementString'))
        self.__range: int = _parse.pss_int(room_design_info.get('Range'))
        self.__refill_cost_string: str = _parse.pss_str(room_design_info.get('RefillCostString'))
        self.__metadata: str = _parse.pss_str(room_design_info.get('Metadata'))
        self.__max_count: int = _parse.pss_int(room_design_info.get('MaxCount'))
        self.__upgrade_from_room_design_id: int = _parse.pss_int(room_design_info.get('UpgradeFromRoomDesignId'))
        self.__missile_design_id: int = _parse.pss_int(room_design_info.get('MissileDesignId'))
        self.__interior_asset_id: int = _parse.pss_int(room_design_info.get('InteriorAssetId'))
        self.__exterior_asset_id: int = _parse.pss_int(room_design_info.get('ExteriorAssetId'))

    @property
    def room_design_id(self) -> int:
        return self.__room_design_id

    @property
    def room_name(self) -> str:
        return self.__room_name

    @property
    def room_short_name(self) -> str:
        return self.__room_short_name

    @property
    def room_type(self) -> str:
        return self.__room_type

    @property
    def max_system_power(self) -> int:
        return self.__max_system_power

    @property
    def construction_time(self) -> int:
        return self.__construction_time

    @property
    def capacity(self) -> int:
        return self.__capacity

    @property
    def reload_time(self) -> int:
        return self.__reload_time

    @property
    def image_sprite_id(self) -> int:
        return self.__image_sprite_id

    @property
    def logo_sprite_id(self) -> int:
        return self.__logo_sprite_id

    @property
    def max_power_generated(self) -> int:
        return self.__max_power_generated

    @property
    def random_improvements(self) -> int:
        return self.__random_improvements

    @property
    def improvement_amounts(self) -> int:
        return self.__improvement_amounts

    @property
    def manufacture_capacity(self) -> int:
        return self.__manufacture_capacity

    @property
    def manufacture_rate(self) -> int:
        return self.__manufacture_rate

    @property
    def manufacture_type(self) -> str:
        return self.__manufacture_type

    @property
    def level(self) -> int:
        return self.__level

    @property
    def category_type(self) -> str:
        return self.__category_type

    @property
    def construction_sprite_id(self) -> int:
        return self.__construction_sprite_id

    @property
    def min_ship_level(self) -> int:
        return self.__min_ship_level

    @property
    def item_rank(self) -> int:
        return self.__item_rank

    @property
    def rotate(self) -> bool:
        return self.__rotate

    @property
    def rows(self) -> int:
        return self.__rows

    @property
    def columns(self) -> int:
        return self.__columns

    @property
    def room_description(self) -> str:
        return self.__room_description

    @property
    def flip_on_enemy_ship(self) -> bool:
        return self.__flip_on_enemy_ship

    @property
    def root_room_design_id(self) -> int:
        return self.__root_room_design_id

    @property
    def refill_unit_cost(self) -> int:
        return self.__refill_unit_cost

    @property
    def default_defence_bonus(self) -> int:
        return self.__default_defence_bonus

    @property
    def price_string(self) -> str:
        return self.__price_string

    @property
    def sort_index(self) -> int:
        return self.__sort_index

    @property
    def flags(self) -> int:
        return self.__flags

    @property
    def target_type(self) -> str:
        return self.__target_type

    @property
    def supported_grid_types(self) -> int:
        return self.__supported_grid_types

    @property
    def enhancement_type(self) -> str:
        return self.__enhancement_type

    @property
    def cooldown_time(self) -> int:
        return self.__cooldown_time

    @property
    def requirement_string(self) -> str:
        return self.__requirement_string

    @property
    def range(self) -> int:
        return self.__range

    @property
    def refill_cost_string(self) -> str:
        return self.__refill_cost_string

    @property
    def metadata(self) -> str:
        return self.__metadata

    @property
    def max_count(self) -> int:
        return self.__max_count

    @property
    def upgrade_from_room_design_id(self) -> int:
        return self.__upgrade_from_room_design_id

    @property
    def missile_design_id(self) -> int:
        return self.__missile_design_id

    @property
    def interior_asset_id(self) -> int:
        return self.__interior_asset_id

    @property
    def exterior_asset_id(self) -> int:
        return self.__exterior_asset_id
