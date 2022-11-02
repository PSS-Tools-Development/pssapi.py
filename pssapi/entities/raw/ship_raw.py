"""
    This file has been generated automatically
"""

from datetime import datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ShipRaw:
    XML_NODE_NAME: str = 'Ship'

    def __init__(self, ship_info: _EntityInfo) -> None:
        self.__salvage_argument: int = _parse.pss_int(
            ship_info.get('SalvageArgument'))
        self.__ship_status: str = _parse.pss_str(ship_info.get('ShipStatus'))
        self.__immunity_date: datetime = _parse.pss_datetime(
            ship_info.get('ImmunityDate'))
        self.__next_star_system_id: int = _parse.pss_int(
            ship_info.get('NextStarSystemId'))
        self.__star_system_id: int = _parse.pss_int(
            ship_info.get('StarSystemId'))
        self.__from_star_system_id: int = _parse.pss_int(
            ship_info.get('FromStarSystemId'))
        self.__hp: int = _parse.pss_int(ship_info.get('Hp'))
        self.__user_id: int = _parse.pss_int(ship_info.get('UserId'))
        self.__ship_name: str = _parse.pss_str(ship_info.get('ShipName'))
        self.__unique_character_draws: int = _parse.pss_int(
            ship_info.get('UniqueCharacterDraws'))
        self.__ship_id: int = _parse.pss_int(ship_info.get('ShipId'))
        self.__origin_star_system_id: int = _parse.pss_int(
            ship_info.get('OriginStarSystemId'))
        self.__shield: int = _parse.pss_int(ship_info.get('Shield'))
        self.__skin_item_design_id: int = _parse.pss_int(
            ship_info.get('SkinItemDesignId'))
        self.__saturation_value: int = _parse.pss_int(
            ship_info.get('SaturationValue'))
        self.__ship_level: int = _parse.pss_int(ship_info.get('ShipLevel'))
        self.__star_system_arrival_date: datetime = _parse.pss_datetime(
            ship_info.get('StarSystemArrivalDate'))
        self.__update_date: datetime = _parse.pss_datetime(
            ship_info.get('UpdateDate'))
        self.__hue_value: float = _parse.pss_float(ship_info.get('HueValue'))
        self.__sticker_string: str = _parse.pss_str(
            ship_info.get('StickerString'))
        self.__upgrade_ship_design_id: int = _parse.pss_int(
            ship_info.get('UpgradeShipDesignId'))
        self.__original_race_id: int = _parse.pss_int(
            ship_info.get('OriginalRaceId'))
        self.__upgrade_start_date: datetime = _parse.pss_datetime(
            ship_info.get('UpgradeStartDate'))
        self.__status_start_date: datetime = _parse.pss_datetime(
            ship_info.get('StatusStartDate'))
        self.__power_score: int = _parse.pss_int(ship_info.get('PowerScore'))
        self.__standard_character_draws: int = _parse.pss_int(
            ship_info.get('StandardCharacterDraws'))
        self.__tags: str = _parse.pss_str(ship_info.get('Tags'))
        self.__ship_design_id: int = _parse.pss_int(
            ship_info.get('ShipDesignId'))
        self.__origin_next_star_system_id: int = _parse.pss_int(
            ship_info.get('OriginNextStarSystemId'))
        self.__brightness_value: float = _parse.pss_float(
            ship_info.get('BrightnessValue'))

    @property
    def salvage_argument(self) -> int:
        return self.__salvage_argument

    @property
    def ship_status(self) -> str:
        return self.__ship_status

    @property
    def immunity_date(self) -> datetime:
        return self.__immunity_date

    @property
    def next_star_system_id(self) -> int:
        return self.__next_star_system_id

    @property
    def star_system_id(self) -> int:
        return self.__star_system_id

    @property
    def from_star_system_id(self) -> int:
        return self.__from_star_system_id

    @property
    def hp(self) -> int:
        return self.__hp

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def ship_name(self) -> str:
        return self.__ship_name

    @property
    def unique_character_draws(self) -> int:
        return self.__unique_character_draws

    @property
    def ship_id(self) -> int:
        return self.__ship_id

    @property
    def origin_star_system_id(self) -> int:
        return self.__origin_star_system_id

    @property
    def shield(self) -> int:
        return self.__shield

    @property
    def skin_item_design_id(self) -> int:
        return self.__skin_item_design_id

    @property
    def saturation_value(self) -> int:
        return self.__saturation_value

    @property
    def ship_level(self) -> int:
        return self.__ship_level

    @property
    def star_system_arrival_date(self) -> datetime:
        return self.__star_system_arrival_date

    @property
    def update_date(self) -> datetime:
        return self.__update_date

    @property
    def hue_value(self) -> float:
        return self.__hue_value

    @property
    def sticker_string(self) -> str:
        return self.__sticker_string

    @property
    def upgrade_ship_design_id(self) -> int:
        return self.__upgrade_ship_design_id

    @property
    def original_race_id(self) -> int:
        return self.__original_race_id

    @property
    def upgrade_start_date(self) -> datetime:
        return self.__upgrade_start_date

    @property
    def status_start_date(self) -> datetime:
        return self.__status_start_date

    @property
    def power_score(self) -> int:
        return self.__power_score

    @property
    def standard_character_draws(self) -> int:
        return self.__standard_character_draws

    @property
    def tags(self) -> str:
        return self.__tags

    @property
    def ship_design_id(self) -> int:
        return self.__ship_design_id

    @property
    def origin_next_star_system_id(self) -> int:
        return self.__origin_next_star_system_id

    @property
    def brightness_value(self) -> float:
        return self.__brightness_value
