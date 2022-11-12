"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class SpriteRaw:
    XML_NODE_NAME: str = 'Sprite'

    def __init__(self, sprite_info: _EntityInfo) -> None:
        self.height: int = _parse.pss_int(sprite_info.get('Height'))
        self.image_file_id: int = _parse.pss_int(
            sprite_info.get('ImageFileId'))
        self.sprite_id: int = _parse.pss_int(sprite_info.get('SpriteId'))
        self.sprite_key: str = _parse.pss_str(sprite_info.get('SpriteKey'))
        self.width: int = _parse.pss_int(sprite_info.get('Width'))
        self.x: int = _parse.pss_int(sprite_info.get('X'))
        self.y: int = _parse.pss_int(sprite_info.get('Y'))
