"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class LeagueRaw(EntityBaseRaw, tag="League"):
    XML_NODE_NAME: str = "League"

    background_sprite_id: Optional[int] = attr(name="BackgroundSpriteId", default=None)
    gas_reward: Optional[int] = attr(name="GasReward", default=None)
    large_logo_sprite_id: Optional[int] = attr(name="LargeLogoSpriteId", default=None)
    league_id: Optional[int] = attr(name="LeagueId", default=None)
    league_name: Optional[str] = attr(name="LeagueName", default=None)
    logo_sprite_id: Optional[int] = attr(name="LogoSpriteId", default=None)
    max_trophy: Optional[int] = attr(name="MaxTrophy", default=None)
    min_trophy: Optional[int] = attr(name="MinTrophy", default=None)
    mineral_reward: Optional[int] = attr(name="MineralReward", default=None)

    def _key(self):
        return (
            self.background_sprite_id,
            self.gas_reward,
            self.large_logo_sprite_id,
            self.league_id,
            self.league_name,
            self.logo_sprite_id,
            self.max_trophy,
            self.min_trophy,
            self.mineral_reward,
        )


__all__ = [
    "LeagueRaw",
]
