"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class ChallengeDesignRaw(EntityBaseRaw, tag="ChallengeDesign"):
    XML_NODE_NAME: str = "ChallengeDesign"

    base_prize: Optional[int] = attr(name="BasePrize", default=None)
    button_animation_id: Optional[int] = attr(name="ButtonAnimationId", default=None)
    challenge_argument: Optional[int] = attr(name="ChallengeArgument", default=None)
    challenge_design_id: Optional[int] = attr(name="ChallengeDesignId", default=None)
    challenge_design_metadata: Optional[str] = attr(name="ChallengeDesignMetadata", default=None)
    challenge_scoring_argument: Optional[int] = attr(name="ChallengeScoringArgument", default=None)
    challenge_scoring_type: Optional[str] = attr(name="ChallengeScoringType", default=None)
    challenge_type: Optional[str] = attr(name="ChallengeType", default=None)
    description: Optional[str] = attr(name="Description", default=None)
    end_date: Optional[datetime] = attr(name="EndDate", default=None)
    entry_fee: Optional[int] = attr(name="EntryFee", default=None)
    flags: Optional[int] = attr(name="Flags", default=None)
    is_first_free: Optional[bool] = attr(name="IsFirstFree", default=None)
    is_realtime: Optional[bool] = attr(name="IsRealtime", default=None)
    lives: Optional[int] = attr(name="Lives", default=None)
    max_battle_prize: Optional[int] = attr(name="MaxBattlePrize", default=None)
    min_battle_prize: Optional[int] = attr(name="MinBattlePrize", default=None)
    name: Optional[str] = attr(name="Name", default=None)
    opponent_ship_ids: Optional[str] = attr(name="OpponentShipIds", default=None)
    poster_sprite_id: Optional[int] = attr(name="PosterSpriteId", default=None)
    requirement_string: Optional[str] = attr(name="RequirementString", default=None)
    reward_string: Optional[str] = attr(name="RewardString", default=None)
    root_achievement_design_id: Optional[int] = attr(name="RootAchievementDesignId", default=None)
    special_rule_argument: Optional[int] = attr(name="SpecialRuleArgument", default=None)
    special_rule_type: Optional[str] = attr(name="SpecialRuleType", default=None)
    start_date: Optional[datetime] = attr(name="StartDate", default=None)

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


__all__ = [
    "ChallengeDesignRaw",
]
