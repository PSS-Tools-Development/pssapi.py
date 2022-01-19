from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import CharacterPartRaw as _CharacterPartRaw


class CharacterPart(_CharacterPartRaw, _EntityWithIdBase):
    def __init__(self, character_part_info: _EntityInfo) -> None:
        super().__init__(character_part_info)

    @property
    def id(self) -> int:
        return self.character_part_id
