"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import List as _List

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class RoomRaw:
    XML_NODE_NAME: str = 'Room'

    def __init__(self, room_info: _EntityInfo) -> None:
        self.capacity_used: int = _parse.pss_int(room_info.get('CapacityUsed'))
        self.column: int = _parse.pss_int(room_info.get('Column'))
        self.construction_start_date: str = _parse.pss_str(room_info.get('ConstructionStartDate'))
        self.current_skin_key: int = _parse.pss_int(room_info.get('CurrentSkinKey'))
        self.item_ids: str = _parse.pss_str(room_info.get('ItemIds'))
        self.manufacture_start_date: str = _parse.pss_str(room_info.get('ManufactureStartDate'))
        self.manufacture_string: str = _parse.pss_str(room_info.get('ManufactureString'))
        self.manufactured: int = _parse.pss_int(room_info.get('Manufactured'))
        self.power_generated: int = _parse.pss_int(room_info.get('PowerGenerated'))
        self.previous_skin_key: int = _parse.pss_int(room_info.get('PreviousSkinKey'))
        self.random_seed: int = _parse.pss_int(room_info.get('RandomSeed'))
        self.room_design_id: int = _parse.pss_int(room_info.get('RoomDesignId'))
        self.room_id: int = _parse.pss_int(room_info.get('RoomId'))
        self.room_status: str = _parse.pss_str(room_info.get('RoomStatus'))
        self.row: int = _parse.pss_int(room_info.get('Row'))
        self.salvage_string: str = _parse.pss_str(room_info.get('SalvageString'))
        self.ship_id: int = _parse.pss_int(room_info.get('ShipId'))
        self.target_manufacture_string: str = _parse.pss_str(room_info.get('TargetManufactureString'))
        self.upgrade_room_design_id: int = _parse.pss_int(room_info.get('UpgradeRoomDesignId'))
