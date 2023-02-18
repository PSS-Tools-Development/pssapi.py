
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import BackgroundRaw as _BackgroundRaw
from ..types import EntityInfo as _EntityInfo


class Background(_EntityWithIdBase, _BackgroundRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<Background {self.id}>'

    def __str__(self) -> str:
        return f'<Background {self.id}>'

    @property
    def id(self) -> int:
        return self.background_id
