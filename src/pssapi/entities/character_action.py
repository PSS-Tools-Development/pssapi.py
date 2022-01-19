from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import CharacterActionRaw as _CharacterActionRaw


class CharacterAction(_CharacterActionRaw, _EntityWithIdBase):
    def __init__(self, character_action_info: _EntityInfo) -> None:
        super().__init__(character_action_info)

    @property
    def id(self) -> int:
        return self.character_action_id
