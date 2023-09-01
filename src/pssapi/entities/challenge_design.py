from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ChallengeDesignRaw as _ChallengeDesignRaw


class ChallengeDesign(_ChallengeDesignRaw, _EntityWithIdBase):
    def __init__(self, challenge_design_info: _EntityInfo) -> None:
        super().__init__(challenge_design_info)
        self._challenge_scoring_type_enum: _enums.ChallengeScoringType = _parse.pss_str_enum(self.challenge_scoring_type, _enums.ChallengeScoringType)
        self._challenge_type_enum: _enums.ChallengeType = _parse.pss_str_enum(self.challenge_type, _enums.ChallengeType)
        self._flags_enum: _enums.ChallengeFlags = _parse.pss_int_flag(self.flags, _enums.ChallengeFlags)
        self._special_rule_type_enum: _enums.SpecialRuleType = _parse.pss_str_enum(self.special_rule_type, _enums.SpecialRuleType)

    @property
    def id(self) -> int:
        return self.challenge_design_id

    @property
    def challenge_scoring_type_enum(self) -> "_enums.ChallengeScoringType":
        return self._challenge_scoring_type_enum

    @property
    def challenge_type_enum(self) -> "_enums.ChallengeType":
        return self._challenge_type_enum

    @property
    def flags_enum(self) -> "_enums.ChallengeFlags":
        return self._flags_enum

    @property
    def special_rule_type_enum(self) -> "_enums.SpecialRuleType":
        return self._special_rule_type_enum
