"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class CraftDesignRaw:
    XML_NODE_NAME: str = 'CraftDesign'

    def __init__(self, craft_design_info: _EntityInfo) -> None:
        self.__craft_name: str = _parse.pss_str(
            craft_design_info.get('CraftName'))
        self.__volley: int = _parse.pss_int(craft_design_info.get('Volley'))
        self.__hp: int = _parse.pss_int(craft_design_info.get('Hp'))
        self.__volley_delay: int = _parse.pss_int(
            craft_design_info.get('VolleyDelay'))
        self.__craft_design_id: int = _parse.pss_int(
            craft_design_info.get('CraftDesignId'))
        self.__sprite_id: int = _parse.pss_int(
            craft_design_info.get('SpriteId'))
        self.__missile_design_id: int = _parse.pss_int(
            craft_design_info.get('MissileDesignId'))
        self.__reload: int = _parse.pss_int(craft_design_info.get('Reload'))
        self.__flight_speed: int = _parse.pss_int(
            craft_design_info.get('FlightSpeed'))

    @property
    def craft_name(self) -> str:
        return self.__craft_name

    @property
    def volley(self) -> int:
        return self.__volley

    @property
    def hp(self) -> int:
        return self.__hp

    @property
    def volley_delay(self) -> int:
        return self.__volley_delay

    @property
    def craft_design_id(self) -> int:
        return self.__craft_design_id

    @property
    def sprite_id(self) -> int:
        return self.__sprite_id

    @property
    def missile_design_id(self) -> int:
        return self.__missile_design_id

    @property
    def reload(self) -> int:
        return self.__reload

    @property
    def flight_speed(self) -> int:
        return self.__flight_speed
