from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import BattleRaw as _BattleRaw


class Battle(_BattleRaw, _EntityWithIdBase):
    def __init__(self, battle_info: _EntityInfo) -> None:
        super().__init__(battle_info)
        self._battle_type_enum: _enums.BattleType = _parse.pss_str_enum(self.battle_type, _enums.BattleType)
        self._client_outcome_type_enum: _enums.OutcomeType = _parse.pss_str_enum(self.client_outcome_type, _enums.OutcomeType)
        self._defending_client_outcome_type_enum: _enums.OutcomeType = _parse.pss_str_enum(self.defending_client_outcome_type, _enums.OutcomeType)
        self._league_type_enum: _enums.LeagueType = _parse.pss_str_enum(self.league_type, _enums.LeagueType)
        self._outcome_type_enum: _enums.OutcomeType = _parse.pss_str_enum(self.outcome_type, _enums.OutcomeType)
        self._server_outcome_type_enum: _enums.OutcomeType = _parse.pss_str_enum(self.server_outcome_type, _enums.OutcomeType)

    @property
    def id(self) -> int:
        return self.battle_id

    @property
    def battle_type_enum(self) -> "_enums.BattleType":
        return self._battle_type_enum

    @property
    def client_outcome_type_enum(self) -> "_enums.OutcomeType":
        return self._client_outcome_type_enum

    @property
    def defending_client_outcome_type_enum(self) -> "_enums.OutcomeType":
        return self._defending_client_outcome_type_enum

    @property
    def league_type_enum(self) -> "_enums.LeagueType":
        return self._league_type_enum

    @property
    def outcome_type_enum(self) -> "_enums.OutcomeType":
        return self._outcome_type_enum

    @property
    def server_outcome_type_enum(self) -> "_enums.OutcomeType":
        return self._server_outcome_type_enum
