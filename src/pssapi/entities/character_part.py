from .entity_base import EntityWithIdBase
from .raw import CharacterPartRaw


class CharacterPart(CharacterPartRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.character_part_id


__all__ = [
    "CharacterPart",
]
