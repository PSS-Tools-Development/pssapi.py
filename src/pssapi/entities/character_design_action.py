from .entity_base import EntityWithIdBase
from .raw import CharacterDesignActionRaw


class CharacterDesignAction(CharacterDesignActionRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.character_design_action_id


__all__ = [
    "CharacterDesignAction",
]
