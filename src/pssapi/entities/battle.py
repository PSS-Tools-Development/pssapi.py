from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import BattleRaw as _BattleRaw


class Battle(_BattleRaw, _EntityWithIdBase):
    def __init__(self, battle_info: _EntityInfo) -> None:
        super().__init__(battle_info)

    @property
    def id(self) -> int:
        return self.battle_id
