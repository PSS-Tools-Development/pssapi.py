"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict
from typing import List as _List

import pssapi.entities as _entities

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ShipRaw:
    XML_NODE_NAME: str = "Ship"

    def __init__(self, ship_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._brightness_value: float = _parse.pss_float(ship_info.get("BrightnessValue"))
        self._characters: _List[_entities.Character] = [_entities.Character(child_info) for child_info in ship_info.get("Characters")] if ship_info.get("Characters") else []
        self._from_star_system_id: int = _parse.pss_int(ship_info.get("FromStarSystemId"))
        self._hp: float = _parse.pss_float(ship_info.get("Hp"))
        self._hue_value: float = _parse.pss_float(ship_info.get("HueValue"))
        self._immunity_date: _datetime = _parse.pss_datetime(ship_info.get("ImmunityDate"))
        self._items: _List[_entities.Item] = [_entities.Item(child_info) for child_info in ship_info.get("Items")] if ship_info.get("Items") else []
        self._next_star_system_id: int = _parse.pss_int(ship_info.get("NextStarSystemId"))
        self._origin_next_star_system_id: int = _parse.pss_int(ship_info.get("OriginNextStarSystemId"))
        self._origin_star_system_id: int = _parse.pss_int(ship_info.get("OriginStarSystemId"))
        self._original_race_id: int = _parse.pss_int(ship_info.get("OriginalRaceId"))
        self._power_score: int = _parse.pss_int(ship_info.get("PowerScore"))
        self._rooms: _List[_entities.Room] = [_entities.Room(child_info) for child_info in ship_info.get("Rooms")] if ship_info.get("Rooms") else []
        self._salvage_argument: int = _parse.pss_int(ship_info.get("SalvageArgument"))
        self._saturation_value: float = _parse.pss_float(ship_info.get("SaturationValue"))
        self._shield: int = _parse.pss_int(ship_info.get("Shield"))
        self._ship_design_id: int = _parse.pss_int(ship_info.get("ShipDesignId"))
        self._ship_id: int = _parse.pss_int(ship_info.get("ShipId"))
        self._ship_level: int = _parse.pss_int(ship_info.get("ShipLevel"))
        self._ship_name: str = _parse.pss_str(ship_info.get("ShipName"))
        self._ship_status: str = _parse.pss_str(ship_info.get("ShipStatus"))
        self._skin_item_design_id: int = _parse.pss_int(ship_info.get("SkinItemDesignId"))
        self._skin_opacity_value: float = _parse.pss_float(ship_info.get("SkinOpacityValue"))
        self._standard_character_draws: int = _parse.pss_int(ship_info.get("StandardCharacterDraws"))
        self._star_system_arrival_date: _datetime = _parse.pss_datetime(ship_info.get("StarSystemArrivalDate"))
        self._star_system_id: int = _parse.pss_int(ship_info.get("StarSystemId"))
        self._status_start_date: _datetime = _parse.pss_datetime(ship_info.get("StatusStartDate"))
        self._sticker_string: str = _parse.pss_str(ship_info.get("StickerString"))
        self._tags: str = _parse.pss_str(ship_info.get("Tags"))
        self._unique_character_draws: int = _parse.pss_int(ship_info.get("UniqueCharacterDraws"))
        self._update_date: _datetime = _parse.pss_datetime(ship_info.get("UpdateDate"))
        self._upgrade_ship_design_id: int = _parse.pss_int(ship_info.get("UpgradeShipDesignId"))
        self._upgrade_start_date: _datetime = _parse.pss_datetime(ship_info.get("UpgradeStartDate"))
        self._user_id: int = _parse.pss_int(ship_info.get("UserId"))
        self._user_star_systems: _List[_entities.UserStarSystem] = [_entities.UserStarSystem(child_info) for child_info in ship_info.get("UserStarSystems")] if ship_info.get("UserStarSystems") else []

    @property
    def brightness_value(self) -> float:
        return self._brightness_value

    @property
    def characters(self) -> _List["_entities.Character"]:
        return self._characters

    @property
    def from_star_system_id(self) -> int:
        return self._from_star_system_id

    @property
    def hp(self) -> float:
        return self._hp

    @property
    def hue_value(self) -> float:
        return self._hue_value

    @property
    def immunity_date(self) -> _datetime:
        return self._immunity_date

    @property
    def items(self) -> _List["_entities.Item"]:
        return self._items

    @property
    def next_star_system_id(self) -> int:
        return self._next_star_system_id

    @property
    def origin_next_star_system_id(self) -> int:
        return self._origin_next_star_system_id

    @property
    def origin_star_system_id(self) -> int:
        return self._origin_star_system_id

    @property
    def original_race_id(self) -> int:
        return self._original_race_id

    @property
    def power_score(self) -> int:
        return self._power_score

    @property
    def rooms(self) -> _List["_entities.Room"]:
        return self._rooms

    @property
    def salvage_argument(self) -> int:
        return self._salvage_argument

    @property
    def saturation_value(self) -> float:
        return self._saturation_value

    @property
    def shield(self) -> int:
        return self._shield

    @property
    def ship_design_id(self) -> int:
        return self._ship_design_id

    @property
    def ship_id(self) -> int:
        return self._ship_id

    @property
    def ship_level(self) -> int:
        return self._ship_level

    @property
    def ship_name(self) -> str:
        return self._ship_name

    @property
    def ship_status(self) -> str:
        return self._ship_status

    @property
    def skin_item_design_id(self) -> int:
        return self._skin_item_design_id

    @property
    def skin_opacity_value(self) -> float:
        return self._skin_opacity_value

    @property
    def standard_character_draws(self) -> int:
        return self._standard_character_draws

    @property
    def star_system_arrival_date(self) -> _datetime:
        return self._star_system_arrival_date

    @property
    def star_system_id(self) -> int:
        return self._star_system_id

    @property
    def status_start_date(self) -> _datetime:
        return self._status_start_date

    @property
    def sticker_string(self) -> str:
        return self._sticker_string

    @property
    def tags(self) -> str:
        return self._tags

    @property
    def unique_character_draws(self) -> int:
        return self._unique_character_draws

    @property
    def update_date(self) -> _datetime:
        return self._update_date

    @property
    def upgrade_ship_design_id(self) -> int:
        return self._upgrade_ship_design_id

    @property
    def upgrade_start_date(self) -> _datetime:
        return self._upgrade_start_date

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def user_star_systems(self) -> _List["_entities.UserStarSystem"]:
        return self._user_star_systems

    def _key(self):
        return (
            self.brightness_value,
            tuple(child._key() for child in self.characters),
            self.from_star_system_id,
            self.hp,
            self.hue_value,
            self.immunity_date,
            tuple(child._key() for child in self.items),
            self.next_star_system_id,
            self.origin_next_star_system_id,
            self.origin_star_system_id,
            self.original_race_id,
            self.power_score,
            tuple(child._key() for child in self.rooms),
            self.salvage_argument,
            self.saturation_value,
            self.shield,
            self.ship_design_id,
            self.ship_id,
            self.ship_level,
            self.ship_name,
            self.ship_status,
            self.skin_item_design_id,
            self.skin_opacity_value,
            self.standard_character_draws,
            self.star_system_arrival_date,
            self.star_system_id,
            self.status_start_date,
            self.sticker_string,
            self.tags,
            self.unique_character_draws,
            self.update_date,
            self.upgrade_ship_design_id,
            self.upgrade_start_date,
            self.user_id,
            tuple(child._key() for child in self.user_star_systems),
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "BrightnessValue": self.brightness_value,
                "Characters": [dict(child) for child in self.characters],
                "FromStarSystemId": self.from_star_system_id,
                "Hp": self.hp,
                "HueValue": self.hue_value,
                "ImmunityDate": self.immunity_date,
                "Items": [dict(child) for child in self.items],
                "NextStarSystemId": self.next_star_system_id,
                "OriginNextStarSystemId": self.origin_next_star_system_id,
                "OriginStarSystemId": self.origin_star_system_id,
                "OriginalRaceId": self.original_race_id,
                "PowerScore": self.power_score,
                "Rooms": [dict(child) for child in self.rooms],
                "SalvageArgument": self.salvage_argument,
                "SaturationValue": self.saturation_value,
                "Shield": self.shield,
                "ShipDesignId": self.ship_design_id,
                "ShipId": self.ship_id,
                "ShipLevel": self.ship_level,
                "ShipName": self.ship_name,
                "ShipStatus": self.ship_status,
                "SkinItemDesignId": self.skin_item_design_id,
                "SkinOpacityValue": self.skin_opacity_value,
                "StandardCharacterDraws": self.standard_character_draws,
                "StarSystemArrivalDate": self.star_system_arrival_date,
                "StarSystemId": self.star_system_id,
                "StatusStartDate": self.status_start_date,
                "StickerString": self.sticker_string,
                "Tags": self.tags,
                "UniqueCharacterDraws": self.unique_character_draws,
                "UpdateDate": self.update_date,
                "UpgradeShipDesignId": self.upgrade_ship_design_id,
                "UpgradeStartDate": self.upgrade_start_date,
                "UserId": self.user_id,
                "UserStarSystems": [dict(child) for child in self.user_star_systems],
            }

        return self._dict
