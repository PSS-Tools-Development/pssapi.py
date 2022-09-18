
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import RoomDesignSpriteRaw as _RoomDesignSpriteRaw
from ..types import EntityInfo as _EntityInfo


class RoomDesignSprite(_EntityWithIdBase, _RoomDesignSpriteRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<RoomDesignSprite {self.id}: {self.name}>'

    def __str__(self) -> str:
        return f'<RoomDesignSprite {self.id}: {self.name}>'

    @property
    def id(self) -> int:
        return self.room_design_sprite_id
