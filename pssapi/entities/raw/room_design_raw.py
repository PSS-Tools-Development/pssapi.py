"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import List as _List

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class RoomDesignRaw:
    XML_NODE_NAME: str = 'RoomDesign'

    def __init__(self, room_design_info: _EntityInfo) -> None:
        self.capacity: int = _parse.pss_int(room_design_info.get('Capacity'))
        self.category_type: str = _parse.pss_str(room_design_info.get('CategoryType'))
        self.columns: int = _parse.pss_int(room_design_info.get('Columns'))
        self.construction_sprite_id: int = _parse.pss_int(room_design_info.get('ConstructionSpriteId'))
        self.construction_time: int = _parse.pss_int(room_design_info.get('ConstructionTime'))
        self.cooldown_time: int = _parse.pss_int(room_design_info.get('CooldownTime'))
        self.default_defence_bonus: int = _parse.pss_int(room_design_info.get('DefaultDefenceBonus'))
        self.enhancement_type: str = _parse.pss_str(room_design_info.get('EnhancementType'))
        self.exterior_asset_id: int = _parse.pss_int(room_design_info.get('ExteriorAssetId'))
        self.flags: int = _parse.pss_int(room_design_info.get('Flags'))
        self.flip_on_enemy_ship: bool = _parse.pss_bool(room_design_info.get('FlipOnEnemyShip'))
        self.image_sprite_id: int = _parse.pss_int(room_design_info.get('ImageSpriteId'))
        self.improvement_amounts: int = _parse.pss_int(room_design_info.get('ImprovementAmounts'))
        self.interior_asset_id: int = _parse.pss_int(room_design_info.get('InteriorAssetId'))
        self.item_rank: int = _parse.pss_int(room_design_info.get('ItemRank'))
        self.level: int = _parse.pss_int(room_design_info.get('Level'))
        self.logo_sprite_id: int = _parse.pss_int(room_design_info.get('LogoSpriteId'))
        self.manufacture_capacity: int = _parse.pss_int(room_design_info.get('ManufactureCapacity'))
        self.manufacture_rate: float = _parse.pss_float(room_design_info.get('ManufactureRate'))
        self.manufacture_type: str = _parse.pss_str(room_design_info.get('ManufactureType'))
        self.max_count: int = _parse.pss_int(room_design_info.get('MaxCount'))
        self.max_power_generated: int = _parse.pss_int(room_design_info.get('MaxPowerGenerated'))
        self.max_system_power: int = _parse.pss_int(room_design_info.get('MaxSystemPower'))
        self.metadata: str = _parse.pss_str(room_design_info.get('Metadata'))
        self.min_ship_level: int = _parse.pss_int(room_design_info.get('MinShipLevel'))
        self.missile_design_id: int = _parse.pss_int(room_design_info.get('MissileDesignId'))
        self.price_string: str = _parse.pss_str(room_design_info.get('PriceString'))
        self.random_improvements: int = _parse.pss_int(room_design_info.get('RandomImprovements'))
        self.range: int = _parse.pss_int(room_design_info.get('Range'))
        self.refill_cost_string: str = _parse.pss_str(room_design_info.get('RefillCostString'))
        self.refill_unit_cost: int = _parse.pss_int(room_design_info.get('RefillUnitCost'))
        self.reload_time: int = _parse.pss_int(room_design_info.get('ReloadTime'))
        self.requirement_string: str = _parse.pss_str(room_design_info.get('RequirementString'))
        self.room_description: str = _parse.pss_str(room_design_info.get('RoomDescription'))
        self.room_design_id: int = _parse.pss_int(room_design_info.get('RoomDesignId'))
        self.room_name: str = _parse.pss_str(room_design_info.get('RoomName'))
        self.room_short_name: str = _parse.pss_str(room_design_info.get('RoomShortName'))
        self.room_type: str = _parse.pss_str(room_design_info.get('RoomType'))
        self.root_room_design_id: int = _parse.pss_int(room_design_info.get('RootRoomDesignId'))
        self.rotate: bool = _parse.pss_bool(room_design_info.get('Rotate'))
        self.rows: int = _parse.pss_int(room_design_info.get('Rows'))
        self.sort_index: int = _parse.pss_int(room_design_info.get('SortIndex'))
        self.supported_grid_types: int = _parse.pss_int(room_design_info.get('SupportedGridTypes'))
        self.target_type: str = _parse.pss_str(room_design_info.get('TargetType'))
        self.upgrade_from_room_design_id: int = _parse.pss_int(room_design_info.get('UpgradeFromRoomDesignId'))
