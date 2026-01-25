"""
This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

import pssapi.entities as _entities

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class StarSystemDetailRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "StarSystemDetail"

    def __init__(self, star_system_detail_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._engagement_cooldown_end_date: _datetime = _parse.pss_datetime(star_system_detail_info.pop("EngagementCooldownEndDate", None))
        self._immunity_end_date: _datetime = _parse.pss_datetime(star_system_detail_info.pop("ImmunityEndDate", None))
        self._owner_icon_sprite_id: int = _parse.pss_int(star_system_detail_info.pop("OwnerIconSpriteId", None))
        self._owner_id: int = _parse.pss_int(star_system_detail_info.pop("OwnerId", None))
        self._owner_name: str = _parse.pss_str(star_system_detail_info.pop("OwnerName", None))
        self._owner_type: str = _parse.pss_str(star_system_detail_info.pop("OwnerType", None))
        self._ship_garrison_info_string: str = _parse.pss_str(star_system_detail_info.pop("ShipGarrisonInfoString", None))
        self._ship_garrison_string: str = _parse.pss_str(star_system_detail_info.pop("ShipGarrisonString", None))
        self._ship_manufacture_start_date: _datetime = _parse.pss_datetime(star_system_detail_info.pop("ShipManufactureStartDate", None))
        self._star_system_detail_id: int = _parse.pss_int(star_system_detail_info.pop("StarSystemDetailId", None))
        self._star_system_id: int = _parse.pss_int(star_system_detail_info.pop("StarSystemId", None))
        self._star_system_infrastructures: _entities.StarSystemInfrastructures = (
            _entities.StarSystemInfrastructures(star_system_detail_info.pop("StarSystemInfrastructures")[0]) if star_system_detail_info.get("StarSystemInfrastructures", []) else None
        )
        super().__init__(star_system_detail_info)

    @property
    def engagement_cooldown_end_date(self) -> _datetime:
        return self._engagement_cooldown_end_date

    @property
    def immunity_end_date(self) -> _datetime:
        return self._immunity_end_date

    @property
    def owner_icon_sprite_id(self) -> int:
        return self._owner_icon_sprite_id

    @property
    def owner_id(self) -> int:
        return self._owner_id

    @property
    def owner_name(self) -> str:
        return self._owner_name

    @property
    def owner_type(self) -> str:
        return self._owner_type

    @property
    def ship_garrison_info_string(self) -> str:
        return self._ship_garrison_info_string

    @property
    def ship_garrison_string(self) -> str:
        return self._ship_garrison_string

    @property
    def ship_manufacture_start_date(self) -> _datetime:
        return self._ship_manufacture_start_date

    @property
    def star_system_detail_id(self) -> int:
        return self._star_system_detail_id

    @property
    def star_system_id(self) -> int:
        return self._star_system_id

    @property
    def star_system_infrastructures(self) -> "_entities.StarSystemInfrastructures":
        return self._star_system_infrastructures

    def _key(self):
        return (
            self.engagement_cooldown_end_date,
            self.immunity_end_date,
            self.owner_icon_sprite_id,
            self.owner_id,
            self.owner_name,
            self.owner_type,
            self.ship_garrison_info_string,
            self.ship_garrison_string,
            self.ship_manufacture_start_date,
            self.star_system_detail_id,
            self.star_system_id,
            self.star_system_infrastructures._key() if self.star_system_infrastructures else None,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "EngagementCooldownEndDate": self.engagement_cooldown_end_date,
                "ImmunityEndDate": self.immunity_end_date,
                "OwnerIconSpriteId": self.owner_icon_sprite_id,
                "OwnerId": self.owner_id,
                "OwnerName": self.owner_name,
                "OwnerType": self.owner_type,
                "ShipGarrisonInfoString": self.ship_garrison_info_string,
                "ShipGarrisonString": self.ship_garrison_string,
                "ShipManufactureStartDate": self.ship_manufacture_start_date,
                "StarSystemDetailId": self.star_system_detail_id,
                "StarSystemId": self.star_system_id,
                "StarSystemInfrastructures": dict(self.star_system_infrastructures) if self.star_system_infrastructures else None,
            }
            self._dict.update(super().__dict__())

        return self._dict
