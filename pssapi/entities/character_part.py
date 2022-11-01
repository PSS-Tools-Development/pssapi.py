
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import CharacterPartRaw as _CharacterPartRaw
from ..types import EntityInfo as _EntityInfo


class CharacterPart(_EntityWithIdBase, _CharacterPartRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<CharacterPart {self.id}>'

    def __str__(self) -> str:
        return f'<CharacterPart {self.id}>'

    @property
    def id(self) -> int:
        return self.character_part_id
