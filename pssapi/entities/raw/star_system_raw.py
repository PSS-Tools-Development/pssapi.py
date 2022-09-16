####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class StarSystemRaw():
    XML_NODE_NAME: str = 'StarSystem'

    def __init__(self, star_system_info: _EntityInfo) -> None:
        self.__star_system_id: int = _parse.pss_int(star_system_info.get('StarSystemId'))
        self.__star_system_title: str = _parse.pss_str(star_system_info.get('StarSystemTitle'))
        self.__star_system_description: str = _parse.pss_str(star_system_info.get('StarSystemDescription'))
        self.__icon_sprite_id: int = _parse.pss_int(star_system_info.get('IconSpriteId'))
        self.__x: int = _parse.pss_int(star_system_info.get('X'))
        self.__y: int = _parse.pss_int(star_system_info.get('Y'))
        self.__z: int = _parse.pss_int(star_system_info.get('Z'))
        self.__requirement_string: str = _parse.pss_str(star_system_info.get('RequirementString'))
        self.__exploration_duration: int = _parse.pss_int(star_system_info.get('ExplorationDuration'))
        self.__requirement_description: str = _parse.pss_str(star_system_info.get('RequirementDescription'))

    @property
    def star_system_id(self) -> int:
        return self.__star_system_id

    @property
    def star_system_title(self) -> str:
        return self.__star_system_title

    @property
    def star_system_description(self) -> str:
        return self.__star_system_description

    @property
    def icon_sprite_id(self) -> int:
        return self.__icon_sprite_id

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def z(self) -> int:
        return self.__z

    @property
    def requirement_string(self) -> str:
        return self.__requirement_string

    @property
    def exploration_duration(self) -> int:
        return self.__exploration_duration

    @property
    def requirement_description(self) -> str:
        return self.__requirement_description
