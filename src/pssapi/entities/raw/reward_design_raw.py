"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class RewardDesignRaw(EntityBaseRaw, tag="RewardDesign"):
    XML_NODE_NAME: str = "RewardDesign"

    argument_string: Optional[str] = attr(name="ArgumentString", default=None)
    available_every_x_days: Optional[int] = attr(name="AvailableEveryXDays", default=None)
    available_from: Optional[datetime] = attr(name="AvailableFrom", default=None)
    available_quantity: Optional[int] = attr(name="AvailableQuantity", default=None)
    available_to: Optional[datetime] = attr(name="AvailableTo", default=None)
    background_sprite_id: Optional[int] = attr(name="BackgroundSpriteId", default=None)
    battle_pass_tier_index: Optional[int] = attr(name="BattlePassTierIndex", default=None)
    flags: Optional[int] = attr(name="Flags", default=None)
    grids: Optional[int] = attr(name="Grids", default=None)
    max_per_user: Optional[int] = attr(name="MaxPerUser", default=None)
    metadata: Optional[str] = attr(name="Metadata", default=None)
    order_index: Optional[int] = attr(name="OrderIndex", default=None)
    price_string: Optional[str] = attr(name="PriceString", default=None)
    requirement_string: Optional[str] = attr(name="RequirementString", default=None)
    reward_description: Optional[str] = attr(name="RewardDescription", default=None)
    reward_design_id: Optional[int] = attr(name="RewardDesignId", default=None)
    reward_name: Optional[str] = attr(name="RewardName", default=None)
    reward_type: Optional[str] = attr(name="RewardType", default=None)
    season_design_id: Optional[int] = attr(name="SeasonDesignId", default=None)
    sprite_id: Optional[int] = attr(name="SpriteId", default=None)

    def _key(self):
        return (
            self.argument_string,
            self.available_every_x_days,
            self.available_from,
            self.available_quantity,
            self.available_to,
            self.background_sprite_id,
            self.battle_pass_tier_index,
            self.flags,
            self.grids,
            self.max_per_user,
            self.metadata,
            self.order_index,
            self.price_string,
            self.requirement_string,
            self.reward_description,
            self.reward_design_id,
            self.reward_name,
            self.reward_type,
            self.season_design_id,
            self.sprite_id,
        )


__all__ = [
    "RewardDesignRaw",
]
