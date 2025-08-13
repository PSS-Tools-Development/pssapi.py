"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from pydantic_xml import attr, element, wrapped


if TYPE_CHECKING:
    from pssapi import entities

from .entity_base_raw import EntityBaseRaw


class RoomRaw(EntityBaseRaw, tag="Room"):
    XML_NODE_NAME: str = "Room"

    assigned_power: Optional[int] = attr(name="AssignedPower", default=None)
    capacity_used: Optional[int] = attr(name="CapacityUsed", default=None)
    center_x: Optional[int] = attr(name="CenterX", default=None)
    center_y: Optional[int] = attr(name="CenterY", default=None)
    column: Optional[int] = attr(name="Column", default=None)
    construction_start_date: Optional[datetime] = attr(name="ConstructionStartDate", default=None)
    current_capacity: Optional[int] = attr(name="CurrentCapacity", default=None)
    current_skin_key: Optional[int] = attr(name="CurrentSkinKey", default=None)
    disable_count: Optional[int] = attr(name="DisableCount", default=None)
    is_power_ai_active: Optional[bool] = attr(name="IsPowerAIActive", default=None)
    is_set_item_ai_active: Optional[bool] = attr(name="IsSetItemAIActive", default=None)
    is_target_ai_active: Optional[bool] = attr(name="IsTargetAIActive", default=None)
    item_ids: Optional[str] = attr(name="ItemIds", default=None)
    item_skin_key: Optional[int] = attr(name="ItemSkinKey", default=None)
    local_center_x: Optional[int] = attr(name="LocalCenterX", default=None)
    local_center_y: Optional[int] = attr(name="LocalCenterY", default=None)
    manufacture_start_date: Optional[datetime] = attr(name="ManufactureStartDate", default=None)
    manufacture_string: Optional[str] = attr(name="ManufactureString", default=None)
    manufactured: Optional[int] = attr(name="Manufactured", default=None)
    power_generated: Optional[int] = attr(name="PowerGenerated", default=None)
    previous_skin_key: Optional[int] = attr(name="PreviousSkinKey", default=None)
    progress: Optional[int] = attr(name="Progress", default=None)
    protect_room_frame: Optional[int] = attr(name="ProtectRoomFrame", default=None)
    random_seed: Optional[int] = attr(name="RandomSeed", default=None)
    room_actions: List["entities.RoomAction"] = wrapped("RoomActions", element(tag="RoomAction", default_factory=list))
    room_design_id: Optional[int] = attr(name="RoomDesignId", default=None)
    room_id: Optional[int] = attr(name="RoomId", default=None)
    room_status: Optional[str] = attr(name="RoomStatus", default=None)
    row: Optional[int] = attr(name="Row", default=None)
    run_room_action: Optional[bool] = attr(name="RunRoomAction", default=None)
    salvage_string: Optional[str] = attr(name="SalvageString", default=None)
    ship_id: Optional[int] = attr(name="ShipId", default=None)
    skin_key: Optional[int] = attr(name="SkinKey", default=None)
    system_power: Optional[int] = attr(name="SystemPower", default=None)
    target_craft_id: Optional[int] = attr(name="TargetCraftId", default=None)
    target_manufacture_string: Optional[str] = attr(name="TargetManufactureString", default=None)
    target_room_id: Optional[int] = attr(name="TargetRoomId", default=None)
    top_left_x: Optional[int] = attr(name="TopLeftX", default=None)
    top_left_y: Optional[int] = attr(name="TopLeftY", default=None)
    total_damage: Optional[int] = attr(name="TotalDamage", default=None)
    upgrade_room_design_id: Optional[int] = attr(name="UpgradeRoomDesignId", default=None)

    def _key(self):
        return (
            self.assigned_power,
            self.capacity_used,
            self.center_x,
            self.center_y,
            self.column,
            self.construction_start_date,
            self.current_capacity,
            self.current_skin_key,
            self.disable_count,
            self.is_power_ai_active,
            self.is_set_item_ai_active,
            self.is_target_ai_active,
            self.item_ids,
            self.item_skin_key,
            self.local_center_x,
            self.local_center_y,
            self.manufacture_start_date,
            self.manufacture_string,
            self.manufactured,
            self.power_generated,
            self.previous_skin_key,
            self.progress,
            self.protect_room_frame,
            self.random_seed,
            tuple(child._key() for child in self.room_actions),
            self.room_design_id,
            self.room_id,
            self.room_status,
            self.row,
            self.run_room_action,
            self.salvage_string,
            self.ship_id,
            self.skin_key,
            self.system_power,
            self.target_craft_id,
            self.target_manufacture_string,
            self.target_room_id,
            self.top_left_x,
            self.top_left_y,
            self.total_damage,
            self.upgrade_room_design_id,
        )


__all__ = [
    "RoomRaw",
]
