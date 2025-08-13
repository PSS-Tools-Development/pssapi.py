from .entity_base import EntityWithIdBase
from .raw import CharacterDesignRaw


class CharacterDesign(CharacterDesignRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.character_design_id


__all__ = [
    "CharacterDesign",
]
