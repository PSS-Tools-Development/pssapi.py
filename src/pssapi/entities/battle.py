from .entity_base import EntityWithIdBase
from .raw import BattleRaw


class Battle(BattleRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.battle_id


__all__ = [
    "Battle",
]
