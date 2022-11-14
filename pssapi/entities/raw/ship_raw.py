"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import List as _List

from ...entities import Character as _Character
from ...entities import Room as _Room
from ...entities import UserStarSystem as _UserStarSystem
from ...entities import Item as _Item
from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ShipRaw:
    XML_NODE_NAME: str = 'Ship'

    def __init__(self, ship_info: _EntityInfo) -> None:
        self.brightness_value: float = _parse.pss_float(ship_info.get('BrightnessValue'))
        self.characters: _List[_Character] = [_Character(child_info) for child_info in ship_info.get('Characters')]
        self.from_star_system_id: int = _parse.pss_int(ship_info.get('FromStarSystemId'))
        self.hp: int = _parse.pss_int(ship_info.get('Hp'))
        self.hue_value: float = _parse.pss_float(ship_info.get('HueValue'))
        self.immunity_date: _datetime = _parse.pss__datetime(ship_info.get('ImmunityDate'))
        self.items: _List[_Item] = [_Item(child_info) for child_info in ship_info.get('Items')]
        self.next_star_system_id: int = _parse.pss_int(ship_info.get('NextStarSystemId'))
        self.origin_next_star_system_id: int = _parse.pss_int(ship_info.get('OriginNextStarSystemId'))
        self.origin_star_system_id: int = _parse.pss_int(ship_info.get('OriginStarSystemId'))
        self.original_race_id: int = _parse.pss_int(ship_info.get('OriginalRaceId'))
        self.power_score: int = _parse.pss_int(ship_info.get('PowerScore'))
        self.rooms: _List[_Room] = [_Room(child_info) for child_info in ship_info.get('Rooms')]
        self.salvage_argument: int = _parse.pss_int(ship_info.get('SalvageArgument'))
        self.saturation_value: int = _parse.pss_int(ship_info.get('SaturationValue'))
        self.shield: int = _parse.pss_int(ship_info.get('Shield'))
        self.ship_design_id: int = _parse.pss_int(ship_info.get('ShipDesignId'))
        self.ship_id: int = _parse.pss_int(ship_info.get('ShipId'))
        self.ship_level: int = _parse.pss_int(ship_info.get('ShipLevel'))
        self.ship_name: str = _parse.pss_str(ship_info.get('ShipName'))
        self.ship_status: str = _parse.pss_str(ship_info.get('ShipStatus'))
        self.skin_item_design_id: int = _parse.pss_int(ship_info.get('SkinItemDesignId'))
        self.standard_character_draws: int = _parse.pss_int(ship_info.get('StandardCharacterDraws'))
        self.star_system_arrival_date: _datetime = _parse.pss__datetime(ship_info.get('StarSystemArrivalDate'))
        self.star_system_id: int = _parse.pss_int(ship_info.get('StarSystemId'))
        self.status_start_date: _datetime = _parse.pss__datetime(ship_info.get('StatusStartDate'))
        self.sticker_string: str = _parse.pss_str(ship_info.get('StickerString'))
        self.tags: str = _parse.pss_str(ship_info.get('Tags'))
        self.unique_character_draws: int = _parse.pss_int(ship_info.get('UniqueCharacterDraws'))
        self.update_date: _datetime = _parse.pss__datetime(ship_info.get('UpdateDate'))
        self.upgrade_ship_design_id: int = _parse.pss_int(ship_info.get('UpgradeShipDesignId'))
        self.upgrade_start_date: _datetime = _parse.pss__datetime(ship_info.get('UpgradeStartDate'))
        self.user_id: int = _parse.pss_int(ship_info.get('UserId'))
        self.user_star_systems: _List[_UserStarSystem] = [_UserStarSystem(child_info) for child_info in ship_info.get('UserStarSystems')]
