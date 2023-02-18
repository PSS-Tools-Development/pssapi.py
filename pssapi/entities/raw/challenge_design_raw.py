"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ChallengeDesignRaw:
    XML_NODE_NAME: str = 'ChallengeDesign'

    def __init__(self, challenge_design_info: _EntityInfo) -> None:
        self.base_prize: int = _parse.pss_int(challenge_design_info.get('BasePrize'))
        self.button_animation_id: int = _parse.pss_int(challenge_design_info.get('ButtonAnimationId'))
        self.challenge_argument: int = _parse.pss_int(challenge_design_info.get('ChallengeArgument'))
        self.challenge_design_id: int = _parse.pss_int(challenge_design_info.get('ChallengeDesignId'))
        self.challenge_design_metadata: str = _parse.pss_str(challenge_design_info.get('ChallengeDesignMetadata'))
        self.challenge_scoring_argument: int = _parse.pss_int(challenge_design_info.get('ChallengeScoringArgument'))
        self.challenge_scoring_type: str = _parse.pss_str(challenge_design_info.get('ChallengeScoringType'))
        self.challenge_type: str = _parse.pss_str(challenge_design_info.get('ChallengeType'))
        self.description: str = _parse.pss_str(challenge_design_info.get('Description'))
        self.end_date: _datetime = _parse.pss_datetime(challenge_design_info.get('EndDate'))
        self.entry_fee: int = _parse.pss_int(challenge_design_info.get('EntryFee'))
        self.flags: int = _parse.pss_int(challenge_design_info.get('Flags'))
        self.is_first_free: bool = _parse.pss_bool(challenge_design_info.get('IsFirstFree'))
        self.is_realtime: bool = _parse.pss_bool(challenge_design_info.get('IsRealtime'))
        self.lives: int = _parse.pss_int(challenge_design_info.get('Lives'))
        self.max_battle_prize: int = _parse.pss_int(challenge_design_info.get('MaxBattlePrize'))
        self.min_battle_prize: int = _parse.pss_int(challenge_design_info.get('MinBattlePrize'))
        self.name: str = _parse.pss_str(challenge_design_info.get('Name'))
        self.opponent_ship_ids: str = _parse.pss_str(challenge_design_info.get('OpponentShipIds'))
        self.poster_sprite_id: int = _parse.pss_int(challenge_design_info.get('PosterSpriteId'))
        self.requirement_string: str = _parse.pss_str(challenge_design_info.get('RequirementString'))
        self.reward_string: str = _parse.pss_str(challenge_design_info.get('RewardString'))
        self.root_achievement_design_id: int = _parse.pss_int(challenge_design_info.get('RootAchievementDesignId'))
        self.special_rule_argument: int = _parse.pss_int(challenge_design_info.get('SpecialRuleArgument'))
        self.special_rule_type: str = _parse.pss_str(challenge_design_info.get('SpecialRuleType'))
        self.start_date: _datetime = _parse.pss_datetime(challenge_design_info.get('StartDate'))
