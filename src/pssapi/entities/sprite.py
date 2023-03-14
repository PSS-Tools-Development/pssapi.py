from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import SpriteRaw as _SpriteRaw


class Sprite(_SpriteRaw, _EntityWithIdBase):
    def __init__(self, sprite_info: _EntityInfo) -> None:
        super().__init__(sprite_info)

    @property
    def id(self) -> int:
        return self.sprite_id
