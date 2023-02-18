
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import CharacterRaw as _CharacterRaw
from ..types import EntityInfo as _EntityInfo


class Character(_EntityWithIdBase, _CharacterRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<Character {self.id}>'

    def __str__(self) -> str:
        return f'<Character {self.id}>'

    @property
    def id(self) -> int:
        return self.character_id
