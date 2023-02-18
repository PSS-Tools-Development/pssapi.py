
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import CharacterActionRaw as _CharacterActionRaw
from ..types import EntityInfo as _EntityInfo


class CharacterAction(_EntityWithIdBase, _CharacterActionRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<CharacterAction {self.id}>'

    def __str__(self) -> str:
        return f'<CharacterAction {self.id}>'

    @property
    def id(self) -> int:
        return self.character_action_id
