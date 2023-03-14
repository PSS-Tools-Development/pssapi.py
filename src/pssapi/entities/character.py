from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import CharacterRaw as _CharacterRaw


class Character(_CharacterRaw, _EntityWithIdBase):
    def __init__(self, character_info: _EntityInfo) -> None:
        super().__init__(character_info)

    @property
    def id(self) -> int:
        return self.character_id
