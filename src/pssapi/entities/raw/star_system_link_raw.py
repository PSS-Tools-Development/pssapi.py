"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class StarSystemLinkRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "StarSystemLink"

    def __init__(self, star_system_link_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._from_star_system_id: int = _parse.pss_int(star_system_link_info.pop("FromStarSystemId", None))
        self._is_two_way: bool = _parse.pss_bool(star_system_link_info.pop("IsTwoWay", None))
        self._star_system_link_id: int = _parse.pss_int(star_system_link_info.pop("StarSystemLinkId", None))
        self._to_star_system_id: int = _parse.pss_int(star_system_link_info.pop("ToStarSystemId", None))
        self._travel_time: int = _parse.pss_int(star_system_link_info.pop("TravelTime", None))
        super().__init__(star_system_link_info)

    @property
    def from_star_system_id(self) -> int:
        return self._from_star_system_id

    @property
    def is_two_way(self) -> bool:
        return self._is_two_way

    @property
    def star_system_link_id(self) -> int:
        return self._star_system_link_id

    @property
    def to_star_system_id(self) -> int:
        return self._to_star_system_id

    @property
    def travel_time(self) -> int:
        return self._travel_time

    def _key(self):
        return (
            self.from_star_system_id,
            self.is_two_way,
            self.star_system_link_id,
            self.to_star_system_id,
            self.travel_time,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "FromStarSystemId": self.from_star_system_id,
                "IsTwoWay": self.is_two_way,
                "StarSystemLinkId": self.star_system_link_id,
                "ToStarSystemId": self.to_star_system_id,
                "TravelTime": self.travel_time,
            }
            self._dict.update(super().__dict__())

        return self._dict
