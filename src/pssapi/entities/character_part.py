from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import CharacterPartRaw as _CharacterPartRaw


class CharacterPart(_CharacterPartRaw, _EntityWithIdBase):
    def __init__(self, character_part_info: _EntityInfo) -> None:
        super().__init__(character_part_info)
        self._character_part_type_enum: _enums.CharacterPartType = _parse.pss_str_enum(self.character_part_type, _enums.CharacterPartType)

    @property
    def id(self) -> int:
        return self.character_part_id

    @property
    def character_part_type_enum(self) -> "_enums.CharacterPartType":
        return self._character_part_type_enum
