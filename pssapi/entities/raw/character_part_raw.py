"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import List as _List

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class CharacterPartRaw:
    XML_NODE_NAME: str = 'CharacterPart'

    def __init__(self, character_part_info: _EntityInfo) -> None:
        self.action_border_file_id: int = _parse.pss_int(character_part_info.get('ActionBorderFileId'))
        self.action_file_id: int = _parse.pss_int(character_part_info.get('ActionFileId'))
        self.action_sprite_id: int = _parse.pss_int(character_part_info.get('ActionSpriteId'))
        self.character_part_id: int = _parse.pss_int(character_part_info.get('CharacterPartId'))
        self.character_part_name: str = _parse.pss_str(character_part_info.get('CharacterPartName'))
        self.character_part_type: str = _parse.pss_str(character_part_info.get('CharacterPartType'))
        self.standard_border_file_id: int = _parse.pss_int(character_part_info.get('StandardBorderFileId'))
        self.standard_file_id: int = _parse.pss_int(character_part_info.get('StandardFileId'))
        self.standard_sprite_id: int = _parse.pss_int(character_part_info.get('StandardSpriteId'))
