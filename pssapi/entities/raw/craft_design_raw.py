"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class CraftDesignRaw:
    XML_NODE_NAME: str = 'CraftDesign'

    def __init__(self, craft_design_info: _EntityInfo) -> None:
        self.craft_design_id: int = _parse.pss_int(
            craft_design_info.get('CraftDesignId'))
        self.craft_name: str = _parse.pss_str(
            craft_design_info.get('CraftName'))
        self.flight_speed: int = _parse.pss_int(
            craft_design_info.get('FlightSpeed'))
        self.hp: int = _parse.pss_int(craft_design_info.get('Hp'))
        self.missile_design_id: int = _parse.pss_int(
            craft_design_info.get('MissileDesignId'))
        self.reload: int = _parse.pss_int(craft_design_info.get('Reload'))
        self.sprite_id: int = _parse.pss_int(craft_design_info.get('SpriteId'))
        self.volley: int = _parse.pss_int(craft_design_info.get('Volley'))
        self.volley_delay: int = _parse.pss_int(
            craft_design_info.get('VolleyDelay'))
