"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as EntityBaseRaw


class SpriteRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "Sprite"

    def __init__(self, sprite_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._height: int = _parse.pss_int(sprite_info.pop("Height", None))
        self._image_file_id: int = _parse.pss_int(sprite_info.pop("ImageFileId", None))
        self._sprite_id: int = _parse.pss_int(sprite_info.pop("SpriteId", None))
        self._sprite_key: str = _parse.pss_str(sprite_info.pop("SpriteKey", None))
        self._width: int = _parse.pss_int(sprite_info.pop("Width", None))
        self._x: int = _parse.pss_int(sprite_info.pop("X", None))
        self._y: int = _parse.pss_int(sprite_info.pop("Y", None))
        super().__init__(sprite_info)

    @property
    def height(self) -> int:
        return self._height

    @property
    def image_file_id(self) -> int:
        return self._image_file_id

    @property
    def sprite_id(self) -> int:
        return self._sprite_id

    @property
    def sprite_key(self) -> str:
        return self._sprite_key

    @property
    def width(self) -> int:
        return self._width

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    def _key(self):
        return (
            self.height,
            self.image_file_id,
            self.sprite_id,
            self.sprite_key,
            self.width,
            self.x,
            self.y,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "Height": self.height,
                "ImageFileId": self.image_file_id,
                "SpriteId": self.sprite_id,
                "SpriteKey": self.sprite_key,
                "Width": self.width,
                "X": self.x,
                "Y": self.y,
            }
            self._dict.update(super().__dict__())

        return self._dict
