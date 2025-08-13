"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from pydantic_xml import attr, element, wrapped


if TYPE_CHECKING:
    from pssapi import entities

from .entity_base_raw import EntityBaseRaw


class ShipRaw(EntityBaseRaw, tag="Ship"):
    XML_NODE_NAME: str = "Ship"

    brightness_value: Optional[float] = attr(name="BrightnessValue", default=None)
    center_x: Optional[int] = attr(name="CenterX", default=None)
    center_y: Optional[int] = attr(name="CenterY", default=None)
    characters: List["entities.Character"] = wrapped("Characters", element(tag="Character", default_factory=list))
    from_star_system_id: Optional[int] = attr(name="FromStarSystemId", default=None)
    hp: Optional[float] = attr(name="Hp", default=None)
    hue_value: Optional[float] = attr(name="HueValue", default=None)
    immunity_date: Optional[datetime] = attr(name="ImmunityDate", default=None)
    items: List["entities.Item"] = wrapped("Items", element(tag="Item", default_factory=list))
    next_android_character_id: Optional[int] = attr(name="NextAndroidCharacterId", default=None)
    next_star_system_id: Optional[int] = attr(name="NextStarSystemId", default=None)
    origin_next_star_system_id: Optional[int] = attr(name="OriginNextStarSystemId", default=None)
    origin_star_system_id: Optional[int] = attr(name="OriginStarSystemId", default=None)
    original_race_id: Optional[int] = attr(name="OriginalRaceId", default=None)
    power_score: Optional[int] = attr(name="PowerScore", default=None)
    rooms: List["entities.Room"] = wrapped("Rooms", element(tag="Room", default_factory=list))
    salvage_argument: Optional[int] = attr(name="SalvageArgument", default=None)
    saturation_value: Optional[float] = attr(name="SaturationValue", default=None)
    shield: Optional[int] = attr(name="Shield", default=None)
    ship_design_id: Optional[int] = attr(name="ShipDesignId", default=None)
    ship_id: Optional[int] = attr(name="ShipId", default=None)
    ship_level: Optional[int] = attr(name="ShipLevel", default=None)
    ship_name: Optional[str] = attr(name="ShipName", default=None)
    ship_status: Optional[str] = attr(name="ShipStatus", default=None)
    skin_item_design_id: Optional[int] = attr(name="SkinItemDesignId", default=None)
    skin_opacity_value: Optional[float] = attr(name="SkinOpacityValue", default=None)
    standard_character_draws: Optional[int] = attr(name="StandardCharacterDraws", default=None)
    star_system_arrival_date: Optional[datetime] = attr(name="StarSystemArrivalDate", default=None)
    star_system_id: Optional[int] = attr(name="StarSystemId", default=None)
    status_start_date: Optional[datetime] = attr(name="StatusStartDate", default=None)
    sticker_string: Optional[str] = attr(name="StickerString", default=None)
    tags: Optional[str] = attr(name="Tags", default=None)
    top_left_x: Optional[int] = attr(name="TopLeftX", default=None)
    top_left_y: Optional[int] = attr(name="TopLeftY", default=None)
    unique_character_draws: Optional[int] = attr(name="UniqueCharacterDraws", default=None)
    update_date: Optional[datetime] = attr(name="UpdateDate", default=None)
    upgrade_ship_design_id: Optional[int] = attr(name="UpgradeShipDesignId", default=None)
    upgrade_start_date: Optional[datetime] = attr(name="UpgradeStartDate", default=None)
    user_id: Optional[int] = attr(name="UserId", default=None)
    user_star_systems: List["entities.UserStarSystem"] = wrapped("UserStarSystems", element(tag="UserStarSystem", default_factory=list))

    def _key(self):
        return (
            self.brightness_value,
            self.center_x,
            self.center_y,
            tuple(child._key() for child in self.characters),
            self.from_star_system_id,
            self.hp,
            self.hue_value,
            self.immunity_date,
            tuple(child._key() for child in self.items),
            self.next_android_character_id,
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
            self.top_left_x,
            self.top_left_y,
            self.unique_character_draws,
            self.update_date,
            self.upgrade_ship_design_id,
            self.upgrade_start_date,
            self.user_id,
            tuple(child._key() for child in self.user_star_systems),
        )


__all__ = [
    "ShipRaw",
]
