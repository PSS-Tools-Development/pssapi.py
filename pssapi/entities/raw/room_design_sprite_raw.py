"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class RoomDesignSpriteRaw:
    XML_NODE_NAME: str = 'RoomDesignSprite'

    def __init__(self, room_design_sprite_info: _EntityInfo) -> None:
        self.animation_id: int = _parse.pss_int(room_design_sprite_info.get('AnimationId'))
        self.flags: int = _parse.pss_int(room_design_sprite_info.get('Flags'))
        self.metadata: str = _parse.pss_str(room_design_sprite_info.get('Metadata'))
        self.race_id: int = _parse.pss_int(room_design_sprite_info.get('RaceId'))
        self.requirement_string: str = _parse.pss_str(room_design_sprite_info.get('RequirementString'))
        self.room_design_id: int = _parse.pss_int(room_design_sprite_info.get('RoomDesignId'))
        self.room_design_sprite_id: int = _parse.pss_int(room_design_sprite_info.get('RoomDesignSpriteId'))
        self.room_effect_parameter: int = _parse.pss_int(room_design_sprite_info.get('RoomEffectParameter'))
        self.room_effect_type: str = _parse.pss_str(room_design_sprite_info.get('RoomEffectType'))
        self.room_sprite_type: str = _parse.pss_str(room_design_sprite_info.get('RoomSpriteType'))
        self.skin_description: str = _parse.pss_str(room_design_sprite_info.get('SkinDescription'))
        self.skin_key: int = _parse.pss_int(room_design_sprite_info.get('SkinKey'))
        self.skin_name: str = _parse.pss_str(room_design_sprite_info.get('SkinName'))
        self.sprite_id: int = _parse.pss_int(room_design_sprite_info.get('SpriteId'))
