"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class ChallengeDesignRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "ChallengeDesign"

    def __init__(self, challenge_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._base_prize: int = _parse.pss_int(challenge_design_info.pop("BasePrize", None))
        self._button_animation_id: int = _parse.pss_int(challenge_design_info.pop("ButtonAnimationId", None))
        self._challenge_argument: int = _parse.pss_int(challenge_design_info.pop("ChallengeArgument", None))
        self._challenge_design_id: int = _parse.pss_int(challenge_design_info.pop("ChallengeDesignId", None))
        self._challenge_design_metadata: str = _parse.pss_str(challenge_design_info.pop("ChallengeDesignMetadata", None))
        self._challenge_scoring_argument: int = _parse.pss_int(challenge_design_info.pop("ChallengeScoringArgument", None))
        self._challenge_scoring_type: str = _parse.pss_str(challenge_design_info.pop("ChallengeScoringType", None))
        self._challenge_type: str = _parse.pss_str(challenge_design_info.pop("ChallengeType", None))
        self._description: str = _parse.pss_str(challenge_design_info.pop("Description", None))
        self._end_date: _datetime = _parse.pss_datetime(challenge_design_info.pop("EndDate", None))
        self._entry_fee: int = _parse.pss_int(challenge_design_info.pop("EntryFee", None))
        self._flags: int = _parse.pss_int(challenge_design_info.pop("Flags", None))
        self._is_first_free: bool = _parse.pss_bool(challenge_design_info.pop("IsFirstFree", None))
        self._is_realtime: bool = _parse.pss_bool(challenge_design_info.pop("IsRealtime", None))
        self._lives: int = _parse.pss_int(challenge_design_info.pop("Lives", None))
        self._max_battle_prize: int = _parse.pss_int(challenge_design_info.pop("MaxBattlePrize", None))
        self._min_battle_prize: int = _parse.pss_int(challenge_design_info.pop("MinBattlePrize", None))
        self._name: str = _parse.pss_str(challenge_design_info.pop("Name", None))
        self._opponent_ship_ids: str = _parse.pss_str(challenge_design_info.pop("OpponentShipIds", None))
        self._poster_sprite_id: int = _parse.pss_int(challenge_design_info.pop("PosterSpriteId", None))
        self._requirement_string: str = _parse.pss_str(challenge_design_info.pop("RequirementString", None))
        self._reward_string: str = _parse.pss_str(challenge_design_info.pop("RewardString", None))
        self._root_achievement_design_id: int = _parse.pss_int(challenge_design_info.pop("RootAchievementDesignId", None))
        self._special_rule_argument: int = _parse.pss_int(challenge_design_info.pop("SpecialRuleArgument", None))
        self._special_rule_type: str = _parse.pss_str(challenge_design_info.pop("SpecialRuleType", None))
        self._start_date: _datetime = _parse.pss_datetime(challenge_design_info.pop("StartDate", None))
        super().__init__(challenge_design_info)

    @property
    def base_prize(self) -> int:
        return self._base_prize

    @property
    def button_animation_id(self) -> int:
        return self._button_animation_id

    @property
    def challenge_argument(self) -> int:
        return self._challenge_argument

    @property
    def challenge_design_id(self) -> int:
        return self._challenge_design_id

    @property
    def challenge_design_metadata(self) -> str:
        return self._challenge_design_metadata

    @property
    def challenge_scoring_argument(self) -> int:
        return self._challenge_scoring_argument

    @property
    def challenge_scoring_type(self) -> str:
        return self._challenge_scoring_type

    @property
    def challenge_type(self) -> str:
        return self._challenge_type

    @property
    def description(self) -> str:
        return self._description

    @property
    def end_date(self) -> _datetime:
        return self._end_date

    @property
    def entry_fee(self) -> int:
        return self._entry_fee

    @property
    def flags(self) -> int:
        return self._flags

    @property
    def is_first_free(self) -> bool:
        return self._is_first_free

    @property
    def is_realtime(self) -> bool:
        return self._is_realtime

    @property
    def lives(self) -> int:
        return self._lives

    @property
    def max_battle_prize(self) -> int:
        return self._max_battle_prize

    @property
    def min_battle_prize(self) -> int:
        return self._min_battle_prize

    @property
    def name(self) -> str:
        return self._name

    @property
    def opponent_ship_ids(self) -> str:
        return self._opponent_ship_ids

    @property
    def poster_sprite_id(self) -> int:
        return self._poster_sprite_id

    @property
    def requirement_string(self) -> str:
        return self._requirement_string

    @property
    def reward_string(self) -> str:
        return self._reward_string

    @property
    def root_achievement_design_id(self) -> int:
        return self._root_achievement_design_id

    @property
    def special_rule_argument(self) -> int:
        return self._special_rule_argument

    @property
    def special_rule_type(self) -> str:
        return self._special_rule_type

    @property
    def start_date(self) -> _datetime:
        return self._start_date

    def _key(self):
        return (
            self.base_prize,
            self.button_animation_id,
            self.challenge_argument,
            self.challenge_design_id,
            self.challenge_design_metadata,
            self.challenge_scoring_argument,
            self.challenge_scoring_type,
            self.challenge_type,
            self.description,
            self.end_date,
            self.entry_fee,
            self.flags,
            self.is_first_free,
            self.is_realtime,
            self.lives,
            self.max_battle_prize,
            self.min_battle_prize,
            self.name,
            self.opponent_ship_ids,
            self.poster_sprite_id,
            self.requirement_string,
            self.reward_string,
            self.root_achievement_design_id,
            self.special_rule_argument,
            self.special_rule_type,
            self.start_date,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "BasePrize": self.base_prize,
                "ButtonAnimationId": self.button_animation_id,
                "ChallengeArgument": self.challenge_argument,
                "ChallengeDesignId": self.challenge_design_id,
                "ChallengeDesignMetadata": self.challenge_design_metadata,
                "ChallengeScoringArgument": self.challenge_scoring_argument,
                "ChallengeScoringType": self.challenge_scoring_type,
                "ChallengeType": self.challenge_type,
                "Description": self.description,
                "EndDate": self.end_date,
                "EntryFee": self.entry_fee,
                "Flags": self.flags,
                "IsFirstFree": self.is_first_free,
                "IsRealtime": self.is_realtime,
                "Lives": self.lives,
                "MaxBattlePrize": self.max_battle_prize,
                "MinBattlePrize": self.min_battle_prize,
                "Name": self.name,
                "OpponentShipIds": self.opponent_ship_ids,
                "PosterSpriteId": self.poster_sprite_id,
                "RequirementString": self.requirement_string,
                "RewardString": self.reward_string,
                "RootAchievementDesignId": self.root_achievement_design_id,
                "SpecialRuleArgument": self.special_rule_argument,
                "SpecialRuleType": self.special_rule_type,
                "StartDate": self.start_date,
            }
            self._dict.update(super().__dict__())

        return self._dict
