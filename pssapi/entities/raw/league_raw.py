"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class LeagueRaw:
    XML_NODE_NAME: str = 'League'

    def __init__(self, league_info: _EntityInfo) -> None:
        self.background_sprite_id: int = _parse.pss_int(league_info.get('BackgroundSpriteId'))
        self.gas_reward: int = _parse.pss_int(league_info.get('GasReward'))
        self.large_logo_sprite_id: int = _parse.pss_int(league_info.get('LargeLogoSpriteId'))
        self.league_id: int = _parse.pss_int(league_info.get('LeagueId'))
        self.league_name: str = _parse.pss_str(league_info.get('LeagueName'))
        self.logo_sprite_id: int = _parse.pss_int(league_info.get('LogoSpriteId'))
        self.max_trophy: int = _parse.pss_int(league_info.get('MaxTrophy'))
        self.min_trophy: int = _parse.pss_int(league_info.get('MinTrophy'))
        self.mineral_reward: int = _parse.pss_int(league_info.get('MineralReward'))
