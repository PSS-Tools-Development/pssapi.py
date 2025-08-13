from .entity_base import EntityWithIdBase
from .raw import CharacterActionRaw


class CharacterAction(CharacterActionRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.character_action_id


__all__ = [
    "CharacterAction",
]
