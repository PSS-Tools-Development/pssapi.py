"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class AllianceRaw(EntityBaseRaw, tag="Alliance"):
    XML_NODE_NAME: str = "Alliance"

    alliance_country_code: Optional[str] = attr(name="AllianceCountryCode", default=None)
    alliance_description: Optional[str] = attr(name="AllianceDescription", default=None)
    alliance_id: Optional[int] = attr(name="AllianceId", default=None)
    alliance_name: Optional[str] = attr(name="AllianceName", default=None)
    alliance_ship_user_id: Optional[int] = attr(name="AllianceShipUserId", default=None)
    alliance_sprite_id: Optional[int] = attr(name="AllianceSpriteId", default=None)
    championship_score: Optional[int] = attr(name="ChampionshipScore", default=None)
    channel_id: Optional[int] = attr(name="ChannelId", default=None)
    credits: Optional[str] = attr(name="Credits", default=None)
    division_design_id: Optional[int] = attr(name="DivisionDesignId", default=None)
    enable_wars: Optional[bool] = attr(name="EnableWars", default=None)
    immunity_date: Optional[datetime] = attr(name="ImmunityDate", default=None)
    min_score_contribution: Optional[int] = attr(name="MinScoreContribution", default=None)
    min_trophy_required: Optional[int] = attr(name="MinTrophyRequired", default=None)
    number_of_approved_members: Optional[int] = attr(name="NumberOfApprovedMembers", default=None)
    number_of_members: Optional[int] = attr(name="NumberOfMembers", default=None)
    ranking: Optional[int] = attr(name="Ranking", default=None)
    requires_approval: Optional[bool] = attr(name="RequiresApproval", default=None)
    score: Optional[int] = attr(name="Score", default=None)
    trophy: Optional[int] = attr(name="Trophy", default=None)

    def _key(self):
        return (
            self.alliance_country_code,
            self.alliance_description,
            self.alliance_id,
            self.alliance_name,
            self.alliance_ship_user_id,
            self.alliance_sprite_id,
            self.championship_score,
            self.channel_id,
            self.credits,
            self.division_design_id,
            self.enable_wars,
            self.immunity_date,
            self.min_score_contribution,
            self.min_trophy_required,
            self.number_of_approved_members,
            self.number_of_members,
            self.ranking,
            self.requires_approval,
            self.score,
            self.trophy,
        )


__all__ = [
    "AllianceRaw",
]
