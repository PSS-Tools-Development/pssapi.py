"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class PrestigeRaw:
    XML_NODE_NAME: str = "Prestige"

    def __init__(self, prestige_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._character_design_id_1: int = _parse.pss_int(prestige_info.get("CharacterDesignId1"))
        self._character_design_id_2: int = _parse.pss_int(prestige_info.get("CharacterDesignId2"))
        self._to_character_design_id: int = _parse.pss_int(prestige_info.get("ToCharacterDesignId"))

    @property
    def character_design_id_1(self) -> int:
        return self._character_design_id_1

    @property
    def character_design_id_2(self) -> int:
        return self._character_design_id_2

    @property
    def to_character_design_id(self) -> int:
        return self._to_character_design_id

    def _key(self):
        return (
            self.character_design_id_1,
            self.character_design_id_2,
            self.to_character_design_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "CharacterDesignId1": self.character_design_id_1,
                "CharacterDesignId2": self.character_design_id_2,
                "ToCharacterDesignId": self.to_character_design_id,
            }

        return self._dict
