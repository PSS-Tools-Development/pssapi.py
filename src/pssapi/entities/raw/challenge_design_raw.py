"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ChallengeDesignRaw:
    XML_NODE_NAME: str = "ChallengeDesign"

    def __init__(self, challenge_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._base_prize: int = _parse.pss_int(challenge_design_info.get("BasePrize"))
        self._button_animation_id: int = _parse.pss_int(challenge_design_info.get("ButtonAnimationId"))
        self._challenge_argument: int = _parse.pss_int(challenge_design_info.get("ChallengeArgument"))
        self._challenge_design_id: int = _parse.pss_int(challenge_design_info.get("ChallengeDesignId"))
        self._challenge_design_metadata: str = _parse.pss_str(challenge_design_info.get("ChallengeDesignMetadata"))
        self._challenge_scoring_argument: int = _parse.pss_int(challenge_design_info.get("ChallengeScoringArgument"))
        self._challenge_scoring_type: str = _parse.pss_str(challenge_design_info.get("ChallengeScoringType"))
        self._challenge_type: str = _parse.pss_str(challenge_design_info.get("ChallengeType"))
        self._description: str = _parse.pss_str(challenge_design_info.get("Description"))
        self._end_date: _datetime = _parse.pss_datetime(challenge_design_info.get("EndDate"))
        self._entry_fee: int = _parse.pss_int(challenge_design_info.get("EntryFee"))
        self._flags: int = _parse.pss_int(challenge_design_info.get("Flags"))
        self._is_first_free: bool = _parse.pss_bool(challenge_design_info.get("IsFirstFree"))
        self._is_realtime: bool = _parse.pss_bool(challenge_design_info.get("IsRealtime"))
        self._lives: int = _parse.pss_int(challenge_design_info.get("Lives"))
        self._max_battle_prize: int = _parse.pss_int(challenge_design_info.get("MaxBattlePrize"))
        self._min_battle_prize: int = _parse.pss_int(challenge_design_info.get("MinBattlePrize"))
        self._name: str = _parse.pss_str(challenge_design_info.get("Name"))
        self._opponent_ship_ids: str = _parse.pss_str(challenge_design_info.get("OpponentShipIds"))
        self._poster_sprite_id: int = _parse.pss_int(challenge_design_info.get("PosterSpriteId"))
        self._requirement_string: str = _parse.pss_str(challenge_design_info.get("RequirementString"))
        self._reward_string: str = _parse.pss_str(challenge_design_info.get("RewardString"))
        self._root_achievement_design_id: int = _parse.pss_int(challenge_design_info.get("RootAchievementDesignId"))
        self._special_rule_argument: int = _parse.pss_int(challenge_design_info.get("SpecialRuleArgument"))
        self._special_rule_type: str = _parse.pss_str(challenge_design_info.get("SpecialRuleType"))
        self._start_date: _datetime = _parse.pss_datetime(challenge_design_info.get("StartDate"))

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

        return self._dict
