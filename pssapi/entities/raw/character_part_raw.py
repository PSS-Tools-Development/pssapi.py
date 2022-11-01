"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class CharacterPartRaw:
    XML_NODE_NAME: str = 'CharacterPart'

    def __init__(self, character_part_info: _EntityInfo) -> None:
        self.__action_sprite_id: int = _parse.pss_int(
            character_part_info.get('ActionSpriteId'))
        self.__standard_sprite_id: int = _parse.pss_int(
            character_part_info.get('StandardSpriteId'))
        self.__action_file_id: int = _parse.pss_int(
            character_part_info.get('ActionFileId'))
        self.__character_part_type: str = _parse.pss_str(
            character_part_info.get('CharacterPartType'))
        self.__standard_file_id: int = _parse.pss_int(
            character_part_info.get('StandardFileId'))
        self.__action_border_file_id: int = _parse.pss_int(
            character_part_info.get('ActionBorderFileId'))
        self.__character_part_id: int = _parse.pss_int(
            character_part_info.get('CharacterPartId'))
        self.__character_part_name: str = _parse.pss_str(
            character_part_info.get('CharacterPartName'))
        self.__standard_border_file_id: int = _parse.pss_int(
            character_part_info.get('StandardBorderFileId'))

    @property
    def action_sprite_id(self) -> int:
        return self.__action_sprite_id

    @property
    def standard_sprite_id(self) -> int:
        return self.__standard_sprite_id

    @property
    def action_file_id(self) -> int:
        return self.__action_file_id

    @property
    def character_part_type(self) -> str:
        return self.__character_part_type

    @property
    def standard_file_id(self) -> int:
        return self.__standard_file_id

    @property
    def action_border_file_id(self) -> int:
        return self.__action_border_file_id

    @property
    def character_part_id(self) -> int:
        return self.__character_part_id

    @property
    def character_part_name(self) -> str:
        return self.__character_part_name

    @property
    def standard_border_file_id(self) -> int:
        return self.__standard_border_file_id
