"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class LeagueRaw:
    XML_NODE_NAME: str = 'League'

    def __init__(self, league_info: _EntityInfo) -> None:
        self.__gas_reward: int = _parse.pss_int(league_info.get('GasReward'))
        self.__min_trophy: int = _parse.pss_int(league_info.get('MinTrophy'))
        self.__league_name: str = _parse.pss_str(league_info.get('LeagueName'))
        self.__background_sprite_id: int = _parse.pss_int(
            league_info.get('BackgroundSpriteId'))
        self.__league_id: int = _parse.pss_int(league_info.get('LeagueId'))
        self.__logo_sprite_id: int = _parse.pss_int(
            league_info.get('LogoSpriteId'))
        self.__max_trophy: int = _parse.pss_int(league_info.get('MaxTrophy'))
        self.__large_logo_sprite_id: int = _parse.pss_int(
            league_info.get('LargeLogoSpriteId'))
        self.__mineral_reward: int = _parse.pss_int(
            league_info.get('MineralReward'))

    @property
    def gas_reward(self) -> int:
        return self.__gas_reward

    @property
    def min_trophy(self) -> int:
        return self.__min_trophy

    @property
    def league_name(self) -> str:
        return self.__league_name

    @property
    def background_sprite_id(self) -> int:
        return self.__background_sprite_id

    @property
    def league_id(self) -> int:
        return self.__league_id

    @property
    def logo_sprite_id(self) -> int:
        return self.__logo_sprite_id

    @property
    def max_trophy(self) -> int:
        return self.__max_trophy

    @property
    def large_logo_sprite_id(self) -> int:
        return self.__large_logo_sprite_id

    @property
    def mineral_reward(self) -> int:
        return self.__mineral_reward
