from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import BackgroundRaw as _BackgroundRaw


class Background(_BackgroundRaw, _EntityWithIdBase):
    def __init__(self, background_info: _EntityInfo) -> None:
        super().__init__(background_info)

    @property
    def id(self) -> int:
        return self.background_id
