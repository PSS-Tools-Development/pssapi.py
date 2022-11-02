"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class SpriteRaw:
    XML_NODE_NAME: str = 'Sprite'

    def __init__(self, sprite_info: _EntityInfo) -> None:
        self.__x: int = _parse.pss_int(sprite_info.get('X'))
        self.__height: int = _parse.pss_int(sprite_info.get('Height'))
        self.__y: int = _parse.pss_int(sprite_info.get('Y'))
        self.__image_file_id: int = _parse.pss_int(
            sprite_info.get('ImageFileId'))
        self.__sprite_id: int = _parse.pss_int(sprite_info.get('SpriteId'))
        self.__sprite_key: str = _parse.pss_str(sprite_info.get('SpriteKey'))
        self.__width: int = _parse.pss_int(sprite_info.get('Width'))

    @property
    def x(self) -> int:
        return self.__x

    @property
    def height(self) -> int:
        return self.__height

    @property
    def y(self) -> int:
        return self.__y

    @property
    def image_file_id(self) -> int:
        return self.__image_file_id

    @property
    def sprite_id(self) -> int:
        return self.__sprite_id

    @property
    def sprite_key(self) -> str:
        return self.__sprite_key

    @property
    def width(self) -> int:
        return self.__width
