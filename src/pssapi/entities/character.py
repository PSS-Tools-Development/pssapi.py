from .entity_base import EntityWithIdBase
from .raw import CharacterRaw


class Character(CharacterRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.character_id


__all__ = [
    "Character",
]
