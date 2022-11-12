"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class StarSystemRaw:
    XML_NODE_NAME: str = 'StarSystem'

    def __init__(self, star_system_info: _EntityInfo) -> None:
        self.exploration_duration: int = _parse.pss_int(
            star_system_info.get('ExplorationDuration'))
        self.icon_sprite_id: int = _parse.pss_int(
            star_system_info.get('IconSpriteId'))
        self.requirement_description: str = _parse.pss_str(
            star_system_info.get('RequirementDescription'))
        self.requirement_string: str = _parse.pss_str(
            star_system_info.get('RequirementString'))
        self.star_system_description: str = _parse.pss_str(
            star_system_info.get('StarSystemDescription'))
        self.star_system_id: int = _parse.pss_int(
            star_system_info.get('StarSystemId'))
        self.star_system_title: str = _parse.pss_str(
            star_system_info.get('StarSystemTitle'))
        self.x: int = _parse.pss_int(star_system_info.get('X'))
        self.y: int = _parse.pss_int(star_system_info.get('Y'))
        self.z: int = _parse.pss_int(star_system_info.get('Z'))
