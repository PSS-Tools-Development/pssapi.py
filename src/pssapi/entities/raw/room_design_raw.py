"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class RoomDesignRaw:
    XML_NODE_NAME: str = "RoomDesign"

    def __init__(self, room_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._capacity: int = _parse.pss_int(room_design_info.get("Capacity"))
        self._category_type: str = _parse.pss_str(room_design_info.get("CategoryType"))
        self._columns: int = _parse.pss_int(room_design_info.get("Columns"))
        self._construction_sprite_id: int = _parse.pss_int(room_design_info.get("ConstructionSpriteId"))
        self._construction_time: int = _parse.pss_int(room_design_info.get("ConstructionTime"))
        self._cooldown_time: int = _parse.pss_int(room_design_info.get("CooldownTime"))
        self._craft_design_id: int = _parse.pss_int(room_design_info.get("CraftDesignId"))
        self._default_defence_bonus: int = _parse.pss_int(room_design_info.get("DefaultDefenceBonus"))
        self._enhancement_type: str = _parse.pss_str(room_design_info.get("EnhancementType"))
        self._exterior_asset_id: int = _parse.pss_int(room_design_info.get("ExteriorAssetId"))
        self._flags: int = _parse.pss_int(room_design_info.get("Flags"))
        self._flip_on_enemy_ship: bool = _parse.pss_bool(room_design_info.get("FlipOnEnemyShip"))
        self._image_sprite_id: int = _parse.pss_int(room_design_info.get("ImageSpriteId"))
        self._improvement_amounts: int = _parse.pss_int(room_design_info.get("ImprovementAmounts"))
        self._interior_asset_id: int = _parse.pss_int(room_design_info.get("InteriorAssetId"))
        self._item_rank: int = _parse.pss_int(room_design_info.get("ItemRank"))
        self._level: int = _parse.pss_int(room_design_info.get("Level"))
        self._logo_sprite_id: int = _parse.pss_int(room_design_info.get("LogoSpriteId"))
        self._manufacture_capacity: int = _parse.pss_int(room_design_info.get("ManufactureCapacity"))
        self._manufacture_rate: float = _parse.pss_float(room_design_info.get("ManufactureRate"))
        self._manufacture_type: str = _parse.pss_str(room_design_info.get("ManufactureType"))
        self._max_count: int = _parse.pss_int(room_design_info.get("MaxCount"))
        self._max_power_generated: int = _parse.pss_int(room_design_info.get("MaxPowerGenerated"))
        self._max_system_power: int = _parse.pss_int(room_design_info.get("MaxSystemPower"))
        self._metadata: str = _parse.pss_str(room_design_info.get("Metadata"))
        self._min_ship_level: int = _parse.pss_int(room_design_info.get("MinShipLevel"))
        self._missile_design_id: int = _parse.pss_int(room_design_info.get("MissileDesignId"))
        self._price_string: str = _parse.pss_str(room_design_info.get("PriceString"))
        self._random_improvements: int = _parse.pss_int(room_design_info.get("RandomImprovements"))
        self._range: int = _parse.pss_int(room_design_info.get("Range"))
        self._refill_cost_string: str = _parse.pss_str(room_design_info.get("RefillCostString"))
        self._refill_unit_cost: int = _parse.pss_int(room_design_info.get("RefillUnitCost"))
        self._reload_time: int = _parse.pss_int(room_design_info.get("ReloadTime"))
        self._requirement_string: str = _parse.pss_str(room_design_info.get("RequirementString"))
        self._room_description: str = _parse.pss_str(room_design_info.get("RoomDescription"))
        self._room_design_id: int = _parse.pss_int(room_design_info.get("RoomDesignId"))
        self._room_name: str = _parse.pss_str(room_design_info.get("RoomName"))
        self._room_short_name: str = _parse.pss_str(room_design_info.get("RoomShortName"))
        self._room_type: str = _parse.pss_str(room_design_info.get("RoomType"))
        self._root_room_design_id: int = _parse.pss_int(room_design_info.get("RootRoomDesignId"))
        self._rotate: bool = _parse.pss_bool(room_design_info.get("Rotate"))
        self._rows: int = _parse.pss_int(room_design_info.get("Rows"))
        self._sort_index: int = _parse.pss_int(room_design_info.get("SortIndex"))
        self._supported_grid_types: int = _parse.pss_int(room_design_info.get("SupportedGridTypes"))
        self._target_type: str = _parse.pss_str(room_design_info.get("TargetType"))
        self._upgrade_from_room_design_id: int = _parse.pss_int(room_design_info.get("UpgradeFromRoomDesignId"))

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def category_type(self) -> str:
        return self._category_type

    @property
    def columns(self) -> int:
        return self._columns

    @property
    def construction_sprite_id(self) -> int:
        return self._construction_sprite_id

    @property
    def construction_time(self) -> int:
        return self._construction_time

    @property
    def cooldown_time(self) -> int:
        return self._cooldown_time

    @property
    def craft_design_id(self) -> int:
        return self._craft_design_id

    @property
    def default_defence_bonus(self) -> int:
        return self._default_defence_bonus

    @property
    def enhancement_type(self) -> str:
        return self._enhancement_type

    @property
    def exterior_asset_id(self) -> int:
        return self._exterior_asset_id

    @property
    def flags(self) -> int:
        return self._flags

    @property
    def flip_on_enemy_ship(self) -> bool:
        return self._flip_on_enemy_ship

    @property
    def image_sprite_id(self) -> int:
        return self._image_sprite_id

    @property
    def improvement_amounts(self) -> int:
        return self._improvement_amounts

    @property
    def interior_asset_id(self) -> int:
        return self._interior_asset_id

    @property
    def item_rank(self) -> int:
        return self._item_rank

    @property
    def level(self) -> int:
        return self._level

    @property
    def logo_sprite_id(self) -> int:
        return self._logo_sprite_id

    @property
    def manufacture_capacity(self) -> int:
        return self._manufacture_capacity

    @property
    def manufacture_rate(self) -> float:
        return self._manufacture_rate

    @property
    def manufacture_type(self) -> str:
        return self._manufacture_type

    @property
    def max_count(self) -> int:
        return self._max_count

    @property
    def max_power_generated(self) -> int:
        return self._max_power_generated

    @property
    def max_system_power(self) -> int:
        return self._max_system_power

    @property
    def metadata(self) -> str:
        return self._metadata

    @property
    def min_ship_level(self) -> int:
        return self._min_ship_level

    @property
    def missile_design_id(self) -> int:
        return self._missile_design_id

    @property
    def price_string(self) -> str:
        return self._price_string

    @property
    def random_improvements(self) -> int:
        return self._random_improvements

    @property
    def range(self) -> int:
        return self._range

    @property
    def refill_cost_string(self) -> str:
        return self._refill_cost_string

    @property
    def refill_unit_cost(self) -> int:
        return self._refill_unit_cost

    @property
    def reload_time(self) -> int:
        return self._reload_time

    @property
    def requirement_string(self) -> str:
        return self._requirement_string

    @property
    def room_description(self) -> str:
        return self._room_description

    @property
    def room_design_id(self) -> int:
        return self._room_design_id

    @property
    def room_name(self) -> str:
        return self._room_name

    @property
    def room_short_name(self) -> str:
        return self._room_short_name

    @property
    def room_type(self) -> str:
        return self._room_type

    @property
    def root_room_design_id(self) -> int:
        return self._root_room_design_id

    @property
    def rotate(self) -> bool:
        return self._rotate

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def sort_index(self) -> int:
        return self._sort_index

    @property
    def supported_grid_types(self) -> int:
        return self._supported_grid_types

    @property
    def target_type(self) -> str:
        return self._target_type

    @property
    def upgrade_from_room_design_id(self) -> int:
        return self._upgrade_from_room_design_id

    def _key(self):
        return (
            self.capacity,
            self.category_type,
            self.columns,
            self.construction_sprite_id,
            self.construction_time,
            self.cooldown_time,
            self.craft_design_id,
            self.default_defence_bonus,
            self.enhancement_type,
            self.exterior_asset_id,
            self.flags,
            self.flip_on_enemy_ship,
            self.image_sprite_id,
            self.improvement_amounts,
            self.interior_asset_id,
            self.item_rank,
            self.level,
            self.logo_sprite_id,
            self.manufacture_capacity,
            self.manufacture_rate,
            self.manufacture_type,
            self.max_count,
            self.max_power_generated,
            self.max_system_power,
            self.metadata,
            self.min_ship_level,
            self.missile_design_id,
            self.price_string,
            self.random_improvements,
            self.range,
            self.refill_cost_string,
            self.refill_unit_cost,
            self.reload_time,
            self.requirement_string,
            self.room_description,
            self.room_design_id,
            self.room_name,
            self.room_short_name,
            self.room_type,
            self.root_room_design_id,
            self.rotate,
            self.rows,
            self.sort_index,
            self.supported_grid_types,
            self.target_type,
            self.upgrade_from_room_design_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "Capacity": self.capacity,
                "CategoryType": self.category_type,
                "Columns": self.columns,
                "ConstructionSpriteId": self.construction_sprite_id,
                "ConstructionTime": self.construction_time,
                "CooldownTime": self.cooldown_time,
                "CraftDesignId": self.craft_design_id,
                "DefaultDefenceBonus": self.default_defence_bonus,
                "EnhancementType": self.enhancement_type,
                "ExteriorAssetId": self.exterior_asset_id,
                "Flags": self.flags,
                "FlipOnEnemyShip": self.flip_on_enemy_ship,
                "ImageSpriteId": self.image_sprite_id,
                "ImprovementAmounts": self.improvement_amounts,
                "InteriorAssetId": self.interior_asset_id,
                "ItemRank": self.item_rank,
                "Level": self.level,
                "LogoSpriteId": self.logo_sprite_id,
                "ManufactureCapacity": self.manufacture_capacity,
                "ManufactureRate": self.manufacture_rate,
                "ManufactureType": self.manufacture_type,
                "MaxCount": self.max_count,
                "MaxPowerGenerated": self.max_power_generated,
                "MaxSystemPower": self.max_system_power,
                "Metadata": self.metadata,
                "MinShipLevel": self.min_ship_level,
                "MissileDesignId": self.missile_design_id,
                "PriceString": self.price_string,
                "RandomImprovements": self.random_improvements,
                "Range": self.range,
                "RefillCostString": self.refill_cost_string,
                "RefillUnitCost": self.refill_unit_cost,
                "ReloadTime": self.reload_time,
                "RequirementString": self.requirement_string,
                "RoomDescription": self.room_description,
                "RoomDesignId": self.room_design_id,
                "RoomName": self.room_name,
                "RoomShortName": self.room_short_name,
                "RoomType": self.room_type,
                "RootRoomDesignId": self.root_room_design_id,
                "Rotate": self.rotate,
                "Rows": self.rows,
                "SortIndex": self.sort_index,
                "SupportedGridTypes": self.supported_grid_types,
                "TargetType": self.target_type,
                "UpgradeFromRoomDesignId": self.upgrade_from_room_design_id,
            }

        return self._dict
