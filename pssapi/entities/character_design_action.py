
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import CharacterDesignActionRaw as _CharacterDesignActionRaw
from ..types import EntityInfo as _EntityInfo


class CharacterDesignAction(_EntityWithIdBase, _CharacterDesignActionRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<CharacterDesignAction {self.id}: {self.name}>'

    def __str__(self) -> str:
        return f'<CharacterDesignAction {self.id}: {self.name}>'

    @property
    def id(self) -> int:
        return self.character_design_action_id
