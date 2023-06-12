from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import CharacterRaw as _CharacterRaw


class Character(_CharacterRaw, _EntityWithIdBase):
    def __init__(self, character_info: _EntityInfo) -> None:
        super().__init__(character_info)
        self._flags_enum: _enums.CharacterFlags = _parse.pss_str_enum(self.flags, _enums.CharacterFlags)

    @property
    def id(self) -> int:
        return self.character_id

    @property
    def flags_enum(self) -> "_enums.CharacterFlags":
        return self._flags_enum
