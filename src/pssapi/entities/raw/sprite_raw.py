"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class SpriteRaw(EntityBaseRaw, tag="Sprite"):
    XML_NODE_NAME: str = "Sprite"

    height: Optional[int] = attr(name="Height", default=None)
    image_file_id: Optional[int] = attr(name="ImageFileId", default=None)
    sprite_id: Optional[int] = attr(name="SpriteId", default=None)
    sprite_key: Optional[str] = attr(name="SpriteKey", default=None)
    width: Optional[int] = attr(name="Width", default=None)
    x: Optional[int] = attr(name="X", default=None)
    y: Optional[int] = attr(name="Y", default=None)

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


__all__ = [
    "SpriteRaw",
]
