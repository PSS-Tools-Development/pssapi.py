"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class CharacterPartRaw:
    XML_NODE_NAME: str = "CharacterPart"

    def __init__(self, character_part_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._action_border_file_id: int = _parse.pss_int(character_part_info.get("ActionBorderFileId"))
        self._action_file_id: int = _parse.pss_int(character_part_info.get("ActionFileId"))
        self._action_sprite_id: int = _parse.pss_int(character_part_info.get("ActionSpriteId"))
        self._character_part_id: int = _parse.pss_int(character_part_info.get("CharacterPartId"))
        self._character_part_name: str = _parse.pss_str(character_part_info.get("CharacterPartName"))
        self._character_part_type: str = _parse.pss_str(character_part_info.get("CharacterPartType"))
        self._standard_border_file_id: int = _parse.pss_int(character_part_info.get("StandardBorderFileId"))
        self._standard_file_id: int = _parse.pss_int(character_part_info.get("StandardFileId"))
        self._standard_sprite_id: int = _parse.pss_int(character_part_info.get("StandardSpriteId"))

    @property
    def action_border_file_id(self) -> int:
        return self._action_border_file_id

    @property
    def action_file_id(self) -> int:
        return self._action_file_id

    @property
    def action_sprite_id(self) -> int:
        return self._action_sprite_id

    @property
    def character_part_id(self) -> int:
        return self._character_part_id

    @property
    def character_part_name(self) -> str:
        return self._character_part_name

    @property
    def character_part_type(self) -> str:
        return self._character_part_type

    @property
    def standard_border_file_id(self) -> int:
        return self._standard_border_file_id

    @property
    def standard_file_id(self) -> int:
        return self._standard_file_id

    @property
    def standard_sprite_id(self) -> int:
        return self._standard_sprite_id

    def _key(self):
        return (
            self.action_border_file_id,
            self.action_file_id,
            self.action_sprite_id,
            self.character_part_id,
            self.character_part_name,
            self.character_part_type,
            self.standard_border_file_id,
            self.standard_file_id,
            self.standard_sprite_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "ActionBorderFileId": self.action_border_file_id,
                "ActionFileId": self.action_file_id,
                "ActionSpriteId": self.action_sprite_id,
                "CharacterPartId": self.character_part_id,
                "CharacterPartName": self.character_part_name,
                "CharacterPartType": self.character_part_type,
                "StandardBorderFileId": self.standard_border_file_id,
                "StandardFileId": self.standard_file_id,
                "StandardSpriteId": self.standard_sprite_id,
            }

        return self._dict
