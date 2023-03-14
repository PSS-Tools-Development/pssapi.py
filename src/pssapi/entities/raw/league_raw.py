"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class LeagueRaw:
    XML_NODE_NAME: str = "League"

    def __init__(self, league_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._background_sprite_id: int = _parse.pss_int(league_info.get("BackgroundSpriteId"))
        self._gas_reward: int = _parse.pss_int(league_info.get("GasReward"))
        self._large_logo_sprite_id: int = _parse.pss_int(league_info.get("LargeLogoSpriteId"))
        self._league_id: int = _parse.pss_int(league_info.get("LeagueId"))
        self._league_name: str = _parse.pss_str(league_info.get("LeagueName"))
        self._logo_sprite_id: int = _parse.pss_int(league_info.get("LogoSpriteId"))
        self._max_trophy: int = _parse.pss_int(league_info.get("MaxTrophy"))
        self._min_trophy: int = _parse.pss_int(league_info.get("MinTrophy"))
        self._mineral_reward: int = _parse.pss_int(league_info.get("MineralReward"))

    @property
    def background_sprite_id(self) -> int:
        return self._background_sprite_id

    @property
    def gas_reward(self) -> int:
        return self._gas_reward

    @property
    def large_logo_sprite_id(self) -> int:
        return self._large_logo_sprite_id

    @property
    def league_id(self) -> int:
        return self._league_id

    @property
    def league_name(self) -> str:
        return self._league_name

    @property
    def logo_sprite_id(self) -> int:
        return self._logo_sprite_id

    @property
    def max_trophy(self) -> int:
        return self._max_trophy

    @property
    def min_trophy(self) -> int:
        return self._min_trophy

    @property
    def mineral_reward(self) -> int:
        return self._mineral_reward

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

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "BackgroundSpriteId": self.background_sprite_id,
                "GasReward": self.gas_reward,
                "LargeLogoSpriteId": self.large_logo_sprite_id,
                "LeagueId": self.league_id,
                "LeagueName": self.league_name,
                "LogoSpriteId": self.logo_sprite_id,
                "MaxTrophy": self.max_trophy,
                "MinTrophy": self.min_trophy,
                "MineralReward": self.mineral_reward,
            }

        return self._dict
