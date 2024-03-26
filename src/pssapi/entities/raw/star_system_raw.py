"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as EntityBaseRaw


class StarSystemRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "StarSystem"

    def __init__(self, star_system_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._exploration_duration: int = _parse.pss_int(star_system_info.pop("ExplorationDuration", None))
        self._icon_sprite_id: int = _parse.pss_int(star_system_info.pop("IconSpriteId", None))
        self._requirement_description: str = _parse.pss_str(star_system_info.pop("RequirementDescription", None))
        self._requirement_string: str = _parse.pss_str(star_system_info.pop("RequirementString", None))
        self._star_system_description: str = _parse.pss_str(star_system_info.pop("StarSystemDescription", None))
        self._star_system_id: int = _parse.pss_int(star_system_info.pop("StarSystemId", None))
        self._star_system_title: str = _parse.pss_str(star_system_info.pop("StarSystemTitle", None))
        self._x: int = _parse.pss_int(star_system_info.pop("X", None))
        self._y: int = _parse.pss_int(star_system_info.pop("Y", None))
        self._z: int = _parse.pss_int(star_system_info.pop("Z", None))
        super().__init__(star_system_info)

    @property
    def exploration_duration(self) -> int:
        return self._exploration_duration

    @property
    def icon_sprite_id(self) -> int:
        return self._icon_sprite_id

    @property
    def requirement_description(self) -> str:
        return self._requirement_description

    @property
    def requirement_string(self) -> str:
        return self._requirement_string

    @property
    def star_system_description(self) -> str:
        return self._star_system_description

    @property
    def star_system_id(self) -> int:
        return self._star_system_id

    @property
    def star_system_title(self) -> str:
        return self._star_system_title

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @property
    def z(self) -> int:
        return self._z

    def _key(self):
        return (
            self.exploration_duration,
            self.icon_sprite_id,
            self.requirement_description,
            self.requirement_string,
            self.star_system_description,
            self.star_system_id,
            self.star_system_title,
            self.x,
            self.y,
            self.z,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "ExplorationDuration": self.exploration_duration,
                "IconSpriteId": self.icon_sprite_id,
                "RequirementDescription": self.requirement_description,
                "RequirementString": self.requirement_string,
                "StarSystemDescription": self.star_system_description,
                "StarSystemId": self.star_system_id,
                "StarSystemTitle": self.star_system_title,
                "X": self.x,
                "Y": self.y,
                "Z": self.z,
            }
            self._dict.update(super().__dict__())

        return self._dict
